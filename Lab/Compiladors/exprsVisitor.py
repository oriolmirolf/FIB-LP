# Generated from exprs.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#instruccions.
    def visitInstruccions(self, ctx:exprsParser.InstruccionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#instruccio.
    def visitInstruccio(self, ctx:exprsParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicial.
    def visitCondicial(self, ctx:exprsParser.CondicialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#bucle.
    def visitBucle(self, ctx:exprsParser.BucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#igualtat.
    def visitIgualtat(self, ctx:exprsParser.IgualtatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#desigualtat.
    def visitDesigualtat(self, ctx:exprsParser.DesigualtatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#expressioBinaria.
    def visitExpressioBinaria(self, ctx:exprsParser.ExpressioBinariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#identificador.
    def visitIdentificador(self, ctx:exprsParser.IdentificadorContext):
        return self.visitChildren(ctx)



del exprsParser