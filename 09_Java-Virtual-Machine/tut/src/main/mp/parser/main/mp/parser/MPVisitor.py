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


    # Visit a parse tree produced by MPParser#declare.
    def visitDeclare(self, ctx:MPParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_declare.
    def visitVar_declare(self, ctx:MPParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_declare.
    def visitFunc_declare(self, ctx:MPParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proc_declare.
    def visitProc_declare(self, ctx:MPParser.Proc_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_body.
    def visitAssign_body(self, ctx:MPParser.Assign_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_lhs.
    def visitAssign_lhs(self, ctx:MPParser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_tail.
    def visitAssign_tail(self, ctx:MPParser.Assign_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#brk_stmt.
    def visitBrk_stmt(self, ctx:MPParser.Brk_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#cont_stmt.
    def visitCont_stmt(self, ctx:MPParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt.
    def visitRet_stmt(self, ctx:MPParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt_proc.
    def visitRet_stmt_proc(self, ctx:MPParser.Ret_stmt_procContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt_func.
    def visitRet_stmt_func(self, ctx:MPParser.Ret_stmt_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_bool.
    def visitExp_bool(self, ctx:MPParser.Exp_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_int.
    def visitExp_int(self, ctx:MPParser.Exp_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_real.
    def visitExp_real(self, ctx:MPParser.Exp_realContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_str.
    def visitExp_str(self, ctx:MPParser.Exp_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operands.
    def visitOperands(self, ctx:MPParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#postfix_array_exp.
    def visitPostfix_array_exp(self, ctx:MPParser.Postfix_array_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primary_exp.
    def visitPrimary_exp(self, ctx:MPParser.Primary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_exp.
    def visitCall_exp(self, ctx:MPParser.Call_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#params_list.
    def visitParams_list(self, ctx:MPParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ids_list_with_type.
    def visitIds_list_with_type(self, ctx:MPParser.Ids_list_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ids_list.
    def visitIds_list(self, ctx:MPParser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exps_list.
    def visitExps_list(self, ctx:MPParser.Exps_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmts_list.
    def visitStmts_list(self, ctx:MPParser.Stmts_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#method_types.
    def visitMethod_types(self, ctx:MPParser.Method_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#data_types.
    def visitData_types(self, ctx:MPParser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_types.
    def visitCompound_types(self, ctx:MPParser.Compound_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_types.
    def visitPrimitive_types(self, ctx:MPParser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#op_and_then.
    def visitOp_and_then(self, ctx:MPParser.Op_and_thenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#op_or_else.
    def visitOp_or_else(self, ctx:MPParser.Op_or_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#number.
    def visitNumber(self, ctx:MPParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boolean_literal.
    def visitBoolean_literal(self, ctx:MPParser.Boolean_literalContext):
        return self.visitChildren(ctx)



del MPParser