# Generated from c:\Users\ACER\Desktop\ppl\exercises\AST2\q1\src\main\mp\parser\MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\31\n\2\r\2")
        buf.write("\16\2\32\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\5\bG\n\b\3\t\6\tJ\n\t\r\t\16\t")
        buf.write("K\3\n\6\nO\n\n\r\n\16\nP\3\n\3\n\3\13\3\13\2\2\f\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\6\3\2\62")
        buf.write(";\4\2>>@@\3\2c|\5\2\13\f\17\17\"\"\2b\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\3\30\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13\60")
        buf.write("\3\2\2\2\r<\3\2\2\2\17F\3\2\2\2\21I\3\2\2\2\23N\3\2\2")
        buf.write("\2\25T\3\2\2\2\27\31\t\2\2\2\30\27\3\2\2\2\31\32\3\2\2")
        buf.write("\2\32\30\3\2\2\2\32\33\3\2\2\2\33\4\3\2\2\2\34\35\7V\2")
        buf.write("\2\35\36\7t\2\2\36\37\7w\2\2\37&\7g\2\2 !\7H\2\2!\"\7")
        buf.write("c\2\2\"#\7n\2\2#$\7u\2\2$&\7g\2\2%\34\3\2\2\2% \3\2\2")
        buf.write("\2&\6\3\2\2\2\'(\7*\2\2(\b\3\2\2\2)*\7+\2\2*\n\3\2\2\2")
        buf.write("+,\7c\2\2,-\7p\2\2-\61\7f\2\2./\7q\2\2/\61\7t\2\2\60+")
        buf.write("\3\2\2\2\60.\3\2\2\2\61\f\3\2\2\2\62\63\7-\2\2\63=\7?")
        buf.write("\2\2\64\65\7/\2\2\65=\7?\2\2\66\67\7(\2\2\67=\7?\2\28")
        buf.write("9\7~\2\29=\7?\2\2:;\7<\2\2;=\7?\2\2<\62\3\2\2\2<\64\3")
        buf.write("\2\2\2<\66\3\2\2\2<8\3\2\2\2<:\3\2\2\2=\16\3\2\2\2>G\7")
        buf.write("?\2\2?@\7>\2\2@G\7@\2\2AB\7@\2\2BG\7?\2\2CD\7>\2\2DG\7")
        buf.write("?\2\2EG\t\3\2\2F>\3\2\2\2F?\3\2\2\2FA\3\2\2\2FC\3\2\2")
        buf.write("\2FE\3\2\2\2G\20\3\2\2\2HJ\t\4\2\2IH\3\2\2\2JK\3\2\2\2")
        buf.write("KI\3\2\2\2KL\3\2\2\2L\22\3\2\2\2MO\t\5\2\2NM\3\2\2\2O")
        buf.write("P\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\b\n\2\2S\24")
        buf.write("\3\2\2\2TU\13\2\2\2U\26\3\2\2\2\n\2\32%\60<FKP\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    BOOLIT = 2
    LB = 3
    RB = 4
    ANDOR = 5
    ASSIGN = 6
    COMPARE = 7
    ID = 8
    WS = 9
    ERROR_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BOOLIT", "LB", "RB", "ANDOR", "ASSIGN", "COMPARE", 
            "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "BOOLIT", "LB", "RB", "ANDOR", "ASSIGN", "COMPARE", 
                  "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


