from __future__ import annotations
from dataclasses import dataclass
import uuid

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import pydot

from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor


# --------------------------#
#          ARBRE            #
# --------------------------#

# Definim l'abre
@dataclass
class NodeLletra:
    val: str


@dataclass
class NodeAplicacio:
    esq: Arbre
    dre: Arbre


@dataclass
class NodeAbstraccio:
    lletra: NodeLletra
    terme: Arbre


Arbre = NodeLletra | NodeAplicacio | NodeAbstraccio


class TreeVisitor(lcVisitor):
    """
    La classe TreeVisitor és un visitador que defineix diversos mètodes per a processar diferents tipus de nodes de l'arbre.
    """
    def __init__(self, taula_usuari: dict):
        # Aqui usem en cada moment la taula del usuari que crida al visitador
        self.taula_macros = taula_usuari

    def visitLletra(self, ctx) -> NodeLletra:
        return NodeLletra(ctx.getText())

    def visitMacroTerme(self, ctx) -> None:
        macro = ctx.getText()
        return self.taula_macros[macro]

    def visitMacroInfixe(self, ctx) -> NodeAplicacio:
        [terme_esq, macro, terme_dre] = list(ctx.getChildren())

        resultat_terme_esq = self.visit(terme_esq)
        terme_macro = self.taula_macros[macro.getText()]
        resultat_terme_dre = self.visit(terme_dre)

        # Resolem l'aplicacio infixa de forma normal
        return NodeAplicacio(
            NodeAplicacio(
                terme_macro,
                resultat_terme_esq),
            resultat_terme_dre)

    def visitDefinicioMacro(self, ctx) -> None:
        [macro, _, terme] = list(ctx.getChildren())
        self.taula_macros[macro.getText()] = self.visit(terme)
        return None

    def visitTermeParentitsat(self, ctx) -> Arbre:
        [_, terme, _] = list(ctx.getChildren())
        return self.visit(terme)

    def visitAplicacio(self, ctx) -> NodeAplicacio:
        [terme_esq, terme_dre] = list(ctx.getChildren())
        resultat_esq = self.visit(terme_esq)
        resultat_dre = self.visit(terme_dre)
        return NodeAplicacio(resultat_esq, resultat_dre)

    def visitAbstraccio(self, ctx) -> NodeAbstraccio:
        [_, lletres, _, terme] = list(ctx.getChildren())
        lletres_string = lletres.getText()

        # Currifiquem
        resultat_terme = self.visit(terme)
        for lletra in reversed(lletres_string):
            resultat_lletra = NodeLletra(lletra)
            resultat_terme = NodeAbstraccio(resultat_lletra, resultat_terme)

        return resultat_terme


def print_arbre(node: Arbre) -> str:
    """
    Aquesta funció rep un arbre com a paràmetre i retorna la representació del arbre en string.
    """
    match node:

        case NodeLletra(val):
            return val

        case NodeAplicacio(esq, dre):
            return ('(') + print_arbre(esq) + print_arbre(dre) + ')'

        case NodeAbstraccio(lletra, terme):
            return '(λ' + print_arbre(lletra) + \
                '.' + print_arbre(terme) + ')'


# --------------------------#
#    FUNCIONS PRINCIPALS    #
# --------------------------#

