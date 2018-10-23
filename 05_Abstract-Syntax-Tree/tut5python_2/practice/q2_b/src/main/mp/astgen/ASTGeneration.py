from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visit(ctx.primtype() if ctx.primtype() else ctx.arraytype())

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if ctx.primtype():
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.primtype()))
        arr = self.visit(ctx.arraytype())
        return ArrayType(UnionType(arr.indexType, self.visit(ctx.dimen())), arr.eleType)

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return IntType() if ctx.INTTYPE() else FloatType()

    # def visitDimens(self,ctx:MPParser.DimensContext):
        # return reduce(lambda x,y: UnionType(x, self.visit(y)), ctx.dimen()[1:], self.visit(ctx.dimen()[0]))

    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx):
        return (-1 if ctx.SIGN() else 1) * int(ctx.INTLIT().getText())
