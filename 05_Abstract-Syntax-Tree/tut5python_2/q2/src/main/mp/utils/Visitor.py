from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    
    def visit(self,ast,param):
        return ast.accept(self,param)

    @abstractmethod
    def visitUnionType(self, param):
        pass
    @abstractmethod
    def visitArrayType(self, param):
        pass
    @abstractmethod
    def visitRangeType(self, param):
        pass
    @abstractmethod
    def visitIntType(self, param):
        pass
    @abstractmethod
    def visitFloatType(self, param):
        pass    
    
        
class BaseVisitor(Visitor):
    
    def visitUnionType(self, param):
        return None
    
    def visitArrayType(self, param):
        return None
    
    def visitRangeType(self, param):
        return None
    
    def visitIntType(self, param):
        return None
    
    def visitFloatType(self, param):
        return None   
   
 