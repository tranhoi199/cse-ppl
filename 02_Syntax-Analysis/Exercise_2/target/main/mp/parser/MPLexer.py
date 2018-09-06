# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0086\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\6")
        buf.write("\20X\n\20\r\20\16\20Y\5\20\\\n\20\3\20\3\20\5\20`\n\20")
        buf.write("\3\20\6\20c\n\20\r\20\16\20d\5\20g\n\20\3\21\3\21\7\21")
        buf.write("k\n\21\f\21\16\21n\13\21\3\21\5\21q\n\21\3\22\3\22\7\22")
        buf.write("u\n\22\f\22\16\22x\13\22\3\23\6\23{\n\23\r\23\16\23|\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\2\2\27\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\n\3\2\60\60")
        buf.write("\3\2\62;\4\2GGgg\4\2--//\3\2\63;\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\5\2\13\f\17\17\"\"\2\u008e\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\64\3\2\2\2\7:\3\2\2")
        buf.write("\2\t>\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2\17D\3\2\2\2\21F\3")
        buf.write("\2\2\2\23H\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31N\3\2\2\2")
        buf.write("\33P\3\2\2\2\35R\3\2\2\2\37T\3\2\2\2!p\3\2\2\2#r\3\2\2")
        buf.write("\2%z\3\2\2\2\'\u0080\3\2\2\2)\u0082\3\2\2\2+\u0084\3\2")
        buf.write("\2\2-.\7t\2\2./\7g\2\2/\60\7v\2\2\60\61\7w\2\2\61\62\7")
        buf.write("t\2\2\62\63\7p\2\2\63\4\3\2\2\2\64\65\7h\2\2\65\66\7n")
        buf.write("\2\2\66\67\7q\2\2\678\7c\2\289\7v\2\29\6\3\2\2\2:;\7k")
        buf.write("\2\2;<\7p\2\2<=\7v\2\2=\b\3\2\2\2>?\7}\2\2?\n\3\2\2\2")
        buf.write("@A\7\177\2\2A\f\3\2\2\2BC\7*\2\2C\16\3\2\2\2DE\7+\2\2")
        buf.write("E\20\3\2\2\2FG\7=\2\2G\22\3\2\2\2HI\7.\2\2I\24\3\2\2\2")
        buf.write("JK\7?\2\2K\26\3\2\2\2LM\7-\2\2M\30\3\2\2\2NO\7/\2\2O\32")
        buf.write("\3\2\2\2PQ\7,\2\2Q\34\3\2\2\2RS\7\61\2\2S\36\3\2\2\2T")
        buf.write("[\5!\21\2UW\t\2\2\2VX\t\3\2\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[U\3\2\2\2[\\\3\2\2\2\\f\3")
        buf.write("\2\2\2]_\t\4\2\2^`\t\5\2\2_^\3\2\2\2_`\3\2\2\2`b\3\2\2")
        buf.write("\2ac\t\3\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e")
        buf.write("g\3\2\2\2f]\3\2\2\2fg\3\2\2\2g \3\2\2\2hl\t\6\2\2ik\t")
        buf.write("\3\2\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mq\3\2\2")
        buf.write("\2nl\3\2\2\2oq\7\62\2\2ph\3\2\2\2po\3\2\2\2q\"\3\2\2\2")
        buf.write("rv\t\7\2\2su\t\b\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3")
        buf.write("\2\2\2w$\3\2\2\2xv\3\2\2\2y{\t\t\2\2zy\3\2\2\2{|\3\2\2")
        buf.write("\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b\23\2\2\177&\3")
        buf.write("\2\2\2\u0080\u0081\13\2\2\2\u0081(\3\2\2\2\u0082\u0083")
        buf.write("\13\2\2\2\u0083*\3\2\2\2\u0084\u0085\13\2\2\2\u0085,\3")
        buf.write("\2\2\2\f\2Y[_dflpv|\3\b\2\2")
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
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'float'", "'int'", "'{'", "'}'", "'('", "')'", 
            "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", "CM", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", 
                  "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


