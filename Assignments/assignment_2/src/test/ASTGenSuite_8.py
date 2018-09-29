import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_ArrayCell(self):
        input = """ procedure main();
                    begin
                        arr[1] := 5;
                        (arr + list)[10] := 20;
                    end"""
        expect = str(Program([
            FuncDecl(
                Id('main'),[],[],
                [Assign(ArrayCell(Id('arr'),IntLiteral(1)),IntLiteral(5)),
                 Assign(ArrayCell(BinaryOp('+',Id('arr'),Id('list')),IntLiteral(10)),IntLiteral(20))
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,320))
