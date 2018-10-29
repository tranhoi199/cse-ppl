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

    def toTuple(self):
        return (self.name, str(self.mtype))

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
    def filterId(listSymbols, id):
        f = [x for x in listSymbols if x.name == id.name]
        return f[0] if len(f) > 0 else None

    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if x.name == symbol.name]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        return reduce(lambda lst, sym: lst if Scope.isExisten(lst, sym) else lst+[sym], currentScope, comingScope)


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

    @staticmethod
    def checkUndeclared(visibleScope, id, kind):
        if len([x for x in visibleScope if x.name == id.name] == 0):
            raise Undeclared(kind, id.name)


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
        # TODO: Check Redeclared variable/function/procedure
        listNewSymbols = [Symbol.fromDecl(x) for x in ast.decl]
        scope = Checker.checkRedeclared(scope, listNewSymbols)
        check = [self.visit(x, scope) for x in ast.decl]

        # check entry procedure
        entryPoint = Symbol('main', MType([], VoidType()))
        res = self.lookup(entryPoint.toTuple(), listNewSymbols, lambda x: x.toTuple())
        if res is None:
            raise NoEntryPoint()

        return []

    def visitFuncDecl(self, ast: FuncDecl, scope):
        # TODO: Check Redeclared parameter/variable
        listParams = [Symbol.fromVarDecl(x, kind=Parameter()) for x in ast.param]
        listLocalVar = [Symbol.fromVarDecl(x) for x in ast.local]
        listNewSymbols = listParams + listLocalVar
        localScope = Checker.checkRedeclared([], listNewSymbols)
        newScope = Scope.merge(scope, localScope)
        check = [self.visit(x) for x in ast.body]

        # check Return Statement

    def visitVarDecl(self, ast, scope):
        return None

    def visitBinaryOp(self, ast, scope):
        return None

    def visitUnaryOp(self, ast, scope):
        return None

    def visitCallExpr(self, ast: CallExpr, scope):
        # TODO: Check Undeclared Function
        Checker.checkUndeclared(scope, ast.method, Function())

    def visitId(self, ast, scope):
        # TODO: Check Undeclared Identifier
        return None

    def visitArrayCell(self, ast, scope):
        return None

    def visitAssign(self, ast, scope):
        # TODO: Type Mismatch In Statement
        return None

    def visitWith(self, ast, scope):
        return None

    def visitIf(self, ast: If, scope):
        condition = self.visit(ast.expr)
        if not isinstance(condition, BooleanLiteral):
            raise TypeMismatchInStatement(ast)
        _ = [self.visit(x, scope) for x in ast.thenStmt]
        _ = [self.visit(x, scope) for x in ast.elseStmt]

    def visitFor(self, ast: For, scope):
        Checker.checkUndeclared(scope, ast.id)

        idSymbol = Scope.filterId(scope, ast.id)
        if not isinstance(ast.expr1, IntLiteral) or \
                not isinstance(ast.expr2, IntLiteral) or \
                not isinstance(idSymbol, IntType):
            raise TypeMismatchInStatement(ast)
        _ = [self.visit(x, scope) for x in ast.loop]

    def visitContinue(self, ast, scope):
        return None

    def visitBreak(self, ast, scope):
        return None

    def visitReturn(self, ast, scope):
        return None

    def visitWhile(self, ast: While, scope):
        if not isinstance(ast.exp, BooleanLiteral):
            raise TypeMismatchInStatement(ast)
        _ = [self.visit(x, scope) for x in ast.sl]

    def visitCallStmt(self, ast, scope):
        # TODO: Check Undeclared Procedure
        Checker.checkUndeclared(scope, ast.method, Procedure())

    # Visit Literal Values

    def visitIntLiteral(self, ast, scope):
        return IntLiteral(ast.value)

    def visitFloatLiteral(self, ast, scope):
        return FloatLiteral(ast.value)

    def visitBooleanLiteral(self, ast, scope):
        return BooleanLiteral(ast.value)

    def visitStringLiteral(self, ast, scope):
        return StringLiteral(ast.value)

    # Visit Types

    def visitIntType(self, ast, scope):
        return IntType()

    def visitFloatType(self, ast, scope):
        return FloatType()

    def visitBoolType(self, ast, scope):
        return BoolType()

    def visitStringType(self, ast, scope):
        return StringType()

    def visitVoidType(self, ast, scope):
        return VoidType()

    def visitArrayType(self, ast, scope):
        return ArrayType()
