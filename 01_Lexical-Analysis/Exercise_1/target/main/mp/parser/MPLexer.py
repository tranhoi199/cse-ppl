# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("\u0087\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\7\bA\n\b\f\b\16\bD\13\b\3\t\5\tG\n\t\3\t\6\tJ\n\t\r\t")
        buf.write("\16\tK\3\t\3\t\6\tP\n\t\r\t\16\tQ\5\tT\n\t\3\t\3\t\5\t")
        buf.write("X\n\t\3\t\6\t[\n\t\r\t\16\t\\\5\t_\n\t\3\n\6\nb\n\n\r")
        buf.write("\n\16\nc\3\13\3\13\3\13\3\13\7\13j\n\13\f\13\16\13m\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\6\21|\n\21\r\21\16\21}\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\2\2\25\3\3\5\2\7\2\t\2\13\4\r\5\17")
        buf.write("\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%")
        buf.write("\21\'\22\3\2\t\3\2c|\3\2\62;\4\2--//\3\2\60\60\3\2gg\3")
        buf.write("\2))\5\2\13\f\17\17\"\"\2\u0090\2\3\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5.\3\2\2\2\7\60\3\2\2\2\t")
        buf.write("\62\3\2\2\2\13\64\3\2\2\2\r8\3\2\2\2\17=\3\2\2\2\21F\3")
        buf.write("\2\2\2\23a\3\2\2\2\25e\3\2\2\2\27p\3\2\2\2\31r\3\2\2\2")
        buf.write("\33t\3\2\2\2\35v\3\2\2\2\37x\3\2\2\2!{\3\2\2\2#\u0081")
        buf.write("\3\2\2\2%\u0083\3\2\2\2\'\u0085\3\2\2\2)*\7o\2\2*+\7c")
        buf.write("\2\2+,\7k\2\2,-\7p\2\2-\4\3\2\2\2./\t\2\2\2/\6\3\2\2\2")
        buf.write("\60\61\t\3\2\2\61\b\3\2\2\2\62\63\t\4\2\2\63\n\3\2\2\2")
        buf.write("\64\65\7k\2\2\65\66\7p\2\2\66\67\7v\2\2\67\f\3\2\2\28")
        buf.write("9\7x\2\29:\7q\2\2:;\7k\2\2;<\7f\2\2<\16\3\2\2\2=B\5\5")
        buf.write("\3\2>A\5\5\3\2?A\5\7\4\2@>\3\2\2\2@?\3\2\2\2AD\3\2\2\2")
        buf.write("B@\3\2\2\2BC\3\2\2\2C\20\3\2\2\2DB\3\2\2\2EG\5\t\5\2F")
        buf.write("E\3\2\2\2FG\3\2\2\2GI\3\2\2\2HJ\5\7\4\2IH\3\2\2\2JK\3")
        buf.write("\2\2\2KI\3\2\2\2KL\3\2\2\2LS\3\2\2\2MO\t\5\2\2NP\5\7\4")
        buf.write("\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2S")
        buf.write("M\3\2\2\2ST\3\2\2\2T^\3\2\2\2UW\t\6\2\2VX\5\t\5\2WV\3")
        buf.write("\2\2\2WX\3\2\2\2XZ\3\2\2\2Y[\5\7\4\2ZY\3\2\2\2[\\\3\2")
        buf.write("\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^U\3\2\2\2^_\3\2\2")
        buf.write("\2_\22\3\2\2\2`b\t\3\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2")
        buf.write("cd\3\2\2\2d\24\3\2\2\2ek\t\7\2\2fj\n\7\2\2gh\t\7\2\2h")
        buf.write("j\t\7\2\2if\3\2\2\2ig\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3")
        buf.write("\2\2\2ln\3\2\2\2mk\3\2\2\2no\t\7\2\2o\26\3\2\2\2pq\7*")
        buf.write("\2\2q\30\3\2\2\2rs\7+\2\2s\32\3\2\2\2tu\7}\2\2u\34\3\2")
        buf.write("\2\2vw\7\177\2\2w\36\3\2\2\2xy\7=\2\2y \3\2\2\2z|\t\b")
        buf.write("\2\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2")
        buf.write("\2\2\177\u0080\b\21\2\2\u0080\"\3\2\2\2\u0081\u0082\13")
        buf.write("\2\2\2\u0082$\3\2\2\2\u0083\u0084\13\2\2\2\u0084&\3\2")
        buf.write("\2\2\u0085\u0086\13\2\2\2\u0086(\3\2\2\2\20\2@BFKQSW\\")
        buf.write("^cik}\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    REAL = 5
    INTLIT = 6
    STRING = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    WS = 13
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "REAL", "INTLIT", "STRING", "LB", 
            "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "LETTER", "DIGIT", "SIGN", "INTTYPE", "VOIDTYPE", 
                  "ID", "REAL", "INTLIT", "STRING", "LB", "RB", "LP", "RP", 
                  "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


