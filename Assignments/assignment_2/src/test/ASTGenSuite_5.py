import unittest

from AST import *
from TestUtils import TestAST


class ASTGenSuite(unittest.TestCase):
    def test_simple_program_300(self):
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id("main"), [], [], [])]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_simple_function_301(self):
        input = """function foo ():REAL; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"), [], [], [
                     CallStmt(Id("putIntLn"), [IntLiteral(4)])], FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_call_without_parameter_302(self):
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(Id("main"), [], [], [CallStmt(Id("getIntLn"), [])]),
            FuncDecl(Id("foo"), [], [], [CallStmt(Id("putIntLn"), [IntLiteral(4)])], IntType())]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_vardecl_303(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            doSomething(0);
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [
                    VarDecl(Id("x"), FloatType()),
                    VarDecl(Id("y"), FloatType()),
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                [
                    CallStmt(Id("doSomething"), [IntLiteral(0)])
                ],
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_assign_id_intlit_304(self):
        input = """
        procedure foo (); 
        begin
            x := 2;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [], [],
                [
                    Assign(Id("x"), IntLiteral(2))
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_assign_manyids_intlit_305(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := y := 2;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [
                    VarDecl(Id("x"), FloatType()),
                    VarDecl(Id("y"), FloatType()),
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                reversed([
                    Assign(Id("x"), Id("y")),
                    Assign(Id("y"), IntLiteral(2))
                ]),
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_reallit_306(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := 9.1E-34;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [
                    VarDecl(Id("x"), FloatType()),
                    VarDecl(Id("y"), FloatType()),
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                [
                    Assign(Id("x"), FloatLiteral(9.1E-34))
                ],
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_ifstmt_307(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then
            begin
                x := y := .5e3;
                bar(TrUe AND tHeN false);
            end
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [],
                [
                    If(BinaryOp('=', Id("a"), IntLiteral(9)),
                       [
                        Assign(Id("y"), FloatLiteral(.5e3)),
                        Assign(Id("x"), Id("y")),
                        CallStmt(Id("bar"),
                                 [
                            BinaryOp('andthen', BooleanLiteral(
                                True), BooleanLiteral(False))
                        ])
                    ],
                        [])
                ],
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_vardecl_308(self):
        input = """ var a,b,c :INTEGER;
        x,y,z: real;
        """
        expect = str(Program([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType(
        )), VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType()), VarDecl(Id("z"), FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_ifelsestmt_309(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then
            begin
                x := y := .5e3;
                bar(TrUe AND tHeN false);
            end
            else
                executeElseStatement(1,"2",a);
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [],
                [
                    If(BinaryOp('=', Id("a"), IntLiteral(9)),
                       [
                        Assign(Id("y"), FloatLiteral(.5e3)),
                        Assign(Id("x"), Id("y")),
                        CallStmt(Id("bar"),
                                 [
                            BinaryOp('andthen', BooleanLiteral(
                                True), BooleanLiteral(False))
                        ])
                    ],
                        [
                        CallStmt(Id("executeElseStatement"),
                                 [
                            IntLiteral(1),
                            StringLiteral("2"),
                            Id("a")
                        ])
                    ])
                ],
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_whilestmt_310(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            a := 0;
            while (a < 10) AND (x <> 0.) do
            begin 
                a := a + 1;
            end
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [],
                [
                    VarDecl(Id("x"), FloatType()),
                    VarDecl(Id("y"), FloatType()),
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                [
                    Assign(Id("a"), IntLiteral(0)),
                    While(BinaryOp("AND",
                                   BinaryOp('<', Id("a"), IntLiteral(10)),
                                   BinaryOp('<>', Id("x"), FloatLiteral(0.))),
                          [
                        Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))
                    ])
                ],
                BoolType()
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_forstmt_311(self):
        input = """
        procedure _foo123(); 
        begin
            for i := 1 to 1e3 do
                a := b := fALsE;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("_foo123"),
                [],
                [],
                [
                    For(Id("i"), IntLiteral(1), FloatLiteral(1e3), True,
                        reversed([
                            Assign(Id("a"), Id("b")),
                            Assign(Id("b"), BooleanLiteral(False))
                        ]))
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_breakstmt_continuestmt_returnstmt_312(self):
        input = """
        procedure _foo123(); 
        begin
            break;
            continue;
            return -1.e-3;
            return;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("_foo123"),
                [],
                [],
                [
                    Break(),
                    Continue(),
                    Return(UnaryOp('-', FloatLiteral(1.e-3))),
                    Return()
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_withstmt_313(self):
        input = """
        procedure _foo123(); 
        begin
            with a,b:integer;c:STRING; do
                d := c[a] + b;
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("_foo123"),
                [],
                [],
                [
                    With(
                        [
                            VarDecl(Id("a"), IntType()),
                            VarDecl(Id("b"), IntType()),
                            VarDecl(Id("c"), StringType()),
                        ],
                        [
                            Assign(Id("d"), BinaryOp(
                                "+", ArrayCell(Id("c"), Id("a")), Id("b")))
                        ]
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_array_314(self):
        input = """
        var a : array [-1 .. 3] of INTEGER;
            b : ArRaY [1 .. 5] of real;
            c : aRRay [5 .. -8] of bOoLeAn;
            d : ARRAY [-20 .. -10] of sTRINg;
        """
        expect = str(Program([
            VarDecl(Id("a"), ArrayType(-1, 3, IntType())),
            VarDecl(Id("b"), ArrayType(1, 5, FloatType())),
            VarDecl(Id("c"), ArrayType(5, -8, BoolType())),
            VarDecl(Id("d"), ArrayType(-20, -10, StringType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_assignstmt_315(self):
        input = """
            function abc(): integer;
            begin
            	a:=b:=c:=3;
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("abc"), [], [],
                         reversed([
                             Assign(Id("a"), Id("b")),
                             Assign(Id("b"), Id("c")),
                             Assign(Id("c"), IntLiteral(3))
                         ]),
                         IntType())
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_indexexp_316(self):
        input = """
            procedure abc();
            begin
            	a[1][2][3] := -.5e3;
            end
            """
        expect = str(Program([FuncDecl(Id("abc"), [], [], [Assign(ArrayCell(ArrayCell(ArrayCell(
            Id("a"), IntLiteral(1)), IntLiteral(2)), IntLiteral(3)), UnaryOp('-', FloatLiteral(.5e3)))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_nested_compountstmts_317(self):
        input = """
            procedure _();
            begin
            	begin
                    begin
                        foo(a);
                    end
                end
            end
            """
        expect = str(
            Program([FuncDecl(Id("_"), [], [], [CallStmt(Id("foo"), [Id("a")])])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_empty_compoundstmt_318(self):
        input = """
            procedure _();
            begin

                //this is an empty compound statement

            end
            """
        expect = str(Program([FuncDecl(Id("_"), [], [], [])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_exp_319(self):
        input = """
            procedure _();
            begin
                foo := 1 * -2e09 div 3;
            end
            """
        expect = str(Program([FuncDecl(Id("_"), [], [],
                                       [
            Assign(Id("foo"), BinaryOp("div", BinaryOp(
                "*", IntLiteral(1), UnaryOp("-", FloatLiteral(2e09))), IntLiteral(3)))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_funcdecl_320(self):
        input = """
            FUNCTION _1() : array [10 .. -10] of sTrInG;
            begin
            end
            """
        expect = str(
            Program([FuncDecl(Id("_1"), [], [], [], ArrayType(10, -10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_funcdecl_with_one_param_321(self):
        input = """
            FUNCTION _1(A:INTEGER) : ARRAY [0 .. 10] of sTrInG;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType())
        ], [], [], ArrayType(0, 10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_funcdecl_with_many_params_322(self):
        input = """
            FUNCTION _1(A,__b,c_2:INTEGER) : ARRAY [0 .. 10] of sTrInG;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType())
        ], [], [], ArrayType(0, 10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_funcdecl_with_many_params_323(self):
        input = """
            FUNCTION _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN) : ARRAY [0 .. 10] of sTrInG;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType()),
            VarDecl(Id("x"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("y"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("z"), ArrayType(1, 3, BoolType()))
        ], [], [], ArrayType(0, 10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_procdecl_with_one_param_324(self):
        input = """
            procedure _1(A:INTEGER);
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType())
        ], [], [])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_procdecl_with_many_params_325(self):
        input = """
            PROCEDURE _1(A,__b,c_2:INTEGER);
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType())
        ], [], [])]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_procdecl_with_many_params_326(self):
        input = """
            Procedure _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN);
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType()),
            VarDecl(Id("x"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("y"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("z"), ArrayType(1, 3, BoolType()))
        ], [], [])]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_funcdecl_with_many_params_and_locals_327(self):
        input = """
            FUNCTION _1(A,__b,c_2:INTEGER) : ARRAY [0 .. 10] of sTrInG;
            var x_, _y_, z : real; m,n: INTEGER;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType())
        ],
            [
            VarDecl(Id("x_"), FloatType()),
            VarDecl(Id("_y_"), FloatType()),
            VarDecl(Id("z"), FloatType()),
            VarDecl(Id("m"), IntType()),
            VarDecl(Id("n"), IntType())
        ], [], ArrayType(0, 10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_funcdecl_with_many_params_and_locals_328(self):
        input = """
            FUNCTION _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN) : ARRAY [0 .. 10] of sTrInG;
            var x_, _y_, z : real; m,n: INTEGER;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType()),
            VarDecl(Id("x"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("y"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("z"), ArrayType(1, 3, BoolType()))
        ],
            [
            VarDecl(Id("x_"), FloatType()),
            VarDecl(Id("_y_"), FloatType()),
            VarDecl(Id("z"), FloatType()),
            VarDecl(Id("m"), IntType()),
            VarDecl(Id("n"), IntType())
        ], [], ArrayType(0, 10, StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_procdel_with_many_params_and_locals_329(self):
        input = """
            PrOcEdUrE _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN) ;
            var x_, _y_, z : real; m,n: INTEGER;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id("_1"),
                                       [
            VarDecl(Id("A"), IntType()),
            VarDecl(Id("__b"), IntType()),
            VarDecl(Id("c_2"), IntType()),
            VarDecl(Id("x"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("y"), ArrayType(1, 3, BoolType())),
            VarDecl(Id("z"), ArrayType(1, 3, BoolType()))
        ],
            [
            VarDecl(Id("x_"), FloatType()),
            VarDecl(Id("_y_"), FloatType()),
            VarDecl(Id("z"), FloatType()),
            VarDecl(Id("m"), IntType()),
            VarDecl(Id("n"), IntType())
        ], [])]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_funcdecl_with_stmts_330(self):
        input = r"""
            fUNCtiON _1(): string ;
            begin
                foo("abc");
                bar("xy\nz");
            end
            """
        expect = str(Program([FuncDecl(Id("_1"), [], [],
                                       [
            CallStmt(Id("foo"), [StringLiteral("abc")]),
            CallStmt(Id("bar"), [StringLiteral(r"xy\nz")])
        ], StringType())]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_procdecl_with_stmts_331(self):
        input = r"""
            procedure _1() ;
            begin
                foo("abc");
                bar("xy\nz",1.5e0);
            end
            """
        expect = str(Program([FuncDecl(Id("_1"), [], [],
                                       [
            CallStmt(Id("foo"), [StringLiteral("abc")]),
            CallStmt(Id("bar"), [StringLiteral(r"xy\nz"), FloatLiteral(1.5e0)])
        ])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_vardecl_332(self):
        input = r"""
            VaR myVar : INTEGER ; foo: real;
            """
        expect = str(Program(
            [
                VarDecl(Id("myVar"), IntType()),
                VarDecl(Id("foo"), FloatType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_manydecls_333(self):
        input = r"""
            VaR myVar : INTEGER ; foo   ,   bar: real;
            function a(b:array [-1 .. 1] of BOOLEAN):boolean;
            begin
                doSomething();
            end
            vAr __ : STRING;
            """
        expect = str(Program(
            [
                VarDecl(Id("myVar"), IntType()),
                VarDecl(Id("foo"), FloatType()),
                VarDecl(Id("bar"), FloatType()),
                FuncDecl(Id("a"), [VarDecl(Id("b"), ArrayType(-1, 1, BoolType()))],
                         [], [CallStmt(Id("doSomething"), [])], BoolType()),
                VarDecl(Id("__"), StringType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_assign_indexexps_334(self):
        input = r"""
            procedure foo();
            begin
                a[1] := b[c] := 3.0E-5;
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         reversed([
                             Assign(ArrayCell(Id("a"), IntLiteral(1)),
                                    ArrayCell(Id("b"), Id("c"))),
                             Assign(ArrayCell(Id("b"), Id("c")),
                                    FloatLiteral(3.0E-5))
                         ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_nested_ifstmts_335(self):
        input = r"""
            procedure foo();
            begin
                if a = 0 then
                    if b = a then
                        bar();
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    If(BinaryOp("=", Id("a"), IntLiteral(0)),
                       [
                        If(BinaryOp("=", Id("b"), Id("a")),
                           [
                            CallStmt(Id("bar"), [])
                        ], [])
                    ], [])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_nested_ifstmts_336(self):
        input = r"""
            procedure foo();
            begin
                if a = 0 then bar();
                else
                    if b or    else TRUE then
                    begin end
                    else
                        foo(bar);  
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    If(BinaryOp("=", Id("a"), IntLiteral(0)),
                       [
                        CallStmt(Id("bar"), [])
                    ],
                        [
                        If(BinaryOp("orelse", Id("b"), BooleanLiteral(True)), [],
                           [
                            CallStmt(Id("foo"), [Id("bar")])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_dangling_else_337(self):
        input = r"""
            procedure foo();
            begin
                if 1 then
                    if 2 then
                        if 3 then
                            bar();
                else
                    print("This is the \'else\' of if 3");
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    If(IntLiteral(1),
                       [
                        If(IntLiteral(2),
                           [
                            If(IntLiteral(3),
                               [
                                CallStmt(Id("bar"), [])
                            ],
                                [
                                CallStmt(Id("print"), [StringLiteral(
                                    r"This is the \'else\' of if 3")])
                            ])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_resolve_dangling_else_with_compoundstmt_338(self):
        input = r"""
            procedure foo();
            begin
                if 1 then
                    if 2 then
                    begin
                        if 3 then
                            bar();
                    end
                else
                    print("This is the \'else\' of if 2");
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    If(IntLiteral(1),
                       [
                        If(IntLiteral(2),
                           [
                            If(IntLiteral(3),
                               [
                                CallStmt(Id("bar"), [])
                            ])
                        ],
                            [
                            CallStmt(Id("print"), [StringLiteral(
                                r"This is the \'else\' of if 2")])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_resolve_dangling_else_with_compoundstmt_339(self):
        input = r"""
            procedure foo();
            begin
                if 1 then
                begin
                    if 2 then
                    begin
                        if 3 then
                            bar();
                    end
                end
                else
                    print("This is the \'else\' of if 1");
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    If(IntLiteral(1),
                       [
                        If(IntLiteral(2),
                           [
                            If(IntLiteral(3),
                               [
                                CallStmt(Id("bar"), [])
                            ])
                        ])
                    ],
                        [
                        CallStmt(Id("print"), [StringLiteral(
                            r"This is the \'else\' of if 1")])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_whilestmt_340(self):
        input = r"""
            procedure foo();
            begin
                while trUE do 
                begin
                    bar();
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    While(BooleanLiteral(True),
                          [
                        CallStmt(Id("bar"), [])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_whilestmt_341(self):
        input = r"""
            procedure foo();
            begin
                WHILE FALSE do 
                begin
                    bar();
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    While(BooleanLiteral(False),
                          [
                        CallStmt(Id("bar"), [])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_whilestmt_342(self):
        input = r"""
            procedure foo();
            begin
                WHILE 1 < 2 do 
                begin
                    foo();
                    bar();
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    While(BinaryOp("<", IntLiteral(1), IntLiteral(2)),
                          [
                        CallStmt(Id("foo"), []),
                        CallStmt(Id("bar"), [])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_nested_whilestmts_343(self):
        input = r"""
            procedure foo();
            begin
                WHILE 1 < 2 do 
                begin
                    wHiLe 0. do
                        something();
                        (*This is a comment*)
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    While(BinaryOp("<", IntLiteral(1), IntLiteral(2)),
                          [
                        While(FloatLiteral(0.),
                              [
                            CallStmt(Id("something"), [])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_nested_whilestmts_344(self):
        input = r"""
            procedure foo();
            begin
                WHILE 1 < 2 do wHiLe 0. do
                    begin
                        While True dO nothing();
                    end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    While(BinaryOp("<", IntLiteral(1), IntLiteral(2)),
                          [
                        While(FloatLiteral(0.),
                              [
                            While(BooleanLiteral(True),
                                  [
                                CallStmt(Id("nothing"), [])
                            ])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_forstmt_downto_345(self):
        input = r"""
            procedure foo();
            begin
                FOR i := 100 downto 1+1 Do
                begin
                    {Do something here}
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    For(Id("i"), IntLiteral(100), BinaryOp("+", IntLiteral(1), IntLiteral(1)), False,
                        [

                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_forstmt_to_346(self):
        input = r"""
            procedure foo();
            begin
                FOR x := a[0] TO a[2] do
                begin
                    PrintLn("Hello");
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    For(Id("x"), ArrayCell(Id("a"), IntLiteral(0)), ArrayCell(Id("a"), IntLiteral(2)), True,
                        [
                        CallStmt(Id("PrintLn"), [
                            StringLiteral("Hello")])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_forstmt_to_347(self):
        input = r"""
            procedure foo();
            begin
                FOR x := -   1 TO 1[2] do
                begin
                    PrintLn("Hello");
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    For(Id("x"), UnaryOp("-", IntLiteral(1)), ArrayCell(IntLiteral(1), IntLiteral(2)), True,
                        [
                        CallStmt(Id("PrintLn"), [
                            StringLiteral("Hello")])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_nested_forstmts_348(self):
        input = r"""
            procedure foo();
            begin
                FOR x := -   1 TO 1[2] do
                    for y := 0 downto -10e1
                    do
                        begin
                            a();
                            b();
                        end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    For(Id("x"), UnaryOp("-", IntLiteral(1)), ArrayCell(IntLiteral(1), IntLiteral(2)), True,
                        [
                        For(Id("y"), IntLiteral(0), UnaryOp("-", FloatLiteral(10e1)), False,
                            [
                            CallStmt(Id("a"), []),
                            CallStmt(Id("b"), [])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_nested_forstmts_349(self):
        input = r"""
            procedure foo();
            begin
                FOR x := -   1 TO 1[2] do
                begin
                    for y := 0 downto -10e1
                    do
                        begin
                            a();
                            for _ := 1.0 to 2.0 do
                                x := nOT arr[tRuE];
                        end
                end
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    For(Id("x"), UnaryOp("-", IntLiteral(1)), ArrayCell(IntLiteral(1), IntLiteral(2)), True,
                        [
                        For(Id("y"), IntLiteral(0), UnaryOp("-", FloatLiteral(10e1)), False,
                            [
                            CallStmt(Id("a"), []),
                            For(Id("_"), FloatLiteral(1.0), FloatLiteral(2.0), True,
                                [
                                Assign(Id("x"), UnaryOp("nOT", ArrayCell(
                                    Id("arr"), BooleanLiteral(True))))
                            ])
                        ])
                    ])
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_nested_withstmts_350(self):
        input = r"""
            procedure foo();
            begin
                WiTh a:integer; b:array [-1 .. 1] of string;
                do
                    with x,y,z:bOOleAn; do
                        say("Something");
            end
            """
        expect = str(Program(
            [
                FuncDecl(Id("foo"),
                         [], [],
                         [
                    With(
                        [
                            VarDecl(Id("a"), IntType()),
                            VarDecl(
                                Id("b"), ArrayType(-1, 1, StringType()))
                        ],
                        [
                            With(
                                [
                                    VarDecl(Id("x"), BoolType()),
                                    VarDecl(Id("y"), BoolType()),
                                    VarDecl(Id("z"), BoolType())
                                ],
                                [
                                    CallStmt(
                                        Id("say"), [StringLiteral("Something")])
                                ]
                            )
                        ]
                    )
                ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_manydecls_351(self):
        input = r"""
            var _, __ : REAL; _1     : STRING;
            procedure foo();
            begin
                
            end
            function bar(i,j:iNtEgEr;A11:boolean):array [0 .. -5] of rEaL;
            var a,b,c:INTEGER;
            begin
                begin
                    begin
                    end
                end
            end
            """
        expect = str(Program(
            [
                VarDecl(Id("_"), FloatType()),
                VarDecl(Id("__"), FloatType()),
                VarDecl(Id("_1"), StringType()),
                FuncDecl(Id("foo"), [], [], []),
                FuncDecl(Id("bar"),
                         [
                    VarDecl(Id("i"), IntType()),
                    VarDecl(Id("j"), IntType()),
                    VarDecl(Id("A11"), BoolType())
                ],
                    [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ], [], ArrayType(0, -5, FloatType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_manydecls_352(self):
        input = r"""
            var _, __ : REAL; _1     : STRING;
            procedure foo();
            begin
                
            end
            function bar(i,j:iNtEgEr;A11:boolean):array [-100 .. -5] of rEaL;
            var a,b,c:INTEGER;
            begin
                begin
                    begin
                        a := b := X := y := (Z+1)[0.0*3] := 1+1-2/3;
                    end
                end
            end
            """
        expect = str(Program(
            [
                VarDecl(Id("_"), FloatType()),
                VarDecl(Id("__"), FloatType()),
                VarDecl(Id("_1"), StringType()),
                FuncDecl(Id("foo"), [], [], []),
                FuncDecl(Id("bar"),
                         [
                    VarDecl(Id("i"), IntType()),
                    VarDecl(Id("j"), IntType()),
                    VarDecl(Id("A11"), BoolType())
                ],
                    [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                    [
                    Assign(ArrayCell(BinaryOp("+", Id("Z"), IntLiteral(1)), BinaryOp("*", FloatLiteral(0.0), IntLiteral(3))),
                           BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(1)), BinaryOp("/", IntLiteral(2), IntLiteral(3)))),
                    Assign(Id("y"), ArrayCell(BinaryOp(
                        "+", Id("Z"), IntLiteral(1)), BinaryOp("*", FloatLiteral(0.0), IntLiteral(3)))),
                    Assign(Id("X"), Id("y")),
                    Assign(Id("b"), Id("X")),
                    Assign(Id("a"), Id("b"))
                ], ArrayType(-100, -5, FloatType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_manydecls_353(self):
        input = r"""
            var _, __ : REAL; _1     : STRING;
            procedure foo();
            begin
                IF (2-1.0) > 1.0 THEN
                    bar();
                elsE return FalSe aNd
                        ThEn TRUE;
            end
            function bar(i,j:iNtEgEr;A11:boolean):array [-100 .. -5] of rEaL;
            var a,b,c:INTEGER;
            begin
                begin
                    begin
                        a := b := X := y := (Z+1)[0.0*3] := 1+1-2/3;
                    end
                end
            end
            """
        expect = str(Program(
            [
                VarDecl(Id("_"), FloatType()),
                VarDecl(Id("__"), FloatType()),
                VarDecl(Id("_1"), StringType()),
                FuncDecl(Id("foo"), [], [],
                         [
                    If(BinaryOp(">", BinaryOp("-", IntLiteral(2), FloatLiteral(1.0)), FloatLiteral(1.0)),
                       [
                        CallStmt(Id("bar"), [])
                    ],
                        [
                        Return(BinaryOp("andthen", BooleanLiteral(
                            False), BooleanLiteral(True)))
                    ])
                ]),
                FuncDecl(Id("bar"),
                         [
                    VarDecl(Id("i"), IntType()),
                    VarDecl(Id("j"), IntType()),
                    VarDecl(Id("A11"), BoolType())
                ],
                    [
                    VarDecl(Id("a"), IntType()),
                    VarDecl(Id("b"), IntType()),
                    VarDecl(Id("c"), IntType())
                ],
                    [
                    Assign(ArrayCell(BinaryOp("+", Id("Z"), IntLiteral(1)), BinaryOp("*", FloatLiteral(0.0), IntLiteral(3))),
                           BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(1)), BinaryOp("/", IntLiteral(2), IntLiteral(3)))),
                    Assign(Id("y"), ArrayCell(BinaryOp(
                        "+", Id("Z"), IntLiteral(1)), BinaryOp("*", FloatLiteral(0.0), IntLiteral(3)))),
                    Assign(Id("X"), Id("y")),
                    Assign(Id("b"), Id("X")),
                    Assign(Id("a"), Id("b"))
                ], ArrayType(-100, -5, FloatType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_callexp_354(self):
        input = r"""
            procedure main(); 
            begin
                a := foo(1,2,3) + bar(x,y);
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
                                       [
            Assign(Id("a"), BinaryOp("+", CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), CallExpr(Id("bar"), [Id("x"), Id("y")])))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_exp_355(self):
        input = r"""
            procedure main(); 
            begin
                myExpr := foo(1,2,3) + bar(x,y) MOD a and THEN b[x + 3];
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
        [
            Assign(Id("myExpr"), BinaryOp("andthen",BinaryOp("+", CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), BinaryOp("MOD",CallExpr(Id("bar"), [Id("x"), Id("y")]),Id("a"))),ArrayCell(Id("b"),BinaryOp("+",Id("x"),IntLiteral(3)))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_exp_356(self):
        input = r"""
            procedure main(); 
            begin
                e := -- -noT TrUe; 
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
        [
            Assign(Id("e"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("noT",BooleanLiteral(True))))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_exp_357(self):
        input = r"""
            procedure main(); 
            begin
                e := a/b*c DIV 9e3Mod 2and FALSE ;
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
        [
            Assign(Id("e"),
                    BinaryOp("and",
                        BinaryOp("Mod",
                            BinaryOp("DIV",
                                BinaryOp("*",
                                    BinaryOp("/",
                                        Id("a"),
                                        Id("b")),
                                    Id("c")),
                                FloatLiteral(9e3)),
                            IntLiteral(2)),
                        BooleanLiteral(False)))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_exp_358(self):
        input = r"""
            procedure main(); 
            begin
                e := x+y-z Or False;
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
        [
            Assign(Id("e"),
                    BinaryOp("Or",
                        BinaryOp("-",
                            BinaryOp("+",Id("x"),Id("y")),
                            Id("z")),
                        BooleanLiteral(False)))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_exp_359(self):
        input = r"""
            procedure main(); 
            begin
                e := ((1. = 2.) <> (3. < 4.)) <= ((5. > 6.) >= (7. = 8.));
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [],
        [
            Assign(Id("e"),
                    BinaryOp("<=",
                        BinaryOp("<>",
                            BinaryOp("=",FloatLiteral(1.),FloatLiteral(2.)),
                            BinaryOp("<",FloatLiteral(3.),FloatLiteral(4.))),
                        BinaryOp(">=",
                            BinaryOp(">",FloatLiteral(5.),FloatLiteral(6.)),
                            BinaryOp("=",FloatLiteral(7.),FloatLiteral(8.)))))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_funcdecl_360(self):
        input = r"""
            function foo(): String;
            begin
            return ok();
            end
        """
        expect =str(Program([FuncDecl( Id("foo"),[],[],[Return(CallExpr(Id("ok"),[]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_assign_361(self):
        input = r"""
            procedure foo();
            begin
                a := b := "hello\nworld";
            end
        """
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),StringLiteral(r'hello\nworld')),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 361))