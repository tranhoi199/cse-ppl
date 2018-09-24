
from abc import ABC,abstractmethod,ABCMeta
from Visitor import Visitor
class AST(ABC):
        def __eq__(self,other):return self.__dict__==other.__dict__
        @abstractmethod
        def accept(self,v,param):return v.visit(self,param)
class Type(AST):__metaclass__=ABCMeta
class IntType(Type):
        def __str__(self):return'{name:"IntType"}'
        def accept(self,v,param):return v.visitIntType(self,param)
class FloatType(Type):
        def __str__(self):return'{name:"FloatType"}'
        def accept(self,v,param):return v.visitFloatType(self,param)
class BoolType(Type):
        def __str__(self):return'{name:"BoolType"}'
        def accept(self,v,param):return v.visitBoolType(self,param)
class StringType(Type):
        def __str__(self):return'{name:"StringType"}'
        def accept(self,v,param):return v.visitStringType(self,param)
class ArrayType(Type):
        def __init__(self,lower,upper,eleType):
                self.lower=lower;self.upper=upper;self.eleType=eleType
        def __str__(self):return'{name:"ArrayType",children:['+str(self.lower)+','+str(self.upper)+','+str(self.eleType)+']}'
        def accept(self,v,param):return v.visitArrayType(self,param)
class VoidType(Type):
        def __str__(self):return'{name:"VoidType()"}'
        def accept(self,v,param):return v.visitVoidType(self,param)
class Program(AST):
        def __init__(self,decl):self.decl=decl
        def __str__(self):return'{name:"Program",children:[{name:"Decl",children:['+','.join((str(i)for i in(self.decl)))+']}]}'
        def accept(self,v,param):return v.visitProgram(self,param)
class Decl(AST):__metaclass__=ABCMeta
class VarDecl(Decl):
        def __init__(self,variable,varType):
                self.variable=variable;self.varType=varType
        def __str__(self):return'{name:"VarDecl",children:['+str(self.variable)+','+str(self.varType)+']}'
        def accept(self,v,param):return v.visitVarDecl(self,param)
class FuncDecl(Decl):
        def __init__(self,name,param,local,body,returnType=VoidType()):
                self.name=name;self.param=param;self.returnType=returnType;self.local=local;self.body=body
        def __str__(self):return'{name:"FuncDecl",children:[{name:"Param",children:['+','.join((str(i)for i in(self.param)))+']},'+str(self.returnType)+',{name:"Local",children:['+','.join((str(i)for i in(self.local)))+']},{name:"Body",children:['+','.join((str(i)for i in(self.body)))+']}]}'
        def accept(self,v,param):return v.visitFuncDecl(self,param)
class Stmt(AST):__metaclass__=ABCMeta
class Assign(Stmt):
        def __init__(self,lhs,exp):
                self.lhs=lhs;self.exp=exp
        def __str__(self):return'{name:"AssignStmt",children:['+str(self.lhs)+','+str(self.exp)+']}'
        def accept(self,v,param):return v.visitAssign(self,param)
class If(Stmt):
        def __init__(self,expr,thenStmt,elseStmt=[]):
                self.expr=expr;self.thenStmt=thenStmt;self.elseStmt=elseStmt
        def __str__(self):return'{name:"If",children:[{name:"ThenStmt",children:['+','.join((str(i)for i in(self.thenStmt)))+']},{name:"ElseStmt",children:['+','.join((str(i)for i in(self.elseStmt)))+']}]}'
        def accept(self,v,param):return v.visitIf(self,param)
class While(Stmt):
        def __init__(self,exp,sl):
                self.sl=sl;self.exp=exp
        def __str__(self):return'{name:"While",children:['+str(self.exp)+','+'{name:"Sl",children:['+','.join((str(i)for i in(self.sl)))+']}]}'
        def accept(self,v,param):return v.visitWhile(self,param)
