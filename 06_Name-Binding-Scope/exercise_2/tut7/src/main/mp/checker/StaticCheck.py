
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType(' + '[' + ', '.join([str(x) for x in self.partype]) + '], ' + str(self.rettype) + ')'


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + self.name + ', ' + str(self.mtype) + ']'


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType()))
        ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        sym = [self.visit(x, c) for x in ast.decl]
        # for x in sym:
            # self.lookup(x.name, sym, lambda x: x.name)
        return []
    
    def visitVarDecl(self, ast, c):
        return None


    def visitFuncDecl(self, ast, c):
        _ = list(map(lambda x: self.visit(x, (c, True)), ast.body))
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType))

    def visitCallStmt(self, ast, c):
        at = [self.visit(x, (c[0], False)) for x in ast.param]

        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        elif len(res.mtype.partype) != len(at) or \
        False in [(type(a) == type(b) or (type(b) is FloatType and type(a) is IntType)) \
            for a,b in zip(at, res.mtype.partype)]:
            raise TypeMismatchInStatement(ast)
        else:
            return res.mtype.rettype


    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitBinaryOp(self, ast, param):
        leftType = self.visit(ast.left, param)
        rightType = self.visit(ast.right, param)

        if (type(leftType) is not IntType and type(leftType) is not FloatType) or \
            (type(rightType) is not IntType and type(rightType) is not FloatType):
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['+', '-', '*']:
            if type(leftType) is FloatType or type(rightType) is FloatType:
                return FloatType()
            return leftType

        if ast.op == '/': return FloatType()
        return leftType
    
    def visitUnaryOp(self, ast, param):
        return self.visit(ast.body)
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast, c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is None: 
            raise Undeclared(Identifier(), ast.name)
        return res.mtype