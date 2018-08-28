# Generated from ./Final.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\5\4\35\n\4\3\5\3\5\3\5\6\5\"\n\5\r\5\16\5#\3\6\3\6\6")
        buf.write("\6(\n\6\r\6\16\6)\3\7\3\7\6\7.\n\7\r\7\16\7/\3\7\3\7\5")
        buf.write("\7\64\n\7\3\7\5\7\67\n\7\3\b\3\b\6\b;\n\b\r\b\16\b<\3")
        buf.write("\t\3\t\3\t\7\tB\n\t\f\t\16\tE\13\t\3\n\3\n\6\nI\n\n\r")
        buf.write("\n\16\nJ\3\n\3\n\3\13\6\13P\n\13\r\13\16\13Q\3\13\3\13")
        buf.write("\2\2\f\3\2\5\2\7\2\t\2\13\2\r\3\17\4\21\5\23\6\25\7\3")
        buf.write("\2\n\3\2c|\3\2\62;\4\2--//\3\2gg\3\2\60\60\3\2))\4\2)")
        buf.write(")``\5\2\13\f\17\17\"\"\2Z\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3")
        buf.write("\2\2\2\7\34\3\2\2\2\t\36\3\2\2\2\13%\3\2\2\2\r+\3\2\2")
        buf.write("\2\178\3\2\2\2\21>\3\2\2\2\23F\3\2\2\2\25O\3\2\2\2\27")
        buf.write("\30\t\2\2\2\30\4\3\2\2\2\31\32\t\3\2\2\32\6\3\2\2\2\33")
        buf.write("\35\t\4\2\2\34\33\3\2\2\2\34\35\3\2\2\2\35\b\3\2\2\2\36")
        buf.write("\37\t\5\2\2\37!\5\7\4\2 \"\5\5\3\2! \3\2\2\2\"#\3\2\2")
        buf.write("\2#!\3\2\2\2#$\3\2\2\2$\n\3\2\2\2%\'\t\6\2\2&(\5\5\3\2")
        buf.write("\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\f\3\2\2\2")
        buf.write("+-\5\7\4\2,.\5\5\3\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60")
        buf.write("\3\2\2\2\60\66\3\2\2\2\61\63\5\13\6\2\62\64\5\t\5\2\63")
        buf.write("\62\3\2\2\2\63\64\3\2\2\2\64\67\3\2\2\2\65\67\5\t\5\2")
        buf.write("\66\61\3\2\2\2\66\65\3\2\2\2\67\16\3\2\2\28:\5\7\4\29")
        buf.write(";\5\5\3\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\20")
        buf.write("\3\2\2\2>C\5\3\2\2?B\5\3\2\2@B\5\5\3\2A?\3\2\2\2A@\3\2")
        buf.write("\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\22\3\2\2\2EC\3\2\2")
        buf.write("\2FH\t\7\2\2GI\t\b\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2J")
        buf.write("K\3\2\2\2KL\3\2\2\2LM\t\7\2\2M\24\3\2\2\2NP\t\t\2\2ON")
        buf.write("\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\b\13")
        buf.write("\2\2T\26\3\2\2\2\16\2\34#)/\63\66<ACJQ\3\b\2\2")
        return buf.getvalue()


class Final(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REAL = 1
    INT = 2
    ID = 3
    STRING = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "REAL", "INT", "ID", "STRING", "WS" ]

    ruleNames = [ "LOWERCASE_LETTER", "DIGIT", "SIGN", "SCIENTIFIC", "DECIMAL_POINT", 
                  "REAL", "INT", "ID", "STRING", "WS" ]

    grammarFileName = "Final.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