class For(Stmt):
        def __init__(self,id,expr1,expr2,up,loop):
                self.id=id;self.expr1=expr1;self.expr2=expr2;self.up=up;self.loop=loop
        def __str__(self):return'{name:"For",children:['+str(self.id)+','+str(self.expr1)+','+str(self.expr2)+','+('{name:"Increase"}'if self.up else'{name:"Decrease"}')+','+'{name:"Loop",children:['+','.join((str(i)for i in(self.loop)))+']}]}'
        def accept(self,v,param):return v.visitFor(self,param)
class Break(Stmt):
        def __str__(self):return'{name:"Break"}'
        def accept(self,v,param):return v.visitBreak(self,param)
class Continue(Stmt):
        def __str__(self):return'{name:"Continue"}'
        def accept(self,v,param):return v.visitContinue(self,param)
class Return(Stmt):
        def __init__(self,expr=None):self.expr=expr
        def __str__(self):return'{name:"Return",children:['+('{name:"None"'if self.expr is None else'{name:"Some",children:['+str(self.expr)+']}')+']}'
        def accept(self,v,param):return v.visitReturn(self,param)
class With(Stmt):
        def __init__(self,decl,stmt):
                self.decl=decl;self.stmt=stmt
        def __str__(self):return'{name:"With",children:[{name:"Decl",children:['+','.join((str(i)for i in(self.decl)))+']},{name:"Stmt",children:['+','.join((str(i)for i in(self.stmt)))+']}]}'
        def accept(self,v,param):return v.visitWith(self,param)
class CallStmt(Stmt):
        def __init__(self,method,param):
                self.method=method;self.param=param
        def __str__(self):return'{name:"CallStmt",children:['+str(self.method)+','+'{name:"Param",children:['+','.join((str(i)for i in(self.param)))+']}]}'
        def accept(self,v,param):return v.visitCallStmt(self,param)
class Expr(AST):__metaclass__=ABCMeta
class BinaryOp(Expr):
        def __init__(self,op,left,right):
                self.op=op;self.left=left;self.right=right
        def __str__(self):return'{name:"BinaryOp",children:[{name:"'+self.op+'"},'+str(self.left)+','+str(self.right)+']}'
        def accept(self,v,param):return v.visitBinaryOp(self,param)
class UnaryOp(Expr):
        def __init__(self,op,body):
                self.op=op;self.body=body
        def __str__(self):return'{name:"UnaryOp",children:[{name:"'+self.op+'"},'+str(self.body)+']}'
        def accept(self,v,param):return v.visitUnaryOp(self,param)
class CallExpr(Expr):
        def __init__(self,method,param):
                self.method=method;self.param=param
        def __str__(self):return'{name:"CallExpr",children:['+str(self.method)+','+'{name:"Param",children:['+','.join((str(i)for i in(self.param)))+']}]}'
        def accept(self,v,param):return v.visitCallExpr(self,param)
class LHS(Expr):__metaclass__=ABCMeta
class Id(LHS):
        def __init__(self,name):self.name=name
        def __str__(self):return'{name:"Id",children:[{name:"'+self.name+'"}]}'
        def accept(self,v,param):return v.visitId(self,param)
class ArrayCell(LHS):
        def __init__(self,arr,idx):
                self.arr=arr;self.idx=idx
        def __str__(self):return'{name:"ArrayCell",children:['+str(self.arr)+','+str(self.idx)+']}'
        def accept(self,v,param):return v.visitArrayCell(self,param)
class Literal(Expr):__metaclass__=ABCMeta
class IntLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'{name:"IntLiteral",children:[{name:"'+str(self.value)+'"}]}'
        def accept(self,v,param):return v.visitIntLiteral(self,param)
class FloatLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'{name:"FloatLiteral",children:[{name:"'+str(self.value)+'"}]}'
        def accept(self,v,param):return v.visitFloatLiteral(self,param)
class StringLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'{name:"StringLiteral",children:[{name:"'+self.value+'"}]}'
        def accept(self,v,param):return v.visitStringLiteral(self,param)
class BooleanLiteral(Literal):
        def __init__(self,value):self.value=value
        def __str__(self):return'{name:"BooleanLiteral",children:[{name:"'+str(self.value)+'"}]}'
        def accept(self,v,param):return v.visitBooleanLiteral(self,param)
