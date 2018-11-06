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
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('+', FloatLiteral(1), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(+,FloatLiteral(1),IntLiteral(4)),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,601))

    def test_602(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('/', IntLiteral(1), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(/,IntLiteral(1),IntLiteral(4)),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,602))

    def test_603(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('/', BinaryOp('+', IntLiteral(1), IntLiteral(4)), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(/,BinaryOp(+,IntLiteral(1),IntLiteral(4)),IntLiteral(4)),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,603))

    def test_604(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('+', BinaryOp('+', IntLiteral(1), FloatLiteral(4)), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(+,BinaryOp(+,IntLiteral(1),FloatLiteral(4)),IntLiteral(4)),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,604))


    def test_605(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('+', BinaryOp('+', IntLiteral(1), BinaryOp('*', BooleanLiteral(True), FloatLiteral(4))), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),FloatLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,605))

    def test_606(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [BinaryOp('+', BinaryOp('+', IntLiteral(1), BinaryOp('+', BinaryOp('*', StringLiteral("a"), FloatLiteral(1)), FloatLiteral(4))), IntLiteral(4)), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Expression: BinaryOp(*,StringLiteral(a),FloatLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,606))

    def test_607(self):
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
                            BinaryOp('/', IntLiteral(1), IntLiteral(4)),
                            BinaryOp('-', IntLiteral(1), FloatLiteral(4))
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
        expect = "Type Mismatch In Statement: CallStmt(Id(go),[BinaryOp(/,IntLiteral(1),IntLiteral(4)),BinaryOp(-,IntLiteral(1),FloatLiteral(4))])"
        self.assertTrue(TestChecker.test(input,expect,607))

    def test_608(self):
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
                            BinaryOp('+', IntLiteral(1), IntLiteral(4)),
                            CallExpr(Id('foo'), [FloatLiteral(1),IntLiteral(1)])
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
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,608))

    def test_609(self):
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
        self.assertTrue(TestChecker.test(input,expect,609))




    def test_501(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        For(Id('i'), IntLiteral(1), IntLiteral(2),  True, [])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,501))

    

    def test_502(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[
                        VarDecl(Id('i'), IntType())
                    ],[
                        For(Id('i'), IntLiteral(1), FloatLiteral(2),  True, [])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),FloatLiteral(2),True,[])"
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_503(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[
                        VarDecl(Id('i'), IntType()),
                        VarDecl(Id('j'), FloatType())
                    ],[
                        For(Id('i'), IntLiteral(1), Id('j'),  True, [])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),Id(j),True,[])"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_504(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[
                        VarDecl(Id('i'), IntType()),
                        VarDecl(Id('j'), FloatType())
                    ],[
                        For(Id('i'), IntLiteral(1), CallExpr(Id('foo'), [IntLiteral(1),IntLiteral(1)]),  True, []),
                        For(Id('i'), IntLiteral(1), CallExpr(Id('bar'), [IntLiteral(1),IntLiteral(1)]),  True, [])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),CallExpr(Id(bar),[IntLiteral(1),IntLiteral(1)]),True,[])"
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_301(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [Id('f'), IntLiteral(2)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType())
                ])
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input,expect,301))

    def test_302(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), BooleanLiteral(True)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(4),BooleanLiteral(True)])"
        self.assertTrue(TestChecker.test(input,expect,302))

    def test_303(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [FloatLiteral(4), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType())
                ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(4),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,303))

    def test_304(self):
        input = Program([ 
                    FuncDecl(Id("main"),[],[],[
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('foo'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putFloatLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])]),
                        CallStmt(Id('putIntLn'), [
                            CallExpr(Id('bar'), [IntLiteral(4), IntLiteral(5)])])
                    ]),
                    FuncDecl(Id("foo"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], IntType()),
                    FuncDecl(Id("bar"),
                        [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),FloatType())],
                        [],[], FloatType())
                ])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[CallExpr(Id(bar),[IntLiteral(4),IntLiteral(5)])])"
        self.assertTrue(TestChecker.test(input,expect,304))


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