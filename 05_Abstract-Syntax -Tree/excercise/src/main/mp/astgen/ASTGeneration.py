from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
class ASTGeneration(MPVisitor):


 def visitProgram(self,ctx:MPParser.ProgramContext):
     ctx.ID().
     [a]if
    return Program()

 def visitVardecls(self,ctx:MPParser.VardeclsContext):

    return Trả lời
 # có 1 for trong đáp án

  def visitVardecl(self,ctx:MPParser.VardeclContext):

    return Trả lời

  def visitType(self,ctx:MPParser.TypeContext):

    return IntType() if ctx.INTTYPE() else FloatType()

  def visitIds(self,ctx:MPParser.IdsContext):

    return Trả lời
 if ctx.getChildCount() == 2 else [ctx.ID().getText()] #nối 2 list bằng dấu +, không có khoảng trắng