#########################################################
#########################################################

from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *
from functools import reduce
import sys

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

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'


class Symbol:
    """
    name: string
    mtype: MType
    value: wtf
    """

    # Define Constants
    VAR_DECLARE_TYPE = "VAR_DECLARE_TYPE"
    FUNC_DECLARE_TYPE = "FUNC_DECLARE_TYPE"

    # Default Declare Type is Function Declare - kind Function
    def __init__(self, name, mtype, value=None, declType=FUNC_DECLARE_TYPE, kind=Function()):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.declType = declType
        self.kind = kind

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + self.declType + ',' + str(self.kind) + ')'

    def isVar(self):
        return self.declType == Symbol.VAR_DECLARE_TYPE

    def isFunc(self):
        return self.declType == Symbol.FUNC_DECLARE_TYPE

    def toVar(self):
        self.declType = Symbol.VAR_DECLARE_TYPE
        return self

    def toFunc(self):
        self.declType = Symbol.FUNC_DECLARE_TYPE
        return self

    # compare function between 2 instances
    @staticmethod
    def cmp(symbol):
        return symbol.name

    @staticmethod
    def toVar(symbol):
        symbol.declType = Symbol.VAR_DECLARE_TYPE
        return symbol

    @staticmethod
    def toFunc(symbol):
        symbol.declType = Symbol.FUNC_DECLARE_TYPE
        return symbol

    @staticmethod
    def fromVarDecl(varDecl, kind=Variable()):
        return Symbol(varDecl.variable.name, MType([], varDecl.varType), declType=Symbol.VAR_DECLARE_TYPE, kind=kind)

    @staticmethod
    def fromFuncDecl(funcDecl):
        kind = Procedure() if isinstance(funcDecl.returnType, VoidType) else Function()
        return Symbol(funcDecl.name.name, MType(funcDecl.param, funcDecl.returnType), kind=kind)

    @staticmethod
    def fromDecl(decl, kindForVarDecl=Variable()):
        return Symbol.fromVarDecl(decl, kind=kindForVarDecl) if isinstance(decl, VarDecl) else Symbol.fromFuncDecl(decl)


class Scope:
    @staticmethod
    def filterVarDecl(listSymbols):
        return [x for x in listSymbols if x.isVar()]

    @staticmethod
    def filterFuncDecl(listSymbols):
        return [x for x in listSymbols if x.isFunc()]

    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if x.name == symbol.name]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        return reduce(lambda lst,sym: lst if Scope.isExisten(lst, sym) else lst+[sym], currentScope, comingScope)


class Checker:

    utils = Utils()

    @staticmethod
    def checkRedeclared(currentScope, listNewSymbols):
        newScope = currentScope
        for x in listNewSymbols:
            f = Checker.utils.lookup(x.name, newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope


class StaticChecker(BaseVisitor, Utils):

    # Global Environement - Built-in Functions - Default is Function
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, scope):
        listNewSymbols = [Symbol.fromDecl(x) for x in ast.decl]
        _ = [print(x) for x in listNewSymbols]

        scope = Checker.checkRedeclared(scope, listNewSymbols)

        _ = [self.visit(x, scope) for x in ast.decl]
        
        return ''

    def visitFuncDecl(self, ast: FuncDecl, scope):
        listParams = [Symbol.fromVarDecl(x, kind=Parameter()) for x in ast.param]
        listLocalVar = [Symbol.fromVarDecl(x) for x in ast.local]
        listNewSymbols = listParams + listLocalVar

        localScope = Checker.checkRedeclared([], listNewSymbols)

        newScope = Scope.merge(scope, localScope)


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
