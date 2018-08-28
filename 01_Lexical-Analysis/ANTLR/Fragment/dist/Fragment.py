# Generated from ./Fragment.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\7\4\23\n\4\f\4\16\4\26\13\4\3\5\6\5\31")
        buf.write("\n\5\r\5\16\5\32\3\5\3\5\2\2\6\3\2\5\2\7\3\t\4\3\2\5\3")
        buf.write("\2c|\3\2\62;\5\2\13\f\17\17\"\"\2\36\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\3\13\3\2\2\2\5\r\3\2\2\2\7\17\3\2\2\2\t\30\3\2")
        buf.write("\2\2\13\f\t\2\2\2\f\4\3\2\2\2\r\16\t\3\2\2\16\6\3\2\2")
        buf.write("\2\17\24\5\3\2\2\20\23\5\3\2\2\21\23\5\5\3\2\22\20\3\2")
        buf.write("\2\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3")
        buf.write("\2\2\2\25\b\3\2\2\2\26\24\3\2\2\2\27\31\t\4\2\2\30\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\35\b\5\2\2\35\n\3\2\2\2\6\2\22\24\32\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class Fragment(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "LOWERCASE_LETTER", "DIGIT", "ID", "WS" ]

    grammarFileName = "Fragment.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