async def representacio_grafica(node: Arbre, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Rep com a paràmetre un terme de lambda calculus i envía un missatge al usuari amb el graf resultant.
    """
    graf = pydot.Dot(graph_type='digraph', rankdir='TB')

    def crear_graf_recursiu(
            node: Arbre,
            parent: Arbre = None,
            parent_id: str = None,
            map_variables={}):

        node_id = str(uuid.uuid1())  # Generem un ID random per el node

        match node:

            case NodeLletra(val):
                node_label = val

            case NodeAplicacio(esq, dre):
                node_label = '@'
                crear_graf_recursiu(esq, node, node_id, map_variables)
                crear_graf_recursiu(dre, node, node_id, map_variables)
            case NodeAbstraccio(lletra, terme):
                node_label = 'λ' + lletra.val
                map_variables[lletra.val] = node_id
                crear_graf_recursiu(terme, node, node_id, map_variables)

        pydot_node = pydot.Node(node_id, label=node_label, shape='plaintext')
        graf.add_node(pydot_node)

        # Si no es el root, afegim l'aresta
        if parent:
            graf.add_edge(pydot.Edge(parent_id, pydot_node))

        # Si es una variable lligada, la conectem. Això s'ha de fer aquí ja que si no no tenim creat el node.
        if isinstance(node, NodeLletra):
            temp = map_variables.get(node.val)
            if temp:
                graf.add_edge(
                    pydot.Edge(
                        temp,
                        pydot_node,
                        style='dotted',
                        dir='back'))

    crear_graf_recursiu(node)
    graf.write_png('graf_resultant.png')
    await update.message.reply_photo(open('graf_resultant.png', 'rb'))


async def avaluar(terme: Arbre, update: Update, context: ContextTypes.DEFAULT_TYPE) -> Arbre:
    """
    Avalua un terme de lamda calcul fins a un cert nombre màxim de beta-reduccions o fins que no hi hagin més reduccions possibles.
    Retorna el terme avaluat.
    """
    reduccio_aplicada = True
    maxim_iteracions = context.user_data["max_reduccions"]

    while maxim_iteracions > 0 and reduccio_aplicada:
        maxim_iteracions -= 1
        terme, reduccio_aplicada = await avaluar_recursiu(terme, update, context)

        if context.user_data["veure_passos"]:
            await representacio_grafica(terme, update, context)

    if maxim_iteracions == 0:
        missatge = "S'ha arribat al limit de β-reduccions permesses (" + str(context.user_data["max_reduccions"]) + ")."
        await update.message.reply_text(missatge)
    return terme


async def avaluar_recursiu(terme: Arbre, update: Update, context: ContextTypes.DEFAULT_TYPE) -> tuple[Arbre, bool]:
    """
    Avalua fins a com a molt una beta-reducció un terme de lambda calcul.
    Retorna el terme i un boolea que indica si s'ha fet alguna reducció.
    """
    # Si es una lletra cas base, la retornem
    match terme:
        case NodeLletra(val):
            return terme, False

        # Si es una aplicació tenim dos casos
        case NodeAplicacio(esq, dre):

            # Si el terme esquerre es una abstracció, apliquem una β-reducció
            if isinstance(esq, NodeAbstraccio):

                # Generem alpha-conversions si cal
                terme = await alpha_conversions_necessaries(terme, update, context)

                return await beta_reduccio(terme, update, context), True

            # D'altre manera, seguim evaluant.
            else:
                # Logica aqui important per no aplicar 2 beta-reduccions seguides
                # sense voler!

                evaluacio_esquerre, reduccio_a_esquerre = await avaluar_recursiu(esq, update, context)

                # Si a l'esquerre fem una beta-reduccio, ja retornem
                if reduccio_a_esquerre:
                    return NodeAplicacio(evaluacio_esquerre, dre), True

                # D'altre manera, seguim per la dreta
                else:
                    evaluacio_dreta, hi_ha_reduccio_a_dreta = await avaluar_recursiu(dre, update, context)
                    return NodeAplicacio(evaluacio_esquerre, evaluacio_dreta), hi_ha_reduccio_a_dreta

        # Si es una abstraccio, continuem evaluant recursivament
        case NodeAbstraccio(lletra, terme_abstraccio):
            evaluacio_terme, hi_ha_reduccio = await avaluar_recursiu(terme_abstraccio, update, context)
            return NodeAbstraccio(lletra, evaluacio_terme), hi_ha_reduccio


async def beta_reduccio(aplicacio: NodeAplicacio, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Realitza una β-reducció substituint, en el cos de l'abstracció, tota instancia de la capselera pel terme dret de l'aplicació.
    Retorna el terme avaluat.
    """

    # Obtenim el cap i el terme de l'abstracció
    cap = aplicacio.esq.lletra.val
    terme = aplicacio.esq.terme

    # Substituim el cap pel terme dret, sobre el terme esquerre
    terme_substituit = substituir(terme, cap, aplicacio.dre)

    if context.user_data["mostrar_reduccions"]:
        terme_antic = print_arbre(aplicacio)
        terme_nou = print_arbre(terme_substituit)
        missatge = terme_antic + ' -> β -> ' + terme_nou
        await update.message.reply_text(missatge)

    return terme_substituit


async def alpha_conversions_necessaries(terme: NodeAplicacio, update: Update, context: ContextTypes.DEFAULT_TYPE) -> NodeAplicacio:
    """
    Realitza les alpha-conversions necessàries per resoldre conflictes de variables en un terme de lambda calcul.
    Retorna el NodeAplicació amb els conflictes resolts.
    """
    [variable_conflictives, variables_usades] = comprobar_conflicte(terme)

    for variable in variable_conflictives:
        # Generem una variable fresca
        nova_variable = generar_variable_fresca(variables_usades)
        # Substituim totes les instancies de la variable conflictiva per la
        # fresca

        terme_substituit = substituir(
            terme.esq, variable, NodeLletra(nova_variable))

        if context.user_data["mostrar_conversions"]:
            terme_antic = print_arbre(terme.esq)
            terme_nou = print_arbre(terme_substituit)
            missatge = terme_antic + \
                ' -> α(' + variable + '->' + nova_variable + ') -> ' + terme_nou
            await update.message.reply_text(missatge)

        # Preparem per a seguir realitzant alpha-conversions, si calgues.
        terme.esq = terme_substituit
        variables_usades.append(nova_variable)

    return NodeAplicacio(terme.esq, terme.dre)


# --------------------------#
#    FUNCIONS AUXILIARS     #
# --------------------------#

def interseccio_llistes(l1: list, l2: list) -> list:
    """
    Retorna l'interseccio sense repetits de dues llistes
    """
    return [valor for valor in l1 if valor in l2]


def unio_llistes(l1: list, l2: list):
    """
    Retorna l'unió sense repetits de dues llistes
    """
    # Convertir les llistes a conjunts per eliminar els duplicats
    conjunt1 = set(l1)
    conjunt2 = set(l2)

    # Unir els conjunts i convertir el resultat a una llista
    return list(conjunt1.union(conjunt2))


def substituir(terme: Arbre, variable: str, terme_nou: Arbre) -> Arbre:
    """
    Substitueix totes les instàncies de la variable en el terme pel terme_nou.
    Retorna el arbre amb les substitucions fetes.
    """
    match terme:
        case NodeLletra(val):
            if val == variable:
                return terme_nou
            else:
                # Variable no encaixa, retorna el terme original
                return terme

        case NodeAplicacio(esq, dre):
            # Substitueix recursivament en el terme esquerre i dret
            substituit_esq = substituir(esq, variable, terme_nou)
            substituit_dre = substituir(dre, variable, terme_nou)
            return NodeAplicacio(substituit_esq, substituit_dre)

        case NodeAbstraccio(lletra, terme_abstraccio):
            # Substituir recursivament en el cos de l'abstracció
            terme_substituit = substituir(terme_abstraccio, variable, terme_nou)

            # En el cas de que volguem substituir el cap de l'abstracció, sabem que sempre tenim a terme_nou
            # un NodeLletra (com en les alpha-conversions)
            if lletra.val == variable:
                return NodeAbstraccio(terme_nou, terme_substituit)
            else:
                return NodeAbstraccio(lletra, terme_substituit)


def comprobar_conflicte(terme: NodeAplicacio) -> tuple[list[str], list[str]]:
    """
    Comprova els conflictes de variables en una aplicació de lambda calcul.
    Retorna una llista amb les variables conflictives i una llista amb les variables usades.
    """
    # Totes les variables a la dreta poden originar conflicte:
    variables_dre = totes_les_variables(terme.dre)

    # A l'esquerre les que poden originar conflicte son

    variable_que_substituirem = terme.esq.lletra.val
    variables_esq = variables_conflictives(
        terme.esq.terme, variable_que_substituirem, [])

    # L'interseccio d'aquestes llistes es el que pot causar conflicte:
    variable_conflictives = interseccio_llistes(variables_esq, variables_dre)

    # I ens hem de guardar les variables que utilitzem, ja que hem de
    # renombrar amb un nom nou:
    variables_usades = unio_llistes(variables_esq, variables_dre)

    return variable_conflictives, variables_usades


def variables_conflictives(
        terme: Arbre,
        variable_que_substituirem: str,
        variables_vistes: list[str]) -> list[str]:
    """
    Retorna totes les variables que poden originar conflicte en el terme.
    """

    # Les variables que poden originar conflicte son les capsaleres de les abstraccions en el cos de les cuals
    # apareix la variable que substituirem.

    # Si es la lletra que sustituirem, tot fins llavors pot causar conflicte
    match terme:
        case NodeLletra(val):
            if terme.val == variable_que_substituirem:
                return variables_vistes
            else:
                return []

        # Si es una aplicació, acumulem recursivament els conflictes
        case NodeAplicacio(esq, dre):
            result_esq = variables_conflictives(
                esq, variable_que_substituirem, variables_vistes)
            result_dre = variables_conflictives(
                dre, variable_que_substituirem, variables_vistes)
            return unio_llistes(result_esq, result_dre)

        # Si es una abstraccio, acumulem la variable vista i seguim recursivament
        case NodeAbstraccio(lletra, terme_abstraccio):
            val = lletra.val

            result_terme = variables_conflictives(
                terme_abstraccio,
                variable_que_substituirem,
                variables_vistes + [val])
            return result_terme


def totes_les_variables(terme: Arbre) -> list[str]:
    """
    Retorna totes les variables en un terme
    """

    # Si es una lletra, la retornem
    match terme:
        case NodeLletra(val):
            return list(val)

        # Si es una aplicació, acumulem recursivament
        case NodeAplicacio(esq, dre):
            result_esq = totes_les_variables(esq)
            result_dre = totes_les_variables(dre)
            return result_esq + result_dre

        # Si es una abstraccio, continuem acumulant recursivament
        case NodeAbstraccio(lletra, terme_abstraccio):
            val = lletra.val
            result_terme = totes_les_variables(terme_abstraccio)
            return list(val) + result_terme


def generar_variable_fresca(variables_utilitzades: list[str]) -> str:
    """
    Donada una llista de les variables que ja s'estan utilitzant, en genera una nova que no estigui en aquesta
    """
    # Caràcters vàlids per a les variables fresques
    caracters_valids = "abcdefghijklmnopqrstuvwxyz"

    # Buscar un caràcter que no estigui a la llista de variables utilitzades
    for char in caracters_valids:
        if char not in variables_utilitzades:
            return char


# --------------------------#
#      HANDLERS DEL BOT     #
# --------------------------#

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari usa la comanda start, envia un missatge de benvinguda.
    """
    await configuracio_per_defecte(context)
    await update.message.reply_text(
        "Benvingut a LambdaLogic Bot!\n\n"
        "Sóc aquí per ajudar-te amb la compilació de codi Lambda Calculus. Simplement envia el teu codi i et mostraré el resultat.\n\n"
        "Per començar, pots utilitzar la comanda /help per obtenir més informació sobre com utilitzar aquest bot.\n\n"
        "Diverteix-te programant amb Lambda Calculus!"
    )


async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari usa la comanda author, informa del autor.
    """
    await update.message.reply_text(
        "Aquest bot ha estat creat per Oriol Miró. Si tens algun suggeriment o problema, si us plau, posa't en contacte amb mi. Gràcies!"
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari usa la comanda help, mostra informació sobre el que es pot fer.
    """
    await update.message.reply_text(
        "Benvingut a l'ajuda de LambdaLogic Bot!\n\n"
        "Aquest bot t'ajudarà a compilar codi Lambda Calculus. Aquí tens algunes comandes que pots utilitzar:\n\n"
        "- /start: Inicia la conversa amb el bot.\n"
        "- /author: Mostra informació sobre l'autor del bot.\n- /help: Mostra aquest missatge d'ajuda.\n"
        "- /settings: Mostra els ajustos possibles sobre el bot.\n- /macros: Mostra una llista de totes les macros disponibles.\n"
        "- Envia el teu codi Lambda Calculus per obtenir-ne el resultat.\n\n"
        "Si tens algun problema o dubte, no dubtis en preguntar. Que t'ho passis bé programant amb Lambda Calculus!"
    )

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari usa la comanda settigns. Permet configurar el comportament del bot.
    """
    try:
        [_, comanda, valor] = update.message.text.split()
    except:
        await update.message.reply_text(
            "Les opcions que hi han disponibles son:\n\n"
            "- max_reduccions <valor>: Indica el nombre màxim de reduccions a aplicar sobre un terme \n"
            "- mostrar_reduccions <si/no>: Indica si vol que es mostrin les beta reduccions \n"
            "- mostrar_conversions <si/no>: Indica si vol que es mostrin les alpha conversions \n"
            "- veure_passos <si/no>: Indica si vol que es mostri el arbre graficament a cada pas\n"
            "- mostrar_info_errors <si/no>: Indica si vol que es mostri informació dels errors en les expressions"
        )
        return

    # Sempre cridem aquesta funció al inici de les comandes que accedeixen context.user_data per evitar errors
    await configuracio_per_defecte(context)

    if comanda == "max_reduccions":
        context.user_data["max_reduccions"] = int(valor)
        await update.message.reply_text("Ajust canviat correctament!")
        return

    # Totes les demés comandes només tenen valors si / no
    if valor != "si" and valor != "no":
        update.message.reply_text("Setting invalid!")

    if comanda == "mostrar_reduccions":
        context.user_data["mostrar_reduccions"] = (valor == "si")
    if comanda == "mostrar_conversions":
        context.user_data["mostrar_conversions"] = (valor == "si")
    if comanda == "veure_passos":
        context.user_data["veure_passos"] = (valor == "si")
    if comanda == "mostrar_info_errors":
        context.user_data["mostrar_info_errors"] = (valor == "si")

    await update.message.reply_text("Ajust canviat correctament!")


async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari usa la comanda macros, envia un missatge amb els macros definits, si n'hi han.
    """

    # Sempre cridem aquesta funció al inici de les comandes que accedeixen context.user_data per evitar errors
    await configuracio_per_defecte(context)

    taula_macros = context.user_data["macros"]
    missatge = "Macros definits:\n"
    for clau in taula_macros:
        nova_linea = clau + '≡' + print_arbre(taula_macros[clau]) + '\n'
        missatge = missatge + nova_linea

    await update.message.reply_text(missatge)

async def carregar_macros_per_defecte(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Funció per carregar una serie de macros per testejar més facilment el programa
    """

    # Inicialització
    context.user_data["macros"] = {}

    # Lògica:
    context.user_data["macros"]["TRUE"] = NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAbstraccio(lletra=NodeLletra(val='y'), terme=NodeLletra(val='x')))
    context.user_data["macros"]["FALSE"] = NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAbstraccio(lletra=NodeLletra(val='y'), terme=NodeLletra(val='y')))
    context.user_data["macros"]["NOT"] = NodeAbstraccio(lletra=NodeLletra(val='a'), terme=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='a'), dre=NodeAbstraccio(lletra=NodeLletra(val='b'), terme=NodeAbstraccio(lletra=NodeLletra(val='c'), terme=NodeLletra(val='c')))), dre=NodeAbstraccio(lletra=NodeLletra(val='d'), terme=NodeAbstraccio(lletra=NodeLletra(val='e'), terme=NodeLletra(val='d')))))
    context.user_data["macros"]["AND"] = NodeAbstraccio(lletra=NodeLletra(val='a'), terme=NodeAbstraccio(lletra=NodeLletra(val='b'), terme=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='a'), dre=NodeLletra(val='b')), dre=NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAbstraccio(lletra=NodeLletra(val='y'), terme=NodeLletra(val='y'))))))
    context.user_data["macros"]["OR"] = NodeAbstraccio(lletra=NodeLletra(val='p'), terme=NodeAbstraccio(lletra=NodeLletra(val='q'), terme=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='p'), dre=NodeLletra(val='p')), dre=NodeLletra(val='q'))))

    # Aritmetica:
    context.user_data["macros"]["N1"] = NodeAbstraccio(lletra=NodeLletra(val='s'), terme=NodeAbstraccio(lletra=NodeLletra(val='z'), terme=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeLletra(val='z'))))
    context.user_data["macros"]["N2"] = NodeAbstraccio(lletra=NodeLletra(val='s'), terme=NodeAbstraccio(lletra=NodeLletra(val='z'), terme=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeLletra(val='z')))))
    context.user_data["macros"]["N3"] = NodeAbstraccio(lletra=NodeLletra(val='s'), terme=NodeAbstraccio(lletra=NodeLletra(val='z'), terme=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeLletra(val='z'))))))
    context.user_data["macros"]["N4"] = NodeAbstraccio(lletra=NodeLletra(val='s'), terme=NodeAbstraccio(lletra=NodeLletra(val='z'), terme=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeAplicacio(esq=NodeLletra(val='s'), dre=NodeLletra(val='z')))))))
    context.user_data["macros"]["SUCC"] = NodeAbstraccio(lletra=NodeLletra(val='a'), terme=NodeAbstraccio(lletra=NodeLletra(val='b'), terme=NodeAbstraccio(lletra=NodeLletra(val='c'), terme=NodeAplicacio(esq=NodeLletra(val='b'), dre=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='a'), dre=NodeLletra(val='b')), dre=NodeLletra(val='c'))))))
    context.user_data["macros"]["+"] = NodeAbstraccio(lletra=NodeLletra(val='p'), terme=NodeAbstraccio(lletra=NodeLletra(val='q'), terme=NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAbstraccio(lletra=NodeLletra(val='y'), terme=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='p'), dre=NodeLletra(val='x')), dre=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='q'), dre=NodeLletra(val='x')), dre=NodeLletra(val='y')))))))
    context.user_data["macros"]["*"] = NodeAbstraccio(lletra=NodeLletra(val='n'), terme=NodeAbstraccio(lletra=NodeLletra(val='m'), terme=NodeAbstraccio(lletra=NodeLletra(val='f'), terme=NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAplicacio(esq=NodeAplicacio(esq=NodeLletra(val='n'), dre=NodeAplicacio(esq=NodeLletra(val='m'), dre=NodeLletra(val='f'))), dre=NodeLletra(val='x'))))))

    # Altres:
    context.user_data["macros"]["ID"] = NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeLletra(val='x'))
    context.user_data["macros"]["TWICE"] = NodeAbstraccio(lletra=NodeLletra(val='f'), terme=NodeAbstraccio(lletra=NodeLletra(val='x'), terme=NodeAplicacio(esq=NodeLletra(val='f'), dre=NodeAplicacio(esq=NodeLletra(val='f'), dre=NodeLletra(val='x')))))

