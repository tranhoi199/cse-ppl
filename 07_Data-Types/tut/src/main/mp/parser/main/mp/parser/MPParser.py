# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6\62\n\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\5\b<\n\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2>\2\25")
        buf.write("\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b&\3\2\2\2\n/\3\2\2")
        buf.write("\2\f\65\3\2\2\2\168\3\2\2\2\20?\3\2\2\2\22A\3\2\2\2\24")
        buf.write("\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2")
        buf.write("\2\33\36\5\b\5\2\34\36\5\6\4\2\35\33\3\2\2\2\35\34\3\2")
        buf.write("\2\2\36\5\3\2\2\2\37 \7\t\2\2 !\7\16\2\2!\"\7\4\2\2\"")
        buf.write("#\7\5\2\2#$\7\6\2\2$%\5\n\6\2%\7\3\2\2\2&\'\7\n\2\2\'")
        buf.write("(\7\16\2\2()\7\4\2\2)*\7\5\2\2*+\7\7\2\2+,\5\22\n\2,-")
        buf.write("\7\6\2\2-.\5\n\6\2.\t\3\2\2\2/\61\7\13\2\2\60\62\5\f\7")
        buf.write("\2\61\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64\7\f")
        buf.write("\2\2\64\13\3\2\2\2\65\66\5\16\b\2\66\67\7\6\2\2\67\r\3")
        buf.write("\2\2\289\7\16\2\29;\7\4\2\2:<\5\20\t\2;:\3\2\2\2;<\3\2")
        buf.write("\2\2<=\3\2\2\2=>\7\5\2\2>\17\3\2\2\2?@\7\3\2\2@\21\3\2")
        buf.write("\2\2AB\7\r\2\2B\23\3\2\2\2\6\27\35\61;")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "LB", "RB", "SEMI", "COLON", 
                      "WS", "PROCEDURE", "FUNCTION", "BEGIN", "END", "INTTYPE", 
                      "ID", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_procdecl = 2
    RULE_funcdecl = 3
    RULE_body = 4
    RULE_stmt = 5
    RULE_funcall = 6
    RULE_exp = 7
    RULE_mtype = 8

    ruleNames =  [ "program", "decl", "procdecl", "funcdecl", "body", "stmt", 
                   "funcall", "exp", "mtype" ]

    EOF = Token.EOF
    INTLIT=1
    LB=2
    RB=3
    SEMI=4
    COLON=5
    WS=6
    PROCEDURE=7
    FUNCTION=8
    BEGIN=9
    END=10
    INTTYPE=11
    ID=12
    ERROR_CHAR=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.DeclContext)
            else:
                return self.getTypedRuleContext(MPParser.DeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.decl()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.PROCEDURE or _la==MPParser.FUNCTION):
                    break

            self.state = 23
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MPParser.FuncdeclContext,0)


        def procdecl(self):
            return self.getTypedRuleContext(MPParser.ProcdeclContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MPParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.funcdecl()
                pass
            elif token in [MPParser.PROCEDURE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.procdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(MPParser.PROCEDURE, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_procdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcdecl" ):
                return visitor.visitProcdecl(self)
            else:
                return visitor.visitChildren(self)




    def procdecl(self):

        localctx = MPParser.ProcdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_procdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MPParser.PROCEDURE)
            self.state = 30
            self.match(MPParser.ID)
            self.state = 31
            self.match(MPParser.LB)
            self.state = 32
            self.match(MPParser.RB)
            self.state = 33
            self.match(MPParser.SEMI)
            self.state = 34
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(MPParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def mtype(self):
            return self.getTypedRuleContext(MPParser.MtypeContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MPParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MPParser.FUNCTION)
            self.state = 37
            self.match(MPParser.ID)
            self.state = 38
            self.match(MPParser.LB)
            self.state = 39
            self.match(MPParser.RB)
            self.state = 40
            self.match(MPParser.COLON)
            self.state = 41
            self.mtype()
            self.state = 42
            self.match(MPParser.SEMI)
            self.state = 43
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(MPParser.BEGIN, 0)

        def END(self):
            return self.getToken(MPParser.END, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MPParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MPParser.BEGIN)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 46
                self.stmt()


            self.state = 49
            self.match(MPParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MPParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.funcall()
            self.state = 52
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MPParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MPParser.ID)
            self.state = 55
            self.match(MPParser.LB)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.INTLIT:
                self.state = 56
                self.exp()


            self.state = 59
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def getRuleIndex(self):
            return MPParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MPParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MPParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMtype" ):
                return visitor.visitMtype(self)
            else:
                return visitor.visitChildren(self)




    def mtype(self):

        localctx = MPParser.MtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MPParser.INTTYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





