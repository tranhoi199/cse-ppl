# Generated from ./Hello.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#hi.
    def visitHi(self, ctx:HelloParser.HiContext):
        return self.visitChildren(ctx)



del HelloParser