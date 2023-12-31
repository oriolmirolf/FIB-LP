# Generated from exprs.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\6\20T\n\20\r\20\16\20U\3\21\6\21")
        buf.write("Y\n\21\r\21\16\21Z\3\22\6\22^\n\22\r\22\16\22_\3\22\3")
        buf.write("\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2\62;")
        buf.write("\4\2C\\c|\5\2\13\f\17\17\"\"\2e\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5(\3\2\2\2\7-")
        buf.write("\3\2\2\2\t\61\3\2\2\2\13\67\3\2\2\2\r:\3\2\2\2\17<\3\2")
        buf.write("\2\2\21?\3\2\2\2\23B\3\2\2\2\25H\3\2\2\2\27J\3\2\2\2\31")
        buf.write("L\3\2\2\2\33N\3\2\2\2\35P\3\2\2\2\37S\3\2\2\2!X\3\2\2")
        buf.write("\2#]\3\2\2\2%&\7k\2\2&\'\7h\2\2\'\4\3\2\2\2()\7v\2\2)")
        buf.write("*\7j\2\2*+\7g\2\2+,\7p\2\2,\6\3\2\2\2-.\7g\2\2./\7p\2")
        buf.write("\2/\60\7f\2\2\60\b\3\2\2\2\61\62\7y\2\2\62\63\7j\2\2\63")
        buf.write("\64\7k\2\2\64\65\7n\2\2\65\66\7g\2\2\66\n\3\2\2\2\678")
        buf.write("\7f\2\289\7q\2\29\f\3\2\2\2:;\7?\2\2;\16\3\2\2\2<=\7>")
        buf.write("\2\2=>\7@\2\2>\20\3\2\2\2?@\7<\2\2@A\7?\2\2A\22\3\2\2")
        buf.write("\2BC\7y\2\2CD\7t\2\2DE\7k\2\2EF\7v\2\2FG\7g\2\2G\24\3")
        buf.write("\2\2\2HI\7`\2\2I\26\3\2\2\2JK\7\61\2\2K\30\3\2\2\2LM\7")
        buf.write(",\2\2M\32\3\2\2\2NO\7/\2\2O\34\3\2\2\2PQ\7-\2\2Q\36\3")
        buf.write("\2\2\2RT\t\2\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2")
        buf.write("\2V \3\2\2\2WY\t\3\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z")
        buf.write("[\3\2\2\2[\"\3\2\2\2\\^\t\4\2\2]\\\3\2\2\2^_\3\2\2\2_")
        buf.write("]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\b\22\2\2b$\3\2\2\2\6\2")
        buf.write("UZ_\3\b\2\2")
        return buf.getvalue()


class exprsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    NUM = 15
    ID = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'then'", "'end'", "'while'", "'do'", "'='", "'<>'", 
            "':='", "'write'", "'^'", "'/'", "'*'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "NUM", "ID", "WS" ]

    grammarFileName = "exprs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


