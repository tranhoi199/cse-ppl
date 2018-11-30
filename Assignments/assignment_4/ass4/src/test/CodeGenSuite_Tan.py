import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """
            procedure main();
            begin
                putIntLn(100);
                putIntLn(-100);
                putInt(0);
            end
        """
        expect = "100\n-100\n0"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_large_int_literal(self):
        input = """
            procedure main();
            begin
                putIntLn(-2147483648);
                putIntLn(-1000000000 + 65565654);
                putFloatLn(-1000000000 / 65565654);
                putIntLn(2147483647);   
            end
        """
        expect = "-2147483648\n-934434346\n-15.251887\n2147483647\n"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    
    def test_float_literal(self):
        input = """
            procedure main();
            begin
                putFloatLn(10.0);
                putFloatLn(1e3);
                putFloatLn(1e-3);
                putFloat(1.e-3);
            end
        """
        expect = "10.0\n1000.0\n0.001\n0.001"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_boolean_literal(self):
        input = """
            procedure main();
            begin
                putBoolLn(True);
                putBool(FalsE);
            end
        """
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    
    def test_string_literal(self):
        input = """
            procedure main();
            begin
                putStringLn("PPL");
                putString("2018");
            end
        """
        expect = "PPL\n2018"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_binary_op_with_add(self):
        input = """
            procedure main();
            begin
                putIntLn(1 + 2);
                putFloatLn(1 + 2.0);
                putFloatLn(1.23 + -9.34);
                putFloat(1.2376 + -9);
            end
        """
        expect = "3\n3.0\n-8.110001\n-7.7624"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_binary_op_with_sub(self):
        input = """
            procedure main();
            begin
                putIntLn(1 - 2);
                putFloatLn(1 - 2.0);
                putFloatLn(1.23 - -9.34);
                putFloat(1.2376 - -9);
            end
        """
        expect = "-1\n-1.0\n10.57\n10.2376"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_binary_op_with_divide(self):
        input = """
            procedure main();
            begin
                putFloatLn(14/2);
                putFloatLn(13 / 2.08783);
                putFloatLn(158.2035564 / --236.256885);
                putFloat(122.23762 / ---9);
            end
        """
        expect = "7.0\n6.2265606\n0.66962516\n-13.581958"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_binary_op_with_mul(self):
        input = """
            procedure main();
            begin
                putFloatLn(14/-2.0);
                putFloatLn(13 * 2.08783);
                putFloatLn(158.2035564 * -236.256885);
                putFloat(122.23762 * 9);
            end
        """
        expect = "-7.0\n27.14179\n-37376.68\n1100.1385"
        self.assertTrue(TestCodeGen.test(input,expect,508))


    def test_binary_op_add_int(self):
        input = """
            procedure main();
            begin
                putInt(1+2+30);
            end
        """
        expect = "33"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test_binary_op_divide(self):
        input = """
            procedure main();
            begin
                putFloat(1*45+30/12);
            end
        """
        expect = "47.5"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_binary_op_div_int(self):
        input = """
            procedure main();
            begin
                putInt(100 div 3 div 2);
            end
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_binary_op_sub(self):
        input = """
            procedure main();
            begin
                putInt(100 - 1 * 12);
            end
        """
        expect = "88"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test_binary_op_boolean_1(self):
        input = """
            procedure main();
            begin
                putBool(FalSE and False);
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_binary_op_boolean_2(self):
        input = """
            procedure main();
            begin
                putBool(1 <= 2);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_binary_op_boolean_3(self):
        input = """
            procedure main();
            begin
                putBool(1 = 2);
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test_unary_op_with_not(self):
        input = """
            procedure main();
            begin
                putBool(not (-10 <> 2));
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    
    def test_unary_op_with_neg(self):
        input = """
            procedure main();
            begin
                putIntLn(-12-2);
                putFloat(-12.3+12);
            end
        """
        expect = "-14\n-0.3000002"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_and_then_op(self):
        input = """
            procedure main();
            begin
                putBool(true and then true);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_or_else_op(self):
        input = """
            procedure main();
            begin
                putBoolLn(1 > 2 or else 7 = 7);
                putBoolLn(1 < 0 or else -1 > 0);
                putBoolLn(1 > -0 or else 2 >= 2);
                putBool(true and (1 = 1) or else 2 < 2);
            end
        """
        expect = "true\nfalse\ntrue\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_float_compare(self):
        input = """
             procedure main();
             begin
                 putBool(1.23 <> 1.23);
                 putBool(1.23 <> 2.1);
                 putBool(1.23 < 2.19);
                 putBool(1.23 < 0.2);
                 putBool(1.23 > 2.11);
                 putBool(1.23 > (-0.1));
                 putBool(1.23 = 2.12);
                 putBool(1.23 = (1 + 0.23));
                 putBool(1.23 >= 2.1);
                 putBool(1.23 >= 1);
                 putBool(1.23 >= 1.23);
                 putBool(1.23 <= 2.1);
                 putBool(1.23 <= 0.12);
                 putBool(1.23 <= 1.23);
             end
        """
        expect = "falsetruetruefalsefalsetruefalsetruefalsetruetruetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_array_type__1(self):
        input = """
             procedure main();
             var x: array [-1 .. 10] of integer;
             begin
                 x[-1] := 2;
                 putInt(x[-1]);
             end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_while_stmt__1(self):
        input = """
             procedure main();
             var i,s: integer;
             begin
                i := 1;
                s := 0;
                while (i <= 10) do
                begin
                    s := s + i;
                    break;
                    i := i + 1;
                end
                putInt(s);
             end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_for_stmt__1(self):
        input = """
             procedure main();
             var i,s: integer;
             begin
                s := 0;
                for i := 10 downto 1 do
                begin
                    s := s + i;
                    break;
                end
                putInt(s);
             end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    

    def test_with_stmt__1(self):
        input = """
             procedure main();
             var a: array [1 .. 10] of string;
             begin
                putBool(True or else (((1/0.0)/(1/0)) = 1));
             end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,524))


    #*************** TEST ARRAY ********************/

    def test_array_boolean(self):
        input = """
             var y: array [2 .. 5] of boolean;
             procedure main();
             var x: array [-1 .. 5] of boolean; i: integer;
             begin
                for i:= 2 to 4 do
                    y[i] := i = 3.0;
                putBoolLn(y[2]);
                putBoolLn(y[3]);
                putBoolLn(y[4]);
                putBoolLn(y[5]);
                for i := -1 to 5 do
                    x[i] := i < 2;
                for i:= -1 to 5 do
                    putBoolLn(x[i]);
             end
        """
        expect = "false\ntrue\nfalse\nfalse\ntrue\ntrue\ntrue\nfalse\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_array_integer(self):
        input = """
             var x: array [0 .. 5] of integer;
             procedure main();
             var y: array [-10 .. -5] of integer; i: integer;
             begin
                i := -9;
                while (i <= -5) do 
                begin
                    y[i] := y[i-1] + 1; 
                    if (i = -8) then
                        with i: integer; do 
                            begin
                                i := 1;
                                for i := 0 to 5 do
                                    putIntLn(x[i]);
                            end
                    i := i + 1;
                end
                for i := -5 downto -10 do 
                    putIntLn(y[i]);
             end
        """
        expect = "0\n0\n0\n0\n0\n0\n5\n4\n3\n2\n1\n0\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_pass_by_value_array_1(self):
        input = """
            procedure foo(x: array [1 .. 5] of integer);
            var i: integer;
            begin
                for i := 1 to 5 do
                    x[i] := i * i;
                for i := 1 to 5 do
                   putIntLn(x[i]);
            end

            procedure main();
            var i: integer; c: array [1 .. 5] of integer;
            begin
                for i:=1 to 5 do
                    c[i] := i;
                for i := 1 to 5 do
                   putIntLn(c[i]);
                foo(c);
                for i := 1 to 5 do
                   putIntLn(c[i]);
            end
        """
        expect = "1\n2\n3\n4\n5\n1\n4\n9\n16\n25\n1\n2\n3\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_pass_by_value_array_2(self):
        input = """
            function foo(x: array [1 .. 5] of integer): integer;
            var i: integer;
            begin
                for i := 1 to 5 do
                    x[i] := i * i;
                for i := 1 to 5 do
                   putIntLn(x[i]);
                return 1;
            end

            procedure main();
            var i, res: integer; c: array [1 .. 5] of integer;
            begin
                for i:= 1 to 5 do
                    c[i] := i;
                for i := 1 to 5 do
                   putIntLn(c[i]);
                res := foo(c);
                for i := 1 to 5 do
                   putIntLn(c[i]);
            end
        """
        expect = "1\n2\n3\n4\n5\n1\n4\n9\n16\n25\n1\n2\n3\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,528))


    #************************* TEST WHILE *************************#

    def test_while_1(self):
        input = """
            procedure main();
            var i: integer; 
            begin
                i := 15;
                while (i < 25) do 
                begin
                    while (i < 20) do
                    begin
                        putIntLn(i);
                        i := i + 1;
                    end
                    i := i + 1;
                    putIntLn(i);
                    break;
                end
            end
        """
        expect = "15\n16\n17\n18\n19\n21\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_for_stmt_1(self):
        input = """
            procedure main();
            var i,j,k: integer; 
            begin
                for i := 1 to 4 do
                    for j:= i + 1 to 4 do 
                        putIntLn(i*j);
                for i := 1 to 10 do
                    begin
                        k := 0;
                        if k = 0 then
                            break;
                        else 
                            i := 5;
                    end
            end
        """
        expect = "2\n3\n4\n6\n8\n12\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_for_stmt_2(self):
        input = """
            procedure main();
            var i,j,k: integer; 
            begin
                for i := 1 to 10 do
                begin
                    if ((i mod 2) = 0) then
                        continue;
                    putIntLn(i);
                end  
            end
        """
        expect = "1\n3\n5\n7\n9\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    #TEST CALL FUNCTION 

    def test_call_function_simple(self):
        input = """
            function foo(a,b,c: integer): integer;
            begin
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
                a := a * 2;
                b := b * 2;
                c := c * 2;
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
                return 1;
            end

            var a,b,c,z: integer;

            procedure main();
            begin
                a := 1;
                b := 2;
                c := 3;
                z := foo(a,b,c);
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
            end
        """
        expect = "1\n2\n3\n2\n4\n6\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_call_recursive(self):
        input = """
            function fact(a: integer): integer;
            begin
                if (a = 1) or (a = 0) then
                    return 1;
                else 
                    return a * fact(a-1);
            end
            var a: integer;

            procedure main();
            begin
                a := 5;
                putIntLn(fact(a));
            end
        """
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))


    #TEST IF STMT 

    def test_if_stmt_1(self):
        input = """ 
            var x,y,z: integer;
            procedure main();
            begin
                if (x = 0) or (x = 1) then 
                    putIntLn(1);
                else 
                    putIntLn(2);
            end
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_if_stmt_2(self):
        input = """ 
            var x: real;
            procedure main();
            begin
                x := 15/3;
                if x = 5 then 
                begin
                    with x: real; do
                    begin
                        x := 15;
                        if x = 15 then
                            putFloatLn(x);
                    end
                    if x = 5 then x := x*x*x-x;
                    putFloatLn(x);   
                end
            end
        """
        expect = "15.0\n120.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_if_stmt_3(self):
        input = """ 
            var x: real;
            procedure main();
            var a : integer;
            begin
                a := -2;
                x := a*a;
                if x >= a then 
                    if x < 0 then
                        x := x*x;
                    else 
                        a := a*a; 
                putIntLn(a);
                putFloatLn(x);
            end
        """
        expect = "4\n4.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_if_stmt_4(self):
        input = """ 
            var x: real;
            procedure main();
            var a : integer;
            begin
                a := -2;
                x := a*a;
                if x >= a then 
                    if x < 0 then
                        x := x*x;
                    else 
                        a := a*a; 
                putIntLn(a);
                putFloatLn(x);
            end
        """
        expect = "4\n4.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_call_stmt_float_pass_int(self):
        input = """ 
            var x: real;
            procedure foo(a: real; b: integer);
            begin
                putFloatLn(a);
                putIntLn(b);
            end

            procedure main();
            var a : integer;
            begin
                foo(12,4);
            end
        """
        expect = "12.0\n4\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))


    def test_call_expr_float_pass_int_1(self):
        input = """ 
            var x: real;
            function foo(a: real; b: integer): integer;
            begin
                putFloatLn(a);
                return b + 12;
            end

            procedure main();
            begin
                x := foo(12,4);
                putFloatLn(x);
            end
        """
        expect = "12.0\n16.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_if_stmt___4(self):
        input = """ 
            var x: real;
            procedure main();
            var i: integer;
            begin
                x := 0;
                i := 1;
                if i = 2 then 
                    putStringLn("No10");
                else 
                    if i = 1 then 
                        if x = 0 then
                            if 0.0 = 10 then
                                putStringLn("No10");
                            else 
                                putFloatLn(i);
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_for_stmt___1(self):
        input = """ 
            var x: real;
            procedure main();
            var i: integer;
            begin
                for i := 1 to 10 do
                begin 
                    putIntLn(i);
                    i := 10;
                end
                for i := 10 downto 1 do
                begin 
                    putIntLn(i);
                    i := 1;
                end
            end
        """
        expect = "1\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_for_stmt___2(self):
        input = """ 
            procedure main();
            var i,j,s1,s2: integer;
            begin
                s1 := 0;
                s2 := 0;
                for i := 10 downto 1 do
                begin
                    s1 := s1 + i;
                    for j := 1 to 10 do 
                    begin
                        s2 := s2 + j;
                        if j = 7 then 
                            break;
                    end
                end 
                putIntLn(s1);          
                putIntLn(s2);
            end
        """
        expect = "55\n280\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_return_1(self):
        input = """ 
            function foo1(): string;
            begin 
                return "Ass 4";
            end

            function foo2(): real;
            begin 
                return 12.0256;
            end

            function foo3(): integer;
            begin 
                return 2;
            end

            function foo4(): boolean;
            begin 
                return TRUE;
            end

            procedure main();
            begin
                putStringLn(foo1());
                putFloatLn(foo2());
                putIntLn(foo3());
                putBoolLn(foo4());
            end
        """
        expect = "Ass 4\n12.0256\n2\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    
    def test_return_2(self):
        input = """ 
            function foo1(): real;
            begin 
                return 10;
            end

            procedure main();
            begin
               putFloat(foo1());
            end
            var x : real;
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_return_3(self):
        input = """ 
            function foo1(): real;
            begin 
                reTurn 10;
            end

            procedure foo();
            begin 
                putIntLn(20);
                REturn;
            end

            procedure main();
            begin
               FOo();
               putFloat(foo1());
            end
            var x : real;
        """
        expect = "20\n10.0"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_with_stmt__1(self):
        input = """
            procedure main();
            var x: integer;
            begin
                y := 20;
                PuTFloatLN(y);
                with y: real; do 
                begin 
                    y := 10;
                    PuTFloatLN(y);
                    with y: real; do
                    begin
                        y := 15;
                        PuTFloatLN(y);
                    end
                    if y = 15 then 
                        PuTFloatLN(15);
                    else 
                        PuTFloatLN(y);
                end
                PuTFloatLN(y);
            end
            var x,y,z : real;
        """
        expect = "20.0\n10.0\n15.0\n10.0\n20.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_assign_stmt_1(self):
        input = """
            procedure main();
            var a,b,c: integer;
            begin
                m[2] := m[3] := m[n[2]] := n[2] := n[3] := a := b := 4;
                putString("Array real: ");
                for c := 1 to 5 do 
                begin
                    putFloat(m[c]);
                    putString("   ");
                end
                putLN();
                putString("Array integer: ");
                for c := 1 to 5 do 
                begin
                    putINt(n[c]);
                    putString("   ");
                end
                putLN();
                putStringLN("a,b: ");
                putINtLn(a);
                putINtLn(b);
            end
            var m: array [1 .. 5] of real;
            var n: array [1 .. 5] of integer;
            var x,y,z : real;
        """
        expect = """Array real: 0.0   4.0   4.0   4.0   0.0   \nArray integer: 0   4   4   0   0   \na,b: \n4\n4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_assign_stmt_2(self):
        input = """
            procedure main();
            begin
                x1 := y1 := z1 := 12 > 5 and then 3 >= 2;
                putBoolLn(x1);
                putBoolLn(y1);
                putBoolLn(z1);
                x2 := y2 := z2 := 15 + 25 MOD 5 + 12 * 5 mod 5 + 15 div 10; 
                putIntLn(x2);
                putIntLn(y2);
                putIntLn(z2);
                x3 := y3 := z3 := 30 / 15;
                putFloatLn(x3);
                putFloatLn(y3);
                putFloatLn(z3);
            end
            var x1,y1,z1: boolean;
            var x2,y2,z2: integer;
            var x3,y3,z3: real;
        """
        expect = """true\ntrue\ntrue\n16\n16\n16\n2.0\n2.0\n2.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_array_cell_1(self):
        input = """
            procedure main();
            var x: array [-10 .. -6] of integer; i: integer;
            begin
                for i := -6 downto -10 do
                    x[i] := i * i;
                for i := -1 to 3 do
                    y[i] := i * i; 
                y[x[-6] - 6*6 -1] := x[-10] := x[-7];
                for i := -6 downto -10 do
                    putIntLn(x[i]);
                for i := -1 to 3 do
                    putFloatLn(y[i]);                
            end
            var x,y: array [-1 .. 3] of real;
        """
        expect = """36\n49\n64\n81\n49\n49.0\n0.0\n1.0\n4.0\n9.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_array_cell_2(self):
        input = """
            procedure main();
            var i: integer;
            begin
                for i := 3 downto -1 do
                begin
                    x[i] := i/10*2;
                    y[i] := "PPL";
                    z[i] := i * i div 2;
                    t[i] := z[i] mod 2 = 0;
                end
                for i := -1 to 3 do
                    putFloatLn(x[i]);
                for i := -1 to 3 do
                    putStringLn(y[i]);
                for i := -1 to 3 do
                    putIntLn(z[i]);
                for i := -1 to 3 do
                    putBoolLn(t[i]);            
            end
            var x: array [-1 .. 3] of real;
            var y: array [-1 .. 3] of string;
            var z: array [-1 .. 3] of integer;
            var t: array [-1 .. 3] of boolean;
        """
        expect = """-0.2\n0.0\n0.2\n0.4\n0.6\nPPL\nPPL\nPPL\nPPL\nPPL\n0\n0\n0\n2\n4\ntrue\ntrue\ntrue\ntrue\ntrue\n"""
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_call_Stmt_1(self):
        input = """
            procedure foo(x: integer; y: real; z: string; t: boolean);
            begin 
                putIntLn(x);
                putFloatLn(y);
                putStringLn(z);
                putBoolLn(t);
            end
            var a: real; b: integer;
            procedure main();
            var c: string; d: boolean;
            begin
                a := 12.87;
                b := 10;
                c := "PPL 10";
                d :=  10 = 10;
                foo(b,a,c,d);     
            end
        """
        expect = """10\n12.87\nPPL 10\ntrue\n"""
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_call_Expression_1(self):
        input = """
            function foo(x: integer; y: real; z: string; t: boolean): integer;
            begin 
                putIntLn(x);
                putFloatLn(y);
                putStringLn(z);
                putBoolLn(t);
                return x;
            end
            var a: real; b: integer;
            procedure main();
            var c: string; d: boolean;
            begin
                a := 12.87;
                b := 10;
                c := "PPL 10";
                d :=  10 = 10;
                a := foo(b,a,c,d);     
            end
        """
        expect = """10\n12.87\nPPL 10\ntrue\n"""
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_array_decl_in_local(self):
        input = """
            function foo(x: array [1 .. 3] of real): integer;
            var i: integer; y: array [1 .. 3] of string; z: array [1 .. 3] of boolean;
            begin 
                for i := 1 to 3 do 
                begin   
                    putFloatLn(x[i]);
                    putStringLn(y[i]);
                    putBoolLn(z[i]);
                end
                return 10;
            end       
            var m : array [1 .. 3] of real;
            procedure main();
            var i: integer;
            begin
                for i := 1 to 3 do 
                    m[i] := i*i;
                i := foo(m);
            end
        """
        expect = """1.0\nnull\nfalse\n4.0\nnull\nfalse\n9.0\nnull\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_short_circuit_evalution_1(self):
        input = """
            var x,y: integer;

            function foo1(): boolean;
            begin
                x := 10;
                return true;
            end

            function foo2(): boolean;
            begin
                y := 10;
                return true;
            end

            procedure main();
            var i: integer;
            begin
                x := 5;
                y := 5;
                putBoolLn((1+1 = 3) and then foo1());
                putBoolLn((1+1 = 3) and foo2());
                putIntLn(x);
                putIntLn(y);
            end
        """
        expect = """false\nfalse\n5\n10\n"""
        self.assertTrue(TestCodeGen.test(input,expect,553))

    
    def test_short_circuit_evalution_2(self):
        input = """
            var x,y: integer;

            function foo1(): boolean;
            begin
                x := 10;
                return true;
            end

            function foo2(): boolean;
            begin
                y := 10;
                return true;
            end

            procedure main();
            var i: integer;
            begin
                x := 5;
                y := 5;
                putBoolLn((1+1 = 2) or else foo1());
                putBoolLn((1+1 = 2) or foo2());
                putIntLn(x);
                putIntLn(y);
            end
        """
        expect = """true\ntrue\n5\n10\n"""
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_short_circuit_evalution_3(self):
        input = """
            var x,y: integer;

            function foo1(): boolean;
            begin
                x := 10;
                return true;
            end

            function foo2(): boolean;
            begin
                y := 10;
                return true;
            end

            procedure main();
            var i: integer;
            begin
                x := 5;
                y := 5;
                putBoolLn((1+1 = 2) and then foo1());
                putBoolLn((1+1 = 2) and foo2());
                putIntLn(x);
                putIntLn(y);
            end
        """
        expect = """true\ntrue\n10\n10\n"""
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_short_circuit_evalution_4(self):
        input = """
            var x,y: integer;

            function foo1(): boolean;
            begin
                x := 10;
                return true;
            end

            function foo2(): boolean;
            begin
                y := 10;
                return true;
            end

            procedure main();
            var i: integer;
            begin
                x := 5;
                y := 5;
                putBoolLn((1+1 = 3) or else foo1());
                putBoolLn((1+1 = 3) or foo2());
                putIntLn(x);
                putIntLn(y);
            end
        """
        expect = """true\ntrue\n10\n10\n"""
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_and_then_or_else__(self):
        input = """
            procedure main();
            begin
                putBoolLn(true or eLse true);
                putBoolLn(true OR eLse false);
                putBoolLn(false OR else true);
                putBoolLn(false or else false);
                putBoolLn(true and THEN true);
                putBoolLn(true and THEN false);
                putBoolLn(false and THEN true);
                putBoolLn(false and THEN false);
            end
        """
        expect = """true\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_pass_by_value_prim_type_in_call_stmt(self):
        input = """
            procedure foo(a: integer; b: real; c: boolean);
            begin
                putIntLn(a);
                putFloatLn(b);
                putBoolLn(c);
                a := 10;
                b := 10.0;
                c := true;
                putIntLn(a);
                putFloatLn(b);
                putBoolLn(c);
            end
            
            var x: integer; y: real; z: boolean;

            procedure main();
            begin
                x := 5;
                y := 5.0;
                z := false;
                putIntLn(x);
                putFloatLn(y);
                putBoolLn(z);
                foo(x,y,z);
                putIntLn(x);
                putFloatLn(y);
                putBoolLn(z); 
            end
        """
        expect = """5\n5.0\nfalse\n5\n5.0\nfalse\n10\n10.0\ntrue\n5\n5.0\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_pass_by_value_prim_type_in_call_expression(self):
        input = """
            function foo(a: integer; b: real; c: boolean): real;
            begin
                putIntLn(a);
                putFloatLn(b);
                putBoolLn(c);
                a := 10;
                b := 10.0;
                c := true;
                putIntLn(a);
                putFloatLn(b);
                putBoolLn(c);
                return 10.0;
            end
            
            var x: integer; y: real; z: boolean;

            procedure main();
            var i: real;
            begin
                x := 5;
                y := 5.0;
                z := false;
                putIntLn(x);
                putFloatLn(y);
                putBoolLn(z);
                i := foo(x,y,z);
                putIntLn(x);
                putFloatLn(y);
                putBoolLn(z); 
            end
        """
        expect = """5\n5.0\nfalse\n5\n5.0\nfalse\n10\n10.0\ntrue\n5\n5.0\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_pass_by_value_array_type_in_call_express(self):
        input = """
            function foo(a: array [1 .. 3] of real): boolean;
            var i: integer;
            begin
                for i := 1 to 3 do 
                    putFloatLn(a[i]);
                for i := 1 to 3 do 
                    a[i] := 444;
                for i := 1 to 3 do 
                    putFloatLn(a[i]);
                return true;
            end
            
            var x: array [1 .. 3] of real;

            procedure main();
            var i: integer; z: boolean;
            begin
                for i := 1 to 3 do 
                    x[i] := 10;
                for i := 1 to 3 do 
                    putFloatLn(x[i]);
                z := foo(x);
                for i := 1 to 3 do 
                    putFloatLn(x[i]);  
            end
        """
        expect = """10.0\n10.0\n10.0\n10.0\n10.0\n10.0\n444.0\n444.0\n444.0\n10.0\n10.0\n10.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_pass_by_value_array_type_in_call_stmt(self):
        input = """
            procedure foo(a: array [1 .. 3] of integer);
            var i: integer;
            begin
                for i := 1 to 3 do 
                    putFloatLn(a[i]);
                for i := 1 to 3 do 
                    a[i] := 444;
                for i := 1 to 3 do 
                    putFloatLn(a[i]);
            end
            
            var x: array [1 .. 3] of integer;

            procedure main();
            var i: integer; z: boolean;
            begin
                for i := 1 to 3 do 
                    x[i] := 10;
                for i := 1 to 3 do 
                    putFloatLn(x[i]);
                foo(x);
                for i := 1 to 3 do 
                    putFloatLn(x[i]);  
            end
        """
        expect = """10.0\n10.0\n10.0\n10.0\n10.0\n10.0\n444.0\n444.0\n444.0\n10.0\n10.0\n10.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,561))


    def test_return_array_1(self):
        input = """
            function foo1(a: array [1 .. 3] of integer): array [1 .. 3] of integer;
            var i: integer;
            begin
                for i := 1 to 3 do 
                    a[i] := 444;
                return a;
            end

            function foo2(a: array [1 .. 3] of real): array [1 .. 3] of real;
            var i: integer;
            begin
                for i := 1 to 3 do 
                    a[i] := 555;
                return a;
            end

            function foo3(a: array [1 .. 3] of boolean): array [1 .. 3] of boolean;
            var i: integer;
            begin
                for i := 1 to 3 do 
                    a[i] := i mod 2 = 0;
                return a;
            end

            procedure printArrayBoolean(a: array [1 .. 3] of boolean);
            var i: integer;
            begin
                for i := 1 to 3 do 
                    putBoolLn(a[i]);
            end

            procedure printArrayInteger(a: array [1 .. 3] of integer);
            var i: integer;
            begin
                for i := 1 to 3 do 
                    putIntLn(a[i]);
            end

            procedure printArrayFloat(a: array [1 .. 3] of real);
            var i: integer;
            begin
                for i := 1 to 3 do 
                    putFloatLn(a[i]);
            end

            var z: array [1 .. 3] of integer;

            procedure main();
            var x: array [1 .. 3] of real; i: integer;
            begin
                with x: array [1 .. 3] of boolean; do
                begin
                    for i := 1 to 3 do
                        x[i] := TRue;
                    printArrayBoolean(x);
                    printArrayBoolean(foo3(x)); 
                end
                
                for i := 1 to 3 do 
                begin
                    x[i] := 10.0;
                    z[i] := 20;
                end
                printArrayFloat(x);
                printArrayFloat(foo2(x));
                printArrayInteger(z);
                printArrayInteger(foo1(z));
            end
        """
        expect = """true
true
true
false
true
false
10.0
10.0
10.0
555.0
555.0
555.0
20
20
20
444
444
444
"""
        self.assertTrue(TestCodeGen.test(input,expect,562))


    def test_array_decla_in_global(self):
            input = """
                procedure main();
                begin
                    for i := -1 to 3 do 
                    begin
                        putIntLn(x[i]);
                        putFloatLn(y[i]);
                        putBoolLn(z[i]);
                        putStringLn(t[i]);
                    end   
                end

                var x: array [-1 .. 3] of integer;
                var y: array [-1 .. 3] of real;
                var z: array [-1 .. 3] of boolean;
                var t: array [-1 .. 3] of string;
                var i: integer;

            """
            expect = """0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
"""
            self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_array_decla_in_local_var(self):
            input = """
                procedure main();
                var x: array [-1 .. 3] of integer;
                  y: array [-1 .. 3] of real;
                  z: array [-1 .. 3] of boolean; 
                  t: array [-1 .. 3] of string; 
                  i: integer;
                begin
                    for i := -1 to 3 do 
                    begin
                        putIntLn(x[i]);
                        putFloatLn(y[i]);
                        putBoolLn(z[i]);
                        putStringLn(t[i]);
                    end   
                end
            """
            expect = """0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
"""
            self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_array_decla_in_with_stmt(self):
            input = """
                procedure main();
                var i: integer;
                begin
                    with 
                         x: array [-1 .. 3] of integer;
                         y: array [-1 .. 3] of real;
                         z: array [-1 .. 3] of boolean;
                         t: array [-1 .. 3] of string;
                    do 
                    begin
                        for i := -1 to 3 do 
                        begin
                            putIntLn(x[i]);
                            putFloatLn(y[i]);
                            putBoolLn(z[i]);
                            putStringLn(t[i]);
                        end   
                    end
                end
            """
            expect = """0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
0
0.0
false
null
"""
            self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_array_cell_complex_1(self):
            input = """
                procedure main();
                var x: array [-1 .. 3] of integer;
                y: array [-1 .. 3] of real;
                z: array [-1 .. 3] of boolean; 
                t: array [-1 .. 3] of string;                  
                i: integer;
                begin
                    for i := -1 to 3 do
                        x[i] := i;
                    i := 2;
                    x[x[x[x[i]]]] := 3;
                    z[x[x[x[x[i]]]]] := not z[x[i]];
                    for i := -1 to 3 do
                        putBoolLn(z[i]);
                end
            """
            expect = """false
false
false
false
true
"""
            self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_array_cell_complex_2(self):
            input = """
                function foo(): array [-1 .. 3] of real;
                begin
                    return z;
                end

                procedure main();
                var y: array [-1 .. 3] of real;   
                x: array [-1 .. 3] of integer;              
                i: integer;
                begin
                    for i := -1 to 3 do
                        z[i] := i;
                    for i := -1 to 3 do
                        x[i] := i*i;
                    for i := -1 to 3 do 
                        putFloatLn(y[i]);
                    y[2] := foo()[2];
                    y[3] := foo()[1];
                    for i := -1 to 3 do 
                        putFloatLn(y[i]);
                end

                var z: array [-1 .. 3] of real; a: integer; 
            """
            expect = """0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
2.0
1.0
"""
            self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_advanced_binary_op_1(self):
            input = """
                procedure main();
                var x: integer; y: real; z : boolean; 
                begin 
                    x := 0;
                    y := 1;
                    z := false or true;
                    putBoolLn(12 <> 3.2);
                    putBoolLn(12 <> 12.0);
                    putBoolLn(12 <> 12);
                    putBoolLn(12 >= 12.0);
                    putBoolLn(12 >= 12);
                    putBoolLn(x = 0);
                    putBoolLn(y = 1);
                    putBoolLn(y = 0.0);
                    putBoolLn(not z and not true);
                end
            """
            expect = """true
false
false
true
true
true
true
false
false
"""
            self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_advanced_binary_op_2(self):
            input = """
                procedure main();
                var x: integer; y: real; z : boolean; 
                begin 
                    x := 29;
                    putIntLn(x mod 10);
                    putIntLn((12 + 5) mod 12);
                    putIntLn(12 + 5 mod 12);
                end
            """
            expect = """9
5
17
"""
            self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_advanced_binary_op_3(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                x := 29;
                putIntLn(x div 10 mod 2);
                putfloatLn(29 div 120);
                putfloatLn(-29 div 8);
            end
        """
        expect = """0
0.0
-3.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_advanced_binary_op_4(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putBoolLn(12 < 5.0);
                putBoolLn(12 < 12.0);
                putBoolLn(78.34 < 12.0);
                putBoolLn(78.34 < 12);
                putBoolLn(12.0 < 24);
                putBoolLn(78.0 < 120);
            end
        """
        expect = """false
false
false
false
true
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_advanced_binary_op_5(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                x := 12;
                y := 4/5 * x / 34 - 3 + 76 /4 - -----4 * 7 -----7 ----- 7;
                putFloatLn(y);
                putBoolLn(y <= 5.0);
                putBoolLn(y >= 5.0);
                putBoolLn(y = 5);
                putBoolLn(x >= 12.0);
                putBoolLn(x <= 12);
                putBoolLn(x = 12);
            end
        """
        expect = """30.282352
false
true
false
true
true
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_advanced_binary_op_6(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                x := 12;
                y := x * x / x / x;
                putFloatLn(y);
                putFloatLn(x);
                x := x * -7 mod 19 div 2 mod 4;
                y := (87 * x mod 12) / 45 * 78 + -------34;
                putFloatLn(y);
                putFloatLn(x);
            end
        """
        expect = """1.0
12.0
-34.0
0.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_unary__op_advanced_1(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putBoolLn( not true and not false);
                putBoolLn( not (12/5=9) and (4 = 4));
            end
        """
        expect = """false
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_unary__op_advanced_2(self):
        input = """
            procedure main();
            var x: integer; y: real; z : boolean; 
            begin 
                putFloatLn(-23-34);
                putFloatLn(-3232323.23232665656);
            end
        """
        expect = """-57.0
-3232323.2
"""
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_call_recursive_complex_1(self):
        input = """
            function fibo(n: integer): integer;
            begin
                if (n = 0) or (n = 1) then
                    return n;
                else 
                    return fibo(n-1) + fibo(n-2);
            end

            procedure main();
            var x: integer; 
            begin 
                x := 28;
                putIntLn(fibo(x));
                putIntLn(fibo(7));
            end
        """
        expect = """317811
13
"""
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_call_recursive_complex_2(self):
        input = """
            function foo1(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo2(n-1);
            end

            function foo2(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo3(n-1);
            end

            function foo3(n: integer): integer;
            begin
                if (n = 0) then
                    return 0;
                putIntLn(n);
                return foo1(n-1);
            end

            var n: integer;

            procedure main();
            var x: integer; 
            begin 
                n := 10;
                x := foo1(n);
            end
        """
        expect = """10
9
8
7
6
5
4
3
2
1
"""
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_build_in_function(self):
        input = """
            procedure main();
            var x: integer; 
            begin 
                putSTRING("PPL \\n 2018");
                putLN();
                putSTRINGLn("PPL \\n 2018");
                putBOOL(true);
                putBoolLN(false);
                putFloat(45);
                putFloat(45.6);
                putFloatLn(45);
                putFloatLN(45.25);
                putInt(89);
                putINTLN(343);  
            end
        """
        expect = """PPL 
 2018
PPL 
 2018
truefalse
45.045.645.0
45.25
89343
"""
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_complex_with_string(self):
        input = """
            function foo(x: string; num: integer): string;
            var i: integer;
            begin
                for i := 1 to num do
                    putStringLn(x);
                n := n + 1;
                if n > 20 then
                    return "END";
                else 
                    return foo("PPL",5);
            end

            procedure main();
            begin 
                n := 15;
                putString(foo("ppl",5));
            end
            var n: integer;
        """
        expect = """ppl
ppl
ppl
ppl
ppl
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
PPL
END"""
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_complex_with_with_stmt(self):
        input = """
            function printAString(x: array [1 .. 3] of string): integer;
            var I: integer;
            begin
                for i := 1 to 3 do 
                    putSTRINGLN(x[i]);
                return 1;
            end

            function printAInt(x: array [1 .. 3] of integer): integer;
            var I: integer;
            begin
                for i := 1 to 3 do 
                    putINtLN(x[i]);
                return 1;
            end

            function printAFloat(x: array [1 .. 3] of Real): integer;
            var I: integer;
            begin
                for i := 1 to 3 do 
                    putFloatLN(x[i]);
                return 1;
            end

            function printABoolean(x: array [1 .. 3] of boolean): integer;
            var I: integer;
            begin
                for i := 1 to 3 do 
                    putBoolLN(x[i]);
                return 1;
            end

            procedure main();
            var i: integer;
            begin 
                with x: array [1 .. 3] of boolean; do
                begin
                    with x: array [1 .. 3] of integer; do
                    begin
                        with x: array [1 .. 3] of real; do
                        begin
                            i := printAFloaT(x);
                        end
                        i := printAInt(x);
                    end
                    i := printABoolean(x);
                end
                i := printAString(x);
            end
            var x: array [1 .. 3] of string;
        """
        expect = """0.0
0.0
0.0
0
0
0
false
false
false
null
null
null
"""
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_complex_break_continue_stmt(self):
        input = """
            procedure main();
            var i,j: integer;
            begin 
                for i := 1 to 100000 do 
                begin
                    for j := 10000 downto 1 do
                        with i: integer; do
                        begin    
                            i := 1;
                            if j = 9999 then
                                break;
                        end
                    if i < 99995 then 
                        continue;
                    else 
                    begin
                        putFloatLn(i);
                        break;
                    end
                end
            end
        """
        expect = """99995.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_while_complex(self):
        input = """
            function sumOdd(x: array [0 .. 100] of integer): integer;
            var i,s : integer;
            begin
                i := 100;
                s := 0;
                while (i >= 0) do
                begin
                    if (x[i] mod 2) = 0 then 
                        s := s + x[i];
                    i := i - 1;
                end
                return s;
            end

            procedure main();
            var z: array [0 .. 100] of integer; i: integer;
            begin 
                for i := 100 downto 0 do
                    z[i] := i;
                putFloatLn(sumOdd(z));
            end
        """
        expect = """2550.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_call_express_complex(self):
        input = """
            function foo(x: integer; y: string; z: real; t: boolean): integer;
            begin
                if t then 
                    putStringLN(y);
                i := i + 1;
                if i = 110 then 
                    return x;
                else 
                    return foo(x+1, "PPL", z + 1.5, not t) + x;
            end

            var i: integer;

            procedure main();
            begin 
                i := 100;
                putFloatLn(foo(10,"ppl",1.23,true));
            end
        """
        expect = """ppl
PPL
PPL
PPL
PPL
145.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_call_stmt_complex(self):
        input = """
            procedure foo(x: integer; y: string; z: real; t: boolean);
            begin
                if t then
                begin 
                    putStringLN(y);
                    putIntLn(x);
                    putFloatLN(z);
                end
                i := i + 1;
                if i = 110 then 
                    return;
                else 
                    foo(x+1, "PPL", z + 1.5, not t);
            end

            procedure foo1(x: array [1 .. 10] of real; y: array [1 .. 10] of integer);
            var i: integer; res: array [1 .. 10] of real;
            begin
                for i := 1 to 10 do 
                    res[i] := x[i] + y[i];
                for i := 10 downto 1 do
                    putFloatLn(res[i]);
            end

            var x: array [1 .. 10] of integer; j,i: integer;

            procedure main();
            begin 
                i := 100;
                foo(10,"ppl",1.23,true);
                with y: array [1 .. 10] of real; do
                begin
                    for j := 10 downto 1 do
                    begin
                        x[j] := j*j;
                        y[j] := j;
                    end
                    foo1(y,x);
                end
            end 
        """
        expect = """ppl
10
1.23
PPL
12
4.23
PPL
14
7.23
PPL
16
10.23
PPL
18
13.23
110.0
90.0
72.0
56.0
42.0
30.0
20.0
12.0
6.0
2.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,584))

    




    



    




    

