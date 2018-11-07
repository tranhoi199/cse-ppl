# 1610852 - Huynh Sam Ha

from StaticError import *
from Utils import Utils
from Visitor import *
from AST import *
from functools import reduce
import sys

sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')


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
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def isOpForNumber(operator):
        return str(operator).lower() in ['+', '-', '*', '/', 'div', 'mod', '<>', '=', '>', '<', '>=', '<=']

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()


class Symbol:
    """
    name: string
    mtype: MType | ArrayType | PrimitiveType(IntType | FloatType | StringType | BoolType)
    value: ???
    kind: Function() | Procedure() | Parameter() | Variable()
    isGlobal: boolean
    """

    # Default Declare Type is Function Declare - kind Function
    def __init__(self, name, mtype, value=None, kind=Function(), isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'

    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    def toTuple(self):
        return (str(self.name).lower(), type(self.getKind()))

    def toTupleString(self):
        return (str(self.name).lower(), str(self.mtype))

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    def toGlobal(self):
        self.isGlobal = True
        return self

    # compare function between 2 instances
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
    def start(section):
        # print("================   " + section + "   ================")
        pass

    @staticmethod
    def end():
        # print("=====================================================")
        pass

    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if str(x.name).lower() == str(symbol.name).lower()]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        return reduce(lambda lst, sym: lst if Scope.isExisten(lst, sym) else lst+[sym], currentScope, comingScope)

    @staticmethod
    def log(scope): [print(x) for x in scope]


class Checker:

    utils = Utils()

    @staticmethod
    def checkRedeclared(currentScope, listNewSymbols):
        # Return merged scope
        newScope = currentScope.copy()
        for x in listNewSymbols:
            f = Checker.utils.lookup(Symbol.cmp(x), newScope, Symbol.cmp)
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

    @staticmethod
    def handleReturnStmts(stmts):
        # stmts: (stmt, type) with type: None, VoidType, (...)Type, Break
        for i in range(0, len(stmts)-1):
            if Checker.isStopTypeStatment(stmts[i][1]):
                raise UnreachableStatement(stmts[i+1][0])
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isReturnTypeFunction(retType):
        return type(retType) in [IntType, FloatType, BoolType, StringType, ArrayType]

    @staticmethod
    def isReturnTypeProcedure(retType):
        return type(retType) is VoidType

    @staticmethod
    def isReturnType(retType):
        return Checker.isReturnTypeFunction(retType) or Checker.isReturnTypeProcedure(retType)

    @staticmethod
    def isStopTypeStatment(retType):
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]


# Graph for Call Statements and Call Expression between Functions and Procedures
class Graph:

    link = {} # { 'n1': ['n2', 'n3'], 'n2': [], 'n3': ['n1', 'n2'] }
    visited = {} # { 'n1': True, 'n2': False, 'n3': False }
    invoked = {} # { 'n1': True, 'n2': False, 'n3': False }

    @staticmethod
    def initialize():
        Graph.link.clear()
        Graph.visited.clear()
        Graph.invoked.clear()

    @staticmethod
    def add(u, v=None): # v is None when add new node, else u call v
        u = str(u).lower()
        if type(Graph.link.get(u)) != list:
            Graph.link[u] = []
            Graph.visited[u] = False
            Graph.invoked[u] = False
        if v is None: return
        v = str(v).lower()
        if v != u and v not in Graph.link[u]: 
            Graph.link[u].append(v)
            Graph.invoked[v] = True # v is invoked by u

    @staticmethod
    def log():
        print('Number of nodes in graph: ', len(Graph.link))
        print(Graph.link)
        print(Graph.visited)

    @staticmethod
    def dfs(u):
        u = str(u).lower()
        Graph.visited[u] = True
        [Graph.dfs(v) for v in Graph.link[u] if not Graph.visited[v]]

    @staticmethod
    def getUnreachableNode():
        for u in Graph.link:
            if not Graph.visited[u] and not Graph.invoked[u]: return u
        for u in Graph.link:
            if not Graph.visited[u]: return u
        return None

    @staticmethod
    def setDefaultVisitedNodes(listNodes):
        for u in listNodes: Graph.visited[str(u).lower()] = True


