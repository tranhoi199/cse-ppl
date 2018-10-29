import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_10(self):
        input = r"""
procedure main(); 
begin
end
"""
        expect = "[Symbol(main, MType([], VoidType())]]"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input = r"""
procedure main(); 
begin
end

procedure foo(); 
begin
end

function bar(): integer;
begin
end
"""
        expect = "[Symbol(main, MType([], VoidType())], Symbol(foo, MType([], VoidType())], Symbol(bar, MType([], IntType)]]"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_12(self):
        input = Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType())],[],[],StringType())])
        expect = "[Symbol(foo, MType([StringType], StringType)]]"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_14(self):
        input = Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),StringType()),VarDecl(Id(r'arr_nodes'),ArrayType(0,1000,FloatType()))],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r'q'),StringType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'dd'),ArrayType(0,1000005,BoolType()))],[],VoidType())])
        expect = "[Symbol(foo, MType([IntType, FloatType, FloatType, StringType, StringType, ArrayType(0,1000,FloatType)], VoidType())]]"
        self.assertTrue(TestChecker.test(input,expect,410))
