import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_11(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[FloatLiteral(1.4)])])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[FloatLiteral(1.4)])"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('/', FloatLiteral(1.4), FloatLiteral(1.4))])])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(/,FloatLiteral(1.4),FloatLiteral(1.4))])"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[BinaryOp('+', IntLiteral(1), FloatLiteral(1.4))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(1), FloatLiteral(1.4))])])]
                    )
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(+,IntLiteral(1),FloatLiteral(1.4))])"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(4), IntLiteral(4))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('-', IntLiteral(4), BooleanLiteral(True))])
                ])])
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLiteral(4),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(4), StringLiteral("123"))])])])
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(4),StringLiteral(123))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(4), BooleanLiteral(False))])])])
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(4),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('-', IntLiteral(4), IntLiteral(7))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('/', IntLiteral(4), BooleanLiteral(False))])
                ])])
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLiteral(4),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_19(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(4), IntLiteral(7))]),
                    CallStmt(Id("putFloatLn"),[BinaryOp('*', IntLiteral(4), IntLiteral(9))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('/', IntLiteral(4), IntLiteral(7))])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(/,IntLiteral(4),IntLiteral(7))])"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_20(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[BinaryOp('/', IntLiteral(4), IntLiteral(9))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('/', IntLiteral(4), IntLiteral(7))])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(/,IntLiteral(4),IntLiteral(7))])"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_21(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[IntLiteral(4)]),
                    CallStmt(Id("putFloatLn"),[StringLiteral("123")])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putFloatLn),[StringLiteral(123)])"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_22(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[IntLiteral(4)]),
                    CallStmt(Id("putFloatLn"),[BinaryOp('/', IntLiteral(4), IntLiteral(9))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('+', IntLiteral(4), IntLiteral(7)), 
                    BinaryOp('+', IntLiteral(4), IntLiteral(7))])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(+,IntLiteral(4),IntLiteral(7)),BinaryOp(+,IntLiteral(4),IntLiteral(7))])"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_23(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[BinaryOp('/', IntLiteral(4), BinaryOp('/', IntLiteral(4), IntLiteral(9)))]),
                    CallStmt(Id("putIntLn"),[BinaryOp('/', IntLiteral(4), BinaryOp('/', IntLiteral(4), IntLiteral(9)))])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(/,IntLiteral(4),BinaryOp(/,IntLiteral(4),IntLiteral(9)))])"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloatLn"),[BinaryOp('/', IntLiteral(4), Id(''))])
                ])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[BinaryOp(/,IntLiteral(4),BinaryOp(/,IntLiteral(4),IntLiteral(9)))])"
        self.assertTrue(TestChecker.test(input,expect,422))