class StaticChecker(BaseVisitor, Utils):

    # Global Environement - Built-in Functions - Default is Function
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putInt", MType([IntType()], VoidType()), kind=Procedure()),
        Symbol("putIntLn", MType([IntType()], VoidType()), kind=Procedure()),
        Symbol("putFloat", MType([FloatType()], VoidType()), kind=Procedure()),
        Symbol("putFloatLn", MType([FloatType()], VoidType()), kind=Procedure()),
        Symbol("putBool", MType([BoolType()], VoidType()), kind=Procedure()),
        Symbol("putBoolLn", MType([BoolType()], VoidType()), kind=Procedure()),
        Symbol("putString", MType([StringType()], VoidType()), kind=Procedure()),
        Symbol("putStringLn", MType([StringType()], VoidType()), kind=Procedure()),
        Symbol("putLn", MType([], VoidType()), kind=Procedure())
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        Graph.initialize()
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, globalEnv):
        Scope.start("Program")
        # Check Redeclared variable/function/procedure
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        scope = Checker.checkRedeclared(globalEnv, symbols)
        # Check no entry procedure "main"
        entryPoint = Symbol('main', MType([], VoidType()), kind=Procedure())
        res = self.lookup(entryPoint.toTupleString(), symbols, lambda x: x.toTupleString())
        if res is None: raise NoEntryPoint()
        # Init graph for unreachable functions and procedures
        listFuncDecl = globalEnv + [entryPoint] + [Symbol.fromDecl(x) for x in ast.decl if type(x) is FuncDecl]
        for x in listFuncDecl: Graph.add(x.name)
        Graph.setDefaultVisitedNodes([u.name for u in globalEnv])
        # Graph.log()
        # Visit declares
        [self.visit(x, scope) for x in ast.decl]
        # Check unreachable function/procedure
        # Graph.log()
        Graph.dfs("main")
        u = Graph.getUnreachableNode()
        if u is not None:
            symbol = self.lookup(u, listFuncDecl, Symbol.cmp)
            raise Unreachable(symbol.getKind(), symbol.name)
        Scope.end()
        return []

    def visitFuncDecl(self, ast: FuncDecl, scope):
        Scope.start("FuncDecl")
        listParams = [self.visit(x, scope).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, scope).toVar() for x in ast.local]
        listNewSymbols = listParams + listLocalVar
        # Check Redeclared parameter/variable
        localScope = Checker.checkRedeclared([], listNewSymbols)
        # Visit statments with params: (scope, retType, inLoop, funcName)
        newScope = Scope.merge(scope, localScope)
        stmts = [self.visit(x, (newScope, ast.returnType, False, ast.name.name)) for x in ast.body]
        # Type of return result
        retType = Checker.handleReturnStmts(stmts)
        # Check function not return
        if Checker.isReturnTypeFunction(ast.returnType) and not Checker.isReturnTypeFunction(retType):
            raise FunctionNotReturn(ast.name.name)
        Scope.end()

    def visitVarDecl(self, ast, scope):
        return Symbol.fromVarDecl(ast)

# Visit Statements - params: (scope, retType, inLoop, funcName)
# Return a tuple (Statement, Type of return type)

    def visitAssign(self, ast: Assign, params):
        # Return None Type
        Scope.start("Assign")
        scope, retType, inLoop, funcName = params
        lhsType = self.visit(ast.lhs, (scope, funcName))
        expType = self.visit(ast.exp, (scope, funcName))
        if type(lhsType) in [ArrayType, VoidType, StringType] or not Checker.matchType(lhsType, expType):
            raise TypeMismatchInStatement(ast)
        Scope.end()
        return (ast, None)

    def visitWith(self, ast: With, params):
        Scope.start("With")
        scope, retType, inLoop, funcName = params
        listVar = [self.visit(x, scope).toVar() for x in ast.decl]
        # Check Redeclared variable
        localScope = Checker.checkRedeclared([], listVar)
        # Visit statements
        newScope = Scope.merge(scope, localScope)
        stmts = [self.visit(x, (newScope, retType, inLoop, funcName)) for x in ast.stmt]
        Scope.end()
        return (ast, Checker.handleReturnStmts(stmts))

    def visitIf(self, ast: If, params):
        Scope.start("If")
        scope, retType, inLoop, funcName = params
        # Check Type Expression
        condType = self.visit(ast.expr, (scope, funcName))
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # Check statments
        stmts1 = [self.visit(x, params) for x in ast.thenStmt]
        stmts2 = [self.visit(x, params) for x in ast.elseStmt]
        # Check return type, is stop when both flow is return
        ret1 = Checker.handleReturnStmts(stmts1)
        ret2 = Checker.handleReturnStmts(stmts2)
        Scope.end()
        if ret1 is None or ret2 is None: return (ast, None)
        if all([x not in [type(ret1), type(ret2)] for x in [Break, Continue]]): return (ast, retType)
        return (ast, Break()) # or use Continue() as alternative

    def visitFor(self, ast: For, params):
        Scope.start("For")
        scope, retType, inLoop, funcName = params
        # Check Undeclared Identifier
        idSymbol = Checker.checkUndeclared(scope, ast.id.name, Identifier(), notGlobal=True)
        # Check Type Expression
        exp1Type = self.visit(ast.expr1, (scope, funcName))
        exp2Type = self.visit(ast.expr2, (scope, funcName))
        if False in [type(x) is IntType for x in [exp1Type, exp2Type, idSymbol.mtype]]:
            raise TypeMismatchInStatement(ast)
        # Visit statements
        stmts = [self.visit(x, (scope, retType, True, funcName)) for x in ast.loop]
        Scope.end()
        retType = Checker.handleReturnStmts(stmts)
        return (ast, None)

    def visitWhile(self, ast: While, params):
        Scope.start("While")
        scope, retType, inLoop, funcName = params
        # Check Type Expression
        condType = self.visit(ast.exp, (scope, funcName))
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # Visit statements
        stmts = [self.visit(x, (scope, retType, True, funcName)) for x in ast.sl]
        Scope.end()
        retType = Checker.handleReturnStmts(stmts)
        return (ast, None)

    def visitContinue(self, ast, params):
        scope, retType, inLoop, funcName = params
        if not inLoop: raise ContinueNotInLoop()
        return (ast, Continue())

    def visitBreak(self, ast, params):
        scope, retType, inLoop, funcName = params
        if not inLoop: raise BreakNotInLoop()
        return (ast, Break())

    def visitReturn(self, ast: Return, params):
        scope, retType, inLoop, funcName = params
        if type(retType) is VoidType and ast.expr:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr, (scope, funcName)) if ast.expr else VoidType()
        if not Checker.matchType(retType, ret):
            raise TypeMismatchInStatement(ast)
        return (ast, ret)

    def visitCallStmt(self, ast: CallStmt, params):
        # Return None Type
        Scope.start("CallStmt")
        scope, retType, inLoop, funcName = params
        self.handleCall(ast, scope, funcName, Procedure())
        Scope.end()
        return (ast, None)


