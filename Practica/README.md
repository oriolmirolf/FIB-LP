# LambdaLogic Bot

LambdaLogic Bot és un bot de Telegram que permet compilar codi de Lambda Calculus. Aquest repositori conté el codi font per al funcionament del bot.

## Funció

Aquest bot permet avaluar expressions en Lambda Calcul fins a la seva forma normal o fins a un límit de lambda reduccions. Mostra un graf que representa l'expressió al principi i al final, i aquest es pot mostrar a cada pas habilitant l'opció pertinent en /settings.

Malgrat no estar molt polit, també efectua control d'errors, especialment de sintaxi, i detecta i informa d'alguns errors en les expressions.

## Ús
(En Linux)
Una vegada es tenen tots els requisits, descomprimir el projecte en una carpeta i executar
```shell
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
```
per generar tots els fichers. Després, amb
```shell
python3 achurch.py
```
El bot començarà a executar-se.


## Comandes disponibles i funcionalitats

El bot respon a les següents comandes:

- /start: Inicia la conversa amb el bot i envia un missatge de benvinguda.
- /author: Mostra informació sobre l'autor del bot.
- /help: Mostra informació sobre el que es pot fer amb el bot i una llista de les comandes disponibles.
- /settings: Permet configurar el comportament del bot.
- /macros: Mostra una llista de les macros definides.
- Enviar una expressió de Lambda Calculus: Avalua l'expressió i mostra el resultat final.

## Configuració del bot

La comanda /settings permet configurar el comportament del bot. S'usa fent /settings Les opcions disponibles són:

- max_reduccions: Indica el nombre màxim de reduccions a aplicar sobre un terme.
- mostrar_reduccions: Indica si es volen mostrar les beta reduccions.
- mostrar_conversions: Indica si es volen mostrar les alpha conversions.
- veure_passos: Indica si es vol mostrar l'arbre gràficament a cada pas.
- mostrar_info_errors: Indica si es vol mostrar informació dels errors en les expressions.

## Macros predefinits

He considerat que seria molt útil tenir una sèrie de macros precarregats. Les macros predefinides són:

### Logics:
- TRUE: Valor lògic True.
- FALSE: Valor lògic False.
- NOT: Funció prefixa que representa l'operació lògica not.
- AND: Funció prefixa que representa l'operació lògica and.
- OR: Funció prefixa que representa l'operació lògica or.
### Aritmètics:
- N1: Natural 1.
- N2: Natural 2.
- N3: Natural 3.
- N4: Natural 4.
- SUCC: Funció prefixa que retorna el successor d'un natural.
- +: Funció infixa que retorna la suma de dos naturals.
- *: Funció infixa que retorna el producte de dos naturals.
### Altres:
- ID: Funció identitat
- TWICE: Funció que donada una funció i un argument aplica la funció dos cops sobre l'argument.

## Requisits
Aquest projecte s'ha desenvolupat amb les següents llibreries
- python 3.10
- antlr 4.13
- antlr4-python3-runtime 4.13
- python-telegram-bot 20.03
- pydot 1.4.2
- graphviz 2.43.0
- uuid 1.30

## Control d'errors
Per falta de temps no s'ha pogut arribar a la qualitat desitjada de control d'errors. Tot i això, detecta i informa l'usuari correctament de la majoria d'errors de sintaxi (tals com usar dues \ consecutives) o en les expressions (tals com usar una macro no definida).

Falla en casos com si s'introdueix una cosa com "n123" ho tracta com si fos únicament l'expressió "n"

## Coses a millorar
De tenir més temps, m'hauria agradat introduir les següents funcionalitats
- Millorar el control d'errors
- Afegir una opció per, al definir un macro, avaluar aquest fins a la seva forma normal (si es pot)