import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):

    def test_int(self):
        input = """
        procedure main();
        var a:integer;
        begin
        a := 1;
        putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_03(self):
        input = """
        procedure main();
        begin
        putFloat(100.02);
        end
        """
        expect = "100.02"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_04(self):
        input = """
        procedure main();
        begin
        putFloat(1.4315E7);
        end
        """
        expect = "1.4315E7"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_05(self):
        input = """
        procedure main();
        begin
        putFloat(121.5E5);
        end
        """
        expect = "1.215E7"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_06(self):
        input = """
        procedure main();
        begin
            if (true)
                then putInt(1);
                else putInt(2);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_07(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := 4;
            putFloatLn(foo(a));
        end
        function foo(a:integer):real;
        var foo:integer;
        begin
            foo := 5;
            return foo + a;
        end 
        """
        expect = """9.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_08(self):
        input = """
        procedure main();
        begin
            putIntLn(000);
        end
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_09(self):
        input = """        
        procedure main();
        begin
            putFloatLn(1.0);
        end"""
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_10(self):
        input = """
        procedure main();
        begin
            putFloatLn(10.5);
        end
        """
        expect = "10.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_11(self):
        input = """
        procedure main();
        begin
            putFloatLn(100.14);
        end
        """
        expect = "100.14\n"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_12(self):
        input = """
        procedure main();
        begin
            putBoolLn(true);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_13(self):
        input = """
        procedure main();
        begin
            putStringLn("programming");
        end
        """
        expect = "programming\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
        input = """
        var a:integer;
        var b:real;
        procedure main();
        begin
            a := 10;
            b := 1.0;
            putInt(a);
        end
        var c:boolean;
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_15(self):
        input =  """
        var a:array[1 .. 5] of integer;
        procedure main();
        begin
            putInt(10);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,515))
        
    def test_16(self):
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        begin
            putInt(10);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_17(self):
        """Program => Test global variable and function whose return type is voidtype."""
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        begin
            putInt(10);
        end
        
        procedure pvoid();
        begin
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_18(self):
        """Program => Main function: declared variable primitive type"""
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        var a:integer;
            b:real;
        begin
            putInt(10);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,518))


    def test_19(self):
        """Program => Main function: It's declared variable primitive and array type"""
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
        begin
            putInt(10);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_20(self):
        """Program => funcVoid function: It's declared variable primitive type in parameter and body"""
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
        begin
            putInt(10);
        end
        
        procedure pvoid();
        var c:integer;
            c, e, f:real;
        begin
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,520))
        
    def test_21(self):
        """Program => funcVoid function: It's declared variable primitive and array type in parameter and body"""
        input = """
        var a:integer;
            b:real;
            frr:array[1 .. 4] of real;
            arr:array[1 .. 5] of integer;
        procedure main();
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
        begin
            putInt(10);
        end
        
        procedure pvoid();
        var c:integer;
            c, e, f:real;
            funcFrr:array[1 .. 10] of real;
        begin
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_22(self):
        """Program => manipulate data in Main function: simple assign the IntLiteral value to global variable IntType."""
        input = """
        var a:integer;
            arr:array[1 .. 5] of integer;
        
        procedure main();
        begin
            a := 1;
            putIntLn(a);
        end
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_23(self):
        """Program => manipulate data in Main function: simple assign the FloatLiteral value to global variable FloatType."""
        input = """
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
        
        procedure main();
        begin
            b := 10.5;
            putFloatLn(b);
        end
        """
        expect = "10.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_24(self):
        """Program => manipulate data in Main function: simple assign the BoolLiteral value to global variable BoolType."""
        input = """
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
            isTrue:boolean;
        procedure main();
        begin
            isTrue := false;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_25(self):
        """Program => manipulate data in Main function: simple assign the StringLiteral value to global variable StringType."""
        input = """
        var a:integer;
            b:real;
            arr:array[1 .. 5] of integer;
            isTrue:boolean;
        procedure main();
        begin
            putStringLn("testString");
        end
        """
        expect = "testString\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))
        
    def test_26(self):
        """rogram => manipulate data in Main function: simple assign the IntLiteral value to global variable ArrayType(IntType)."""
        input = """
        var arr:array[1 .. 5] of integer;
        procedure main();
        begin
            arr[1] := 15;
            putIntLn(arr[1]);
        end
        """
        expect = "15\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_27(self):
        """Program => manipulate data in Main function: simple assign the FloatLiteral value to global variable ArrayType(FloatType)"""
        input = """
        var arr:array[1 .. 5] of integer;
            frr:array[1 .. 4] of real;
        procedure main();
        begin
            frr[1] := 14.3;
            putFloatLn(frr[1]);
        end
        """
        expect = "14.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_29(self):
        """Program => manipulate data in Main function: simple assign the BoolLiteral value to global variable ArrayType(BoolType)."""
        input = """
        var arr:array[1 .. 5] of integer;
            brr:array[1 .. 4] of boolean;
        procedure main();
        begin
            brr[1] := false;
            putBoolLn(brr[1]);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_30(self):
        """Program => manipulate data in Main function: simple assign the IntLiteral value to local variable IntType."""
        input = """
        var a, b:integer;
        procedure main();
        var iNum:integer;
        begin
            iNum := 9;
            putInt(iNum);
        end
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,530))
        
    def test_31(self):
        """Program => manipulate data in Main function: simple assign the FloatLiteral value to local variable FloatType."""
        input = """
        var a, b:integer;
        procedure main();
        var fNum:real;
        begin
            fNum := 9.15;
            putFloat(fNum);
        end
        """
        expect = "9.15"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_32(self):
        """Program => manipulate data in Main function: simple assign the BoolLiteral value to local variable BoolType."""
        input = """
        var a, b:integer;
        procedure main();
        var isTrue:boolean;
        begin
            isTrue := true;
            putBool(isTrue);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_34(self):
        """Program => manipulate data in Main function: simple assign the IntLiteral value to local variable ArrayType(IntType)."""
        input = """
        var a, b:integer;
        procedure main();
        var arr:array[1 .. 5] of integer;
        begin
            arr[1] := 111;
            putInt(arr[1]);
        end
        """
        expect = "111"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_35(self):
        """Program => manipulate data in Main function: simple assign the FloatLiteral value to local variable ArrayType(FloatType)."""
        input = """
        var a, b:integer;
        procedure main();
        var arr:array[1 .. 5] of real;
        begin
            arr[1] := 111.2;
            putFloat(arr[1]);
        end
        """
        expect = "111.2"
        self.assertTrue(TestCodeGen.test(input,expect,535))
        
    def test_36(self):
        """Program => manipulate data in Main function: Assign the int value to local variable FloatType (have coercion)."""
        input = """
        var a, b:integer;
        procedure main();
        var fNum:real;
        begin
            fNum := 19;
            putFloat(fNum);
        end
        """
        expect = "19.0"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_37(self):
        """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type: IntType"""
        input = """
        var a, b:integer;
        procedure main();
        var iNum:integer;
        begin
            a := -1;
            iNum := a;
            putInt(iNum);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_38(self):
        """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type - FloatType"""
        input = """
        var a, b:real;
        procedure main();
        var fNum:real;
        begin
            a := 11.5;
            fNum := a;
            putFloat(fNum);
        end
        """
        expect = "11.5"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_40(self):
        """Program => manipulate data in Main function: Assign var to var (global & local), coercion int to float"""
        input = """
        var fNum:real;
        procedure main();
        var iNum:integer;
        begin
            iNum := 14;
            fNum := iNum;
            putFloat(fNum);
        end
        """
        expect = "14.0"
        self.assertTrue(TestCodeGen.test(input,expect,540))
        
    def test_41(self):
        """Program => manipulate data in Main function: Assign recur 2 times: true and false"""
        input = """
        var fNum:real;
        procedure main();
        var isT, isTrue:boolean;
        begin
            isT := false;
            isTrue := true;
            isT := isTrue;
            putBool(isT);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_43(self):
        """Program => manipulate data in Main function: Assign recur 2 times: Arraytype and primitiveType"""
        input = """
        procedure main();
        var arr:array[1 .. 4] of integer;
        begin
            arr[1] := 1;
            arr[2] := 2;
            arr[3] := 3;
            putInt(arr[2]);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_44(self):
        """Program => manipulate data in Main function: Assign recur many times: Arraytype and primitiveType"""
        input = """
        var fNum:real;
        procedure main();
        var arr:array[1 .. 4] of integer;
            a, b:integer;
        begin
            b := 10;
            a := b;
            arr[1] := a;
            b := a;
            arr[1] := b;
            arr[2] := arr[1];
            arr[1] := 18;
            a := arr[1];
            arr[3] := a;
            putIntLn(arr[3]);
        end
        """
        expect = "18\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_45(self):
        """Program => manipulate data in Main function: Assign recur many times: It's has coercion!"""
        input = """
        var fNum:real;
        procedure main();
        var arr:array[1 .. 4] of integer;
            a, b:integer;
            f:real;
        begin
            b := 10;
            a := b;
            fNum := a;
            arr[2] := a;
            f := arr[1];
            b := a;
            arr[2] := b;
            arr[3] := arr[2];
            fNum := arr[3];
            putFloatLn(fNum);
        end
        """
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_46(self):
        """Program => manipulate data in Main function: Assign recur many times: It's has complex coercion!"""
        input = """
        var a, b:integer;
            gArr:array[1 .. 4] of integer;
        procedure main();
        var arr:array[1 .. 4] of integer;
            c, d:integer;
        begin
            a := 1;
            b := a := 1;
            c := a;
            b := a := c := b;
            gArr[1] := arr[1] := 1;
            gArr[2] := gArr[1] := 11;
            d := gArr[2] := arr[4] := gArr[1] := a := gArr[3] := b := 11;
            putIntLn(gArr[2]);
        end
        """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_47(self):
        """Program => manipulate data in Main function: Assign recur many times type array type and primitive type of FloatType (coercion)"""
        input = """
        var a, b:real;
            gArr:array[1 .. 4] of real;
        procedure main();
        var arr:array[1 .. 4] of integer;
            c, d:integer;
        begin
            c := 1;
            c := d := 3;
            a := c;
            b := d := 4;
            arr[1] := 5;
            gArr[1] := arr[1] := 11;
            gArr[2] := gArr[3] := arr[3] := c;
            putFloatLn(gArr[3]);
        end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_48(self):
        """Program => manipulate data in Main function: Assign recur many times type array type and primitive type of BooleanType"""
        input = """
        var a, b:boolean;
            gArr:array[1 .. 4] of boolean;
        procedure main();
        var arr:array[1 .. 4] of boolean;
            c, d:boolean;
        begin
            c := true;
            c := d := false;
            a := c;
            b := d := false;
            arr[1] := true;
            gArr[1] := arr[1] := true;
            gArr[2] := gArr[3] := arr[3] := d;
            putBoolLn(gArr[2]);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_50(self):
        """Program => manipulate data in Main function: Expression : Operator are add, minus; operand are array cell, literal in"""
        input = """
        var a, b, c:integer;
            arr:array[1 .. 3] of integer;
        procedure main();
        var iNum, i, j:integer;
        begin
            arr[1] := 0;
            arr[2] := 1;
            arr[3] := 2;
            a := 3;
            b := a + 2;
            c := b + a + 3;
            iNum := arr[1] + c + (arr[2] - b) - (arr[3] - arr[1]);
            i := iNum - arr[1] + arr[2] - arr[3] - c;
            j := iNum - i + 11;
            putIntLn(j);
        end
        """
        expect = "23\n"
        self.assertTrue(TestCodeGen.test(input,expect,550))
        
    def test_51(self):
        """Program => manipulate data in Main function: Expression : Operator are add, minus; operand are array cell, literal :float and int"""
        input = """
        var a,b,c:integer;
            arr:array[1 .. 3] of integer;
            fa,fb,fc:real;
            frr:array[1 .. 4] of real;
        procedure main();
        var fNum:real;
        begin
            arr[1] := arr[2] := arr[3] := 3;
            a := 3;
            b := a + 2;
            c := b + a + 3;
            fNum := a + b + arr[1] - 1;
            fa := fNum + c;
            fb := fa + a;
            fc := fb + b;
            frr[1] := fa + fb + fc;
            frr[2] := frr[1] + a + b +c;
            putFloatLn(frr[2]);
        end
        """
        expect = "93.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_52(self):
        """Program => manipulate data in Main function: Expression : Operator are add, minus, mul; operand are array cell, literal :float and int"""
        input = """
        var a,b,c:integer;
            arr:array[1 .. 3] of integer;
            fa,fb,fc:real;
            frr:array[1 .. 4] of real;
        procedure main();
        var fNum:real;
        begin
            arr[1] := arr[2] := arr[3] := 3;
            a := 3*5;
            b := a + 2;
            c := b + a * 3;
            fNum := a + b + arr[1] * 4;
            fa := fNum + c * arr[1];
            fb := fa + a * arr[2];
            fc := fb + b * arr[3]+ fNum * a;
            frr[1] := fa * a + fb * b + fc * c;
            frr[2] := frr[1] + a * b * c;
            putFloatLn(frr[2]);
        end
        """
        expect = "85067.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,552))
        
    def test_53(self):
        """Program => manipulate data in Main function: Expression : Operator are add, minus, mul, div; operand are array cell, literal :float and int"""
        input = """
        var a,b,c:integer;
            arr:array[1 .. 3] of integer;
            fa,fb,fc:real;
            frr:array[1 .. 4] of real;
        procedure main();
        var fNum:real;
        begin
            arr[1] := arr[2] := arr[3] := 3;
            a := 3 * 5;
            b := a div 2;
            c := b + a * 3;
            fNum := a + b / arr[1] + arr[1]*4;
            fa := fNum / arr[1] + c * arr[1];
            fb := fa + a * arr[2] + a / arr[1];
            fc := fb + b * arr[3]+ fNum * a + fNum / (arr[1] + a);
            frr[1] := fa * a + fb / b + fc / c;
            frr[2] := frr[1] + a * b / c;
            putFloatLn(frr[2]);
        end
        """
        expect = "2532.5576\n"
        self.assertTrue(TestCodeGen.test(input,expect,553))
        
    def test_54(self):
        """Program => manipulate data in Main function: Expression : Operator is Modulus; operand are array cell, literal : int"""
        input = """
        var a, b, c:integer;
            arr:array[1 .. 3] of integer;
        procedure main();
        begin
            arr[1] := arr[2] := arr[3] := 3;
            b := 10 div arr[1];
            putIntLn(arr[3]);
        end
        """
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_55(self):
        """Program => manipulate data in Main function: Expression : Operator is Modulus; operand are array cell, literal : int"""
        input = """
        var a, b, c:integer;
            arr:array[1 .. 3] of integer;
        procedure main();
        begin
            arr[1] := arr[2] := arr[3] := 3;
            a := 19;
            b := a + a div arr[1];
            c := b div a + arr[1] * arr[2];
            arr[3] := (c * a) div b;
            putIntLn(arr[3]);
        end
        """
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input,expect,555))
        
    def test_56(self):
        """Program => manipulate data in Main function: UniryOp : Operator is Negative; operand is boolLiteral"""
        input = """
        var isTrue:boolean;
            arr:array[1 .. 4] of boolean;
        procedure main();
        var isT, isF:boolean;
        begin
            arr[1] := arr[2] := arr[3] := false;
            isT := not arr[1];
            isF := not (not arr[2]);
            isTrue := not not not not not not isF;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_57(self):
        """Program => manipulate data in Main function: UniryOp : Operator is Minus; operand is IntLiteral"""
        input = """
        var arr:array[1 .. 4] of integer;
        procedure main();
        var iNum, i, j:integer;
        begin
            arr[1] := arr[2] := arr[3] := 10;
            i := -arr[1];
            j := -arr[2];
            iNum := i + j;
            putIntLn(iNum);
        end
        """
        expect = "-20\n"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_58(self):
        """Program => manipulate data in Main function: UniryOp : Operator is Minus; operand is FloatLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var fNum, i, j:real;
        begin
            arr[1] := arr[2] := 11.5;
            arr[3] := 8.5;
            i := -arr[1] + -arr[2];
            j := -arr[3]*3;
            fNum := i + j;
            putFloatLn(fNum);
        end
        """
        expect = "-48.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,558))
        
    def test_59(self):
        """Program => manipulate data in Main function: Operator are < ; operand is IntLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var a, b:integer;
            isTrue:boolean;
        begin
            a := 10;
            b := 11;
            isTrue := a > b ;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_60(self):
        """Program => manipulate data in Main function: Operator are <= ; operand is FloatLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var a:real;
            b:integer;
            isTrue:boolean;
        begin
            a := 11.0;
            b := 11;
            isTrue := a <= b ;
            putBoolLn(isTrue);
        end"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,560))
        
    def test_61(self):
        """Program => manipulate data in Main function: Operator are > ; operand is IntLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var a:array[1 .. 4] of integer; 
            b:integer;
            isTrue:boolean;
        begin
            arr[1] := 11;
            arr[2] := arr[1] + 2;
            isTrue := arr[2] > 12 ;
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_62(self):
        """Program => manipulate data in Main function: Operator are >= ; operand is FloatLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var arr:array[1 .. 4] of real;
            b:real;
            isTrue:boolean;
        begin
            arr[1] := 11.5;
            arr[2] := arr[1] + 2.5;
            isTrue := arr[2] >= 14.0 ;
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_63(self):
        """Program => manipulate data in Main function: Operator are == ; operand is IntLiteral"""
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var isTrue:boolean;
            a, b:integer;
            arr:array[1 .. 2] of integer;
        begin
            isTrue := false;
            a := 14;
            b := 12;
            arr[1] := 14;
            isTrue := arr[1] = a;
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_64(self):
        """Program => manipulate data in Main function: Operator are == ; operand is BoolLiteral"""
        input = """
        procedure main();
        var arr:array[1 .. 2] of boolean;
            a, isTrue:boolean;
        begin
            a := false;
            arr[1] := not a;
            isTrue := arr[1] = not a;
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_65(self):
        """Program => manipulate data in Main function: Operator are != ; operand is IntLiteral"""
        input = """
        procedure main();
        var a, b:integer;
            isTrue:boolean;
            arr:array[1 .. 2] of integer;
        begin
            a := 10;
            b := 11;
            arr[1] := b mod a + a;
            arr[2] := a mod b + b;
            isTrue := arr[2] <> arr[1];
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,565))
        
    def test_66(self):
        """Program => manipulate data in Main function: Operator are != ; operand is BoolLiteral"""
        input = """
        procedure main();
        var a, b, isTrue:boolean;
            arr:array[1 .. 3] of boolean;
        begin
            a := true;
            b := not true;
            arr[1] := not not a;
            arr[2] := not b;
            isTrue := arr[1] <> not arr[2];
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_67(self):
        """Program => manipulate data in Main function: Operator are && ; operand is BoolLiteral"""
        input = """
        procedure main();
        var a, b, isTrue:boolean;
            arr:array[1 .. 3] of boolean;
        begin
            a := true;
            b := not true;
            arr[1] := not not a;
            arr[2] := not b;
            isTrue := arr[1] and arr[2];
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_68(self):
        """Program => manipulate data in Main function: Operator are || ; operand is BoolLiteral"""
        input = """
        procedure main();
        var a, b, isTrue:boolean;
            arr:array[1 .. 3] of boolean;
        begin
            a := true;
            b := not true;
            arr[1] := not not a;
            arr[2] := not b;
            isTrue := arr[1] or not arr[2];
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_73(self):
        """Program => manipulate data in Main function: Combine operator: +,/,%,<,>,<=,>="""
        input = """
        var a,b,c:integer;
            fa,fb,fc:real;
        procedure main();
        var isTrue:boolean;
        begin
            a := 1;
            b := a + 1;
            c := b mod 1;
            fa := (a + b) div (c + a);
            fb := (fa + a) / (c + b);
            fc := fa * fb / c;
            isTrue := fa <= fb;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,573))
        
    def test_74(self):
        """Program => manipulate data in Main function: Combine operator: +,-,*,/,%,<,>,<=,>=, ==, !="""
        input = """
        var a,b,c:integer;
            fa,fb,fc:real;
        procedure main();
        var isTrue, isT, isF:boolean;
        begin
            a := 10;
            b := a * 2;
            c := b div 7;
            fa := (a * b) - (c div a);
            fb := a * (fa + a) * (c - b);
            fc := fa * fb / c;
            isT := fa < fc;
            isF := fb >= fa;
            isTrue := isT=isF;
            putBoolLn(isTrue);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        """Program => manipulate data in Main function: Combine operator: +,-,*,/,%,<,>,<=,>=, ==, !=, &&, ||"""
        input = """
        var a,b,c:integer;
            fa,fb,fc:real;
        procedure main();
        var arr:array[1 .. 3] of integer;
            isTrue, isT, isF:boolean;
        begin
            a := 10;
            b := a * 2;
            c := b div 7;
            arr[1] := c + b div 2;
            arr[2] := a div 2 + c div 3;
            arr[3] := b * a div 4 + c div 4;
            fa := (arr[1] * b div a) - (c * arr[3] - arr[2]);
            fb := a * (fa + arr[3]) * (c - arr[2]);
            fc := fa * fb / arr[2];
            isT := fa < fc;
            isF := fb >= fa;
            isTrue := isT or isF and ((a + 3) < 17) or ((a + 7) <> 19) and ((arr[3] + c) <> 11);
            putInt(arr[2]);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_76(self):
        """Program => manipulate data in Main function: if no else stmt"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            if a > 1
                then a := 10;
            putIntLn(a);
        end
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
        """Program => manipulate data in Main function: return stmt"""
        input = """
        procedure main();
        var a:real;
        begin
            a := ax(2);
            putFloat(a);
        end
        
        function ax(a:integer):real;
        begin
            if a=2
                then return 1.2;
                else return 2.0;
        end
        """
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_78(self):
        """Program => manipulate data in Main function: return void stmt"""
        input = """
        procedure main();
        begin
            foo(10);
        end
        
        procedure foo(a:integer);
        begin
            if a > 1
                then return;
                else
                    begin
                        a := a + 2;
                        return;
                    end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
        """Program => manipulate data in Main function:another return void stmt and print Int"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            test(a);
        end
        
        procedure test(a:integer);
        begin
            putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_80(self):
        """Program => manipulate data in Main function: if-else stmt simple!(enter thenStmt)"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 1
                then a := 10;
                else a := 11;
            putInt(a);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,580))
        
    def test_81(self):
        """Program => manipulate data in Main function: if-else stmt simple!(enter elseStmt)"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5
                then a := 10;
                else a := 11;
            putInt(a);
        end
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_82(self):
        """Program => manipulate data in Main function: if no else stmt inner if-else stmt"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5 
            then
                if a mod 2=0
                then 
                    a := a * 2;
                else
                    begin
                    end
            else 
            begin
                a := 11;
                if a mod 3 <> 0 then a := a * 3;
            end
            putInt(a);
        end
        """
        expect = "33"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_83(self):
        """Program => manipulate data in Main function: if-else stmt inner if-else stmt"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5 then
                if a mod 2=0 then
                    a := a * 2;
                else
                begin
                end
            else begin
                a := 11;
                if a mod 3 <> 0 then
                    a := a * 3 div 2;
            end
            putInt(a);
        end
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_84(self):
        """Program => manipulate data in Main function: dowhile stmt simple!"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            while a < 5 do
            begin
                putInt(a);
                a := a + 1;
            end
        end
        """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_85(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It has continue stmt!"""
        input = """
        procedure main();
        var a, iSum:integer;
        begin
            a := 0;
            iSum := 0;
            while a < 20 do
            begin
                a := a + 1;
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
    def test_86(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It has break stmt!"""
        input = """
        procedure main();
        var a, iSum:integer;
        begin
            a := 0;
            iSum := 0;
            while a < 20 do
            begin
                a := a + 1;
                if a > 17 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "153"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_87(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It have continue stmt & break stmt!"""
        input = """
        procedure main();
        var a, iSum:integer;
        begin
            a := 0;
            iSum := 0;
            while a < 20 do
            begin
                a := a + 1;
                if a > 17 then break;
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "81"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_88(self):
        """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt!"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            a := b := iSum := 0;
            while a < 20 do
            begin
                b := 0;
                a := a + 1;
                while b < a do
                begin
                    b := b + 1;
                    iSum := iSum + b;
                end
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "1750"
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_89(self):
        """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt complex: It have break and continue stmt!"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            a := b := iSum := 0;
            while a < 20 do
            begin
                b := 0;
                a := a + 1;
                while b < a do
                begin
                    b := b + 1;
                    if b > 10 then break;
                    if b mod 2=1 then continue;
                    iSum := iSum + b;
                end
                if a mod b=0 then continue;
                if a + b > 40 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "554"
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_90(self):
        """Program => manipulate data in Main function: for stmt simple"""
        input = """
        procedure main();
        var a:integer;
        begin
            for a := 0 to 10 do
            begin
                putInt(a);
                break;
            end
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,590))
        
    def test_91(self):
        """Program => manipulate data in Main function: for stmt simple: It has continue stmt"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_92(self):
        """Program => manipulate data in Main function: for stmt simple: It has break stmt"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if iSum > 27 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "28"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_93(self):
        """Program => manipulate data in Main function: for stmt simple: It have continue stmt and break stmt"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if iSum > 27 then break;
                if a mod 3=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "27"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_94(self):
        """Program => manipulate data in Main function: for stmt innner for stmt: It have continue stmt and break stmt"""
        input = """procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                for b := 0 to a - 1 do
                begin
                    if a + b > 17 then break;
                    if b mod 2=0 then continue;
                    iSum := iSum + b;
                end
                if iSum > 27 then break;
                if a mod 3 <> 0 then continue;
                iSum := iSum + a;
            end
            putIntLn(iSum);
        end
        """
        expect = "37\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_95(self):
        """Program => manipulate data in Main function: block inner main block"""
        input = """
        var i, j:integer;
        procedure main();
        var a, b, iSum:integer;
        begin
            i := 10;
            with i:real; do
            begin
                i := 11.8;
                putFloat(i);
            end
            i := 11;
            putIntLn(i);
        end
        """
        expect = "11.811\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_96(self):
        """Program => manipulate data in Main function: block inner block"""
        input = """
        var i, j:integer;
        procedure main();
        var a, b, iSum:integer;
        begin
            i := 10;
            with i:real; do
            begin
                i := 14.3;
                with i:integer; do
                begin
                    i := 19;
                    putInt(i);
                end
                putFloat(i);
            end
            putInt(i);
        end
        """
        expect = "1914.310" 
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_97(self):
        """Program => Funcall is stmt in main function"""
        input = """
        var a:integer;
        procedure main();
        var b:integer;
            c:real;
        begin
            b := 5;
            c := foo(b);
            putFloat(c);
        end
        
        function foo(a:integer):integer;
        begin
            return a * a;
        end
        """
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input,expect,597))


    def test_99(self):
        """Program => Funcall is expression in BinaryOp in main function - return type of Function is ArrayPointerType - FloatType"""
        input = """
        procedure main();
        var arr:array[1 .. 3] of real;
        begin
            arr[3] := 1.5;
            arr[3] := foo(arr)[3] + 1.1;
            putFloatLn(arr[3]);
        end
        
        function foo(x:array[1 .. 3] of real):array[1 .. 3] of real;
        begin
            x[3] := 5.1;
            return x;
        end
        """
        expect = "6.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,599))

    def test_101(self):
        """Program => return stmt in if-else stmt in function call"""
        input = """
        procedure main();
        var a, b, res:integer;
        begin
            a := 1;
            b := 1;
            res := foo(a, b);
            putIntLn(res);
        end
        
        function foo(a:integer; b:integer):integer;
        begin
            if a=b
                then return 111;
                else return 222;
        end
        """
        expect = "111\n"
        self.assertTrue(TestCodeGen.test(input,expect,601))