from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        return self.visit(ctx.arraytype())
        
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if (ctx.primtype()):
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.primtype()))
        arrayType = self.visit(ctx.arraytype())
        indexType = arrayType.indexType
        eleType = arrayType.eleType
        dimen = self.visit(ctx.dimen())

        return ArrayType(UnionType(indexType, dimen), eleType)

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitDimen(self,ctx:MPParser.DimenContext):
        lowerbound = self.visit(ctx.num(0))
        upperbound = self.visit(ctx.num(1))
        return RangeType(lowerbound, upperbound)
    
    def visitNum(self,ctx:MPParser.NumContext):
        return int((ctx.SIGN().getText() if ctx.SIGN() else "") + ctx.INTLIT().getText())

        

