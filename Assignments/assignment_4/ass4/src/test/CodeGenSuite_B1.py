import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_bool_ast223(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putBool"),[BinaryOp(">=",IntLiteral(1),IntLiteral(2))])])])
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,7))
    def test_bool_ast245(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a:integer;
        b: array [1 .. 4] of integer;
        c:integer;
        d:integer;
        begin
        a:=2;
        c:=3;
        if a>c then
        d:=3;
        else
        d:=4;
        putInt(d);

        end

        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,8))
    def test_bool_ast3(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a,b:integer;
        begin
        a:=2;
        b:=3;
        while a < b do
        a:=a+1;
        putInt(a);

        end

        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,9))

    def test_bool_ast4(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a,b,i:integer;

        begin
        a:=0;
        while True do
        begin
        a:=a+1;
        if a=2 then
        break;
        end
        putInt(a);

        end

        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,10))

    def test_bool_ast5(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a,b,i:integer;

        begin
        a:=0;
        while True do
        begin
        a:=a+1;
        if a=2 then
        break;
        else
        continue;
        end
        putInt(a);

        end

        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,11))
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
    	self.assertTrue(TestCodeGen.test(input,expect,12))
    def test_bool_ast7(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a,b,i:integer;
        begin
        a:=0;
        with a:integer; do
            begin
            a:=5;
            putInt(a);
            end

        end

        '''
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,13))
    def test_bool_ast8(self):
    	input = '''
        var b:array [1 .. 3] of real;
        procedure main();
        var a,b,i:integer;
        begin
        a:=0;
        with a:integer; do
            begin
            a:=5+6*3;
            putInt(a);
            end

        end

        '''
    	expect = "23"
    	self.assertTrue(TestCodeGen.test(input,expect,14))
    def test_bool_ast9(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        a:=2.5+3;
        putFloat(a);

        end

        '''
    	expect = "5.5"
    	self.assertTrue(TestCodeGen.test(input,expect,15))
    def test_bool_ast10(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5.0<>6.0);

        end

        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,16))

    def test_bool_ast11(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5.0=6.0);

        end

        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,17))
    def test_bool_ast12(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5=6.0);

        end

        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,18))
    def test_bool_ast13(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5.5=6);

        end

        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,19))
    def test_bool_ast14(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5.5<>6);

        end

        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,20))

    def test_bool_ast15(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (5<>6.5) then
        i:=1;
        else
        i:=0;
        putInt(i);
        end

        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,21))

    def test_bool_ast16(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        a:=0.0;
        if (a<>5) then
        a:=a+1; 
        putFloat(a);
        end

        '''
    	expect = "1.0"
    	self.assertTrue(TestCodeGen.test(input,expect,22))
    def test_bool_ast17(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        a:=0.0;
        while (a<>5) do
        a:=a+1; 
        putFloat(a);
        end

        '''
    	expect = "5.0"
    	self.assertTrue(TestCodeGen.test(input,expect,23))
    def test_bool_ast18(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        a:=0;
        while (a<>5) do
        a:=a+1; 
        putFloat(a);
        end

        '''
    	expect = "5.0"
    	self.assertTrue(TestCodeGen.test(input,expect,24))

    def test_bool_ast19(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        a:=0;
        while (a=0.0) do
        a:=a+2; 
        putFloat(a);
        end

        '''
    	expect = "2.0"
    	self.assertTrue(TestCodeGen.test(input,expect,25))

    def test_bool_ast20(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        putBool(5>6.0);
        end

        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,26))

    def test_bool_ast21(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (5.0>6.0) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,27))

    def test_bool_ast22(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (5<6.0) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,28))

    def test_bool_ast23(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (5.0<6.0) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,29))
    def test_bool_ast24(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (5.0>=6) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,30))
    def test_bool_ast25(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6.0>=6) and (7>=3.5) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,31))
    def test_bool_ast26(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6.0<=7) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,32))

    def test_bool_ast27(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6<=5.3) and (3.4<=1) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,33))

    def test_bool_ast28(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5.3) or (3.4<=1) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,34))
    def test_bool_ast29(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5.3) and not (3.4<=1) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,35))
    def test_bool_ast30(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5) and not not(-3<=1) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,36))
    def test_bool_ast31(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5) and not not(-3.0<=-1.05) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,37))

    def test_bool_ast32(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5) and not not(-3.0<=-1.05) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,38))

    def test_bool_ast33(self):
    	input = '''
        var b:array [1 .. 3] of real;
        a:real;
        procedure main();
        var i:integer;
        begin
        if (6>=5) and not not(-3<=-1.05) then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,39))
    def test_bool_ast34(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        begin
        a:=true;
        b:=false;
        if a and not b then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,40))
    def test_bool_ast35(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        begin
        a:=true;
        b:=false;
        if a and not not not b then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,41))
    def test_bool_ast36(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        begin
        a:=true and false;
        b:=false;
        if a and not not not b then
        i:=3;
        else
        i:=4;
        putInt(i);
        end
        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,42))

    def test_bool_ast37(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        for i:=2 to 6 do
            i:=i+1;
        putInt(i);
        end
        '''
    	expect = "8"
    	self.assertTrue(TestCodeGen.test(input,expect,43))

    def test_bool_ast38(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        for i:=1 to 6 do
            i:=i+1;
        putInt(i);
        end
        '''
    	expect = "7"
    	self.assertTrue(TestCodeGen.test(input,expect,44))

    def test_bool_ast39(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        for i:=5 downto -1 do
            a:=3;
        putInt(i);
        end
        '''
    	expect = "-2"
    	self.assertTrue(TestCodeGen.test(input,expect,45))

    def test_bool_ast40(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(True and then true);
        end
        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,46))

    def test_bool_ast41(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(True and then false);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,47))

    def test_bool_ast42(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(true and then true and then false);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,48))

    def test_bool_ast43(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(true and then false and then true);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,49))

    def test_bool_ast44(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(false and then 0 div 0 = 1);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,50))
    def test_bool_ast45(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(false and then 0 div 0 = 1);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,51))

    def test_bool_ast46(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(false and then 0 div 0 = 1);
        end
        '''
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,52))
    def test_bool_ast47(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        if (false and then 0 div 0 = 1) then 
        a:=1;
        else
        a:=2;
        putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,53))

    def test_bool_ast48(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        if (true and then true) then 
        a:=1;
        else
        a:=2;
        putInt(a);
        end
        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,54))

    def test_bool_ast49(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(true or else true);
        end
        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,55))

    def test_bool_ast50(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(false or else true);
        end
        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,56))

    def test_bool_ast51(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(false or else true or else false);
        end
        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,57))

    def test_bool_ast52(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        putBool(true or else 0 div 0=1);
        end
        '''
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,58))

    def test_bool_ast53(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        if (true or else 0 div 0=1) then
        a:=2;
        else
        a:=3;
        putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,59))

    def test_bool_ast54(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        d:=true;
        b:=false;
        if (d or else not b) then
        a:=2;
        else
        a:=3;
        putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,60))

    def test_bool_ast55(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        d:=true;
        b:=false;
        if (d or else 0 div 0=1) then
        a:=2;
        else
        a:=3;
        putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,61))

    def test_bool_ast56(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        with c:integer; do
            putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,62))

    def test_bool_ast57(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        with c:integer; do
            a:=3;
        putInt(a);
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,63))


    def test_bool_ast58(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2+foo();

        putInt(a);
        end
        function foo():integer;
        begin
        return 1;
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,64))

    def test_bool_ast573(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=2;
        with a,c:integer; do
            a:=3;
        putInt(a);
        end
        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,65))
    def test_bool_ast581(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=foo(3);
        putInt(a);
        end

        function foo(n:integer):integer;
        var result:integer;
        begin
        return n;
        end
        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,66))

    def test_bool_ast59(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=0;
        while true do
        if true then
        break;
        else
        a:=1;
        
        putInt(a);
        end
        '''
    	expect = "0"
    	self.assertTrue(TestCodeGen.test(input,expect,67))

    def test_bool_ast60(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=foo(3);
        putInt(a);
        end


        function foo(n:integer):integer;
        begin
        if n<=1 then
        return 1;
        else
        return n*foo(n-1);
        end
        '''
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,68))

    def test_bool_ast61(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a:integer;
        begin
        a:=1;
        while true do 
        if true then
        begin
        a:=a+1;
        break;
        end
        else
        break;
        
        putInt(a);
        end


        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,69))

    def test_bool_ast62(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [0 .. 4] of integer;
        begin
        a[3]:=4;
        a[2]:=1;
        putInt(a[2]);
        end


        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,70))

    def test_bool_ast63(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-5 .. 1] of integer;
        begin
        a[-1]:=4;
        a[-4]:=1;
        putInt(a[-4]);
        end


        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,71))

    def test_bool_ast64(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-5 .. 1] of integer;
        begin
        a[1]:=5;
        
        putInt(a[1]);
        end


        '''
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,72))

    def test_bool_ast65(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-5 .. -1] of integer;
        begin
        a[-4]:=1;
        putInt(a[-4]);
        end


        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,73))

    def test_bool_ast66(self):
    	input = '''
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


        '''
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,74))
    def test_bool_ast67(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-1 .. 5] of integer;
        begin
        e:=6;
        putInt(e);
        end


        '''
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,75))

    def test_bool_ast68(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-1 .. 5] of integer;
        begin
        a[4]:=2;
        a[4]:=a[4]+2;
        putInt(a[4]);
        end


        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,76))

    def test_bool_ast69(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-1 .. 5] of integer;
        begin
        c[3]:=4.5;
        putFloat(c[3]);
        end


        '''
    	expect = "4.5"
    	self.assertTrue(TestCodeGen.test(input,expect,77))

    def test_bool_ast70(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        var b:boolean;
        d:boolean;
        i:integer;
        a: array [-1 .. 5] of integer;
        begin
        c[3]:=4.5;
        c[3]:=c[3]+c[3];
        putFloat(c[3]);
        end


        '''
    	expect = "9.0"
    	self.assertTrue(TestCodeGen.test(input,expect,78))

    def test_bool_ast71(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        begin
        e:=foo()[2];
        putInt(e);
        end

        function foo(): array [1 .. 3] of integer;
        var result:array [1 .. 3] of integer;
        begin
        result[2]:=4;
        return result;
        end


        '''
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,79))

    def test_bool_ast72(self):
    	input = '''
        var c:array [1 .. 3] of real;
        a:boolean;
        e:integer;
        procedure main();
        begin
        e:=3;
        foo(e);
        putInt(e);
        end

        procedure foo(a:integer);
        begin
        a:=a+1;
        end


        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,80))

    def test_bool_ast73(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        begin
        e:=3;
        foo();
        putInt(e);
        end

        function foo():string;
        
        begin
        return "thay Phung dep trai";
        end


        '''
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,81))

    def test_bool_ast74(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        begin
        putString("thay phung dep trai");
        end



        '''
    	expect = "thay phung dep trai"
    	self.assertTrue(TestCodeGen.test(input,expect,82))

    def test_bool_ast75(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        var a,b:integer;
        begin
        a:=2;
        with a,c:integer; do 
            with d,e:integer; do
                a:=1;
        putInt(a);
        end



        '''
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,83))

    def test_bool_ast76(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        var a,b:integer;
        begin
        putString(foo(1,2,3,4,5.5,"abc"));
        end

        function foo(a,b,c,d:integer;e:real;f:string):string;
        
        begin
        return "thay Phung dep trai";
        end

        '''
    	expect = "thay Phung dep trai"
    	self.assertTrue(TestCodeGen.test(input,expect,84))

    def test_bool_ast77(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        var a,b:integer;
        begin
        a:=1;
        putInt(a);
        end

        function foo(a,b,c,d:integer;e:real;f:string):array [1 ..3] of string;
        var result:array [1 .. 3] of string;
        begin
        return result;
        end

        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,85))

    def test_bool_ast78(self):
    	input = '''
        var c:array [1 .. 3] of string;
        a:boolean;
        e:integer;
        procedure main();
        var a,b:integer;
        begin
        a:=1;
        putInt(a);
        end

        function foo(a,b,c,d:integer;e:real;f:string):array [1 ..3] of integer;
        var result:array [1 .. 3] of integer;
        begin
        return result;
        end

        '''
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,86))

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
        self.assertTrue(TestCodeGen.test(input, expect, 87))

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
        self.assertTrue(TestCodeGen.test(input, expect, 88))

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
        self.assertTrue(TestCodeGen.test(input, expect, 89))

    def test_bool_ast5433(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 90))

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
        self.assertTrue(TestCodeGen.test(input, expect, 91))

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
        self.assertTrue(TestCodeGen.test(input, expect, 92))

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
        self.assertTrue(TestCodeGen.test(input, expect, 93))

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
        self.assertTrue(TestCodeGen.test(input, expect, 94))

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
        self.assertTrue(TestCodeGen.test(input, expect, 95))

    def test_bool_ast5699(self):
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
            self.assertTrue(TestCodeGen.test(input,expect,96))

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
        self.assertTrue(TestCodeGen.test(input, expect, 97))

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
        self.assertTrue(TestCodeGen.test(input, expect, 98))

    def test99(self):
        input = """
        procedure main();
        begin
        putInt(1);
        end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 99))

    def test911(self):
        input = """
        procedure main();
        begin
        putFloat(1.0);
        end
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 100))
    def test912(self):
        input = """
        procedure main();
        begin
        putint(5);
        end
        """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input, expect, 1))
    def test913(self):
        input = """
        procedure main();
        begin
        putint(6);
        end
        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 2))
    def test914(self):
        input = """
        procedure main();
        begin
        putint(7);
        end
        """
        expect = """7"""
        self.assertTrue(TestCodeGen.test(input, expect, 3))
    def test915(self):
        input = """
        procedure main();
        begin
        putint(8);
        end
        """
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input, expect, 4))
    def test916(self):
        input = """
        procedure main();
        begin
        putint(9);
        end
        """
        expect = """9"""
        self.assertTrue(TestCodeGen.test(input, expect, 5))
    def test919(self):
        input = """
        procedure main();
        begin
        putint(10);
        end
        """
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input, expect, 6))
    def test999(self):
        input = """
        procedure main();
        begin
        putint(11);
        end
        """
        expect = """11"""
        self.assertTrue(TestCodeGen.test(input, expect, 8))

