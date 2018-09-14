from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return VoidType()

    def visitBody(self,ctx:MPParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))
        

