# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\20\6\20R\n\20\r\20\16\20S\5\20V\n\20\3\20")
        buf.write("\3\20\5\20Z\n\20\3\20\6\20]\n\20\r\20\16\20^\5\20a\n\20")
        buf.write("\3\21\3\21\7\21e\n\21\f\21\16\21h\13\21\3\21\5\21k\n\21")
        buf.write("\3\22\3\22\7\22o\n\22\f\22\16\22r\13\22\3\23\6\23u\n\23")
        buf.write("\r\23\16\23v\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\3\2\n\3\2\60\60\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0082")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\3\'\3\2\2\2\5.\3\2\2\2\7\64\3\2\2\2\t8\3\2\2")
        buf.write("\2\13:\3\2\2\2\r<\3\2\2\2\17>\3\2\2\2\21@\3\2\2\2\23B")
        buf.write("\3\2\2\2\25D\3\2\2\2\27F\3\2\2\2\31H\3\2\2\2\33J\3\2\2")
        buf.write("\2\35L\3\2\2\2\37N\3\2\2\2!j\3\2\2\2#l\3\2\2\2%t\3\2\2")
        buf.write("\2\'(\7t\2\2()\7g\2\2)*\7v\2\2*+\7w\2\2+,\7t\2\2,-\7p")
        buf.write("\2\2-\4\3\2\2\2./\7h\2\2/\60\7n\2\2\60\61\7q\2\2\61\62")
        buf.write("\7c\2\2\62\63\7v\2\2\63\6\3\2\2\2\64\65\7k\2\2\65\66\7")
        buf.write("p\2\2\66\67\7v\2\2\67\b\3\2\2\289\7}\2\29\n\3\2\2\2:;")
        buf.write("\7\177\2\2;\f\3\2\2\2<=\7*\2\2=\16\3\2\2\2>?\7+\2\2?\20")
        buf.write("\3\2\2\2@A\7=\2\2A\22\3\2\2\2BC\7.\2\2C\24\3\2\2\2DE\7")
        buf.write("?\2\2E\26\3\2\2\2FG\7-\2\2G\30\3\2\2\2HI\7/\2\2I\32\3")
        buf.write("\2\2\2JK\7,\2\2K\34\3\2\2\2LM\7\61\2\2M\36\3\2\2\2NU\5")
        buf.write("!\21\2OQ\t\2\2\2PR\t\3\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2")
        buf.write("\2ST\3\2\2\2TV\3\2\2\2UO\3\2\2\2UV\3\2\2\2V`\3\2\2\2W")
        buf.write("Y\t\4\2\2XZ\t\5\2\2YX\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[]\t")
        buf.write("\3\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_a\3\2")
        buf.write("\2\2`W\3\2\2\2`a\3\2\2\2a \3\2\2\2bf\t\6\2\2ce\t\3\2\2")
        buf.write("dc\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gk\3\2\2\2hf\3")
        buf.write("\2\2\2ik\7\62\2\2jb\3\2\2\2ji\3\2\2\2k\"\3\2\2\2lp\t\7")
        buf.write("\2\2mo\t\b\2\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2")
        buf.write("q$\3\2\2\2rp\3\2\2\2su\t\t\2\2ts\3\2\2\2uv\3\2\2\2vt\3")
        buf.write("\2\2\2vw\3\2\2\2wx\3\2\2\2xy\b\23\2\2y&\3\2\2\2\f\2SU")
        buf.write("Y^`fjpv\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    FLOAT = 2
    INT = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SM = 8
    CM = 9
    EQ = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    FLOATLIT = 15
    INTLIT = 16
    ID = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'float'", "'int'", "'{'", "'}'", "'('", "')'", 
            "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", "CM", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", "ID", 
            "WS" ]

    ruleNames = [ "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", 
                  "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", 
                  "ID", "WS" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


