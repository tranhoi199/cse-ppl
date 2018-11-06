
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
import sys

sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType(' + '[' + ','.join([str(x) for x in self.partype]) + '],' + str(self.rettype) + ')'


class ExpUtils:
    @staticmethod
    def isNumberType(expType):
        return type(expType) in [IntType, FloatType]

    @staticmethod
    def isNaNType(expType):
        return not ExpUtils.isNumberType(expType)

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()


class Symbol:
    def __init__(self, name, mtype, value=None, kind=Function()):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ']'

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    def getKind(self):
        return self.kind if self.isFunc() else Identifier()

    def toTuple(self):
        return (str(self.name).lower(), type(self.getKind()))

    def toTupleString(self):
        return (str(self.name).lower(), str(self.mtype))

    def isVar(self):
        return type(self.mtype) is not MType

    def isFunc(self):
        return type(self.mtype) is MType

    @staticmethod
    def cmp(symbol):
        return str(symbol.name).lower()

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
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if str(x.name).lower() == str(symbol.name).lower()]) > 0

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
        newScope = currentScope.copy()
        for x in listNewSymbols:
            f = Checker.utils.lookup(str(x.name).lower(), newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope

    @staticmethod
    def checkUndeclared(visibleScope, name, kind, notGlobal=False):
        # Return Symbol declared in scope
        scope = visibleScope if not notGlobal else [x for x in visibleScope if not x.isGlobal]
        res = Checker.utils.lookup((str(name).lower(), type(kind)), scope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res

    @staticmethod
    def matchArrayType(a, b):
        return a.lower == b.lower and a.upper == b.upper and type(a.eleType) == type(b.eleType)

    @staticmethod
    def matchType(patternType, paramType):
        # Handle Array Type
        if ArrayType in [type(x) for x in [patternType, paramType]]:
            if type(patternType) != type(paramType): return False
            return Checker.matchArrayType(patternType, paramType)

        # Handle Primitive Types
        if type(patternType) == type(paramType): return True
        if type(patternType) is FloatType and type(paramType) is IntType: return True
        return False

    @staticmethod
    def checkParamType(pattern, params):
        if len(pattern) != len(params): return False
        return all([Checker.matchType(a, b) for a, b in zip(pattern, params)])




class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()), kind=Procedure()),
        Symbol("putFloatLn", MType([FloatType()], VoidType()), kind=Procedure())
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, globalEnv):
        symbols = [Symbol.fromDecl(x) for x in ast.decl]
        scope = Checker.checkRedeclared(globalEnv, symbols)
        [self.visit(x, scope) for x in ast.decl]
        return []
    
    def visitVarDecl(self, ast, scope):
        return Symbol.fromDecl(ast)

    def visitFuncDecl(self, ast, scope):
        listParams = [self.visit(x, scope).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, scope).toVar() for x in ast.local]
        listNewSymbols = listParams + listLocalVar
        # Check Redeclared parameter/variable
        localScope = Checker.checkRedeclared([], listNewSymbols)
        # Visit statments with params: (scope, retType, inLoop, funcName)
        newScope = Scope.merge(scope, localScope)
        [self.visit(x, (newScope, ast.returnType, False, ast.name.name)) for x in ast.body]
        return Symbol.fromDecl(ast)

    def visitCallStmt(self, ast, params):
        scope = params[0]
        funcName = params[3]
        self.handleCall(ast, scope, funcName, Procedure())
        return (ast, None)

    def visitCallExpr(self, ast, params):
        scope = params[0]
        funcName = params[1]
        symbol = self.handleCall(ast, scope, funcName, Function())
        return symbol.mtype.rettype

    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndeclared(scope, ast.method.name, kind)
        paramType = [self.visit(x, (scope, funcName)) for x in ast.param]
        if not Checker.checkParamType(symbol.mtype.partype, paramType):
            if type(kind) is Procedure:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        return symbol

    def visitBinaryOp(self, ast, params):
        scope = params[0]
        funcName = params[1]
        lType = self.visit(ast.left, (scope, funcName))
        rType = self.visit(ast.right, (scope, funcName))
        op = str(ast.op).lower()
        if str(op).lower() in ['+', '-', '*', '/', 'div', 'mod', '<>', '=', '>', '<', '>=', '<=']:
            if ExpUtils.isNaNType(lType) or ExpUtils.isNaNType(rType):
                raise TypeMismatchInExpression(ast)
            if str(op).lower() in ['div', 'mod']:
                if FloatType in [type(lType), type(rType)]:
                    raise TypeMismatchInExpression(ast)
                return IntType()
            if op in ['+', '-', '*']: return ExpUtils.mergeNumberType(lType, rType)
            if op == '/': return FloatType()
            return BoolType()  # = <> >= ...
        else:  # for logical
            if type(lType) is not BoolType or type(rType) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitFor(self, ast: For, params):
        scope = params[0]
        retType = params[1]
        funcName = params[3]
        idSymbol = Checker.checkUndeclared(scope, ast.id.name, Identifier())
        exp1Type = self.visit(ast.expr1, (scope, funcName))
        exp2Type = self.visit(ast.expr2, (scope, funcName))
        if False in [type(x) is IntType for x in [exp1Type, exp2Type, idSymbol.mtype]]:
            raise TypeMismatchInStatement(ast)
        [self.visit(x, (scope, retType, True, funcName)) for x in ast.loop]
        return (ast, None)

    def visitId(self, ast, params):
        scope = params[0]
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        return symbol.mtype

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()