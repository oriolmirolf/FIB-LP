# Generated from exprs.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\4\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\78\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\5\nD\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\nU\n\n\f\n\16\nX\13\n\3\n\2\3\22")
        buf.write("\13\2\4\6\b\n\f\16\20\22\2\2\2[\2\24\3\2\2\2\4\32\3\2")
        buf.write("\2\2\6!\3\2\2\2\b#\3\2\2\2\n)\3\2\2\2\f\67\3\2\2\2\16")
        buf.write("9\3\2\2\2\20=\3\2\2\2\22C\3\2\2\2\24\25\5\4\3\2\25\26")
        buf.write("\7\2\2\3\26\3\3\2\2\2\27\31\5\6\4\2\30\27\3\2\2\2\31\34")
        buf.write("\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2\2\34\32")
        buf.write("\3\2\2\2\35\"\5\16\b\2\36\"\5\20\t\2\37\"\5\b\5\2 \"\5")
        buf.write("\n\6\2!\35\3\2\2\2!\36\3\2\2\2!\37\3\2\2\2! \3\2\2\2\"")
        buf.write("\7\3\2\2\2#$\7\3\2\2$%\5\f\7\2%&\7\4\2\2&\'\5\4\3\2\'")
        buf.write("(\7\5\2\2(\t\3\2\2\2)*\7\6\2\2*+\5\f\7\2+,\7\7\2\2,-\5")
        buf.write("\4\3\2-.\7\5\2\2.\13\3\2\2\2/\60\5\22\n\2\60\61\7\b\2")
        buf.write("\2\61\62\5\22\n\2\628\3\2\2\2\63\64\5\22\n\2\64\65\7\t")
        buf.write("\2\2\65\66\5\22\n\2\668\3\2\2\2\67/\3\2\2\2\67\63\3\2")
        buf.write("\2\28\r\3\2\2\29:\7\22\2\2:;\7\n\2\2;<\5\22\n\2<\17\3")
        buf.write("\2\2\2=>\7\13\2\2>?\5\22\n\2?\21\3\2\2\2@A\b\n\1\2AD\7")
        buf.write("\21\2\2BD\7\22\2\2C@\3\2\2\2CB\3\2\2\2DV\3\2\2\2EF\f\t")
        buf.write("\2\2FG\7\f\2\2GU\5\22\n\tHI\f\b\2\2IJ\7\r\2\2JU\5\22\n")
        buf.write("\tKL\f\7\2\2LM\7\16\2\2MU\5\22\n\bNO\f\6\2\2OP\7\17\2")
        buf.write("\2PU\5\22\n\7QR\f\5\2\2RS\7\20\2\2SU\5\22\n\6TE\3\2\2")
        buf.write("\2TH\3\2\2\2TK\3\2\2\2TN\3\2\2\2TQ\3\2\2\2UX\3\2\2\2V")
        buf.write("T\3\2\2\2VW\3\2\2\2W\23\3\2\2\2XV\3\2\2\2\b\32!\67CTV")
        return buf.getvalue()


class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'end'", "'while'", 
                     "'do'", "'='", "'<>'", "':='", "'write'", "'^'", "'/'", 
                     "'*'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "WS" ]

    RULE_root = 0
    RULE_instruccions = 1
    RULE_instruccio = 2
    RULE_condicial = 3
    RULE_bucle = 4
    RULE_condicio = 5
    RULE_assignacio = 6
    RULE_write = 7
    RULE_expr = 8

    ruleNames =  [ "root", "instruccions", "instruccio", "condicial", "bucle", 
                   "condicio", "assignacio", "write", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    NUM=15
    ID=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


        def EOF(self):
            return self.getToken(exprsParser.EOF, 0)

        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.instruccions()
            self.state = 19
            self.match(exprsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.InstruccioContext)
            else:
                return self.getTypedRuleContext(exprsParser.InstruccioContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_instruccions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccions" ):
                return visitor.visitInstruccions(self)
            else:
                return visitor.visitChildren(self)




    def instruccions(self):

        localctx = exprsParser.InstruccionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << exprsParser.T__0) | (1 << exprsParser.T__3) | (1 << exprsParser.T__8) | (1 << exprsParser.ID))) != 0):
                self.state = 21
                self.instruccio()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignacio(self):
            return self.getTypedRuleContext(exprsParser.AssignacioContext,0)


        def write(self):
            return self.getTypedRuleContext(exprsParser.WriteContext,0)


        def condicial(self):
            return self.getTypedRuleContext(exprsParser.CondicialContext,0)


        def bucle(self):
            return self.getTypedRuleContext(exprsParser.BucleContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_instruccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccio" ):
                return visitor.visitInstruccio(self)
            else:
                return visitor.visitChildren(self)




    def instruccio(self):

        localctx = exprsParser.InstruccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccio)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assignacio()
                pass
            elif token in [exprsParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.write()
                pass
            elif token in [exprsParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.condicial()
                pass
            elif token in [exprsParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.bucle()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(exprsParser.CondicioContext,0)


        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_condicial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicial" ):
                return visitor.visitCondicial(self)
            else:
                return visitor.visitChildren(self)




    def condicial(self):

        localctx = exprsParser.CondicialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(exprsParser.T__0)
            self.state = 34
            self.condicio()
            self.state = 35
            self.match(exprsParser.T__1)
            self.state = 36
            self.instruccions()
            self.state = 37
            self.match(exprsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BucleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(exprsParser.CondicioContext,0)


        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_bucle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle" ):
                return visitor.visitBucle(self)
            else:
                return visitor.visitChildren(self)




    def bucle(self):

        localctx = exprsParser.BucleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bucle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(exprsParser.T__3)
            self.state = 40
            self.condicio()
            self.state = 41
            self.match(exprsParser.T__4)
            self.state = 42
            self.instruccions()
            self.state = 43
            self.match(exprsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_condicio

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IgualtatContext(CondicioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondicioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualtat" ):
                return visitor.visitIgualtat(self)
            else:
                return visitor.visitChildren(self)


    class DesigualtatContext(CondicioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondicioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesigualtat" ):
                return visitor.visitDesigualtat(self)
            else:
                return visitor.visitChildren(self)



    def condicio(self):

        localctx = exprsParser.CondicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicio)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = exprsParser.IgualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(exprsParser.T__5)
                self.state = 47
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = exprsParser.DesigualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(exprsParser.T__6)
                self.state = 51
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_assignacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)




    def assignacio(self):

        localctx = exprsParser.AssignacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(exprsParser.ID)
            self.state = 56
            self.match(exprsParser.T__7)
            self.state = 57
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = exprsParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(exprsParser.T__8)
            self.state = 60
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class ExpressioBinariaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressioBinaria" ):
                return visitor.visitExpressioBinaria(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.NUM]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(exprsParser.NUM)
                pass
            elif token in [exprsParser.ID]:
                localctx = exprsParser.IdentificadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(exprsParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 68
                        self.match(exprsParser.T__9)
                        self.state = 69
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 71
                        self.match(exprsParser.T__10)
                        self.state = 72
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 74
                        self.match(exprsParser.T__11)
                        self.state = 75
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        self.match(exprsParser.T__12)
                        self.state = 78
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 80
                        self.match(exprsParser.T__13)
                        self.state = 81
                        self.expr(4)
                        pass

             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