async def tractar_missatge_expressio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Funcio que s'activa quan l'usuari introdueix una expressio en lambda calcul.
    Avalua l'expressió i mostra el resultat final al usuari.
    """

    # He afegit un handler d'errors per poder enviar missatges descriptius d'aquests.
    # Al ser una classe molt especifica, he decidir no ferla general.

    errors = []

    class CustomErrorListener(ErrorListener):
        """
        Aquesta classe serveix unicament per acumular els errors de sintaxis en una llista, i poder-los mostrar al usuari posteriorment.
        """
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            errors.append(f"Error de sintaxis en columna {column}: {msg}")

    # Sempre cridem aquesta funció al inici de les comandes que accedeixen context.user_data per evitar errors.
    await configuracio_per_defecte(context)

    msg = InputStream(update.message.text)

    lexer = lcLexer(msg)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.root()

    # Logica pels errors de sintaxis.
    if parser.getNumberOfSyntaxErrors() != 0:
        await update.message.reply_text("ERROR SINTAXIS\nEl que has introduit no es una expressió o una definició de macro correcte")

        if context.user_data["mostrar_info_errors"]:
            missatge = f"Hi han {parser.getNumberOfSyntaxErrors()} errors de sintaxi.\n"

            for error_especific in errors:
                missatge = missatge + f"{error_especific}\n"

            await update.message.reply_text(missatge)
        return

    # Li pasem la taula de macros del usuari perque el visitador la pugui usar.
    tree_visitor = TreeVisitor(context.user_data["macros"])

    # Creem el arbre corresponen al terme.
    try:
        arbre_terme = tree_visitor.visit(tree)
    except Exception as error:
        await update.message.reply_text("ERROR EXPRESSIO\nEl que has introduit no es una expressió o una definició de macro correcte")

        if context.user_data["mostrar_info_errors"]:
            await update.message.reply_text(f"error en {error}")
        return

    if arbre_terme:
        missatge_arbre = print_arbre(arbre_terme)
        await update.message.reply_text(missatge_arbre)
        await representacio_grafica(arbre_terme, update, context)

        arbre_terme_avaluat = await avaluar(arbre_terme, update, context)

        missatge_avaluacio = print_arbre(arbre_terme_avaluat)
        await update.message.reply_text(missatge_avaluacio)
        await representacio_grafica(arbre_terme_avaluat, update, context)
    else:
        # Entrem aqui si el terme no era la definició d'un macro
        await update.message.reply_text("Macro afegit correctament!")

async def configuracio_per_defecte(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Funció per definit la configuració per defecte del bot en aquells llocs on on s'hagi fet encara.
    """

    if "macros" not in context.user_data:
        await carregar_macros_per_defecte(context)

    if "max_reduccions" not in context.user_data:
        context.user_data["max_reduccions"] = 10

    if "mostrar_reduccions" not in context.user_data:
        context.user_data["mostrar_reduccions"] = True

    if "mostrar_conversions" not in context.user_data:
        context.user_data["mostrar_conversions"] = True

    if "veure_passos" not in context.user_data:
        context.user_data["veure_passos"] = False

    if "mostrar_info_errors" not in context.user_data:
        context.user_data["mostrar_info_errors"] = True


# --------------------------#
#           MAIN            #
# --------------------------#

def main() -> None:
    """
    Main. Permet iniciar el bot i definit tots els seus comportaments.
    """
    # declara una constant amb el access token que llegeix de token.txt
    # open("token.txt").read().strip()
    TOKEN = "6061831017:AAFPEzRNC7kdOOfl9zld29S1oQPkngXz5TY"

    # crea objecte per treballar amb Telegram
    application = Application.builder().token(TOKEN).build()

    # Diferentes comandes
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('author', author))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('settings', settings))
    application.add_handler(CommandHandler('macros', macros))

    # Si ens entra text sense comanda, es una expressio.
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            tractar_missatge_expressio))

    # engega el bot
    application.run_polling()


if __name__ == '__main__':
    print(('[LambdaLogicBot] Start...'))
    main()
