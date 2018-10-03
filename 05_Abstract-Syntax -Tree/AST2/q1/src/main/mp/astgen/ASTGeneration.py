from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce
class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if (ctx.ASSIGN()):
            rl = ctx.term()[::-1]
            cl = list(zip(ctx.ASSIGN()[::-1],rl[1:]))
            return reduce(lambda x,y: Binary(y[0].getText(),self.visit(y[1]),x),cl,self.visit(rl[0]))
        return self.visit(ctx.term(0))

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        # factor: [1,2,3,4,5]
        # rl: [5,4,3,2,1]
        # dl = [(ANDOR,2),(ANDOR,3),...]
        # cl = [(ANDOR,4), (ANDOR,3),...]
       
        if (ctx.ANDOR()):
            rl = ctx.operand()[::-1]
            dl = list(zip(ctx.ANDOR(),ctx.operand()[1:]))
            return reduce(lambda x,y: Binary(y[0].getText(),x,self.visit(y[1])),dl,self.visit(rl[-1]))
        return self.visit(ctx.operand(0))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT(): return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        return self.visit(ctx.exp())