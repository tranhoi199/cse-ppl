# update: 16/07/2018
from abc import ABC

# Kind
class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"

class Procedure(Kind):
    def __str__(self):
        return "Procedure"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"


# Static Error
class StaticError(Exception):
    pass

class Redeclared(StaticError):
    """
    2.1 Redeclared Variable/Function/Procedure/Parameter

    k: Kind
    n: string: name of identifier
    """

    def __init__(self, k: Kind, n: str):
        self.k = k
        self.n = n

    def __str__(self):
        return "Redeclared " + str(self.k) + ": " + self.n


class Undeclared(StaticError):
    """
    2.2 Undeclared Identifier/Function/Procedure

    k: Kind
    n: string: name of identifier
    """

    def __init__(self, k, n):
        self.k = k
        self.n = n

    def __str__(self):
        return "Undeclared " + str(self.k) + ": " + self.n


class TypeMismatchInStatement(StaticError):
    """
    2.3 Type Mismatch In Statement

    stmt:AST.Stmt
    """

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


class TypeMismatchInExpression(StaticError):
    """
    2.4 Type Mismatch In Expression

    exp: AST.Expr
    """

    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.exp)


class FunctionNotReturn(StaticError):
    """
    m is a string that is the name of the function
    """

    def __init__(self, m):
        self.m = m

    def __str__(self):
        return "Function " + self.m + "Not Return "


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

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Unreachable statement: " + str(self.stmt)


class Unreachable(StaticError):
    """
    k: kind
    m is a string that is the name of
    the unreachable function/procedure
    """

    def __init__(self, k, m):
        self.k = k
        self.m = m

    def __str__(self):
        return "Unreachable " + str(self.k) + ": " + self.m
