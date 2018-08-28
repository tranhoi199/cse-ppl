# Generated from ./Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2\2\2")
        buf.write("\4\5\7\3\2\2\5\6\7\4\2\2\6\3\3\2\2\2\2")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_hi = 0

    ruleNames =  [ "hi" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class HiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_hi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHi" ):
                return visitor.visitHi(self)
            else:
                return visitor.visitChildren(self)




    def hi(self):

        localctx = HelloParser.HiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_hi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.T__0)
            self.state = 3
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





