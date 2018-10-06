import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_expression_with_assignment(self):
        """Simple program: int main() {} """
        input = """a := b := 4"""
        expect = str(Binary(":=",Id("a"),Binary(":=",Id("b"),IntLiteral(4))))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_expression_with_andor_compare(self):
        """More complex program"""
        input = """a += b -= a and (b > 3)"""
        expect = str(Binary("+=",Id("a"),Binary("-=",Id("b"),Binary("and",Id("a"),Binary(">",Id("b"),IntLiteral(3))))))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_expression_with_boolean(self):
        """More complex program"""
        input = """a or b and True"""
        expect = str(Binary("and",Binary("or",Id("a"),Id("b")),BooleanLiteral(True)))
        self.assertTrue(TestAST.test(input,expect,302))