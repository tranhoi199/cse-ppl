from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    
    def visit(self,ast, param):
        return ast.accept(self,param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass
    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass
    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass
    @abstractmethod
    def visitIntType(self, ast, param):
        pass
    @abstractmethod
    def visitFloatType(self, ast, param):
        pass
    @abstractmethod
    def visitBoolType(self, ast, param):
        pass
    @abstractmethod
    def visitStringType(self, ast, param):
        pass
    @abstractmethod
    def visitVoidType(self, ast, param):
        pass
    @abstractmethod
    def visitArrayType(self, ast, param):
        pass
    @abstractmethod
    def visitBinaryOp(self, ast, param):
        pass
    @abstractmethod
    def visitUnaryOp(self, ast, param):
        pass
    @abstractmethod
    def visitCallExpr(self, ast, param):
        pass
    @abstractmethod
    def visitId(self, ast, param):
        pass
    @abstractmethod
    def visitArrayCell(self, ast, param):
        pass
    @abstractmethod
    def visitAssign(self, ast, param):
        pass
    @abstractmethod
    def visitWith(self, ast, param):
        pass
    @abstractmethod
    def visitIf(self, ast, param):
        pass
    @abstractmethod
    def visitFor(self, ast, param):
        pass
    @abstractmethod
    def visitContinue(self, ast, param):
        pass
    @abstractmethod
    def visitBreak(self, ast, param):
        pass
    @abstractmethod
    def visitReturn(self, ast, param):
        pass
    @abstractmethod
    def visitWhile(self, ast, param):
        pass
    @abstractmethod
    def visitCallStmt(self, ast, param):
        pass
    @abstractmethod
    def visitIntLiteral(self, ast, param):
        pass
    @abstractmethod
    def visitFloatLiteral(self, ast, param):
        pass
    @abstractmethod
    def visitBooleanLiteral(self, ast, param):
        pass
    @abstractmethod
    def visitStringLiteral(self, ast, param):
        pass
        
class BaseVisitor(Visitor):
    
    def visitProgram(self, ast, param):
        return None
    
    def visitVarDecl(self, ast, param):
        return None
    
    def visitFuncDecl(self, ast, param):
        return None
    
    def visitIntType(self, ast, param):
        return None
    
    def visitFloatType(self, ast, param):
        return None
    
    def visitBoolType(self, ast, param):
        return None
    
    def visitStringType(self, ast, param):
        return None
    
    def visitVoidType(self, ast, param):
        return None
    
    def visitArrayType(self, ast, param):
        return None
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitWith(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitWhile(self, ast, param):
        return None
    
    def visitCallStmt(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return None
    
    def visitFloatLiteral(self, ast, param):
        return None
    
    def visitBooleanLiteral(self, ast, param):
        return None
    
    def visitStringLiteral(self, ast, param):
        return None