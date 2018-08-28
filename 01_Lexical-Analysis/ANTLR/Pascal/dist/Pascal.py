# Generated from ./Pascal.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\25\b\1\4\2\t\2\4\3\t\3\3\2\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\3\6\3\20\n\3\r\3\16\3\21\3\3\3\3\2\2\4\3\3\5\4\3")
        buf.write("\2\5\3\2c|\4\2\62;c|\5\2\13\f\17\17\"\"\2\26\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\3\7\3\2\2\2\5\17\3\2\2\2\7\13\t\2\2\2\b")
        buf.write("\n\t\3\2\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3")
        buf.write("\2\2\2\f\4\3\2\2\2\r\13\3\2\2\2\16\20\t\4\2\2\17\16\3")
        buf.write("\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\23")
        buf.write("\3\2\2\2\23\24\b\3\2\2\24\6\3\2\2\2\5\2\13\21\3\b\2\2")
        return buf.getvalue()


class Pascal(Lexer):

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

    ruleNames = [ "ID", "WS" ]

    grammarFileName = "Pascal.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


