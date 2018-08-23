# update: 16/07/2018
from abc import ABC

class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass
class Undeclared(StaticError):
    """k: Kind
       n: string: name of identifier """
    def __init__(self,k,n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n

class Redeclared(StaticError):
    """k: Kind
       n: string: name of identifier """
    def __init__(self,k,n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

class TypeMismatchInExpression(StaticError):
    """exp: AST.Expr"""
    def __init__(self,exp):
        self.exp = exp

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

class TypeMismatchInStatement(StaticError):
    """stmt:AST.Stmt"""
    def __init__(self,stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

class FunctionNotReturn(StaticError):
    """m is a string that is the name of the function"""
    def __init__(self,m):
        self.m = m

    def __str__(self):
        return "Function "+ m + "Not Return "

class BreakNotInLoop(StaticError):
    def __str__(self):
        return "Break Not In Loop"

class ContinueNotInLoop(StaticError):
    def __str__(self):
        return "Continue Not In Loop"

class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"

class UnreachableStatement(StaticError):
    """stmt is AST.Stmt"""
    def __init__(self,stmt):
        self.stmt = stmt
    def __str__(self):
        return "Unreachable statement: "+ str(self.stmt)

class UnreachableFunction(StaticError):
    """m is a string that is the name of the unreachable function"""
    def __init__(self,m):
        self.m = m

    def __str__(self):
        return "Unreachable function: "+ m 

