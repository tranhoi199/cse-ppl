import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_601(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('go'), [
                            BinaryOp('+', IntLiteral(1), IntLiteral(4)),
                            BinaryOp('-', IntLiteral(1), FloatLiteral(4))
                        ]),
                        CallStmt(Id('go'), [
                            BinaryOp('+', IntLiteral(1), IntLiteral(4)),
                            BinaryOp('-', IntLiteral(1), IntLiteral(4))
                        ]),
                        CallStmt(Id('go'), [
                            CallExpr(Id('bar'), [IntLiteral(1),IntLiteral(1)]),
                            BinaryOp('+', IntLiteral(1), IntLiteral(4))
                        ])
                    ]),
                    FuncDecl(Id("go"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Statement: CallStmt(Id(go),[CallExpr(Id(bar),[IntLiteral(1),IntLiteral(1)]),BinaryOp(+,IntLiteral(1),IntLiteral(4))])"
        self.assertTrue(TestChecker.test(input,expect,100))