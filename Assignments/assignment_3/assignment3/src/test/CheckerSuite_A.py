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

    def test_redeclared(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[]),FuncDecl(Id("a"),[],[],[]),FuncDecl(Id("a"),[],[],[])])
        expect = "Redeclared Procedure: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_normal_prog(self):
        input = Program([FuncDecl(Id("main"),[],[],[]),FuncDecl(Id("a"),[],[],[]),FuncDecl(Id("b"),[],[],[])])
        expect = "Unreachable Procedure: a"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_noentry1(self):
        input= """
            procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_noentry2(self):
        """ Test no entry point Statment """
        input = """
                function main():integer;
                var
                    a: real;
                begin
                    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
                end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_undecl1(self):
        """ Test Associative """
        input = """
                var a: integer;
                procedure main();
                var
                    a: real;
                begin
                    a := b + 2 + n or 4 + 5 - g or 2 - 9;
                end
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_multi56(self):
        """ Test Associative """
        input = """
                var a,b: integer;
                procedure main();
                var
                    a: integer;
                begin
                    a := abc();
                end

                function abc():integer;
                var
                    a: integer;
                begin
                    a := a+c;
                end
                var c : integer;
                """
        expect = "Function abcNot Return "
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_multi57(self):
        """ Test Precedence """
        input = """
                var a,b: integer;
                procedure main();
                var
                    a: integer;
                begin
                    a := abc();
                end
                
                procedure abc();
                var
                    a: integer;
                begin
                    a := a+c;
                end
                var c : integer;
                """
        expect = "Undeclared Function: abc"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_multi58(self):
        """ Test Associative """
        input = """
                procedure main();
                var
                    a: real;
                begin
                    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(<,BinaryOp(<>,IntLiteral(5),IntLiteral(6)),BinaryOp(=,IntLiteral(6),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_multi59(self):
        """ Test Associative """
        input = """
                procedure main();
                var
                    a: real;
                begin
                    a := TRUE and then FALSE or     else True or      else false ;
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BinaryOp(orelse,BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_multi62(self):
        """ Test If Statement """
        input = """
                procedure main();
                var a: real;
                b:real;
                c: integer;
                e,g,h: real;
                begin
                    if a = 1 then begin
                        if b > 3 then c := 5;
                        else d := 1;

                        if e < 4 then ok();
                    end else begin
                        if h > 5 then ok(); else lyo();
                        g := 5;
                    end 
                    return ;
                end
                
                procedure ok();
                begin 
                end 
                
                procedure lyo();
                begin
                end
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_multi60(self):
        """ Test If Statement """
        input = """
                procedure main();
                var a: real;
                b:real;
                c: integer;
                d: real;
                e,g,h: real;
                begin
                    if a = 1 then begin
                        if b > 3 then c := 5;
                        else d := 1;

                        if e < 4 then ok();
                    end else begin
                        if h > 5 then ok(); else lyo();
                        g := 5;
                    end 
                    return ;
                end
                
                procedure ok();
                begin 
                end 
                
                function test():boolean;
                var a:integer;
                begin 
                    if a = 1 then return 3;
                    else return true;
                end

                procedure lyo();
                begin
                end
                """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_multi61(self):
        """ Test For Statment """
        input = """
                procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                    continue;
                end
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_unreach3(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if i=1 then return; else i:=foo(1);
                while true do i:= 1;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                function bar(a:integer):integer;
                begin 
                if false then return 4;
                end
            """
        expect = "Function barNot Return "
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_unreach4(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if i=1 then return; else i:=foo(1);
                while true do i:= 1;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                procedure bar(a:integer);
                begin 
                if false then return ;
                end
            """
        expect = "Unreachable Procedure: bar"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_unreach5(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if true then return; else bar(3);
                while true do i:= 1;
                end

                procedure bar(a:integer);
                begin 
                if false then return ;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return a;
                end

                
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_unreach6(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if true then return; else bar(3);
                while true do i:= 1;
                with a:integer; do
                    a:= foo(a);
                end

                procedure bar(a:integer);
                begin 
                if false then return ;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else if true then if true then return 3;
                end

                
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_unreach7(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                A:real;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if true then return; else bar(3);
                while true do 
                begin 
                    for I:= 4 to i+1 do
                    begin
                        with a:integer; do
                            a:= Foo1(a);
                    end
                end
                wITH A:integer; do
                    a:= foo(a);
                end

                procedure bar(a:integer);
                begin 
                if False then return ;
                end

                function foo1(a:integer):integer;
                begin 
                if false then return 4;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                end

                
            """
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_unreach8(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:=1;
                while false do if true then return; else bar(3);
                while true do 
                begin 
                    for I:= 4 to i+1 do
                    begin
                        with a:integer; do
                            a:= Foo1(a);
                    end
                end
                wITH A:integer; do
                    a:= foo(a);
                end

                procedure bar(a:integer);
                begin 
                if False then return ;
                end

                function foO(a:integer):integer;
                begin 
                if false then return 4;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                end

                
            """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_unreach9(self):
        input = """
                var a: real;

                procedure main();
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:= 1;
                while false do if true then return; else i := fOO1(3);
                while true do 
                begin 
                    for I:= 4 to i+1 do
                    begin
                        with a:integer; do
                            a:= Foo1(a);
                    end
                end
                wITH A:integer; do
                    a:= foo(a);
                end

                procedure bar(a:integer);
                begin 
                if False then return ;
                end

                function foO(a:integer):integer;
                begin 
                if false then return 4;
                else return 4;
                end

                function foo1(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                
            """
        expect = "Unreachable Procedure: bar"
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_unreach10(self):
        input = """
                var a: real;
                var i:string;
                procedure main();
                var j:real;
                I:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                if false then i:= FOO(I);
                while false do if true then return; else bar(3);
                while true do 
                begin 
                    for I:= 4 to i+1 do
                    begin
                        with a:integer; do
                            a:= Foo1(a);
                    end
                end
                wITH A:integer; do
                    a:= foo1(a);
                end

                procedure bar(a:integer);
                begin 
                if False then return ;
                end

                function foO(a:integer):integer;
                begin 
                if false then return 4;
                else
                begin
                    for a:=3 to 4 do 
                        return 3;
                end
                end

                function foo1(a:integer):integer;
                begin 
                if false then return 4;
                with a,b:integer; do
                    begin
                        with c,d: integer; do
                            return 3;
                    end
                end

                
            """
        expect = "Function foONot Return "
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_mismatchexp12(self):
        input = """
                var a: string;
                var k:string;
                var b:real;
                procedure main();
                var i,j:real;
                K:boolean;
                A:string;
                B:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[1];
                end
                
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_mismatchexp13(self):
        input = """
                var a: string;
                var k:string;
                var b:real;
                procedure main();
                var i,j:real;
                K:boolean;
                A:string;
                B:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[1];
                end
                procedure foo(a:integer);
                var A:string;
                begin
                end
            """
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_mismatchexp14(self):
        input = """
                var a: string;
                var k:string;
                var b:real;
                procedure main();
                var i,j:real;
                K:boolean;
                A:string;
                B:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[1];
                end
                procedure foo(a:integer);
                var B:string;
                begin
                end
                procedure FOO(a:integer);
                var b:string;
                begin
                end
            """
        expect = "Redeclared Procedure: FOO"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_mismatchexp15(self):
        input = """
                var a: string;
                var k:string;
                var b:real;
                procedure main();
                var i,j:real;
                K:boolean;
                A:string;
                B:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[1];
                end
                function foo(a:integer):integer;
                var B:string;
                begin
                    if true then
                    begin
                        if false then return 0.5;
                        else return 3;
                    end
                    else return 1;
                end
                
            """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(0.5)))"
        self.assertTrue(TestChecker.test(input, expect, 498))
