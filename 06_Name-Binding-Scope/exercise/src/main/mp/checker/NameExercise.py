import sys,os
sys.path.append('../utils')

from Visitor import BaseVisitor
from AST import *

class RedeclaredException(Exception):
    def __init__(self,s):
        self.message = "Redeclared variable \'" + s + '\''

class NameExercise(BaseVisitor):
    def visitProgram(self,ast,param):
        arr = list(filter(lambda x: isinstance(x, FuncDecl), ast.decl))
        [self.visitFuncDecl(ast, func) for func in arr]
        return True

    def visitFuncDecl(self,ast,param):
        lst = param.local
        for i in range(1, len(lst)):
            for j in range(i):
                if lst[i].variable == lst[j].variable:
                    raise RedeclaredException(lst[i].variable.name)