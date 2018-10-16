# Generated from c:\Users\ACER\Desktop\ppl\exercises\AST2\q2tn\src\main\mp\parser\MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("=\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\31\n\2\r\2")
        buf.write("\16\2\32\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\6\n\66\n\n\r\n\16\n\67\3\n\3\n\3\13\3\13\2\2\f\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\4\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2>\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\30\3\2\2\2")
        buf.write("\5\34\3\2\2\2\7$\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2")
        buf.write("\2\2\17/\3\2\2\2\21\62\3\2\2\2\23\65\3\2\2\2\25;\3\2\2")
        buf.write("\2\27\31\t\2\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2")
        buf.write("\2\2\32\33\3\2\2\2\33\4\3\2\2\2\34\35\7k\2\2\35\36\7p")
        buf.write("\2\2\36\37\7v\2\2\37 \7g\2\2 !\7i\2\2!\"\7g\2\2\"#\7t")
        buf.write("\2\2#\6\3\2\2\2$%\7t\2\2%&\7g\2\2&\'\7c\2\2\'(\7n\2\2")
        buf.write("(\b\3\2\2\2)*\7]\2\2*\n\3\2\2\2+,\7_\2\2,\f\3\2\2\2-.")
        buf.write("\7/\2\2.\16\3\2\2\2/\60\7\60\2\2\60\61\7\60\2\2\61\20")
        buf.write("\3\2\2\2\62\63\7.\2\2\63\22\3\2\2\2\64\66\t\3\2\2\65\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2")
        buf.write("\2\29:\b\n\2\2:\24\3\2\2\2;<\13\2\2\2<\26\3\2\2\2\5\2")
        buf.write("\32\67\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    INTTYPE = 2
    FLOATTYPE = 3
    LSB = 4
    RSB = 5
    SIGN = 6
    DOTDOT = 7
    COMMA = 8
    WS = 9
    ERROR_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'real'", "'['", "']'", "'-'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "INTTYPE", "FLOATTYPE", "LSB", "RSB", "SIGN", "DOTDOT", 
            "COMMA", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "INTTYPE", "FLOATTYPE", "LSB", "RSB", "SIGN", 
                  "DOTDOT", "COMMA", "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


