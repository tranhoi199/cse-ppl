import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_201(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('a'),FloatType())],
                        [],[])
                ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,201))

    def test_202(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],
                        [VarDecl(Id('b'),FloatType())],[])
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,202))


    def test_203(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [],
                        [VarDecl(Id('b'),FloatType()), VarDecl(Id('b'),FloatType())],[])
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,203))

    def test_204(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [],
                        [VarDecl(Id('a'),FloatType()), VarDecl(Id('b'),FloatType()), VarDecl(Id('d'),FloatType()) , VarDecl(Id('b'),FloatType())],[])
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,204))

    def test_205(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),FloatType()), VarDecl(Id('b'),FloatType()), VarDecl(Id('d'),FloatType()) , VarDecl(Id('r'),FloatType())],
                        [VarDecl(Id('w'),FloatType()), VarDecl(Id('q'),FloatType()), VarDecl(Id('d'),FloatType()) , VarDecl(Id('t'),FloatType())],[])
                ])
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,205))

    def test_206(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),FloatType()), VarDecl(Id('b'),FloatType()), VarDecl(Id('c'),FloatType()) , VarDecl(Id('d'),FloatType())],
                        [VarDecl(Id('h'),FloatType()), VarDecl(Id('g'),FloatType()), VarDecl(Id('f'),FloatType()) , VarDecl(Id('e'),FloatType())],[]),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),FloatType()), VarDecl(Id('b'),FloatType()), VarDecl(Id('c'),FloatType()) , VarDecl(Id('d'),FloatType())],
                        [VarDecl(Id('h'),FloatType()), VarDecl(Id('c'),FloatType()), VarDecl(Id('f'),FloatType()) , VarDecl(Id('e'),FloatType())],[])
                ])
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,206))

    # ==============================Last week=============================

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