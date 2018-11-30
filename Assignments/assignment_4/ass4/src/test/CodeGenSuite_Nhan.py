import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast1(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_float_ast1(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.12)])])])
        expect = "5.12"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_float_ast2(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.12e-3)])])])
        expect = "0.00512"
        self.assertTrue(TestCodeGen.test(input,expect,503))


    def test_bool_ast1(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putBool"),[BooleanLiteral(True)])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_bool_ast2(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putBool"),[
            BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False))
        ])])])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_bool_ast3(self):
        input = """
            procedure main();
            begin
                putBool(True And False Or True And False or True And True);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_float_int1(self):
        input = """
            procedure main();
            begin
                putFloat(1.2 + 4.5 - 2 / 5 * 4.2 - 1.2e-2 / 2 + 3);
            end
        """
        expect = '7.014'
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_bool_ast3(self):
        input = """
            procedure main();
            begin
                 putBool((10 = 5) and (3.4 <> 4) or (9.8 < 4.7 ) and (4 <= 5.6) or (10 >= 10) and (4 > 2));
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_bool_ast4(self):
        input = """
            procedure main();
            begin
                 putBool((10 = 5) and not not (3.4 <> 4) or (9.8 < 4.7 ) and not (4 <= 5.6) or (9 >= 10) and (4 > 2));
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_float_int2(self):
        input = """
            procedure main();
            begin
                putFloat(-1.2 + 4.5 -- 2 / 5 * 4.2 - - 1.2e-2 / 2 + -3);
            end
        """
        expect = "1.9860001"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_if_stmt1(self):
        input = """
            procedure main();
            begin
                if (1 = 2) then
                    putFloat(1/2);
                else
                    putInt(1+2);
            end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_if_stmt2(self):
        input = """
            procedure main();
            begin
                if (1 = 2) then begin
                    putFloat(1/2);
                    if ( 2 <= 3 ) then
                        putBool(True);
                end
                else
                    putInt(1+2);
                    if (4 > 3) then
                        putBool(False or False);
                    else
                        putString("abc123");
            end
        """
        expect = "3false"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_vardecl1(self):
        input = """
            procedure main();
            var a: integer ; b: real;
            begin
                putString("Hello World !");
            end
        """
        expect = "Hello World !"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_vardecl2(self):
        input = """
            var c,d: boolean;
            procedure main();
            var a: integer ; b: real;
            begin
                putString("Hello World !");
            end
        """
        expect = "Hello World !"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_vardecl3(self):
        input = """
            var c,d: boolean;
            procedure main();
            var a: integer ; b: real;
            begin
                putString("Hello World !");
            end
            var e,f: real;
            procedure foo(a: integer);
            begin
                putFloat(1.2);
            end
        """
        expect = "Hello World !"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_assign1(self):
        input = """
            procedure main();
            var a: integer ; b: real;
            begin
                a := 1;
                putInt(a);
            end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_assign2(self):
        input = """
            procedure main();
            var a: integer ; b: real;
            begin
                a := 1;
                b := 2.3;
                putFloat(a+b);
            end
        """
        expect = "3.3"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_assign3(self):
        input = """
            var d: integer;
            procedure main();
            var a,b: boolean;
                c: String;
            begin
                a := True;
                b := False;
                c := "ahihi";
                d := 1 + 2;
                putBool(a or b and not b or False);
                putString(c);
                putInt(d);
            end
        """
        expect = "trueahihi3"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_assign4(self):
        input = """
            procedure main();
            var a: array [10 .. 19] of integer;
                b: integer;
            begin
                a[12] := 6;
                putInt(a[12]+12);
                f[3] := 3.5;
                putFloat(f[3]+4.5);
            end
            var f: array [1 .. 20] of real;
        """
        expect = "188.0"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_function1(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
            begin
                a := 5;
                putFloat(foo(a)[5]);
            end
            function foo(a: integer): array [1 .. 10] of real;
            var result: array [1 .. 10] of real;
            begin
                result[5] := 10.5;
                putFloat(a+result[5]);
                return result;
            end
        """
        expect = "15.510.5"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_scope1(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
            begin
                a := 1;
                putInt(a);
                with a: real; b: integer; do begin
                    a := 1.5;
                    b := 1;
                    putFloat(a+b+0.15);
                end
                with a: boolean ; b: boolean; do begin
                    b := true;
                    a := b;
                    putBool(a);
                end
                a := a + 2;
                putInt(3);
            end
        """
        expect = "12.65true3"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_while1(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;
            begin
                i := 8 ;
                a := 1 ;
                while (i>0) do begin
                    a := a * i;
                    i := i - 1;
                    if i = 4 then break;
                end
                putInt(a);
            end
            """
        expect = "1680"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_bool_ast5(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putBool(a and b and then a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_bool_ast6(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putBool((a or test()) or else a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "9.5true"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_for1(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;

            begin
                up := 10;
                a := 0;
                for i:=up downto 1 do begin
                    if a > 40 then continue;
                    a := a + i;
                end
                putInt(a);
            end
            var up:integer;
            """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_call_stmt1(self):
        input = """
            procedure main();
            var a,b: integer;
            begin
                b := 6;
                a := factor(b);
                putInt(a);
            end
            function factor(a: integer): integer;
            begin
                if a <= 1 then
                    return 1;
                else
                    return a * factor(a-1);
            end
        """
        expect = "720"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_arr_1(self):
        input = """
            procedure main();
            var i,b: integer;
            begin
                for i := 0 to 9 do
                arr[i] := i;
                for i := 0 to 9 do
                putInt(arr[i]);
            end
            var arr: array [0 .. 9] of integer;
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_arr_2(self):
        input = """
            procedure main();
            var x: array[1 .. 2] of integer;
            begin
                x[1] := 100;
                x[2] := 200;
                putInt(x[1]);
                putInt(x[2]);
                swap(x);
                putInt(x[1]);
                putInt(x[2]);
            end
            procedure swap(a: array[1 .. 2] of integer);
            var temp: integer;
            begin
                temp := a[2];
                a[2] := a[1];
                a[1] := temp;
            end
        """
        expect = "100200100200"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_function2(self):
        input = """
            procedure main();
            var x: array[1 .. 2] of real;
                a: integer;
            begin
                x[2] := 8.45;
                a := 9;
                x[1] := foo(a);
                putFloatLn(x[1] + x[2]);
                putBoolLN(True);
                putInTLn(1);
                putStrinGLn("ahihi");
            end
            function foo(a: real): real;
            var b: integer;
            begin
                b := 10;
                return a + b;
            end
            """
        expect = "27.45\ntrue\n1\nahihi\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_function3(self):
        input = """
            var i : integer ;
             function f (): integer ;
             begin
             return 200;
             end
             procedure main ();
             var main : integer ;
             begin
                 main := f ();
                 putIntLn (main );
                 with
                 i : integer ;
                 main : integer ;
                 f : integer ;
                 do begin
                 main := f := i := 100;
                 putIntLn(i);
                 putIntLn(main);
                 putIntLn(f);
                 end
                 putIntLn (main);
             end
             var g : real ;
             """
        expect = "200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_operator(self):
        input = """
            procedure main();
            var a,b: integer;
                arr: array [-10 .. -5] of integer;
            begin
                arr[-10] := -9;
                arr[-9] := -12;
                a := arr[-10];
                b := arr[-9];
                putInt(b - a);
            end
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_multi1(self):
        input = """
            procedure main();
            begin
                NewPutString("ahihi");
            end
            procedure NewPutString(a: String);
            begin
                putString(a);
                return ;
            end
        """
        expect = "ahihi"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test_multi2(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
                c,d: boolean;
                e: String;
            begin
                a := 10+2;
                b := 1.1;
                d := False or True;
                c := False;
                c := c and then foo1(a,b, d, "ahihi");
                putBoolLN(c);
            end
            function foo1(a: integer ; b: real; c: boolean; d: String): boolean;
            begin
                putStringLn(d);
                return c;
            end
        """
        expect = """false\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_multi3(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
                c,d: boolean;
                e: String;
            begin
                a := 10+2;
                b := 1.1;
                d := False or True;
                c := False;
                c := c and foo1(a,b, d, "ahihi");
                putBoolLN(c);
            end
            function foo1(a: integer ; b: real; c: boolean; d: String): boolean;
            begin
                putStringLn(d);
                return c;
            end
        """
        expect = """ahihi\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_arr_9(self):
        input = """
            procedure main();
            var a,i: integer;
                arr: array[-10 .. 10] of integer;
            begin
                a := 10;
                for i:=-10 to -10 + a - 1 do arr[i] := a - i;
                printArray(arr, a);
                putStringLn("Before");
                bubbleSort(arr,a);
                putStringLn("After");
                printArray(arr, a);
            end
            procedure printArray(a: array[-10 .. 10] of integer; num: integer);
            var i: integer;
            begin
                for i:=-10 to -10 + num - 1 do begin
                    putInt(a[i]);
                end
            end
            procedure bubbleSort(a: array[-10 .. 10] of integer; num: integer);
            var i,j: integer;
            begin
                for i:=-10 to -10 + num - 2 do begin
                    for j:= i + 1 to -10 + num -1 do begin
                        if a[i] > a[j] then begin
                            with term: integer; do begin
                                term := a[i];
                                a[i] := a[j];
                                a[j] := term;
                            end
                        end
                    end
                end
                printArray(a, num);
            end
        """
        expect = """20191817161514131211Before\n11121314151617181920After\n20191817161514131211"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    def test_arr_3(self):
        input = """
                var lower: integer;
                procedure main();
                var a,i: integer;
                    arr: array[-10 .. 10] of real;
                begin
                    lower := -10;
                    a:= 6; i := lower;
                    while i < lower + 6 do begin
                        arr[i] := i + 1;
                        i:= i+1;
                    end
                    with result: real; do begin
                    result := sumreal(arr, a);
                    putFloatLn(result);
                    end
                end
                function sumreal(a: array[-10 .. 10] of real; num: integer): real;
                var result: real;
                    i: integer;
                begin
                    result := 0;
                    for i:= lower to lower + num - 1 do
                    result := result + a[i];
                    return result;
                end
        """
        expect = "-39.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))
        
    def test_arr_4(self):
        input = """
                var lower: integer;
                procedure main();
                var a,i: integer;
                    arr: array[-10 .. 10] of real;
                begin
                    lower := -10;
                    a:= 6; i := lower;
                    while i < lower + 6 do begin
                        arr[i] := lower;
                        i:= i+1;
                    end
                    with result: real; do begin
                    result := frequency(arr, a, lower);
                    putFloatLn(result);
                    end
                end
                function frequency(a: array[-10 .. 10] of real; num: integer; key: real): real;
                var result: integer;
                    i: integer;
                begin
                    result := 0;
                    for i:= lower to lower + num - 1 do
                        if a[i] = key then result := result + 1;
                    return result;
                end
        """
        expect = "6.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    def test_arr_5(self):
        input = """
            var lower: integer;
            var result: real;
            procedure main();
            var a,i: integer;
                arr: array[-10 .. 10] of real;
            begin
                lower := -10;
                a:= 6; i := lower;
                while i < lower + 6 do begin
                    arr[i] := lower;
                    i:= i+1;
                end
                result := sumRecurence(arr, a);
                putFloat(result);
            end
            function sumRecurence(a: array[-10 .. 10] of real; num: integer): real;
            begin
                if num <= 0 then return 0;
                else
                return a[lower+num-1] + sumRecurence(a, num-1) ;
            end
        """
        expect = "-60.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))
        
    def test_multi4(self):
        input = """
            procedure main();
            var a: array[4 .. 10] of boolean;
                i: integer;
            begin
                for i := 4 to 10 do begin
                    a[i] := i div 3 < 3 or else i div 3 > 5;
                end
                foo(a);
                putLN();
                for i := 4 to 10 do ha_b_space(a[i]);
            end

            procedure foo(a: array[4 .. 10] of boolean);
            var i: integer;
            begin
                for i := 4 to 10 do ha_b_space(a[i]);
                for i := 4 to 10 do begin
                    a[i] := not (i div 3 < 3 or else i div 3 > 5);
                end
                for i := 4 to 10 do ha_b_space(a[i]);
            end

            procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
            procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
            procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

            function ha_str_1(): string; begin return "0852 1"; end
            function ha_str_2(): string; begin return "0852 2"; end
            function ha_str_3(): string; begin return "0852 3"; end
        """
        expect = """true true true true true false false false false false false false true true \ntrue true true true true false false """
        self.assertTrue(TestCodeGen.test(input, expect, 539))
        
    def test_arr_6(self):
        input = """
        var lower,i: integer;
        var result: real;
        procedure main();
        var a,i: integer;
            arr: array[10 .. 25] of real;
        begin
            lower := 10;
            a:= 9; i := lower;
            for i:= lower + a - 1 downto lower do
            begin
                arr[i] := i + 1.7;
                putFloat(arr[i]);
            end
            putInt(find_index(a, arr, 17.7));
        end
        function find_index(n: integer ; a : array[10 .. 25] of real; key:real): integer;
        begin
            for i:= lower to n+lower-1 do
                if a[i] = key then return i;
            return lower;
        end
        """
        expect = "19.718.717.716.715.714.713.712.711.716"
        self.assertTrue(TestCodeGen.test(input, expect, 540))
        
    def test_arr_7(self):
        input = """
        var lower: integer;
        var result: real;
        procedure main();
        var a,i: integer;
            arrbool: array[10 .. 25] of boolean;
            arrresult: array[0 .. 1] of integer;
        begin
            lower := 10;a:= 12;
            arrresult[0] := 0; arrresult[1] := 0;
            for i:= lower to lower + a - 1 do
                if i mod 2 = 0 then begin
                    arrbool[i] := True;
                    arrresult[0] := arrresult[0] + 1;
                end
                else begin 
                    arrbool[i] := False;
                    arrresult[1] := arrresult[1] + 1;
                end
                printarR(a, arrbool);
                putInTLn(arrresult[0]);
                putInTLn(arrresult[1]);
        end
        procedure printarr(num: integer ; a: array[10 .. 25] of boolean);
        begin
            with i: integer; do
            for i:=lower to lower + num - 1 do begin
                putBool(a[i]);
                putString(" ");
            end
        end
        """
        expect = """true false true false true false true false true false true false 6\n6\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))
        
    def test_recurence_8(self):
        input = """
            var result: real;
            procedure main();
            var i1, i2: integer;
            begin
                i1 := fiboNacy(0);
                i2 := fiboNacy(1);
                result := fibonacy(10);
                putInTLn(i1);
                putInTLn(i2);
                putFloatLn(result);
            end
            function fibonacy(a: integer): integer;
            begin
                if (a = 0) or (a = 1) then return 1;
                else return fibonacy(a-1) + fibonacy(a-2); 
            end
        """
        expect = "1\n1\n89.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test_expression1(self):
        """ Test Associative """
        input = """
                procedure Main();
                var
                    a: real;
                begin
                    with a: boolean; do begin
                        a := True;
                        a := (((5 <> 6) and (6 = 5)) and (4 + 5 > 1)) or else a;
                        putBoolLN(a);
                    end
                    a := 1 + 0.99;
                    putFloatLn(a);
                end
                """
        expect = "true\n1.99\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
        
    def test_expression2(self):
        """ Test Associative """
        input = """
                procedure Main();
                var
                    a: real;
                begin
                    with a: boolean; do begin
                        a := True;
                        a := (((5 <> 6) and (6 = 5)) and (4 + 5 > 1)) or else a;
                        putBoolLN(a);
                    end
                    a := 1 + 0.99;
                    putFloatLn(a);
                end
                """
        expect = "true\n1.99\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_expression3(self):
        """ Test If Statement """
        input = """
                procedure main();
                var a: real;
                    b: integer;
                begin
                    a := 1;
                    b := 1;
                    if a = 1 then 
                        with b: integer; c: integer ; d: integer; do begin
                            b := 4;
                            if b > 3 then begin 
                                c := 5;
                                putIntLN(c);
                            end
                            else d := 1;
                            
                        end
                    with h: REAL ;g: integer; do begin 
                        h := 10.11;
                        if h > 5 then putLN(); else a:= 10;
                        g := 5;
                    end
                end
                """
        expect = "5\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_multi5(self):
        input= """
            procedure MaIN();
            Var
            Tong, n, i, k: Integer;
            Begin
             putStrinGLn("Hay nhap so");
             n := 19202034;
             putStrinGLn("Muon tinh tong bao nhieu chu so tan cung");
             k := 6;
             {Tinh tong k chu so tan cung}
             i := 1;
             Tong := 0;
             While i <= k do Begin
              Tong := Tong + n mod 10;
              n := n div 10;
              i := i + 1;
             End
             putFloatLn(Tong);
            End
            """
        expect = "Hay nhap so\nMuon tinh tong bao nhieu chu so tan cung\n11.0\n"
        self.assertTrue(TestCodeGen.test(input,expect, 545))
        
    def test_multi6(self):
        """ Test Assign Statment """
        input = """
                function foo(): array [0 .. 4] of real;
                begin
                    with a: array [0 .. 4] of real; do begin 
                        a[1] := 1.13;
                        return a;
                    end
                end
                function foo2(a: array [0 .. 4] of real): boolean;
                begin
                    putFloatLn(a[1]);
                    return True;
                end
                pROCEDURE main();
                var a: boolean ;
                begin
                    a:= False;
                    a := a and foo2(foo());
                    putBoolLn(a);
                end
                """
        expect = "1.13\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 546))
        
    def test_multi7(self):
        input= """
                Function LuyThua(a, k: Integer): integer;
                Begin
                 If k = 1 then return a;
                 Else return LuyThua(a, k-1) * a;
                End
                procedure main();
                Var
                 A: Array [1 .. 10] of Integer;
                 i, n: Integer;
                Begin
                 n := 10;
                 For i := 1 to n do begin
                    A[i] := i;
                 End
                 For i := 1 to n do begin
                  putFloat(LuyThua(2, A[i]));
                  PutString(" ");
                  end
                End
               """
        expect = "2.0 4.0 8.0 16.0 32.0 64.0 128.0 256.0 512.0 1024.0 "
        self.assertTrue(TestCodeGen.test(input,expect, 547))
        
    def test_multi8(self):
        input= """
                procedure main();
                var i: integer;
                 S: integer;
                begin
                 S:= 0;
                 i:= 1;
                 while i <= 100 do begin
                  S:= S + i;
                  i:= i +1;
                 end
                 putStringLn("Tong tu 1 den 100 la: ");
                 putIntLn(s);
                end
               """
        expect = "Tong tu 1 den 100 la: \n5050\n"
        self.assertTrue(TestCodeGen.test(input,expect, 548))
        
    def test_multi9(self):
        """ Test Assign Statment """
        input = """
                function foo(): array [0 .. 4] of real;
                begin
                    with a: array [0 .. 4] of real; do begin 
                        a[1] := 1.13;
                        return a;
                    end
                end
                function foo2(a: array [0 .. 4] of real): real;
                begin
                    return a[1];
                end
                pROCEDURE main();
                var a: real ;
                begin
                    a := 15.67;
                    a := 15.67 + foo2(foo());
                    putFloatLn(16.8);
                end
                """
        expect = "16.8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test_loop_1(self):
        input = """
                pROCEDURE main();
                var a: real ;
                    i: integer;
                begin
                    i := 1;
                    a := 0;
                    while true do begin
                        a := a + i;
                        i := i + 1;
                        if i >= 50 then break;
                    end
                    puTFloatLn(a);
                end
                """
        expect = "1225.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))
        
    def test_loop_2(self):
        input = """
                pROCEDURE main();
                var a: real ;
                    i: integer;
                begin
                    i := 1;
                    a := 0;
                    while true do begin
                        if i >= 70 then break;
                        a := a + i;
                        i := i + 1;
                    end
                    puTFloatLn(a);
                end
                """
        expect = "2415.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 551))
        
    def test_loop_3(self):
        input = """
                pROCEDURE main();
                var a: real ;
                    i: integer;
                begin
                    i := 1;
                    a := 0;
                    for i := 1 to 100 do beGin
                        if i<50 then continue;
                        if i>80 then continue;
                        a := a + i;
                    end
                    puTFloatLn(a);
                end
                """
        expect = "2015.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 552))
        
    def test_loop_4(self):
        input = """
                pROCEDURE main();
                var a: real ;
                    i: integer;
                begin
                    i := 0;
                    a := 0;
                    while (i<100) do begin
                        with j: integer; do begin
                            for j := i to j + 10 do begin
                                if j > i + 5  then break;
                                putInt(j);putString(" ");
                            end
                        end
                        i := i + 10;
                    end
                end
                """
        expect = "0 1 2 3 4 5 10 11 12 13 14 15 20 21 22 23 24 25 30 31 32 33 34 35 40 41 42 43 44 45 50 51 52 53 54 55 60 61 62 63 64 65 70 71 72 73 74 75 80 81 82 83 84 85 90 91 92 93 94 95 "
        self.assertTrue(TestCodeGen.test(input, expect, 553))
        
    def test_scope2(self):
        input = """
            pROCEDURE main();
            var Main: real;
            begin
                Main := 1.6;
                with main: boolean; do begin
                    main := False;
                    putBoolLN(main);
                end
                putFloatLn(main);
            end
        """
        expect = "false\n1.6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
        
    def test_scope3(self):
        input = """
            pROCEDURE main();
            var Main: real;
                proc1: integer;
            begin
                proc1 := -10 + -11 * 8 div 2 ;
                putFloatLn(proc1);
            end
            pROCEDURE proc1(a: String);
            begin
                putStringLn(a);
            end
        """
        expect = "-54.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))
        
    def test_scope4(self):
        input = """
            pROCEDURE main();
            var Main: real;
            begin
                with proc1: integer; do begin
                    proc1 := -10 + -11 * 8 div 2 ;
                    putFloatLn(proc1);
                end
                proc1("ahihi1");
            end
            pROCEDURE proc1(a: String);
            begin
                putStringLn(a);
            end
        """
        expect = "-54.0\nahihi1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
        
    def test_scope5(self):
        input = """
            pROCEDURE main();
            var Main: real;
            begin
                with proc1: integer; do begin
                    proc1 := -10 + -11 * 8 div 2 ;
                    putFloatLn(proc1);
                end
                proc1("ahihi1");
                proc2("ahuhu1");
            end
            pROCEDURE proc1(a: String);
            begin
                putStringLn(a);
            end
            pROCEDURE proc2(a: String);
            var Proc1: Real;
            begin
                proc1 := 1.12;
                putFloatLN(proc1);
            end
        """
        expect = "-54.0\nahihi1\n1.12\n"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
        
    def test_arr_8(self):
        input = """
            pROCEDURE main();
            var a: array[1 .. 10] of real;
                i: integer;
            begin
                for i:=1 to 10 do a[i] := i;
                puTFloatLn(find_index_gt(7, a, 10));
            end
            function find_index_gt(key: Integer; a: array[1 .. 10] of real; n: integer): real;
            var i: integer;
            begin
                for i := 1 to n do begin
                    if a[i] > key then return i;
                end 
                return i;
            end
        """
        expect = "8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test_multi10(self):
        input = """
                pROCEDURE main();
                Var
                   so1,so2,so3,so4,solon1,solon2,solon:Integer;
                Begin
                    so1 := 10 ; so2 := -16; so3 := -100000 ; so4 := 100;
                    If so1 > so2 Then
                       solon1:= so1;
                   Else
                       Solon1:=so2;
                   If so3 > so4 Then
                       solon2:=so3;
                   Else
                       solon2:=so4;
                    If solon1 > solon2 Then
                        solon:=solon1;
                    Else
                        solon:=solon2;
                    putIntLN(solon);
                end
                    """
        expect = "100\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))
        
    def test_arr_10(self):
        input = """
                var lower: integer;
                function find_max_idx(a: Array [0 .. 10] of real ; num:integer): real;
                var i: integer;
                    rs: real;
                beGin
                    rs := a[0];
                    for i:=1 to num do begin
                        if a[i] > rs then rs := a[i];
                    end
                    return rs;
                end
                pROCEDURE main();
                var a: Array [0 .. 10] of real;
                begin
                    with n,i: integer; do begin
                        n := 10;
                        for i:=0 to n do a[i] := i;
                        putFloatLn(find_max_idx(a, n));
                    end
                end
        """
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_arr_18(self):
        input = """
                var lower: integer;
                function mean(a: Array [0 .. 10] of real ; num:integer): real;
                var i: integer;
                    rs: real;
                beGin
                    rs := 0;
                    for i:=0 to num do begin
                        rs := rs + a[i];
                    end
                    rs := rs / num;
                    return rs;
                end
                pROCEDURE main();
                var a: Array [0 .. 10] of real;
                begin
                    with n,i: integer; do begin
                        n := 10;
                        for i:=0 to n do a[i] := i;
                        putFloatLn(mean(a, n));
                    end
                end
        """
        expect = "5.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
        
    def test_multi11(self):
        input = """
                pROCEDURE main();
                Var t:Integer;
                Begin
                   PutStringLN("CHON LOAI GIAI TRI THICH HOP");
                   PutString("-Cho biet nhiet do ngay hom nay: ");
                   t := 28;
                   If t < 20 Then
                       PutStringLN("Troi lanh, ban nen o nha coi TV");
                   If ((t > 20) And (t < 25)) Then
                       PutStringLN("Troi mat me, ban nen di cam trai");
                   If ((t > 25) And (t < 30)) Then
                       PutStringLN("Troi hoi nong, ban nen di tam bien Vung Tau");
                   If t > 30 Then
                       PutStringLN("Troi nong, ban nen di nghi mat o Da Lat");
                   PutLN();
                End
        """
        expect = "CHON LOAI GIAI TRI THICH HOP\n-Cho biet nhiet do ngay hom nay: Troi hoi nong, ban nen di tam bien Vung Tau\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))
        
    def test_multi12(self):
        input = """
            pROCEDURE main();
            Var
               a,b,c:Integer;
               tamgiac,deu,can:Boolean;
            Begin
                a:= 3; b := 4 ; c:=4;
               tamgiac := False;
               deu:=False;
               can:=False;
               If (a+b>c) And (b+c>a) And (c+a>b) Then
                   Begin
                     tamgiac:=True;
                     If (a=b) And (b=c) Then
                         deu:=True;
                     If (a=b) Or (b=c) Or (c=a) Then
                         can:=True;
                  End
                putLN();
               PutStringLN("+Tam giac: ");
               putBool(tamgiac);
               PutStringLN("+Tam giac deu: ");
               putBool(deu);
               PutStringLN("+Tam giac can: ");
               putBool(can);
            End
        """
        expect = "\n+Tam giac: \ntrue+Tam giac deu: \nfalse+Tam giac can: \ntrue"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test_multi17(self):
        input = """
            procedure Main();
           var x: array[0 .. 2] of integer;
           y:array[1 .. 4] of integer;
           t:array[-5 .. 5] of real;
           n:string;
           begin
            t[-5]:=2;
            putFloat(t[-5]);
           end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_multi13(self):
        input = """
            procedure Main();
           var x: array[0 .. 2] of integer;
           y:array[1 .. 4] of integer;
           n:string;
           begin
                y[1] := 10;
                y[4] := -100000;
                if y[4] < y[1] then begin
                    putInTLn(y[4]);
                    putStrIngLn("less than");
                end
                else y[1] := 100;
                    
           end
        """
        expect = "-100000\nless than\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
        
    def test_multi14(self):
        input = """
        var fNum123:real;
        procedure main();
        var arr:array[1 .. 4] of integer;
            c, d:integer;
            f:real;
        begin
            d := 99;
            c := d;
            fNum123 := c;
            arr[2] := c;
            arr[1] := 9999;
            f := arr[1];
            d := c;
            arr[2] := d;
            arr[3] := arr[2];
            fNum123 := arr[3];
            putFloatLn(fNum123);
        end
        """
        expect = "99.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,567))
        
    def test_multi15(self):
        input = """
        var a, b:integer;
            gArr:array[1 .. 4] of integer;
        procedure main();
        var arr:array[1 .. 4] of integer;
            c, d:integer;
        begin
            a := 12;
            b := a := 75;
            c := a;
            b := a := c := b;
            gArr[2] := arr[2] := 1;
            gArr[3] := gArr[2] := 16;
            puTFloatLn(b);
            d := gArr[3] := arr[4] := gArr[1] := a := gArr[3] := b := 11;
            putIntLn(gArr[3]);
        end
        """
        expect = "75.0\n11\n"
        self.assertTrue(TestCodeGen.test(input,expect,568))
        
    def test_multi16(self):
        input = """
            var num: integer;
            pROCEDURE main();
            var lower: integer;
             arr1: array [-10 .. 10] of integer;
             arr2: array [-10 .. 10] of real;
             arr3: array [-10 .. 10] of integer;
             arr4: array [-10 .. 10] of real;
            begin
                lower := -10;
                arr1[0] := 9;
                arr2[1] := 9;
                arr3[2] := 9;
                arr4[3] := 9;
                num := 0;
                putFloatLN(sUm(num, arr1, arr2, arr3, arr4));
            end
            function sum(num: integer; arr1: array [-10 .. 10] of integer;arr2: array [-10 .. 10] of real;arr3: array [-10 .. 10] of integer;arr4: array [-10 .. 10] of real): real;
            var i: integer;
                rs: real;
            begin
                RS := arr1[0] + arr2[1] + arr3[2] + arr4[3];
                return RS;
            end
        """
        expect = "36.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,569))
        
    def test_scope6(self):
        input = """
            var X: integer;
                Y: integer;
            pROCEDURE fie();
            begin
                x := x + 1;
            end
            pROCEDURE foo();
            begin
                x := x + 1;
                fiE();  
            end
            pROCEDURE maIn();
            begin
                x := 0;
                y := 6;
                if y > 0 then begin
                    with X: Integer; do Foo();
                end
                else foo();
                putInTLn(x);
            end
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
        
    def test_scope7(self):
        input = """
            var X: integer;
                Y: integer;
            pROCEDURE fie();
            begin
                x := x + 1;
            end
            pROCEDURE foo();
            begin
                x := x + 1;
                fiE();  
            end
            pROCEDURE maIn();
            begin
                x := 0;
                y := -61;
                if y > 0 then begin
                    with X: Integer; do Foo();
                end
                else foo();
                putInTLn(x);
            end
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_scope8(self):
        input = """
        var x: integer;
        pROCEDURE fie(y: integer);
        begin
            x := x + y;
        end
        pROCEDURE main();
        begin
            x := 2;
            with x: integer; do begin 
                x := 5;
                fiE(x);
                putInTLn(x);
            end
            putInTLn(X);
        end
        """
        expect = "5\n7\n"
        self.assertTrue(TestCodeGen.test(input,expect,572))
        
    def test_expression4(self):
        input = r"""
        procedure main(); 
        begin 
            putFloat(123 / 3 + 46/5/2/2/2/2/4);
        end
        """
        expect = r"""41.14375"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))
        
    def test_arr_19(self):
        input = """
        var lower : integer;
        procedure main(); 
        var arr: array[-10 .. 10] of integer;
            i,n: integer;
        begin 
            lower := -10;
            n := 10;
            for i := lower to lower + n -1 do
            arr[i] := i;
            putInT(sumdiv5(arr, n));
        end
        function sumdiv5(arr: array[-10 .. 10] of integer; n: integer): integer;
        var i, rs: integer;
        begin
            rs := 0;
            for i := lower to lower + n -1 do
            if arr[i] mod 5 = 0 then rs := rs + arr[i];
            return rs;
        end
        """
        expect = "-15"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
        
    def test_arr_20(self):
        input = """
        var lower : integer;
        procedure main(); 
        var arr: array[-10 .. 10] of real;
            i,n: integer;
        begin 
            lower := -10;
            n := 12;
            for i := lower to lower + n -1 do
            arr[i] := i;
            replace(arr, n, -1);
            for i := lower to lower + n -1 do begin
                putFloat(arr[i]);
                putStrinG(" ");
            end
        end
        pROCEDURE replace(arr: array[-10 .. 10] of real; n: integer; key:integer);
        var i: integer;
        begin
            for i := lower to lower + n -1 do
            if arr[i] = key then begin
                arr[i] := 100;
                break;
            end
            for i := lower to lower + n -1 do begin
                putFloat(arr[i]);
                putStrinG(" ");
            end
        end
        """
        expect = "-10.0 -9.0 -8.0 -7.0 -6.0 -5.0 -4.0 -3.0 -2.0 100.0 0.0 1.0 -10.0 -9.0 -8.0 -7.0 -6.0 -5.0 -4.0 -3.0 -2.0 -1.0 0.0 1.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 575))
        
    def test_arr_21(self):
        input = """
                var lower : integer;
                procedure main(); 
                var arr: array[-10 .. 10] of boolean;
                    i,n: integer;
                begin 
                    lower := -10;
                    n := 12;
                    for i := lower to lower + n -1 do
                    if i mod 2 = 0 then arr[i] := True;
                    else arr[i] := False;
                    PutBoOLLN(checkAllTrue(arr, n));
                end
                function checkAllTrue(arr: array[-10 .. 10] of boolean; n: integer): boolean;
                var i: integer;
                begin
                    for i := lower to lower + n -1 do
                    if not arr[i] then begin
                        PuTIntLn(i);
                        return False;
                    end
                    return True;
                end
                """
        expect = "-9\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
        
    def test_arr_22(self):
        input = """
                var lower : integer;
                procedure main(); 
                var arr: array[-10 .. 10] of boolean;
                    i,n: integer;
                begin 
                    lower := -10;
                    n := 12;
                    for i := lower to lower + n -1 do
                    if i mod 2 = 0 then arr[i] := True;
                    else arr[i] := False;
                    PutBoOLLN(checkAllTrue(arr, n));
                end
                function checkAllTrue(arr: array[-10 .. 10] of boolean; n: integer): boolean;
                var i: integer;
                    rs: boolean;
                begin
                    rs := True;
                    for i := lower to lower + n -1 do
                        rs := rs and arr[i] ;
                    PuTIntLn(i);
                    return rs;
                end
                """
        expect = "2\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 577))
        
    def test_expression5(self):
        input = """
            proCeduRe main();
            var a, b: boolean;
                i,j : integer;
            begin
                a := True;
                b := false;
                i := 10 ;
                j := 0;
                a := a or else (i div j = 0) or b;
                PutBoOLLN(a);
            end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test_recurence_9(self):
        input = """
        pROCEDURE indaonguoc(n: integer);
        begin
            if n<>0 then begin
                putInT(n mod 10);
                indaonguoc(n div 10);
            end
        end
        pROCEDURE main();
        var n: integer;
        begin
            n := 123456;
            indaonguoc(n);
        end
        """
        expect = "654321"
        self.assertTrue(TestCodeGen.test(input, expect, 579))
        
    def test_recurence_10(self):
        input = """
        function demnguyenduong(n: integer): integer;
        begin
            if n=0 then return 0;
            return 1 + demnguyenduong(n div 10);
        end
        pROCEDURE main();
        var n: integer;
        begin
            n := 123456;
            with RS: integer; do begin
                rs := demnguyenduong(n);
                PuTIntLn(rs);
            end
        end
        """
        expect = "6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 580))
        
    def test_recurence_11(self):
        input = """
        var max: integer;
        function chusolonnhat(n: integer): integer;
        var m: integer;
        begin
            if n = 0 then return max;
            else beGin
                m := n mod 10;
                if m > max then max := m;
            end
            return chusoLONnhat(n div 10);
        end
        pROCEDURE main();
        var n: integer;
        begin
            n := 1239456;
            max := 0;
            with RS: integer; do begin
                rs := chusoLONnhat(n);
                PuTIntLn(RS);
            end
        end
        """
        expect = "9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_recurence_12(self):
        input = """
        var max: integer;
        function UCLN(a: integer; b: integer): integer;
        var m: integer;
        begin
            if a = b then return a;
            else beGin
                if a > b then a:= a-b;
                else b := b - a;
            end
            return UCLN(A,B);
        end
        pROCEDURE main();
        var n: integer;
            m: integer;
        begin
            n := 150;
            m := 175;
            max := 0;
            with RS: integer; do begin
                rs := UCLN(M,N);
                PuTIntLn(25);
            end
        end
        """
        expect = "25\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
        
    def test_expression6(self):
        input = """
            pROCEDURE main();
            var n: integer;
                m: integer;
                o: real;
            begin
                n := 10;
                m := 15;
                o := 12.45;
                o := o + m/n*-n-m+n;
                putFloatLN(o);
            end
        """
        expect = "-7.549999\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test_expression7(self):
        input = """
            pROCEDURE main();
            var n: integer;
                m: integer;
                o: real;
                p: Boolean;
            begin
                p := False;
                n := 10;
                m := 15;
                o := 12.45;
                o := o + m/n*-n-m+n;
                p := (o > 0) or (o < n) and p or False;
                PutBoOLLN(p);
            end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
        
    def test_multi18(self):
        input = """
        pROCEDURE main();
        var a,b,n,rs,i : integer;
        begin
            n := 10;
            rs := 0;
            if (n = 0) or (n = 1) then rs := 1;
            else begin
                a := 1; b:=1;i:=3;
                while (true) do begin
                    rs := b + a;
                    a := b;
                    b := rs;
                    i := i + 1;
                    if i > n then break;
                end
            end
            putInTLn(RS);
        end
        """
        expect = "55\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test_expression8(self):
        input = r"""
            procedure main(); 
            begin 
                putBool(1.85 > 2);
                putBool(1.85 < 2);
                putBool(2.0 = 2);
                putBool(1.85 >= 2);
                putBool(1.85 <= 2);
                putBool(2.0 <> 2);
            end

"""
        expect = r"""falsetruetruefalsetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))
        
    def test_expression9(self):
        input = r"""
            procedure main(); 
            begin
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 > 4*6 + 3*4/2 - 5*7.3/15 + 2);
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 < 4*6 + 3*4/2 - 5*7.3/15 + 2);
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 = 4*6 + 3*4/2 - 5*7.3/15 + 2);
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 >= 4*6 + 3*4/2 - 5*7.3/15 + 2);
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 <= 4*6 + 3*4/2 - 5*7.3/15 + 2);
                putBool(1.8*2.1 + 1.9 - 5.5*2.3 <> 4*6 + 3*4/2 - 5*7.3/15 + 2);
            end
"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))
        
    def test_expression10(self):
        input = r"""
            procedure main();
            begin
                putBoolLn(not true);
                PutBooLLN(not false);
                putbOOLLN(not not true);
                PUtbOOLLN(not not false);
                PutBoOLLN(not not not true);
                PutBoOLLN(not not not false);
                PutBoOLLN(not true and false);
                PutBoOLLN(not false and true);
                PutBoOLLN(not not true and not not not false or true and false);
                PutBoOLLN(not not false or true);
                PutBOOLLN(not not false or true and false);
                PutBOOLLN(false or not not true or false and true);
            end
            """
        expect = """false\ntrue\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\ntrue\ntrue\nfalse\ntrue\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 588))
        
    def test_expression11(self):
        input = """
            var c,d,e:integer;
                fc,fd,fe:real;
            procedure main();
            var isTrue, isT, isF:boolean;
            begin
                c := 10;
                d := 14;
                e := 18;
                c := d mod c ;
                d := e div d;
                fc := c + d/e;
                fd := fc/e*c-fc;
                fe := fd;
                putFloatLN(FC);
                putFloatLN(FD);
                putFloatLN(FE);
            end
        """
        expect = "4.0555553\n-3.1543207\n-3.1543207\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_expression12(self):
        input = """
            procedure main();
            begin
                putFLoatLn(11.0);
                putFlOatLn(12e3);
                putFloAtLn(1e-4);
                putFloaT(1.1e-3);
                putFloaT(1.25e-3);
            end
        """
        expect = "11.0\n12000.0\n1.0E-4\n0.00110.00125"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    
    def test_expression13(self):
        input = """
            procedure main();
            begin
                putInt(49 - 1 * 12);
                putFlOatLn(- 1 / 12 + 1.2*1.2/-2);
            end
        """
        expect = "37-0.80333334\n"
        self.assertTrue(TestCodeGen.test(input,expect,591))
        
    def test_loop_5(self):
        input = """
            procedure main();
            var lower: integer;
            begin
                lower := -10;
                with i: integer; a: array[-10 .. -1] of integer; do begin
                    for i:=-1 downto lower do
                    PuTIntLn(i) ;
                end
            end
        """
        expect = "-1\n-2\n-3\n-4\n-5\n-6\n-7\n-8\n-9\n-10\n"
        self.assertTrue(TestCodeGen.test(input,expect,592))
        
    def test_arr_11(self):
        input = """
             procedure main();
             var x: array [-1 .. 10] of integer;
             begin
                 x[-1] := 2;
                 putInt(x[-1]);
             end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,593))
        
    def test_arr_12(self):
        input = """
            procedure foo(x: array [1 .. 6] of integer);
            var i: integer;
            begin
                for i := 1 to 6 do
                    x[i] := i * i * i;
                for i := 1 to 6 do
                   putIntLn(x[i]);
            end

            procedure main();
            var i: integer; c: array [1 .. 6] of integer;
            begin
                for i:=1 to 6 do
                    c[i] := i;
                for i := 1 to 6 do
                   putIntLn(c[i]);
                foo(c);
                for i := 1 to 6 do
                   putIntLn(c[i]);
            end
        """
        expect = "1\n2\n3\n4\n5\n6\n1\n8\n27\n64\n125\n216\n1\n2\n3\n4\n5\n6\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))
        
    def test_arr_13(self):
        input = """
            procedure main();
            var i,j,k: integer; 
            begin
                for i := 1 to 12 do
                begin
                    if ((i mod 3) = 0) then
                        continue;
                    putIntLn(i);
                end  
            end
        """
        expect = "1\n2\n4\n5\n7\n8\n10\n11\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_return_1(self):
        input = """ 
            function ham1(): string;
            begin 
                return "ahihi";
            end

            function ham2(): real;
            begin 
                return 0.99;
            end

            function ham3(): integer;
            begin 
                return 5;
            end

            function ham4(): boolean;
            begin 
                return FALSE;
            end

            procedure main();
            begin
                putStringLn(HAM1());
                putFloatLn(HAM2());
                putIntLn(HAM3());
                putBoolLn(HAM4());
            end
        """
        expect = "ahihi\n0.99\n5\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,596))
        
    def test_multi22(self):
        input = """ 
            function ham11(): real;
            begin 
                return 10.66;
            end

            procedure main();
            begin
               putFloat(ham11());
            end
            var x : real;
        """
        expect = "10.66"
        self.assertTrue(TestCodeGen.test(input,expect,597))
        
    def test_multi23(self):
        input = r"""
            procedure main();
            var aa: integer;
            begin
                aa := foo(42, 16);
                putInt(aa);
            end

            function foo(a,b: integer): integer;
            begin
                return (a * b) mod 2;
            end
            """
        expect = """0"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))
        
    def test_multi24(self):
        input = r"""
            procedure main();
            begin
                yul := 1010;
                putInt(yul);
            end

            var yul: integer;
            """
        expect = """1010"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
        
    def test_multi25(self):
        input = r"""
            procedure main();
            var i: integer;
            begin
                for i := 1 to 10 do begin
                    if i > 6 then putFlOatLn(-i); else putFloatLN(i);
                end
            end
            """
        expect = """1.0\n2.0\n3.0\n4.0\n5.0\n6.0\n-7.0\n-8.0\n-9.0\n-10.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 600))
        
    
