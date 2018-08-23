from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    
    def visit(self,ast,param):
        return ast.accept(self,param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass
    
    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass
    @abstractmethod
    def visitIntType(self, ast, param):
        pass
    
    @abstractmethod
    def visitVoidType(self, ast, param):
        pass
    
    @abstractmethod
    def visitCallExpr(self, ast, param):
        pass
    @abstractmethod
    def visitId(self, ast, param):
        pass
    
    @abstractmethod
    def visitBlock(self, ast, param):
        pass
    
    @abstractmethod
    def visitIntLiteral(self, ast, param):
        pass
    
        
class BaseVisitor(Visitor):
    
    def visitProgram(self, ast, param):
        return None
    
    def visitFuncDecl(self, ast, param):
        return None
    
    def visitIntType(self, ast, param):
        return None
    
    def visitVoidType(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        return None
    
    def visitBlock(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return None
    