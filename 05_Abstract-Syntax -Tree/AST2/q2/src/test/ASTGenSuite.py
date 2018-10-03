import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_array(self):
        """Simple array:"""
        input = """integer[1..3]"""
        expect = str(ArrayType(RangeType(1,3),IntType()))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_two_dimension_array(self):
        """Two dimension array with negative lower bound"""
        input = """real [-3..0][-10..-1]"""
        expect = str(ArrayType(UnionType(RangeType(-3,0),RangeType(-10,-1)),FloatType()))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_three_dimension_array(self):
        """Three dimension array"""
        input = """integer [1..100][-5..20][100..3000]"""
        expect = str(ArrayType(UnionType(UnionType(RangeType(1,100),RangeType(-5,20)),RangeType(100,3000)),IntType()))
        self.assertTrue(TestAST.test(input,expect,302))
   