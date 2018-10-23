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

class CompoundType(Type):
    __metaclass__ = ABCMeta
    pass

class UnionType(CompoundType):
    #firstType: Type
    #secondType: PrimType
    def __init__(self, firstType, secondType):
        self.firstType = firstType
        self.secondType = secondType
        
    def __str__(self):
        return "UnionType(" + str(self.firstType) +  "," + str(self.secondType) + ")"

    def accept(self, v, param):
        return v.visitUnionType(self, param)

class ArrayType(CompoundType):
    #indexType:Type
    #eleType:PrimType
    def __init__(self, indexType, eleType):
        self.indexType = indexType
        self.eleType = eleType
        
    def __str__(self):
        return "ArrayType(" + str(self.indexType) +  "," + str(self.eleType) + ")"

    def accept(self, v, param):
        return v.visitArrayType(self, param)

class PrimType(Type):
    __metaclass__ = ABCMeta
    pass

class IntType(PrimType):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(PrimType):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)

class RangeType(PrimType):
    #lowbound:int
    #highbound:int
    def __init__(self,lowbound,highbound):
        self.lowbound = lowbound
        self.highbound = highbound

    def __str__(self):
        return "RangeType(" + str(self.lowbound) + ',' + str(self.highbound) + ')'

    def accept(self, v, param):
        return v.visitRangeType(self, param)

