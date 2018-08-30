# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\3\7\3/\n\3\f\3\16\3\62\13")
        buf.write("\3\3\4\6\4\65\n\4\r\4\16\4\66\3\5\6\5:\n\5\r\5\16\5;\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\6\24f\n\24\r\24\16\24g\3\24\3\24")
        buf.write("\2\2\25\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13")
        buf.write("\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24\3\2\6\4")
        buf.write("\2C\\c|\4\2\62;aa\3\2\62;\5\2\13\f\17\17\"\"\2n\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\3)\3\2\2\2\5+\3\2\2\2\7\64\3\2\2\2\t9\3\2\2\2\13=\3")
        buf.write("\2\2\2\r?\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23E\3\2\2\2")
        buf.write("\25G\3\2\2\2\27I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35O\3")
        buf.write("\2\2\2\37Q\3\2\2\2!S\3\2\2\2#Z\3\2\2\2%`\3\2\2\2\'e\3")
        buf.write("\2\2\2)*\t\2\2\2*\4\3\2\2\2+\60\5\3\2\2,/\5\3\2\2-/\t")
        buf.write("\3\2\2.,\3\2\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\6\3\2\2\2\62\60\3\2\2\2\63\65\t\4\2\2\64")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67\b\3\2\2\28:\t\4\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2")
        buf.write(";<\3\2\2\2<\n\3\2\2\2=>\7}\2\2>\f\3\2\2\2?@\7\177\2\2")
        buf.write("@\16\3\2\2\2AB\7*\2\2B\20\3\2\2\2CD\7+\2\2D\22\3\2\2\2")
        buf.write("EF\7=\2\2F\24\3\2\2\2GH\7.\2\2H\26\3\2\2\2IJ\7?\2\2J\30")
        buf.write("\3\2\2\2KL\7-\2\2L\32\3\2\2\2MN\7/\2\2N\34\3\2\2\2OP\7")
        buf.write(",\2\2P\36\3\2\2\2QR\7\61\2\2R \3\2\2\2ST\7t\2\2TU\7g\2")
        buf.write("\2UV\7v\2\2VW\7w\2\2WX\7t\2\2XY\7p\2\2Y\"\3\2\2\2Z[\7")
        buf.write("h\2\2[\\\7n\2\2\\]\7q\2\2]^\7c\2\2^_\7v\2\2_$\3\2\2\2")
        buf.write("`a\7k\2\2ab\7p\2\2bc\7v\2\2c&\3\2\2\2df\t\5\2\2ed\3\2")
        buf.write("\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\b\24\2")
        buf.write("\2j(\3\2\2\2\b\2.\60\66;g\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INTLIT = 2
    FLOATLIT = 3
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
    RETURN = 15
    FLOAT = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'('", "')'", "';'", "','", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'return'", "'float'", "'int'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "LB", "RB", "LP", "RP", "SM", "CM", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "RETURN", "FLOAT", "INT", 
            "WS" ]

    ruleNames = [ "LETTER", "ID", "INTLIT", "FLOATLIT", "LB", "RB", "LP", 
                  "RP", "SM", "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "RETURN", 
                  "FLOAT", "INT", "WS" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


