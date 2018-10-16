#########################################################
########### Code used for Pylint to link code ###########
######    REMEMBER: Comment before submit code    #######
#########################################################

import sys
sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################

F_LOG = False

def log(*arg):
    if F_LOG: print('>>>>>', *arg)
def log1(*arg):
    if F_LOG: print('>>>>>>>>>>', *arg)
def log2(*arg):
    if F_LOG: print('>>>>>>>>>>>>>>>', *arg)


from MPVisitor import MPVisitor
from MPParser import MPParser
# from AST import *
from AntiAST import *


class ASTGeneration(MPVisitor):
    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        log('visitProgram')
        declList = []
        for x in ctx.declare():
            decl = self.visitDeclare(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        log1(declList)
        return Program(declList)


    # Visit a parse tree produced by MPParser#declare.
    def visitDeclare(self, ctx:MPParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_declare.
    def visitVar_declare(self, ctx:MPParser.Var_declareContext):
        log('visitVar_declare')
        varDeclList = []
        for x in ctx.ids_list_with_type():
            varDeclList.extend(self.visitIds_list_with_type(x))
        log1(varDeclList)
        return [VarDecl(id, dataType) for (id, dataType) in varDeclList]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_declare.
    def visitFunc_declare(self, ctx:MPParser.Func_declareContext):
        log('visitFunc_declare')
        name = Id(ctx.ID().getText())
        log1(name)
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        log1(param)
        returnType = self.visit(ctx.data_types())
        log1(returnType)
        local = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        log1(local)
        body = self.visit(ctx.compound_stmt())
        log1(body)
        return FuncDecl(name, param, local, body, returnType)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proc_declare.
    def visitProc_declare(self, ctx:MPParser.Proc_declareContext):
        log('visitProc_declare')
        name = Id(ctx.ID().getText())
        log1(name)
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        log1(param)
        local = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        log1(local)
        body = self.visit(ctx.compound_stmt())
        log1(body)
        return FuncDecl(name, param, local, body)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        log('visitStmt')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        log('visitAssign_stmt')
        return self.visit(ctx.assign_body())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_body.
    def visitAssign_body(self, ctx:MPParser.Assign_bodyContext):
        log('visitAssign_body')
        lhs = self.visit(ctx.assign_lhs())
        exp, otherLHS = self.visit(ctx.assign_tail())
        log1(lhs)
        log1(exp)
        log1(otherLHS)
        lhsList = [lhs] + otherLHS + [exp]
        return [Assign(lhsList[i], lhsList[i+1]) for i in range(len(lhsList)-1)][::-1]
        # return [Assign(lhs, exp) for lhs in lhsList]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_lhs.
    def visitAssign_lhs(self, ctx:MPParser.Assign_lhsContext):
        log('visitAssign_lhs')
        if ctx.ID():
            log1(ctx.ID().getText())
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.index_exp())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_tail.
    def visitAssign_tail(self, ctx:MPParser.Assign_tailContext):
        log('visitAssign_tail')
        if ctx.ASSIGN():
            lhs = self.visit(ctx.assign_lhs())
            exp, otherLHS = self.visit(ctx.assign_tail())
            return exp, [lhs] + otherLHS
        exp = self.visit(ctx.exp())
        return exp, []
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        log('visitIf_stmt')
        expr = self.visit(ctx.exp_bool())
        log1(expr)
        thenStmt = self.visit(ctx.stmt(0))
        log1(thenStmt)
        if not isinstance(thenStmt, list): thenStmt = [thenStmt]
        if ctx.stmt(1):
            elseStmt = self.visit(ctx.stmt(1))
            if not isinstance(elseStmt, list): elseStmt = [elseStmt]
            return If(expr, thenStmt, elseStmt)
        return If(expr, thenStmt)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        log('visitWhile_stmt')
        exp = self.visit(ctx.exp_bool())
        log1(exp)
        stmtsList = self.visit(ctx.stmt())
        log1(stmtsList)
        if not isinstance(stmtsList, list): stmtsList = [stmtsList]
        return While(exp, stmtsList)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        log('visitFor_stmt')
        id = Id(ctx.ID().getText())
        log1(id)
        expr1 = self.visit(ctx.exp(0))
        log1(expr1)
        expr2 = self.visit(ctx.exp(1))
        log1(expr2)
        loop = self.visit(ctx.stmt())
        log1(loop)
        up = False if ctx.DOWNTO() else True
        log1(up)

        if not isinstance(loop, list): loop = [loop]
        return For(id, expr1, expr2, up, loop)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        log('visitWith_stmt')
        varDeclList = []
        for x in ctx.ids_list_with_type():
            varDeclList.extend(self.visitIds_list_with_type(x))
        log1(varDeclList)
        stmt = self.visit(ctx.stmt())
        log1(stmt)

        if not isinstance(stmt, list): stmt = [stmt]
        return With([VarDecl(id, dataType) for (id, dataType) in varDeclList], stmt)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#brk_stmt.
    def visitBrk_stmt(self, ctx:MPParser.Brk_stmtContext):
        log('visitBrk_stmt')
        return Break()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#cont_stmt.
    def visitCont_stmt(self, ctx:MPParser.Cont_stmtContext):
        log('visitCont_stmt')
        return Continue()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt.
    def visitRet_stmt(self, ctx:MPParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt_proc.
    def visitRet_stmt_proc(self, ctx:MPParser.Ret_stmt_procContext):
        log('visitRet_stmt_proc')
        return Return()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ret_stmt_func.
    def visitRet_stmt_func(self, ctx:MPParser.Ret_stmt_funcContext):
        log('visitRet_stmt_func')
        return Return(expr=self.visit(ctx.exp()))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        log('visitCall_stmt')
        callExp = self.visit(ctx.call_exp())
        method = callExp.method
        param = callExp.param
        log1(method)
        log1(param)
        return CallStmt(method, param)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        log('visitCompound_stmt')
        return self.visit(ctx.stmts_list()) if ctx.stmts_list() else []
        # return self.visitChildren(ctx)


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
        log('visitExp')
        if ctx.getChildCount() == 1: # exp1
            return self.visit(ctx.exp1())
        left = self.visit(ctx.exp())
        right = self.visit(ctx.exp1())
        op = 'andthen' if ctx.op_and_then() else 'orelse'
        log1(left)
        log1(right)
        log1(op)
        return BinaryOp(op, left, right)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        log('visitExp1')
        if ctx.getChildCount() == 1: # exp2
            return self.visit(ctx.exp2(0))
        left = self.visit(ctx.exp2(0))
        right = self.visit(ctx.exp2(1))
        op = ctx.getChild(1).getText()
        log1(left)
        log1(right)
        log1(op)
        return BinaryOp(op, left, right)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        log('visitExp2')
        if ctx.getChildCount() == 1: # exp3
            return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        op = ctx.getChild(1).getText()
        log1(left)
        log1(right)
        log1(op)
        return BinaryOp(op, left, right)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        log('visitExp3')
        if ctx.getChildCount() == 1: # exp4
            return self.visit(ctx.exp4())
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        op = ctx.getChild(1).getText()
        log1(left)
        log1(right)
        log1(op)
        return BinaryOp(op, left, right)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        log('visitExp4')
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        op = ctx.NOT().getText() if ctx.NOT() else ctx.SUB().getText()
        body = self.visit(ctx.exp4())
        log1(body)
        log1(op)
        return UnaryOp(op, body)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operands.
    def visitOperands(self, ctx:MPParser.OperandsContext):
        log('visitOperands')
        if ctx.getChildCount() == 1:
            # literal, ID, call_exp
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.literal(): return self.visit(ctx.literal())
            return self.visit(ctx.call_exp())
        if ctx.LP():
            # LP exp RP
            return self.visit(ctx.exp())
        arr = self.visit(ctx.operands())
        log1(arr)
        idx = self.visit(ctx.postfix_array_exp())
        log1(idx)
        return ArrayCell(arr, idx)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#postfix_array_exp.
    def visitPostfix_array_exp(self, ctx:MPParser.Postfix_array_expContext):
        log('visitPostfix_array_exp')
        return self.visit(ctx.exp())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primary_exp.
    def visitPrimary_exp(self, ctx:MPParser.Primary_expContext):
        log('visitPrimary_exp')
        return ctx.ID().getText() if ctx.ID() else self.visit(ctx.literal())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_exp.
    def visitCall_exp(self, ctx:MPParser.Call_expContext):
        method = Id(ctx.ID().getText())
        log1(method)
        param = self.visit(ctx.exps_list()) if ctx.exps_list() else []
        log1(param)
        return CallExpr(method, param)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        log('visitIndex_exp')
        arr = self.visit(ctx.operands())
        log1(arr)
        idx = self.visit(ctx.postfix_array_exp())
        log1(idx)
        return ArrayCell(arr, idx)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#params_list.
    def visitParams_list(self, ctx:MPParser.Params_listContext):
        log('visitParams_list')
        varDeclList = []
        for x in ctx.ids_list_with_type():
            varDeclList.extend(self.visitIds_list_with_type(x))
        log1(varDeclList)
        return [VarDecl(id, dataType) for (id, dataType) in varDeclList]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ids_list_with_type.
    def visitIds_list_with_type(self, ctx:MPParser.Ids_list_with_typeContext):
        log('visitIds_list_with_type')
        ids_list = self.visit(ctx.ids_list())
        dataType = self.visit(ctx.data_types())
        log1(ids_list)
        log1(dataType)
        return [(id, dataType) for id in ids_list]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ids_list.
    def visitIds_list(self, ctx:MPParser.Ids_listContext):
        log('visitIds_list')
        log1([id.getText() for id in ctx.ID()])
        return [Id(id.getText()) for id in ctx.ID()]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exps_list.
    def visitExps_list(self, ctx:MPParser.Exps_listContext):
        log('visitExps_list')
        return [self.visitExp(x) for x in ctx.exp()]
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmts_list.
    def visitStmts_list(self, ctx:MPParser.Stmts_listContext):
        log('visitStmts_list')
        log1(ctx.getChildCount())
        stmtsList = []
        for i in ctx.stmt():
            j = self.visitStmt(i)
            if isinstance(j, list): stmtsList.extend(j if j else [])
            else: stmtsList.append(j)
        return stmtsList
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#method_types.
    def visitMethod_types(self, ctx:MPParser.Method_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#data_types.
    def visitData_types(self, ctx:MPParser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_types.
    def visitCompound_types(self, ctx:MPParser.Compound_typesContext):
        log('visitCompound_types')
        lower = self.visit(ctx.number(0))
        upper = self.visit(ctx.number(1))
        eleType = self.visit(ctx.primitive_types())
        log1(lower, upper, eleType)
        return ArrayType(lower, upper, eleType)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_types.
    def visitPrimitive_types(self, ctx:MPParser.Primitive_typesContext):
        log('visitPrimitive_types')
        if ctx.INTEGER(): return IntType()
        if ctx.REAL(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.BOOLEAN(): return BoolType()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#op_and_then.
    def visitOp_and_then(self, ctx:MPParser.Op_and_thenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#op_or_else.
    def visitOp_or_else(self, ctx:MPParser.Op_or_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        log('visitLiteral')
        if ctx.INTEGER_LITERAL():
            log1('INTEGER_LITERAL')
            log1(int(ctx.INTEGER_LITERAL().getText()))
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        if ctx.REAL_LITERAL():
            log1('REAL_LITERAL')
            log1(float(ctx.REAL_LITERAL().getText()))
            return FloatLiteral(float(ctx.REAL_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            log1('STRING_LITERAL')
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return self.visit(ctx.boolean_literal())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#number.
    def visitNumber(self, ctx:MPParser.NumberContext):
        log('visitNumber')
        val = int(ctx.INTEGER_LITERAL().getText())
        if ctx.SUB(): val = -val
        log1(val)
        return val
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boolean_literal.
    def visitBoolean_literal(self, ctx:MPParser.Boolean_literalContext):
        log1('visitBoolean_literal')
        val = True if ctx.TRUE() else False
        return BooleanLiteral(val)
        # return self.visitChildren(ctx)