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
    mtype: MType | IntType | FloatType | StringType | BoolType | ArrayType
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

    @staticmethod
    def fromVarDecl(decl):
        return Symbol(decl.variable.name, decl.varType, kind=Variable())
    
    @staticmethod
    def fromFuncDecl(decl):
        kind = Procedure() if type(decl.returnType) is VoidType else Function()
        paramType = [x.varType for x in decl.param]
        return Symbol(decl.name.name, MType(paramType, decl.returnType), kind=kind)

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

class Scope:
    @staticmethod
    def start(section):
        print("================   " + section + "   ================")

    @staticmethod
    def end():
        print("=====================================================")


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

    @staticmethod
    def log(scope):
        [print(x) for x in scope]

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
        # Handle Array Type
        if type(patternType) is ArrayType or type(paramType) is ArrayType:
            if type(patternType) != type(paramType): return False
            return patternType.lower == paramType.lower and \
                    patternType.upper == paramType.upper and \
                    type(patternType.eleType) == type(paramType.eleType)

        # Handle Primitive Types
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
        # Return []
        Scope.start("Program")
        symbols = [Symbol.fromDecl(x) for x in ast.decl]
        # Check Redeclared variable/function/procedure
        scope = Checker.checkRedeclared(scope, symbols)
        # Check entry procedure
        entryPoint = Symbol('main', MType([], VoidType()), kind=Procedure())
        res = self.lookup(entryPoint.toTuple(), symbols, lambda x: x.toTuple())
        if res is None:
            raise NoEntryPoint()

        [self.visit(x, scope) for x in ast.decl]
        Scope.end()
        return []

    def visitFuncDecl(self, ast: FuncDecl, scope):
        # Return Symbol
        Scope.start("FuncDecl")
        listParams = [self.visit(x, scope).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, scope).toVar() for x in ast.local]
        listNewSymbols = listParams + listLocalVar
        # Check Redeclared parameter/variable
        localScope = Checker.checkRedeclared([], listNewSymbols)
        # new scope for statements
        newScope = Scope.merge(scope, localScope)
        Scope.log(newScope)

        stmts = [self.visit(x, newScope) for x in ast.body]

        # check Return Statement

        # check Function Not Return

        Scope.end()
        return Symbol.fromDecl(ast)

    def visitVarDecl(self, ast, scope):
        # Return Symbol
        return Symbol.fromDecl(ast)

    def visitAssign(self, ast: Assign, scope):
        Scope.start("Assign")
        Scope.log(scope)
        lhsType = self.visit(ast.lhs, scope)
        expType = self.visit(ast.exp, scope)
        if type(lhsType) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if not Checker.matchType(lhsType, expType):
            raise TypeMismatchInStatement(ast)
        Scope.end()
        return None

    def visitWith(self, ast: With, scope):
        Scope.start("With")
        listVar = [self.visit(x, scope).toVar() for x in ast.decl]
        # Check Redeclared variable
        localScope = Checker.checkRedeclared([], listVar)
        # new scope for statements
        newScope = Scope.merge(scope, localScope)

        _ = [self.visit(x, newScope) for x in ast.stmt]

        Scope.end()
        return None

    def visitIf(self, ast: If, scope):
        Scope.start("If")
        condType = self.visit(ast.expr, scope)
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        _ = [self.visit(x, scope) for x in ast.thenStmt]
        _ = [self.visit(x, scope) for x in ast.elseStmt]
        Scope.end()

    def visitFor(self, ast: For, scope):
        Scope.start("For")
        idSymbol = Checker.checkUndeclared(scope, ast.id.name, Identifier())
        exp1Type = self.visit(ast.expr1, scope)
        exp2Type = self.visit(ast.expr2, scope)
        if type(exp1Type) is not IntType or \
                type(exp2Type) is not IntType or \
                type(idSymbol) is not IntType:
            raise TypeMismatchInStatement(ast)

        _ = [self.visit(x, scope) for x in ast.loop]
        Scope.end()

    def visitContinue(self, ast, scope):
        return None

    def visitBreak(self, ast, scope):
        return None

    def visitReturn(self, ast, scope):
        return None

    def visitWhile(self, ast: While, scope):
        Scope.start("While")
        condType = self.visit(ast.exp, scope)
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        _ = [self.visit(x, scope) for x in ast.sl]
        Scope.end()

    def visitCallStmt(self, ast, scope):
        Scope.start("CallStmt")
        # Check Undeclared Procedure
        Checker.checkUndeclared(scope, ast.method.name, Procedure())
        Scope.end()

    
    # Visit Expression
    # Return Type
    def visitBinaryOp(self, ast: BinaryOp, scope):
        # Return Type
        Scope.start("BinaryOp")
        lType = self.visit(ast.left, scope)
        rType = self.visit(ast.right, scope)
        op = str(ast.op).lower()
        Scope.end()
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
        # Return Type, op: ['-', 'not']
        Scope.start("UnaryOp")
        expType = self.visit(ast.body, scope)
        if (ast.op == '-' and ExpUtils.isNaN(expType)) or (str(ast.op).lower() == 'not' and type(expType) is not BoolType):
            raise TypeMismatchInExpression(ast)
        Scope.end()
        return expType

    def visitCallExpr(self, ast: CallExpr, scope):
        # Return Type
        Scope.start("CallExpr")
        symbol = Checker.checkUndeclared(scope, ast.method.name, Function())
        paramType = [self.visit(x, scope) for x in ast.param]
        Scope.log(symbol.mtype.partype)
        Scope.log(paramType)
        if not Checker.checkParamType(symbol.mtype.partype, paramType):
            raise TypeMismatchInExpression(ast)
        Scope.end()
        return symbol.mtype.rettype

    def visitId(self, ast: Id, scope):
        # Return Type
        Scope.start("Id")
        Scope.log(scope)
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        Scope.end()
        return symbol.mtype

    def visitArrayCell(self, ast: ArrayCell, scope):
        # Return Type
        Scope.start("ArrayCell")
        # arr[idx] - a[1], foo()["bar" + goo()]
        arrType = self.visit(ast.arr) # type of arr
        idxType = self.visit(ast.idx) # type of idx
        if type(idxType) is not IntType or type(arrType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        Scope.end()
        return arrType.eleType

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

    def visitArrayType(self, ast: ArrayType, scope):
        return ArrayType(ast.lower, ast.upper, ast.eleType)