# Visit Expression - params: (scope, funcName)
# Return Type of expression

    def visitBinaryOp(self, ast: BinaryOp, params):
        scope, funcName = params
        op = str(ast.op).lower()
        lType = self.visit(ast.left, (scope, funcName))
        rType = self.visit(ast.right, (scope, funcName))
        if ExpUtils.isOpForNumber(op): # for number
            if ExpUtils.isNaNType(lType) or ExpUtils.isNaNType(rType):
                raise TypeMismatchInExpression(ast)
            if op in ['div', 'mod']:
                if FloatType in [type(lType), type(rType)]:
                    raise TypeMismatchInExpression(ast)
                return IntType()
            if op in ['+', '-', '*']: return ExpUtils.mergeNumberType(lType, rType)
            if op == '/': return FloatType()
            return BoolType() # operators: =, <>, <, >=, ...
        # for logical
        if False in [type(x) is BoolType for x in [lType, rType]]:
            raise TypeMismatchInExpression(ast)
        return BoolType()

    def visitUnaryOp(self, ast: UnaryOp, params):
        scope, funcName = params
        op = str(ast.op).lower() # op: ['-', 'not']
        expType = self.visit(ast.body, (scope, funcName))
        if (op == '-' and ExpUtils.isNaNType(expType)) or (op == 'not' and type(expType) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return expType

    def visitCallExpr(self, ast: CallExpr, params):
        scope, funcName = params
        symbol = self.handleCall(ast, scope, funcName, Function())
        return symbol.mtype.rettype

    def visitId(self, ast: Id, params):
        scope, funcName = params
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        return symbol.mtype

    def visitArrayCell(self, ast: ArrayCell, params):
        scope, funcName = params
        # arr[idx], example: a[1], a[x+5], foo()[4], foo()["bar" + goo()], ...
        arrType = self.visit(ast.arr, (scope, funcName))  # type of arr
        idxType = self.visit(ast.idx, (scope, funcName))  # type of idx
        if type(idxType) is not IntType or type(arrType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return arrType.eleType

    def handleCall(self, ast, scope, funcName, kind): # kind: Procedure() | Function()
        symbol = Checker.checkUndeclared(scope, ast.method.name, kind)
        # Check Match Type
        paramType = [self.visit(x, (scope, funcName)) for x in ast.param]
        if not Checker.checkParamType(symbol.mtype.partype, paramType):
            raise TypeMismatchInExpression(ast) if type(kind) is Function else TypeMismatchInStatement(ast)
        # Update Graph
        Graph.add(funcName, ast.method.name)
        return symbol

# Visit Literal Values => Return Type of Literal

    def visitIntLiteral(self, ast, params):
        return IntType()

    def visitFloatLiteral(self, ast, params):
        return FloatType()

    def visitBooleanLiteral(self, ast, params):
        return BoolType()

    def visitStringLiteral(self, ast, params):
        return StringType()