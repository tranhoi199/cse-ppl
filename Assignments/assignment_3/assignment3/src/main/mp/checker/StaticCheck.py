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
    MType: type of function declaration
    partype: list(Type) - params type
    rettype: Type       - return type
    """

    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class ExpUtils:
    @staticmethod
    def isNumberType(expType):
        return type(expType) is IntType or type(expType) is FloatType

    @staticmethod
    def isNaNType(expType):
        return not ExpUtils.isNumberType(expType)

    @staticmethod
    def isOpForNumber(operator):
        return str(operator).lower() in ['+', '-', '*', '/', 'div', 'mod', '<>', '=', '>', '<', '>=', '<=']

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if type(lType) is FloatType or type(rType) is FloatType else IntType()


class Symbol:
    """
    name: string
    mtype: MType | IntType | FloatType | StringType | BoolType
    value: ???
    kind: Function() | Procedure() | Parameter() | Variable()
    """

    # Default Declare Type is Function Declare - kind Function
    def __init__(self, name, mtype, value=None, kind=Function()):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'

    def getKind(self):
        return self.kind if self.isFunc() else Identifier()

    def toTuple(self):
        return (self.name, type(self.getKind()))

    def isVar(self):
        return type(self.mtype) is not MType

    def isFunc(self):
        return type(self.mtype) is MType

    def toFunc(self):
        self.kind = Function()
        return self

    def toProc(self):
        self.kind = Procedure()
        return self

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    # compare function between 2 instances
    @staticmethod
    def cmp(symbol):
        return symbol.name

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
        # Return merged scope
        newScope = currentScope
        for x in listNewSymbols:
            f = Checker.utils.lookup(x.name, newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope

    @staticmethod
    def checkUndeclared(visibleScope, name, kind):
        # Return Symbol declared in scope
        res = Checker.utils.lookup((name, type(kind)), visibleScope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res

    @staticmethod
    def matchType(patternType, paramType):
        if type(patternType) == type(paramType): return True
        if type(patternType) is FloatType and type(paramType) is IntType: return True
        return False

    @staticmethod
    def checkParamType(pattern, params):
        if len(pattern) != len(params): return False
        return all([Checker.matchType(a, b) for a, b in zip(pattern, params)])


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
        symbols = [self.visit(x, scope) for x in ast.decl]
        # Check Redeclared variable/function/procedure
        scope = Checker.checkRedeclared(scope, symbols)
        # Check entry procedure
        entryPoint = Symbol('main', MType([], VoidType()))
        res = self.lookup(entryPoint.toTuple(), symbols, lambda x: x.toTuple())
        if res is None:
            raise NoEntryPoint()

        return []

    def visitFuncDecl(self, ast: FuncDecl, scope):
        # Return Symbol
        listParams = [self.visit(x, scope).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, scope).toVar() for x in ast.local]
        listNewSymbols = listParams + listLocalVar
        # Check Redeclared parameter/variable
        localScope = Checker.checkRedeclared(scope, listNewSymbols)
        # new scope for statements
        newScope = Scope.merge(scope, localScope)

        stmts = [self.visit(x, newScope) for x in ast.body]

        # check Return Statement

        # check Function Not Return

        kind = Procedure() if type(ast.returnType) is VoidType else Function()
        return Symbol(ast.name.name, MType(listParams, ast.returnType), None, skind)

    def visitVarDecl(self, ast, scope):
        # Return Symbol
        return Symbol(ast.variable.name, MType([], ast.varType), None, Variable())

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
        Checker.checkUndeclared(scope, ast.id.name, Identifier())

        idSymbol = Scope.filterId(scope, ast.id)
        exp1Type = self.visit(ast.expr1)
        exp2Type = self.visit(ast.expr2)
        if not isinstance(exp1Type, IntType) or \
                not isinstance(exp2Type, IntType) or \
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
        # Check Undeclared Procedure
        Checker.checkUndeclared(scope, ast.method.name, Procedure())

    
    # Visit Expression
    # Return Type
    def visitBinaryOp(self, ast: BinaryOp, scope):
        # Return Type
        lType = self.visit(ast.left)
        rType = self.visit(ast.right)
        op = str(ast.op).lower()
        if ExpUtils.isOpForNumber(op): # for number
            if ExpUtils.isNaNType(lType) or ExpUtils.isNaNType(rType):
                raise TypeMismatchInExpression(ast)
            if str(op).lower() in ['div', 'mod']:
                if type(lType) is FloatType or type(rType) is FloatType:
                    raise TypeMismatchInExpression(ast)
                return IntType
            if op in ['+', '-', '*']: return ExpUtils.mergeNumberType(lType, rType)
            if op == '/': return FloatType()
            return BoolType() # = <> >= ...
        else: # for logical
            if type(lType) is not BoolType or type(rType) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitUnaryOp(self, ast: UnaryOp, scope):
        # Return Type
        expType = self.visit(ast.body, scope)
        if (ast.op == '-' and ExpUtils.isNaN(expType)) or (str(ast.op).lower() == 'not' and type(expType) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return expType

    def visitCallExpr(self, ast: CallExpr, scope):
        # Return Type
        symbol = Checker.checkUndeclared(scope, ast.method.name, Function())
        paramType = [self.visit(x) for x in ast.param]
        Checker.checkParamType(symbol.mtype, paramType)
        return symbol.mtype

    def visitId(self, ast: Id, scope):
        # Return Type
        symbol = Checker.checkUndeclared(scope, ast.name, Variable())
        return symbol.mtype

    def visitArrayCell(self, ast: ArrayCell, scope):
        return None

    # Visit Literal Values
    # Return Type of Literal
    def visitIntLiteral(self, ast, scope):
        return IntType()

    def visitFloatLiteral(self, ast, scope):
        return FloatType()

    def visitBooleanLiteral(self, ast, scope):
        return BoolType()

    def visitStringLiteral(self, ast, scope):
        return StringType()


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
