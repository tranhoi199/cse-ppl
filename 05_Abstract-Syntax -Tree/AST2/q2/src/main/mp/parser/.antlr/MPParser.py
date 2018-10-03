# Generated from c:\Users\ACER\Desktop\ppl\exercises\AST2\q2tn\src\main\mp\parser\MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\4\3\4\5\4\37\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\5\7*\n\7\3\7\3\7\3\7\2\3\4\b\2\4\6\b\n\f\2\3\3")
        buf.write("\2\4\5\2*\2\16\3\2\2\2\4\21\3\2\2\2\6\36\3\2\2\2\b \3")
        buf.write("\2\2\2\n\"\3\2\2\2\f)\3\2\2\2\16\17\5\6\4\2\17\20\7\2")
        buf.write("\2\3\20\3\3\2\2\2\21\22\b\3\1\2\22\23\5\b\5\2\23\24\5")
        buf.write("\n\6\2\24\31\3\2\2\2\25\26\f\4\2\2\26\30\5\n\6\2\27\25")
        buf.write("\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\5\3\2\2\2\33\31\3\2\2\2\34\37\5\b\5\2\35\37\5\4\3\2\36")
        buf.write("\34\3\2\2\2\36\35\3\2\2\2\37\7\3\2\2\2 !\t\2\2\2!\t\3")
        buf.write("\2\2\2\"#\7\6\2\2#$\5\f\7\2$%\7\t\2\2%&\5\f\7\2&\'\7\7")
        buf.write("\2\2\'\13\3\2\2\2(*\7\b\2\2)(\3\2\2\2)*\3\2\2\2*+\3\2")
        buf.write("\2\2+,\7\3\2\2,\r\3\2\2\2\5\31\36)")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'integer'", "'real'", "'['", 
                     "']'", "'-'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "INTTYPE", "FLOATTYPE", "LSB", 
                      "RSB", "SIGN", "DOTDOT", "COMMA", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_arraytype = 1
    RULE_mptype = 2
    RULE_primtype = 3
    RULE_dimen = 4
    RULE_num = 5

    ruleNames =  [ "program", "arraytype", "mptype", "primtype", "dimen", 
                   "num" ]

    EOF = Token.EOF
    INTLIT=1
    INTTYPE=2
    FLOATTYPE=3
    LSB=4
    RSB=5
    SIGN=6
    DOTDOT=7
    COMMA=8
    WS=9
    ERROR_CHAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MPParser.MptypeContext,0)


        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_program




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.mptype()
            self.state = 13
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraytypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def dimen(self):
            return self.getTypedRuleContext(MPParser.DimenContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MPParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_arraytype



    def arraytype(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MPParser.ArraytypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_arraytype, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.primtype()
            self.state = 17
            self.dimen()
            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MPParser.ArraytypeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arraytype)
                    self.state = 19
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 20
                    self.dimen() 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MPParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_mptype




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mptype)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.arraytype(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MPParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_primtype




    def primtype(self):

        localctx = MPParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==MPParser.INTTYPE or _la==MPParser.FLOATTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.NumContext)
            else:
                return self.getTypedRuleContext(MPParser.NumContext,i)


        def DOTDOT(self):
            return self.getToken(MPParser.DOTDOT, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_dimen




    def dimen(self):

        localctx = MPParser.DimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MPParser.LSB)
            self.state = 33
            self.num()
            self.state = 34
            self.match(MPParser.DOTDOT)
            self.state = 35
            self.num()
            self.state = 36
            self.match(MPParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def SIGN(self):
            return self.getToken(MPParser.SIGN, 0)

        def getRuleIndex(self):
            return MPParser.RULE_num




    def num(self):

        localctx = MPParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.SIGN:
                self.state = 38
                self.match(MPParser.SIGN)


            self.state = 41
            self.match(MPParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.arraytype_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arraytype_sempred(self, localctx:ArraytypeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




