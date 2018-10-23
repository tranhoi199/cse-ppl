import sys, os

sys.path.append('../main/mp/checker')

import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        input = """procedure main(); begin foo();end"""
        expect = [Symbol("main", MType([], VoidType()))]
        self.assertTrue(TestChecker.test(input,expect,400))
    def test2(self):
        input = Program([
            VarDecl(Id('a'), IntType())
        ])
        expect = """[Symbol("a",MType([],IntType])]"""
        self.assertTrue(TestChecker.test(input,expect,401))
    def test3(self):
        input = Program([
            VarDecl(Id('a'), IntType()),
            VarDecl(Id('b'), FloatType()),
            FuncDecl(Id('func'))
        ])
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,402))
    # def test3(self):
    #     input = Program([])
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         putIntLn();
    #     end"""
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],[],[
    #         CallStmt(Id("foo"),[])])])
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],[],[
    #                 CallStmt(Id("putIntLn"),[])])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    
    