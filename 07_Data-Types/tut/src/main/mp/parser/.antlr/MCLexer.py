# Generated from /Users/nhphung/Documents/fromSamsungLaptop/Monhoc/KS-NNLT/Materials/Assignments/MC/MC1-Python/Assignment2/upload/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\6\5/\n\5\r\5\16\5\60\3\6\6\6\64")
        buf.write("\n\6\r\6\16\6\65\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\6\fC\n\f\r\f\16\fD\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5")
        buf.write("$\3\2\2\2\7(\3\2\2\2\t.\3\2\2\2\13\63\3\2\2\2\r\67\3\2")
        buf.write("\2\2\179\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27")
        buf.write("B\3\2\2\2\31H\3\2\2\2\33J\3\2\2\2\35L\3\2\2\2\37 \7o\2")
        buf.write("\2 !\7c\2\2!\"\7k\2\2\"#\7p\2\2#\4\3\2\2\2$%\7k\2\2%&")
        buf.write("\7p\2\2&\'\7v\2\2\'\6\3\2\2\2()\7x\2\2)*\7q\2\2*+\7k\2")
        buf.write("\2+,\7f\2\2,\b\3\2\2\2-/\t\2\2\2.-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60.\3\2\2\2\60\61\3\2\2\2\61\n\3\2\2\2\62\64\t\3\2\2")
        buf.write("\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2")
        buf.write("\2\66\f\3\2\2\2\678\7*\2\28\16\3\2\2\29:\7+\2\2:\20\3")
        buf.write("\2\2\2;<\7}\2\2<\22\3\2\2\2=>\7\177\2\2>\24\3\2\2\2?@")
        buf.write("\7=\2\2@\26\3\2\2\2AC\t\4\2\2BA\3\2\2\2CD\3\2\2\2DB\3")
        buf.write("\2\2\2DE\3\2\2\2EF\3\2\2\2FG\b\f\2\2G\30\3\2\2\2HI\13")
        buf.write("\2\2\2I\32\3\2\2\2JK\13\2\2\2K\34\3\2\2\2LM\13\2\2\2M")
        buf.write("\36\3\2\2\2\6\2\60\65D\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


