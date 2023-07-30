from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor


class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0
        # self.taula_continguts = {}

    def visitExpressioBinaria(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + str(operador))
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())
    

class EvalVisitor(exprsVisitor):
    def __init__(self):
        self.taula_continguts = {}

    def visitExpressioBinaria(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        
        if str(operador) == '+':
            return  self.visit(expressio1) + self.visit(expressio2)
        elif str(operador) == '-':
            return  self.visit(expressio1) - self.visit(expressio2)
        elif str(operador) == '*':
            return  self.visit(expressio1) * self.visit(expressio2)
        elif str(operador) == '/':
            return  self.visit(expressio1) / self.visit(expressio2)
        elif str(operador) == '^':
            return  self.visit(expressio1) ** self.visit(expressio2)
        
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())

    def visitIdentificador(self, ctx):
        [variable] = list(ctx.getChildren())
        return self.taula_continguts[variable.getText()]

    def visitAssignacio(self, ctx):
        [variable, _, expressio] = list(ctx.getChildren())
        self.taula_continguts[variable.getText()] = self.visit(expressio)

    def visitWrite(self, ctx):
        [_, expressio] = list(ctx.getChildren())
        result = self.visit(expressio)
        print(result)

    def visitCondicial(self, ctx):
        [_, condicio, _, instruccions, _] = list(ctx.getChildren())
        if self.visit(condicio):
            self.visit(instruccions)

    def visitBucle(self, ctx):
        [_, condicio, _, instruccions, _] = list(ctx.getChildren())
        while self.visit(condicio):
            self.visit(instruccions)

    def visitIgualtat(self, ctx):
        [expr1, _, expr2] = list(ctx.getChildren())
        return self.visit(expr1) == self.visit(expr2)

    def visitDesigualtat(self, ctx):
        [expr1, _, expr2] = list(ctx.getChildren())
        return self.visit(expr1) != self.visit(expr2)

input_stream = FileStream("code.txt")

lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

#if parser.getNumberOfSyntaxErrors() == 0:

# Visitador per construir els ABRES visuals
# visitor_tree = TreeVisitor()
# visitor_tree.visit(tree)

# Visitador per EVALUAR l'abtre
visitor_evaluation = EvalVisitor()
visitor_evaluation.visit(tree)


#else:
#print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
#print(tree.toStringTree(recog=parser))