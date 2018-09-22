from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)

class BoolType(Type):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitBoolType(self, param)

class StringType(Type):
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return v.visitStringType(self, param)

class ArrayType(Type):
    #lower:int
    #upper:int
    #eleType:Type
    def __init__(self, lower, upper, eleType):
        self.lower = lower
        self.upper = upper
        self.eleType = eleType
        
    def __str__(self):
        return "ArrayType(" + str(self.lower) + "," + str(self.upper) + "," + str(self.eleType) + ")"

    def accept(self, v, param):
        return v.visitArrayType(self, param)

class VoidType(Type): 
    def __str__(self):
        return "VoidType()" 

    def accept(self, v, param):
        return v.visitVoidType(self, param)

class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    #variable:Id
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

class FuncDecl(Decl):
    #name: Id
    #param: list(VarDecl)
    #returnType: Type => VoidType for Procedure
    #local:list(VarDecl)
    #body: list(Stmt)
    def __init__(self, name, param, local, body, returnType=VoidType()):
        self.name = name
        self.param = param
        self.returnType = returnType
        self.local = local
        self.body = body

    def __str__(self):
        return "FuncDecl(" + str(self.name) +               \
        ",[" +  ','.join(str(i) for i in self.param) +      \
        "]," + str(self.returnType) +                       \
        ",[" +  ','.join(str(i) for i in self.local) +      \
        "],[" + ','.join(str(i) for i in self.body) + "])"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Assign(Stmt):
    #lhs:Expr
    #exp:Expr
    def __init__(self, lhs, exp):
        self.lhs = lhs
        self.exp = exp

    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + "," +  str(self.exp) + ")"

    def accept(self, v, param):
        return v.visitAssign(self, param)

class If(Stmt):
    #expr:Expr
    #thenStmt:list(Stmt)
    #elseStmt:list(Stmt)
    def __init__(self, expr, thenStmt, elseStmt=[]):
        self.expr = expr
        self.thenStmt = thenStmt
        self.elseStmt = elseStmt

    def __str__(self):
        return "If(" + str(self.expr) + ",[" + ','.join(str(i) for i in self.thenStmt) + "],[" +  ','.join(str(i) for i in self.elseStmt)  + "])"

    def accept(self, v, param):
        return v.visitIf(self, param)

class While(Stmt):
    #sl:list(Stmt)
    #exp: Expr
    def __init__(self, exp,sl):
        self.sl = sl
        self.exp = exp

    def __str__(self):
        return "While(" + str(self.exp) + ",[" + ','.join(str(i) for i in self.sl) + "])" 

    def accept(self, v, param):
        return v.visitWhile(self, param)

class For(Stmt):
    #id:Id
    #expr1,expr2:Expr
    #loop:list(Stmt)
    #up:Boolean #True => increase; False => decrease
    def __init__(self, id, expr1, expr2,up,loop):
        self.id = id
        self.expr1 = expr1
        self.expr2 = expr2
        self.up = up
        self.loop = loop

    def __str__(self):
        return "For(" + str(self.id) + "" + str(self.expr1) + "," + str(self.expr2) + "," + str(self.up) + ',[' + ','.join(str(i) for i in self.loop) + "])"

    def accept(self, v, param):
        return v.visitFor(self, param)

class Break(Stmt):
    def __str__(self):
        return "Break"

    def accept(self, v, param):
        return v.visitBreak(self, param)
    
class Continue(Stmt):
    def __str__(self):
        return "Continue"

    def accept(self, v, param):
        return v.visitContinue(self, param)

class Return(Stmt):
    #expr:Expr
    def __init__(self, expr = None):
        self.expr = expr

    def __str__(self):
        return "Return(" + ("None" if (self.expr is None) else "Some(" + str(self.expr) + ")") + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)

class With(Stmt):
    #decl:list(VarDecl)
    #stmt:list(Stmt)
    def __init__(self, decl, stmt):
        self.decl = decl
        self.stmt = stmt

    def __str__(self):
        return "With([" + ','.join(str(i) for i in self.decl) + "],[" + ','.join(str(i) for i in self.stmt) +  "])"

    def accept(self, v, param):
        return v.visitWith(self, param)

class CallStmt(Stmt):
    #method:Id
    #param:list(Expr)
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallStmt(" + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

    def accept(self, v, param):
        return v.visitCallStmt(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class BinaryOp(Expr):
    #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class UnaryOp(Expr):
    #op:string
    #body:Expr
    def __init__(self, op, body):
        self.op = op
        self.body = body

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)

class CallExpr(Expr):
    #method:Id
    #param:list(Expr)
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallExpr(" + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Id(LHS):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class ArrayCell(LHS):
    #arr:Expr
    #idx:Expr
    def __init__(self, arr, idx):
        self.arr = arr
        self.idx = idx

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)



class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class IntLiteral(Literal):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class FloatLiteral(Literal):
    #value:float
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)

class StringLiteral(Literal):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)

class BooleanLiteral(Literal):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)
