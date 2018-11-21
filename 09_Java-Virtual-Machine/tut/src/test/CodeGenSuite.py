import sys

import unittest
from TestUtils import TestCodeGen
from AST import *


sys.path.append('../utils')
sys.path.append('../checker')

class CheckCodeGenSuite(unittest.TestCase):

    def test_if_stmt_1(self):
    	input = Program([VarDecl(Id("otr"),IntType()),
    		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),IntLiteral(2)),If(BinaryOp(">",Id("otr"),IntLiteral(3)),
            [CallStmt(Id("putBool"),[BooleanLiteral(True)])],[CallStmt(Id("putBool"),[BooleanLiteral(False)])])])])
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_if_stmt_2(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[If(BinaryOp("=",IntLiteral(5),IntLiteral(3)),
            [CallStmt(Id("putBool"),[BooleanLiteral(True)])],[]),CallStmt(Id("putInt"),[IntLiteral(10)])])])
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_if_stmt_3(self):
    	input = Program([VarDecl(Id("otr"),BoolType()),VarDecl(Id("trl"),IntType()),VarDecl(Id("love"),BoolType()),
    		FuncDecl(Id("main"),[],[],[Assign(Id("trl"),IntLiteral(19)),
            Assign(Id("love"),BooleanLiteral(True)),
            Assign(Id("love"),BinaryOp("and",BinaryOp("<>",Id("trl"),IntLiteral(20)),Id("love"))),If(Id("love"),
            [CallStmt(Id("putInt"),[BooleanLiteral(100)])],[CallStmt(Id("putBool"),[BooleanLiteral(True)])])])])
    	expect = "100"
    	self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_if_stmt_4(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
                If(BooleanLiteral(True),[
                    If(BooleanLiteral(False),[
                        CallStmt(Id("putFloat"),[FloatLiteral(2.4)])
                    ],[
                        CallStmt(Id("putString"),[StringLiteral("Oanh Trinh")])
                    ])
                ],[
                    If(BooleanLiteral(True),[
                        CallStmt(Id("putBool"),[BooleanLiteral(False)])
                    ],[
                        CallStmt(Id("putInt"),[IntLiteral(20)])
                    ])
                ]),
                CallStmt(Id("putString"),[StringLiteral(" loves Trong Luan")])
            ])])
    	expect = "Oanh Trinh loves Trong Luan"
    	self.assertTrue(TestCodeGen.test(input,expect,514))
    

    def test_1(self):
        input = r"""

procedure main();
begin
    if false then begin
        putInt(100);
    end else begin
        putInt(200);
    end
end

"""
        expect = r"""200"""
        self.assertTrue(TestCodeGen.test(input, expect, 101))


    def test_2(self):
        input = r"""

procedure main();
begin
    if false then begin
        putInt(100);
        putFloat(100);
    end else begin
        putInt(200);
        putFloat(200);
    end
end

"""
        expect = r"""200200.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 102))


    def test_3(self):
        input = r"""

procedure main();
begin
    if 5 > 2 then begin
        putInt(100);
        putFloat(100);
    end else begin
        putInt(200);
        putFloat(200);
    end
end

"""
        expect = r"""100100.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 103))


    def test_4(self):
        input = r"""

procedure main();
begin
    if 5 > 2 then begin
        putInt(100);
        putFloat(100);
        if true then putInt(101); else putInt(102);
    end else begin
        putInt(200);
        putFloat(200);
        if true then putInt(201); else putInt(202);
    end
end

"""
        expect = r"""100100.0101"""
        self.assertTrue(TestCodeGen.test(input, expect, 104))


    def test_5(self):
        input = r"""

procedure main();
begin
    if 5*2 + 3 - 5*2 - 3 = 0 then begin
        putInt(100);
        putFloat(100);
        if true then putInt(101); else putInt(102);
    end else begin
        putInt(200);
        putFloat(200);
        if true then putInt(201); else putInt(202);
    end
end

"""
        expect = r"""100100.0101"""
        self.assertTrue(TestCodeGen.test(input, expect, 105))


#     def test_global_otr_1(self):
#     	input = Program([VarDecl(Id("otr"),IntType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),IntLiteral(100)),CallStmt(Id("putInt"),[Id("otr")])])])
#     	expect = "100"
#     	self.assertTrue(TestCodeGen.test(input,expect,501))
#     def test_global_otr_2(self):
#     	input = Program([VarDecl(Id("otr"),BoolType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),BooleanLiteral(True)),CallStmt(Id("putBool"),[Id("otr")])])])
#     	expect = "true"
#     	self.assertTrue(TestCodeGen.test(input,expect,502))
#     def test_global_otr_3(self):
#     	input = Program([VarDecl(Id("otr"),FloatType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),FloatLiteral(16.111998)),CallStmt(Id("putFloat"),[Id("otr")])])])
#     	expect = "16.111998"
#     	self.assertTrue(TestCodeGen.test(input,expect,503))
#     def test_global_otr_4(self):
#     	input = Program([VarDecl(Id("otr"),IntType()),VarDecl(Id("trl"),FloatType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),IntLiteral(22)),CallStmt(Id("putFloat"),[Id("otr")]),
#             Assign(Id("trl"),FloatLiteral(22.1)),CallStmt(Id("putFloat"),[Id("trl")])])])
#     	expect = "22.022.1"
#     	self.assertTrue(TestCodeGen.test(input,expect,504))
#     def test_global_otr_5(self):
#     	input = Program([VarDecl(Id("otr"),IntType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),IntLiteral(22)),CallStmt(Id("putFloat"),[Id("otr")]),
#             Assign(Id("trl"),FloatLiteral(22.1)),CallStmt(Id("putFloat"),[Id("trl")])]),VarDecl(Id("trl"),FloatType())])
#     	expect = "22.022.1"
#     	self.assertTrue(TestCodeGen.test(input,expect,505))
#     def test_global_otr_6(self):
#     	input = Program([VarDecl(Id("otr"),BoolType()),VarDecl(Id("trl"),BoolType()),
#     		FuncDecl(Id("main"),[],[],[Assign(Id("otr"),BooleanLiteral(False)),Assign(Id("trl"),Id("otr")),
#             CallStmt(Id("putBool"),[Id("trl")])])])
#     	expect = "false"
#     	self.assertTrue(TestCodeGen.test(input,expect,506))




