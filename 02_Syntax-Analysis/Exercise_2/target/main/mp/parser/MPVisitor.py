# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variables_declaration.
    def visitVariables_declaration(self, ctx:MPParser.Variables_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variables.
    def visitVariables(self, ctx:MPParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#function_declaration.
    def visitFunction_declaration(self, ctx:MPParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt_assign.
    def visitStmt_assign(self, ctx:MPParser.Stmt_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt_call.
    def visitStmt_call(self, ctx:MPParser.Stmt_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt_return.
    def visitStmt_return(self, ctx:MPParser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operands.
    def visitOperands(self, ctx:MPParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mc_type.
    def visitMc_type(self, ctx:MPParser.Mc_typeContext):
        return self.visitChildren(ctx)



del MPParser