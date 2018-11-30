import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = """         
        procedure main();
        var b: array[0 .. 100] of real;
        x: real;
        e: string;
        begin
        e := ":D:D";
            x := -100;
            b[0] := 100 + 2*x;
            b[1] := 2*b[0] - 900;
            putFloatLn(b[1]);
            putFloatLn(x);
            putStringLn(e);
        end"""
        expect = """-1100.0
-100.0
:D:D
"""

        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_1(self):
        input = """         

        var z: integer;

        procedure main();
        var b: array[0 .. 2] of string;
        e: integer;
        x: real;
        z: string;
        begin
            z := "?? :D ??";
            putString(z);
        end

        procedure foo();
        begin

        end
        """
        expect = """?? :D ??"""

        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test2(self):
        input = """
        var z: integer;
        var b: array[0 .. 2] of real;

        procedure main();
     //   var b: array[0 .. 2] of real;
        var e: integer;
        x: real;
        begin
			foo();
			putFloatLn(b[0]);
			putFloatLn(b[1]);
			putInt(z);
        end

		procedure foo();
		begin
			b[0] := 1000;
			z := 10;
		end
        """
        expect = """1000.0
0.0
10"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test3(self):
        input = """

        var z: integer;
        var b: array[0 .. 2] of real;

        procedure main();
        var e: integer;
        x: real;
        z: string;
        begin
            e := 12;
            x := 12*100;
            b[1] := e + x - 200;
            putFloatLn(b[1]);
            foo();
        end

        procedure foo();
        begin
            putFloat(b[1]);
        end        """
        expect = """1012.0\n1012.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test04(self):
        input = """
        
        var z: integer;

        procedure main();
        var b: array[0 .. 2] of real;
        e: integer;
        x: real;
        begin
            e := 12;
            x := 12*100 - e;
            b[1] := e*x - 200;
            z := 122*2;
            putFloat(z);
        end
        """
        expect = """244.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test05(self):
        input = """
        var x: integer;
        var z: array[0 .. 3] of integer;
        procedure main();
        begin
        x := 10;
        foo();
        putIntLn(z[2]);
        putIntLn(x);
        end

        procedure foo();
        begin
            z[2] := 100;
        end
        """
        expect = """100
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test06(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (x > 100) then
                putStringLn("100 < x < 200");
            else if (x > 200) then
                putStringLn("200 < x < 300");
            else if (x > 300) then
                putStringLn("x > 300");
            else 
            begin
                if (x > 100) then
                 x := x + 100;
            end
            putIntLn(x);
        end
"""
        expect = """100 < x < 200
123
"""
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test07(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (true and false) then
                x := x - 100;
            putIntLn(x);
        end
        """
        expect = """123\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test08(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 1;
            while x <= 10 do
            begin
 putIntLn(x);
                if x = 10 then putStringLn("lmao");

                x := x + 1;
            end
        end
        """
        expect = """1
2
3
4
5
6
7
8
9
10
lmao
"""
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test09(self):
        input = """
function isPrime(x: integer): boolean;
var i : integer;
begin
    for i := 2 to x div 2 do
    begin
        if x mod i = 0 then return false;
    end

    return true;
end

procedure main();
var x, i : integer;
begin
    i := 0;
    x := 100;

    while i <= x do
    begin
        if isPrime(i) then putIntLn(i);
        i := i + 1;
    end

end
        """
        expect = """0
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test10(self):
        input = """
function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end

procedure main();
var s, i : integer;
begin
    i := 1;
    s := 0;

    while i <= 10 do 
    begin
        putIntLn(fact(i));
        i := i + 1;
    end

end
        """
        expect = """1
2
6
24
120
720
5040
40320
362880
3628800
"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test11(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;

    while i <= 10 do 
    begin
        if (i > 4) and (i < 7) then 
        begin
            i := i + 1;
            continue;
        end

        s := 0;
        for j := i * 10 to (i + 1)*10 do
        begin
            if (j mod 2 = 0) then continue;
            s := s + j;
        end
        putInt(i);
        putString(", ");
        putInt(s);
        putLn();
        i := i + 1;
    end

end

function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end
        """
        expect = """1, 75
2, 125
3, 175
4, 225
7, 375
8, 425
9, 475
10, 525
"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test12(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;
    putIntLn(fact(7));
end

function fact(x: integer): integer;
begin
    if x < 2 then
        return 1;
    else
    return x * fact(x - 1);
end
        """
        expect = """5040\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test13(self):
        input = """
        var z : array[0 .. 3] of real; 
        
        procedure main();
        var x: integer;
        begin
            z[0] := 10;
            x := 20;
            z[1] := z[0]* x * 2 - 3*x + z[0];
            putFloatLn(z[1]);
            bar();
        end

        procedure bar();
        begin
            putFloatLn(z[1]);
        end
        """
        expect = """350.0
350.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test14(self):
        input = """
       procedure main();
       var x : array[0 .. 100] of integer;
       i : integer;
       begin
            x[0] := 1;
            x[1] := 2;
            x[2] := x[0] - 2*x[1] - 100;

            for i := 0 to 2 do putIntLn(x[i]);
       end
        """
        expect = """1
2
-103
"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test15(self):
        input = """
              procedure main();
       var x : array[0 .. 100] of boolean;
       i : integer; z : boolean;
       begin
           x[0] := false;
            x[1] := true;
            x[2] := (10 > 12 - 100) and x[1];
            z := x[2];
            for i := 0 to 2 do putBoolLn(x[i]);

            putBoolLn(z);
       end
        """
        expect = """false
true
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test16(self):
        input = """
       procedure main();
       var x : integer; z : array[0 .. 3] of integer;
       begin
        z[1] := 12;
        x := -z[1] + 100;
        putInt(x);
        end

        """
        expect = """88"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test17(self):
        input = """
       procedure main();
       var x: integer;
       begin
            x := 1;
            with x : integer; do 
            begin
                x := 2;
                with x : integer; do
                begin
                    x := 3;
                    putInt(x);
                end
                putInt(x);
            end
       end
        """
        expect = """32"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test18(self):
        input = """

    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo");
        return false;
    end

    procedure main();
    begin
        x := 10;

        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end
        """
        expect = """in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test20(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in then\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test19(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        return false;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test21(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");

        putIntLn(x);
    end        """
        expect = """in else\n10\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test22(self):
        input = """
       function foo(): real;
       begin
            return 1;
        end

        procedure main();
        begin
            putFloat(foo());
        end
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test23(self):
        input = """
        procedure main();
        var x, y: integer;
        begin
            x := 10;
            y := 12;
            putInt(gcd(x + y, x));
        end

        function gcd(a,b : integer): integer;
        begin
            if b = 0 then
                return a;
            else
                return gcd(b, a mod b);
        end        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test24(self):
        input = """
        procedure main();
        var x, y: integer; b: array[0 .. 100] of integer;
        begin
            x := 6;
            b[1] := 12;
            putInt(gcd(x + b[1], x*2+b[1]));
        end

        function gcd(a,b : integer): integer;
        begin
            if b = 0 then
                return a;
            else
                return gcd(b, a mod b);
        end        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test25(self):
        input = """
        procedure main();
        var x: array[0 .. 2] of integer;
        begin
            x[0] := 100;
            x[1] := 200;
            swap(x);
            putInt(x[0]);
            putInt(x[1]);
        end

        procedure swap(a: array[0 .. 2] of integer);
        var temp: integer;
        begin
                temp := a[1];
                a[1] := a[0];
                a[0] := temp;
            end        """
        expect = """100200"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test26(self):
        input = """
       procedure main();
       var x: array[0 .. 2] of integer;
       begin
        x[0] := 100;
        x[1] := 50;

        putIntLn(x[0]);
        putStringLn("x");
        putInt(foo(x) + 50);
       end

       function foo(a: array[0 .. 2] of integer): integer;
       var temp: integer;
       begin
            putIntLn(a[0]);
            return a[0];
        end        """
        expect = """100
x
100
150"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test27(self):
        input = """
       procedure main();
       var x : array[-1 .. 3] of integer;
       begin
            x[-1] := 12;
            x[1] := 3;

            putInt(x[0]);
        end
        """
        expect = """0"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test28(self):
        input = """
     procedure main();
       var a : array[0 .. 3] of integer;
       begin
            a[0] := 10;
            foo(a);
            putInt(a[0]);
        end

        procedure foo(b: array[0 .. 3] of integer);
        begin
            b[0] := 100;
        end        """
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test29(self):
        input = """
       procedure main();
       var x: array[1 .. 1] of integer;
       begin
        x[1] := 12;
        foo(x);
        putIntLn(x[1]);
        end

        procedure foo(x: array[1 .. 1] of integer);
        begin
            putIntLn(x[1]);
            x[1] := 1000;
            putIntLn(x[1]);
        end        """
        expect = """12
1000
12
"""
        self.assertTrue(TestCodeGen.test(input, expect, 529))


    def test30(self):
        input = r"""
	   procedure main();
	   var x: array[0 .. 4] of integer;
	   i, j, temp: integer;
	   begin


			bbsort();
	   end

	   procedure bbsort();
	   var n, temp, i, j: integer;x: array[0 .. 4] of integer;
	   begin
		n := 5;
			x[0] := 5;
			x[1] := 2;
			x[2] := 8;
			x[3] := 9;
			x[4] := 1;
		for i := 0 to n - 2 do
			for j := 0 to n - i - 2 do
				if x[j] > x[j+1] then
					begin
					temp := x[j];
					x[j] := x[j + 1];
					x[j+1] := temp;
					end

		for i := 0 to n - 1 do
		begin
			putInt(i);
			putString("\t");
		end
	   end        """
        expect = """0	1	2	3	4	"""
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test31(self):
        input = r"""
	   procedure main();
	   var x: array[0 .. 4] of integer;
	   i, j, temp: integer;
	   begin

			x[0] := 5;
			x[1] := 2;
			x[2] := 8;
			x[3] := 9;
			x[4] := 1;
			bbsort(x);
			putLn();
		for i := 0 to 4 do
		begin
			putInt(x[i]);
			putString("\t");
		end
	   end

	   procedure bbsort(x: array[0 .. 4] of integer);
	   var n, temp, i, j: integer;
	   begin
		n := 5;
		for i := 0 to n - 1 do
		for i := 0 to n - 2 do
			for j := 0 to n - i - 2 do
				if x[j] > x[j+1] then
					begin
					temp := x[j];
					x[j] := x[j + 1];
					x[j+1] := temp;
					end

		for i := 0 to n - 1 do
		begin
			putInt(x[i]);
			putString("\t");
		end
	   end        """
        expect = """1	2	5	8	9	
5	2	8	9	1	"""
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test32(self):
        input = """
	   procedure main();
	   var x: array[0 .. 4] of integer;
	   i, j, temp: integer;
	   begin
			putFloatLn(2);
	   end
        """
        expect = """2.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test33(self):
        input = """
		   procedure main();
		   var x: array[-1 .. 5] of integer;
		   begin
			
			x[0] := 1;
			x[1] := 2;
			x[3] := 2*x[0] + 10*x[1] - 4*x[0]*x[1];
			putInt(x[3]);
			
		   end        """
        expect = """14"""
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test34(self):
        input = """
		procedure main();
		var x: integer;
		begin
			x := 10;
			foo(x);
			putFloat(x);
		end

		procedure foo(x: real);
		begin
			putFloat(x);
		end        """
        expect = """10.010.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

#     def test35(self):
#         input = """
# 		procedure main();
# 		var x: array[-5 .. 5] of integer; y: integer;
# 		begin
# 			x := foo(-3);
# 			putIntLn(x[-3]);
# 			y := 12;
# 			putIntLn(y);
# 		end

# 		function foo(x: integer): array[-5 .. 5] of integer;
# 		var a: array[-5 .. 5] of integer;
# 		begin
# 			a[-3] := 10;
# 			a[x] := a[x] + x*x;
# 			putIntLn(a[-3]);
# 			return a;
# 		end        """
#         expect = """19
# 19
# 12
# """
#         self.assertTrue(TestCodeGen.test(input, expect, 535))


    def test_bin_andthen_36(self):
        input = """

    procedure main();
    
    var a: array [0 .. 10] of real;
    
    begin
        a[0] := 10;

        a[1] := a[0]*10 - 2*a[0] + 100;

        a[2] := a[0] - 2*a[1]/a[0];

        putFloatLn(a[2]);
        putFloatLn(a[1]);
    end
        """
        expect = """-26.0
180.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test37(self):
        input = """

        procedure main();
        var i, max : integer; a: array[0 .. 10] of integer;
        begin
            a[0] := 9;
            a[1] := 3;
            a[2] := 12;
            a[3] := 7;
            a[4] := 43;
            a[5] := 32;
            a[6] := 17;
            a[7] := 4;
            a[8] := -2;
            a[9] := 12;
            a[10] := 9;

            max := a[0];

            for i := 1 to 10 do 
            begin
                if a[i] > max then
                    max := a[i];
            end

            putInt(max);
        end

        """
        expect = """43"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test38(self):
        input = """
        var i: integer;
        procedure main();
        begin
            foo();
            putInt(i);
        end

        procedure foo();
        begin
            i := 100;
        end
        """
        expect = """100"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test39(self):
        input = """
        var x: integer;

        procedure main();
        var n, i, j : integer;
        begin
            n := 10;
            for i := 1 to n do
            begin
                for j := 1 to i do
                    putString("*");
                putLn();
            end
        end

        """
        expect = """*
**
***
****
*****
******
*******
********
*********
**********
"""
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test40(self):
        input = r"""
    procedure main();
        var i, j, n, max, temp : integer; a: array[0 .. 10] of integer;
        begin
            a[0] := 9;
            a[1] := 3;
            a[2] := 12;
            a[3] := 7;
            a[4] := 43;
            a[5] := 32;
            a[6] := 17;
            a[7] := 4;
            a[8] := -2;
            a[9] := 12;
            a[10] := 9;

            n := 10;

        for i := 0 to n do
        begin
            max := i;
            for j := i + 1 to n do
                if a[max] < a[j] then
                    max := j;
            
            temp := a[i];
            a[i] := a[max];
            a[max] := temp;
        end
            
        for i := 0 to n do
        begin
            putInt(a[i]);
            putString("\t");
        end

    end        
        """
        expect = """43	32	17	12	12	9	9	7	4	3	-2	"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test41(self):
        input = """
        var x: integer;
        procedure main();

        begin
            for x := 0 to 0 do
                continue;
            putInt(x);

        end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test42(self):
        input = """
        function fib(x : integer):integer;
        begin
            if (x < 2) then return 1;
            return fib(x-1) + fib(x-2);
        end

        procedure main();
        var x : integer;

        begin
            putInt(fib(5));
        end
        """
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test43(self):
        input = """
        var x: integer;

        var z : array[1 .. 23] of integer;

        procedure main();
        begin
            putInt(foo()[10]);
        end

        function foo(): array[1 .. 23] of integer;
        var x : array[1 .. 23] of integer;
        begin
            x[10] := 100;
            return x;
        end
        """
        expect = """100"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test44(self):
        input = """
        procedure main();
        var x : integer;
        begin
            x := foo()[5];
            putInt(x);
        end

        function foo(): array[1 .. 23] of integer;
        var a: array[1 .. 23] of integer;
        begin
            a[5] := 12;
            return a;
        end
        """
        expect = """12"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test45(self):
        input = """
        procedure main();
        var x : array[1 .. 20] of real;
        begin
            x[5] := 100;
            foo(x);
            putFloat(x[5]);
        end

        procedure foo(a : array[1 .. 20] of real);
        begin 
            a[5] := 200;
            putFloat(a[5]);
        end
        """
        expect = """200.0100.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))


    def test46(self):
        input = """
        procedure main();
        var i, sum: integer; 
        begin

            i := 0;
            sum := 0;

            while i < 100 do begin
                sum := sum +i;
                i := i + 1;
            end

            putInt(sum);

            sum := sum + 100;

            putInt(sum);

        end
        """
        expect = """49505050"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test47(self):
        input = """
        procedure main();
        var i, j: integer;
        begin
            i := 0;
            while i < 10 do begin
                for j := 0 to 10 do begin
                    if j mod 2 = 0 then continue;
                    putIntLn(foo(i, j));
                end
                if i > 2 then break; 
                i := i + 1;
            end
        end

        function foo(i, j: integer): integer;
        begin
            return i*10 + j;
        end
        """
        expect = """1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

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
                putBoolLn(True);
                putIntLn(1);
                putStringLn("ahihi");
            end
            function foo(a: real): real;
            var b: integer;
            begin
                b := 10;
                return a + b;
            end
            """
        expect = "27.45\ntrue\n1\nahihi\n"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

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
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test50(self):
        input = """
        procedure main();
        var X: integer;
        begin
            x := 12;
            putint(X);
            Foo();
        end

        procedure foo();
        begin
            putString("Hello world");
        end
        """
        expect = """12Hello world"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

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
        self.assertTrue(TestCodeGen.test(input, expect, 551))

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
        self.assertTrue(TestCodeGen.test(input, expect, 552))

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
        self.assertTrue(TestCodeGen.test(input, expect, 553))

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
        self.assertTrue(TestCodeGen.test(input, expect, 554))

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
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_bool_ast5(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putbool(a and b and then a and not b and test());
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
        self.assertTrue(TestCodeGen.test(input, expect, 556))

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
        self.assertTrue(TestCodeGen.test(input, expect, 557))

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
        self.assertTrue(TestCodeGen.test(input, expect, 558))

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
        self.assertTrue(TestCodeGen.test(input, expect, 559))

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
        self.assertTrue(TestCodeGen.test(input, expect, 560))

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
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_bool_ast6(self):
            input = '''
            var b:array [1 .. 3] of real;
            procedure main();
            var a,b,i:integer;

            begin
            a:=0;
            for i:=0 to 5 do
                a:=a+1;
            putInt(a);

            end

            '''
            expect = "6"
            self.assertTrue(TestCodeGen.test(input,expect,562))

    def test63(self):
        input = """
     var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-1 .. 5] of integer;
        begin
        a[-1]:=6;
        putInt(a[-1]);
        end

        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test64(self):
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
        expect = """720"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test99(self):
        input = """
        procedure main();
        begin
        end
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
