#########################################################
#########################################################

import sys

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')

#########################################################
#########################################################


class MType:
    """
    partype: list(Type) - params type
    rettype: Type       - return type
    """

    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    """
    name: string
    mtype: MType
    value:
    """
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    # Global Environement - Built-in Functionas
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putInt", MType([IntType()], VoidType()))
        Symbol("putIntLn", MType([IntType()], VoidType()))
        Symbol("putFloat", MType([FloatType()], VoidType()))
        Symbol("putFloatLn", MType([FloatType()], VoidType()))
        Symbol("putBool", MType([BoolType()], VoidType()))
        Symbol("putBoolLn", MType([BoolType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        return [self.visit(x, c) for x in ast.decl]

    def visitFuncDecl(self, ast, c):
        return list(map(lambda x: self.visit(x, (c, True)), ast.body))

    def visitCallStmt(self, ast, c):
        at = [self.visit(x, (c[0], False)) for x in ast.param]

        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self, ast, c):
        return IntType()
