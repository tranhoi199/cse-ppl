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
    
    ##############################################
    # 2.1 Test Redeclared 
    ##############################################

    def test_redeclare1(self):
        input = """
                var a: real;
                procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                end
                """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_redeclare2(self):
        input = """
                var a: real;
                procedure main();
                var a: real;
                b:real;
                i,j:integer;
                a:boolean;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                end
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclare3(self):
        input = """
                var a: real;

                procedure main();
                var a: real;
                b:real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                end

                var a :boolean;

                procedure b();
                var a: real;
                begin 
                end
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_redeclare4(self):
        input = """
                var a: real;
                
                procedure main();
                var a: real;
                b:real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                    i := foo();
                end
                
                function foo():integer;
                var a: real;
                begin 
                    with a,b:integer; do 
                    begin
                    end
                    return 1;
                end
                
                """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclare5(self):
        input = """
                var a: real;

                procedure main();
                var a: real;
                b:real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                end

                procedure b();
                var a: real;
                begin 
                    with wi,wi:integer; do 
                    begin
                    end
                end
                """
        expect = "Redeclared Variable: wi"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    #########################################
    # Test 2.2 Undeclare
    #########################################
    
    def test_undeclare1(self):
        input = """
                var a: real;
                procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for k := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                end
                """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_undeclare2(self):
        input = """
                var a: real;
                procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    foo(3);
                    end
                end
                function foo():integer;
                begin
                end
                """
        #FIXME: Not sure this is an exception or not
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_undeclare3(self):
        input = """
                var a: real;
                procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod foo() = 1 then break;
                    end
                end
            """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_undeclare4(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod i = 1 then break;
                    end
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    #####################################################
    # 2.3 Type MisMatch in statement 
    #####################################################

    def test_mismatchstmt1(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                begin
                    for a := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 1 = 1 then break;
                    end
                end
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_mismatchstmt2(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                begin
                    if i then j := i;
                end
            """
        expect = "Type Mismatch In Statement: If(Id(i),[AssignStmt(Id(j),Id(i))],[])"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_mismatchstmt3(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                begin
                    for i := 1 to a do begin
                        for j := i downto 1 do
                            if (i + j) mod 1 = 1 then break;
                    end
                end
            """
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),Id(a),True,[For(Id(j)Id(i),IntLiteral(1),False,[If(BinaryOp(=,BinaryOp(mod,BinaryOp(+,Id(i),Id(j)),IntLiteral(1)),IntLiteral(1)),[Break],[])])])"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_mismatchstmt4(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                begin
                    while i do j := i;
                end
            """
        expect = "Type Mismatch In Statement: While(Id(i),[AssignStmt(Id(j),Id(i))])"
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_mismatchstmt5(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                    while true do j := i;
                    if true then a:= 4.9;
                    while k do while k do while k do j := i;
                    if k then if k then if k then k:=true;
                    for i := i downto 1 do
                        if (i + j) mod 1 = 1 then break;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_mismatchstmt6(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                    return 3;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_mismatchstmt7(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                    return;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_mismatchstmt8(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_mismatchstmt9(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                a:=foo();
                end
                function foo():real;
                var a:integer;
                begin
                return a ;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_mismatchstmt10(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                end
                function foo():real;
                var a:boolean;
                begin
                return a;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_mismatchstmt11(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                a:= foo();
                end
                function foo():real;
                var a:boolean;
                begin
                if a then return 1;
                else return a;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_mismatchstmt12(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                a:= foo();
                end
                function foo():integer;
                var a:boolean;
                begin
                
                if a then 
                    begin
                        if a then  
                        begin
                            return 3;
                        end
                        return 3.5;
                    end
                else return 4;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(3.5)))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_mismatchstmt13(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                a:=foo();
                end
                function foo():real;
                var a:boolean;
                begin
                if a then return 1;
                else return 2.69;
                if a then 
                    begin
                        if a then  
                        begin
                            return 3.9;
                        end
                        return 5;
                    end
                else return 4;
                end
            """
        expect = "Unreachable statement: If(Id(a),[If(Id(a),[Return(Some(FloatLiteral(3.9)))],[]),Return(Some(IntLiteral(5)))],[Return(Some(IntLiteral(4)))])"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_mismatchstmt14(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                a:= foo()[3];
                end
                function foo():array [1 .. 5] of integer;
                var a:array[1 .. 5] of integer;
                begin
                return a ;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_mismatchstmt15(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                end
                function foo():array [1 .. 5] of real;
                var a:array[1 .. 5] of integer;
                begin
                return a ;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_mismatchstmt16(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                end
                function foo():array [1 .. 5] of integer;
                var a:array[1 .. 6] of integer;
                begin
                return a ;
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_mismatchstmt17(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                foo(i,j,i);
                end
                procedure foo(a:integer;b,c:integer);
                var d:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_mismatchstmt18(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                foo(i,j,i);
                end
                procedure foo(a:integer;b,c:real);
                var d:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_mismatchstmt19(self):
        input = """
                var a: real;
                procedure main();
                var i,j:integer;
                k:boolean;
                begin
                foo(i,j,k);
                end
                procedure foo(a:integer;b,c:integer);
                var d:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i),Id(j),Id(k)])"
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_mismatchstmt20(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                begin
                foo(i,j,i);
                end
                procedure foo(a:integer;b,c:integer);
                var a:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i),Id(j),Id(i)])"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_mismatchstmt21(self):
        input = """
                var a,b: real;
                procedure main();
                var i,j:real;
                k:boolean;
                A:string;
                B:array[1 .. 5] of integer;
                d:string;
                begin
                fOo(a,b,b);
                end
                procedure foO(a:string;b,c:array[1 .. 5] of integer);
                var d:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_mismatchstmt22(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(a,b,b);
                end
                procedure FOO(a:string;b,c:array[1 .. 5] of real);
                var a:array[1 .. 5] of integer;
                begin
                end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(a),Id(b),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    ###########################################################
    # 2.4 Type MisMatch in Expr
    ##########################################################
    def test_mismatchexp1(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[1];
                end
                
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_mismatchexp2(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[2*d];
                end
                
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_mismatchexp3(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[2*i];
                end
                
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(*,IntLiteral(2),Id(i)))"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_mismatchexp4(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := a[2*d];
                end
                
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(*,IntLiteral(2),Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_mismatchexp5(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := k := b[2*d];
                end
                
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(k),ArrayCell(Id(b),BinaryOp(*,IntLiteral(2),Id(d))))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_mismatchexp6(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                i := j := b[2*d/4];
                end
                
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(/,BinaryOp(*,IntLiteral(2),Id(d)),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_mismatchexp7(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                d := ((d+1*2)+3*4) div 5;
                i := i*2+4/5+6-1;
                i := d/4;
                i := d;
                k := d > i;
                k := k and not k;
                d := -d;
                end
                
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_mismatchexp8(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[3],b,b);
                i := foo(b[3],b,b)*3+4-5 div 6;

                end
                function foo(a:integer;b,c:array[1 .. 5] of integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                return a[3];
                end
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_mismatchexp9(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(i,b,b);
                i := foo(b[3],b,b)*3+4-5 div 6;

                end
                function foo(a:integer;b,c:array[1 .. 5] of integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                return a[3];
                end
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(i),Id(b),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_mismatchexp10(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[6],b,b);
                i := foo(b[3],b,b)*3+4-5 div 6;

                end
                function foo(a:real;b,c:array[1 .. 5] of integer):integer;
                var b:array[1 .. 5] of integer;
                begin
                return a[3];
                end
            """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_mismatchexp11(self):
        input = """
                var a: real;
                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:integer;
                begin
                d := ((d+1*2)+3*4) div 5;
                i := i*2+4/5+6-1;
                i := d/4;
                i := d;
                k := d > foo()*6;
                k := k and not k and then b[2] > i or else b[2] < 5;
                d := -d;
                k := not k;
                d := d*2.5;
                end
                function foo():integer;
                begin
                return 3;
                end
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),BinaryOp(*,Id(d),FloatLiteral(2.5)))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    #############################################################
    # 2.5 Function not return
    #############################################################

    def test_funcnotret1(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(a,b,b);
                end
                procedure foo(a:string;b,c:array[1 .. 5] of integer);
                var d:array[1 .. 5] of integer;
                begin
                return;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_funcnotret2(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(a,b,b);
                end
                function foo(a:string;b,c:array[1 .. 5] of integer):integer;
                var d:array[1 .. 5] of integer;
                begin
                return 3;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_funcnotret3(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(a,b,b);
                end

                function foo(a:string;b,c:array[1 .. 5] of integer):integer;
                var d:array[1 .. 5] of integer;
                begin
                    with a:integer; do
                    begin 
                        if a < 3 then a:=4 ;
                        else begin 
                            for a := 1 to a do return 4;
                        end                
                        return a;            
                    end
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_funcnotret4(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(a,b,b);
                end

                function foo(a:string;b,c:array[1 .. 5] of integer):integer;
                var d:array[1 .. 5] of integer;
                begin
                    with a:integer; do
                    begin 
                        if a < 3 then a:=4 ;
                        else begin 
                            for a := 1 to a do break;
                        end                            
                    end
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_funcnotret5(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(a,b,b);
                end

                function foo(a:string;b,c:array[1 .. 5] of integer):integer;
                var d:array[1 .. 5] of integer;
                begin
                    with a:integer; do
                    begin 
                        if a < 3 then a:=4 ;
                        else begin 
                            for a := 1 to a do break;
                        end                            
                    end
                end

                function bar(a:string;b,c:array[1 .. 5] of integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    with a:integer; do
                    begin 
                        if a < 3 then a:=4 ;
                        else begin 
                            for a := 1 to a do break;
                        end                            
                    end
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_funcnotret6(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := fOo(b[10]);
                end

                function Foo(a:integer):integer;
                var b:array[1 .. 5] of integer;
                begin
                    with b:integer; do
                    begin 
                        if b < 3 then return foo(a) ;
                        else begin 
                            for b := 1 to b do return 3;
                        end                            
                    end
                end
            """
        expect = "Function FooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_funcnotret7(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(a:integer):integer;
                var c:array[1 .. 5] of integer;
                begin
                    with b:integer; do
                    begin 
                        if b < 3 then b:= foo(c) ;
                        else begin 
                            for b := 1 to b do return 3;
                        end                            
                    end
                end
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_funcnotret8(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then return b + foo(b+1);
                    else return b;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_funcnotret9(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(a:integer):integer;
                var b:array[1 .. 5] of integer;
                begin
                    if b>3 then return b + foo(b+1);
                    else return b;
                end
            """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(b),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_funcnotret10(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then b:= b + foo(b+1);
                    else b := foo(b+1);
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_funcnotret11(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                        end
                    end
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 468))

    ##################################################################
    # 2.6 Break Continue not in loop
    ##################################################################

    def test_breakcontinue1(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                            else break;
                        end
                    end
                end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_breakcontinue2(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                            else continue;
                        end
                    end
                end
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_breakcontinue3(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                break;
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                            else return 3;
                        end
                    end
                end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_breakcontinue4(self):
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
                i := foo(b[10]);
                for i := 4 to 5 do
                begin
                    if i < 3 then continue;
                    else
                    begin
                        for i := 4 to 5 do break;
                    end
                end
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                            else return 3;
                        end
                    end
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_breakcontinue5(self):
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
                for i := 4 to 5 do
                begin
                    if i < 3 then continue;
                    else
                    begin
                        for i := 4 to 5 do break;
                    end
                end
                if i < 3 then break;
                end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_breakcontinue6(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then continue;
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_breakcontinue7(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then continue;
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                while true do
                begin 
                    while false do break;
                    if i > 5 then continue;
                    else while false do continue;
                end
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 475))

    #################################################################
    # 2.7 No Entry Point
    #################################################################
    def test_noentry3(self):
        input = """
                var a: real;

                function main():integer;
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then continue;
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                while true do
                begin 
                    while false do break;
                    if i > 5 then continue;
                    else while false do continue;
                end
                end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_noentry4(self):
        input = """
                var a: real;

                function bar():integer;
                var j:real;
                i:integer;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then continue;
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                while true do
                begin 
                    while false do break;
                    if i > 5 then continue;
                    else while false do continue;
                end
                end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    ##############################################################
    # 2.8 Unreachable Stmt
    #############################################################
    def test_unreachstmt1(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then continue;
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                while true do
                begin 
                    while false do break;
                    if i > 5 then begin continue; i:=6; end
                    else while false do continue;
                end
                end
            """
        expect = "Unreachable statement: AssignStmt(Id(i),IntLiteral(6))"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_unreachstmt2(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then begin continue; i:= i;end 
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                end
            """
        expect = "Unreachable statement: AssignStmt(Id(i),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_unreachstmt3(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then begin continue;end 
                        else
                        begin
                            for i := 4 to 5 do break;
                        end
                    end
                    if i < 3 then break;
                end
                return;
                i:=i;
                i:= i*2 div 3 + 1;
                end
            """
        expect = "Unreachable statement: AssignStmt(Id(i),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test_unreachstmt4(self):
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
                for i := 4 to 5 do
                begin
                    for i:= 3 to 4 do
                    begin 
                        if i < 3 then begin continue;end 
                        else
                        begin
                            for i := 4 to 5 do begin continue ; j := 3.14159; end
                        end
                    end
                    if i < 3 then break;
                end
                return;
                end
            """
        expect = "Unreachable statement: AssignStmt(Id(j),FloatLiteral(3.14159))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_unreachstmt5(self):
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
                end
                
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_unreachstmt6(self):
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
                i := foo(4);
                if false then i:=1;
                while false do i:=1;
                while true do i:= 1;
                i:=1;
                end
                function foo(a:integer):integer;
                begin 
                if false then return 4;
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_unreachstmt7(self):
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
                while false do begin i:=1; break; return; end 
                while true do i:= 1;
                i:=1;
                end
                function foo(a:integer):integer;
                begin 
                if false then return 4;
                end
            """
        expect = "Unreachable statement: Return(None)"
        self.assertTrue(TestChecker.test(input, expect, 484))

    #####################################################
    # 2.9 Unreachable func/proc
    #####################################################

    def test_unreach1(self):
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
                while false do i:=1;
                while true do i:= 1;
                i:=1;
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                function bar(a:integer):integer;
                begin 
                if false then return 4;
                else return 2;
                end
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_unreach2(self):
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
                while false do i:=1;
                while true do i:= 1;
                i:=foo(1);
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                function bar(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end
            """
        expect = "Unreachable Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 486))
    
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
        self.assertTrue(TestChecker.test(input, expect, 487))

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
        self.assertTrue(TestChecker.test(input, expect, 488))

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
        self.assertTrue(TestChecker.test(input, expect, 489))

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
        self.assertTrue(TestChecker.test(input, expect, 490))
    
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
        self.assertTrue(TestChecker.test(input, expect, 491))

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

    def test_mismatchexp16(self):
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
                i := j := b[1] := foo(b[2]);
                end
                function foo(a:integer):integer;
                var B:string;
                begin
                    if true then
                    begin
                        if false then return A;
                        else return 3;
                        if false then return 3;
                    end
                    else return 1;
                end
                
            """
        expect = "Unreachable statement: If(BooleanLiteral(False),[Return(Some(IntLiteral(3)))],[])"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_mismatchexp17(self):
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
                i := j := b[1] := foo(b[2]);
                end
                function foo(a:integer):integer;
                var B:string;
                begin
                    if true then
                    begin
                        if false then 
                            return 1 ;
                        for a:= 1 to 10 do
                            begin 
                                if false then return 5;
                                if true then return 6;
                            end
                    end
                    else return 1;
                end
                
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 500))


    def test_redeclared_parameter_2(self):
        input = """
var x4:integer;

function x3(x1:string; x2:integer):integer;
begin
    return x6(1, "x");
end

function x6(x2:integer; x2:string):integer;
begin
    return 100;
end

procedure main(); 
var x1:integer;
    x2:real;
    x3:string;
begin
    x1:= x3("a",2);
    x2:= x6(2,"2");
    return;
end
"""
        expect = "Redeclared Parameter: x2"
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_redeclared_parameter_3(self):
        input = """
var x4:integer;

function x3(x1:string; x2:integer):integer;
begin
    return x6(1, "x");
end

function x6(a:integer; x2:string):integer;
begin
    if true then
        a := a + 1;
    else
        return 0;
end

procedure main(); 
var x1:integer;
    x2:real;
    x3:string;
begin
    x1:= x3("a",2);
    x2:= x6(2,"2");
    return;
end
"""
        expect = "Function x6Not Return "
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_redeclared_parameter_4(self):
        input = """
var x4:integer;

function x6(a:integer; x2:string):integer;
begin
    if true then
    begin
        a := a + 1;
        return a;
    end
    else
        return 0;
    
    a := 1;
end

procedure main(); 
var x1:integer;
    x2:real;
    x3:string;
begin
    x2:= x6(2,"2");
    return;
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_redeclared_parameter_5(self):
        input = """
var x4:integer;

procedure x6(a:integer; x2:string);
begin
    if true then
    begin
        a := a + 1;
        return;
    end
    else
        return;
    
    a := 1;
end

procedure main(); 
var x1:integer;
    x2:real;
    x3:string;
begin
    x6(1,"a");
    return;
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_redeclared_parameter_6(self):
        input = """
            var x4:integer;

            procedure x6(a:integer; x2:string);
            begin
                if true then
                begin
                    a := a + 1;
                    return 6;
                end
                else
                    return;
            end

            procedure main(); 
            var x1:integer;
                x2:real;
                x3:string;
            begin
                x6(1,"a");
                return;
            end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(6)))"
        self.assertTrue(TestChecker.test(input,expect,505))
    
    def test_funcnotret12(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                i := foo(b[10]);
                end

                function foo(b:integer):integer;
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return foo(3);
                            else 
                            begin
                                if b > 5 then return 3;
                            end
                        end
                    end
                    else return 1;
                end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 506))
    
    def test_funcnotret13(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(b[10]);
                end

                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    if b>3 then 
                    begin
                        with a,b:integer;do 
                        begin
                            if b < 4 then return;
                            else 
                            begin
                                if b > 5 then return;
                            end
                        end
                    end
                    else return ;
                end
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 507))

    def test_funcnotret14(self):
        input = """
                var a: real;

                procedure main();
                var i,j:real;
                k:boolean;
                a:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(b[10]);
                end

                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
            """
        expect = "Redeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 508))
    def test_funcnotret15(self):
        input = """
                var a: integer;

                procedure main();
                var i,j:real;
                k:boolean;
                h:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(1);
                fOO2(a);
                for a:= 1 to 10 do
                    return;
                end

                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
                procedure foo2(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 509))
    def test_funcnotret16(self):
        input = """
                var a: integer;

                procedure main();
                var i,j:real;
                k:boolean;
                h:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(a);
                FOO2(1);
                for a:= 1 to 10 do
                    return;
                end

                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
                procedure foo2(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 510))
    
    def test_funcnotret17(self):
        input = """
                var a: integer;

                procedure main(a:integer);
                var i,j:real;
                k:boolean;
                h:string;
                b:array[1 .. 5] of integer;
                d:string;
                begin
                foo(a);
                FOO2(1);
                for a:= 1 to 10 do
                    return;
                end

                procedure foo(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
                procedure foo2(b:integer);
                var a:array[1 .. 5] of integer;
                begin
                    
                end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 511))