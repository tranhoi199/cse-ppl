from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    
    def visit(self,ast,param):
        return ast.accept(self,param)

    @abstractmethod
    def visitProgram(self, param):
        pass
    @abstractmethod
    def visitVarDecl(self, param):
        pass
    @abstractmethod
    def visitFuncDecl(self, param):
        pass
    @abstractmethod
    def visitIntType(self, param):
        pass
    @abstractmethod
    def visitFloatType(self, param):
        pass
    @abstractmethod
    def visitBoolType(self, param):
        pass
    @abstractmethod
    def visitStringType(self, param):
        pass
    @abstractmethod
    def visitVoidType(self, param):
        pass
    @abstractmethod
    def visitArrayType(self, param):
        pass
    @abstractmethod
    def visitBinaryOp(self, param):
        pass
    @abstractmethod
    def visitUnaryOp(self, param):
        pass
    @abstractmethod
    def visitCallExpr(self, param):
        pass
    @abstractmethod
    def visitId(self, param):
        pass
    @abstractmethod
    def visitArrayCell(self, param):
        pass
    @abstractmethod
    def visitAssign(self, param):
        pass
    @abstractmethod
    def visitWith(self, param):
        pass
    @abstractmethod
    def visitIf(self, param):
        pass
    @abstractmethod
    def visitFor(self, param):
        pass
    @abstractmethod
    def visitContinue(self, param):
        pass
    @abstractmethod
    def visitBreak(self, param):
        pass
    @abstractmethod
    def visitReturn(self, param):
        pass
    @abstractmethod
    def visitWhile(self, param):
        pass
    @abstractmethod
    def visitCallStmt(self, param):
        pass
    @abstractmethod
    def visitIntLiteral(self, param):
        pass
    @abstractmethod
    def visitFloatLiteral(self, param):
        pass
    @abstractmethod
    def visitBooleanLiteral(self, param):
        pass
    @abstractmethod
    def visitStringLiteral(self, param):
        pass
        
class BaseVisitor(Visitor):
    
    def visitProgram(self, param):
        return None
    
    def visitVarDecl(self, param):
        return None
    
    def visitFuncDecl(self, param):
        return None
    
    def visitIntType(self, param):
        return None
    
    def visitFloatType(self, param):
        return None
    
    def visitBoolType(self, param):
        return None
    
    def visitStringType(self, param):
        return None
    
    def visitVoidType(self, param):
        return None
    
    def visitArrayType(self, param):
        return None
    
    def visitBinaryOp(self, param):
        return None
    
    def visitUnaryOp(self, param):
        return None
    
    def visitCallExpr(self, param):
        return None
    
    def visitId(self, param):
        return None
    
    def visitArrayCell(self, param):
        return None
    
    def visitAssign(self, param):
        return None
    
    def visitWith(self, param):
        return None
    
    def visitIf(self, param):
        return None
    
    def visitFor(self, param):
        return None
    
    def visitContinue(self, param):
        return None
    
    def visitBreak(self, param):
        return None
    
    def visitReturn(self, param):
        return None
    
    def visitWhile(self, param):
        return None
    
    def visitCallStmt(self, param):
        return None
    
    def visitIntLiteral(self, param):
        return None
    
    def visitFloatLiteral(self, param):
        return None
    
    def visitBooleanLiteral(self, param):
        return None
    
    def visitStringLiteral(self, param):
        return None