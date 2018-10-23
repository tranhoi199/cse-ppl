import sys, os
sys.path.append('../utils')
sys.path.append('../parser')
sys.path.append('../../../../target')

from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
        return self.visit(ctx.term())

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))
        return self.visit(ctx.operand())

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT(): return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        return self.visit(ctx.exp())