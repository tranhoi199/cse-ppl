# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\7\b?\n\b\f\b\16")
        buf.write("\bB\13\b\3\t\5\tE\n\t\3\t\6\tH\n\t\r\t\16\tI\3\t\3\t\6")
        buf.write("\tN\n\t\r\t\16\tO\5\tR\n\t\3\t\3\t\5\tV\n\t\3\t\6\tY\n")
        buf.write("\t\r\t\16\tZ\5\t]\n\t\3\n\6\n`\n\n\r\n\16\na\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20o\n\20\r")
        buf.write("\20\16\20p\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\2\2")
        buf.write("\24\3\3\5\4\7\5\t\2\13\2\r\2\17\6\21\7\23\b\25\t\27\n")
        buf.write("\31\13\33\f\35\r\37\16!\17#\20%\21\3\2\b\3\2c|\3\2\62")
        buf.write(";\4\2--//\3\2\60\60\3\2gg\5\2\13\f\17\17\"\"\2\u0081\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5,\3\2\2\2\7\60\3\2")
        buf.write("\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r9\3\2\2\2\17;\3\2\2\2")
        buf.write("\21D\3\2\2\2\23_\3\2\2\2\25c\3\2\2\2\27e\3\2\2\2\31g\3")
        buf.write("\2\2\2\33i\3\2\2\2\35k\3\2\2\2\37n\3\2\2\2!t\3\2\2\2#")
        buf.write("v\3\2\2\2%x\3\2\2\2\'(\7o\2\2()\7c\2\2)*\7k\2\2*+\7p\2")
        buf.write("\2+\4\3\2\2\2,-\7k\2\2-.\7p\2\2./\7v\2\2/\6\3\2\2\2\60")
        buf.write("\61\7x\2\2\61\62\7q\2\2\62\63\7k\2\2\63\64\7f\2\2\64\b")
        buf.write("\3\2\2\2\65\66\t\2\2\2\66\n\3\2\2\2\678\t\3\2\28\f\3\2")
        buf.write("\2\29:\t\4\2\2:\16\3\2\2\2;@\5\t\5\2<?\5\t\5\2=?\5\13")
        buf.write("\6\2><\3\2\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2")
        buf.write("A\20\3\2\2\2B@\3\2\2\2CE\5\r\7\2DC\3\2\2\2DE\3\2\2\2E")
        buf.write("G\3\2\2\2FH\5\13\6\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3")
        buf.write("\2\2\2JQ\3\2\2\2KM\t\5\2\2LN\5\13\6\2ML\3\2\2\2NO\3\2")
        buf.write("\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QK\3\2\2\2QR\3\2\2\2")
        buf.write("R\\\3\2\2\2SU\t\6\2\2TV\5\r\7\2UT\3\2\2\2UV\3\2\2\2VX")
        buf.write("\3\2\2\2WY\5\13\6\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3")
        buf.write("\2\2\2[]\3\2\2\2\\S\3\2\2\2\\]\3\2\2\2]\22\3\2\2\2^`\t")
        buf.write("\3\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\24\3\2")
        buf.write("\2\2cd\7*\2\2d\26\3\2\2\2ef\7+\2\2f\30\3\2\2\2gh\7}\2")
        buf.write("\2h\32\3\2\2\2ij\7\177\2\2j\34\3\2\2\2kl\7=\2\2l\36\3")
        buf.write("\2\2\2mo\t\7\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2")
        buf.write("\2qr\3\2\2\2rs\b\20\2\2s \3\2\2\2tu\13\2\2\2u\"\3\2\2")
        buf.write("\2vw\13\2\2\2w$\3\2\2\2xy\13\2\2\2y&\3\2\2\2\16\2>@DI")
        buf.write("OQUZ\\ap\3\b\2\2")
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
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    SEMI = 11
    WS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "REAL", "INTLIT", "LB", "RB", "LP", 
            "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "LETTER", "DIGIT", "SIGN", 
                  "ID", "REAL", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


