import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 101))


    def test_2(self):
        input = r"""

procedure main(); 
begin 
    putIntLn(1);
end

"""
        expect = r"""1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 102))


    def test_3(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.5);
end

"""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 103))


    def test_4(self):
        input = r"""

procedure main(); 
begin 
    putFloat(0.5);
end

"""
        expect = r"""0.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 104))


    def test_5(self):
        input = r"""

procedure main(); 
begin 
    putFloat(0.005);
end

"""
        expect = r"""0.005"""
        self.assertTrue(TestCodeGen.test(input, expect, 105))


    def test_6(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1000.0001);
end

"""
        expect = r"""1000.0001"""
        self.assertTrue(TestCodeGen.test(input, expect, 106))


    def test_7(self):
        input = r"""

procedure main(); 
begin 
    putFloatLn(999.8999999);
end

"""
        expect = r"""999.9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 107))


    def test_8(self):
        input = r"""

procedure main(); 
begin 
    putBool(True);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 108))


    def test_9(self):
        input = r"""

procedure main(); 
begin 
    putBool(falSE);
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 109))


    def test_10(self):
        input = r"""

procedure main(); 
begin 
    putBoolLn(FalSE);
end

"""
        expect = r"""false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 110))


    def test_11(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2);
end

"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 111))


    def test_12(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2+3+4+5);
end

"""
        expect = r"""15"""
        self.assertTrue(TestCodeGen.test(input, expect, 112))


    def test_13(self):
        input = r"""

procedure main(); 
begin 
    putInt(2-1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 113))


    def test_14(self):
        input = r"""

procedure main(); 
begin 
    putInt(1-2);
end

"""
        expect = r"""-1"""
        self.assertTrue(TestCodeGen.test(input, expect, 114))


    def test_15(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2-3+4-5+6-7-8-9);
end

"""
        expect = r"""-19"""
        self.assertTrue(TestCodeGen.test(input, expect, 115))


    def test_16(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6);
end

"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 116))


    def test_17(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6*9*1*2);
end

"""
        expect = r"""432"""
        self.assertTrue(TestCodeGen.test(input, expect, 117))


    def test_18(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6*9 - 9*4*6);
end

"""
        expect = r"""0"""
        self.assertTrue(TestCodeGen.test(input, expect, 118))


    def test_19(self):
        input = r"""

procedure main(); 
begin 
    putInt(1*2*3 + 4*5*6 - 5*6 + 123-456);
end

"""
        expect = r"""-237"""
        self.assertTrue(TestCodeGen.test(input, expect, 119))


    def test_20(self):
        input = r"""

procedure main(); 
begin 
    putInt(5 div 2);
end

"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 120))


    def test_21(self):
        input = r"""

procedure main(); 
begin 
    putInt(198 div 8);
end

"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 121))


    def test_22(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.5 + 456);
end

"""
        expect = r"""579.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 122))


    def test_23(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.5 + 456.1);
end

"""
        expect = r"""579.6"""
        self.assertTrue(TestCodeGen.test(input, expect, 123))


    def test_24(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.2+3.4-5.6+7.8);
end

"""
        expect = r"""6.8000007"""
        self.assertTrue(TestCodeGen.test(input, expect, 124))


    def test_25(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.2 * 5.4);
end

"""
        expect = r"""6.4800005"""
        self.assertTrue(TestCodeGen.test(input, expect, 125))


    def test_26(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 2);
end

"""
        expect = r"""61.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 126))


    def test_27(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 127))


    def test_28(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 3 + 46/5/1/1/1/2/4);
end

"""
        expect = r"""42.15"""
        self.assertTrue(TestCodeGen.test(input, expect, 128))


    def test_29(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 2.3);
end

"""
        expect = r"""53.478264"""
        self.assertTrue(TestCodeGen.test(input, expect, 129))


    def test_30(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.1/5 + 123/5.1 - (123*5.1 + 123.1*5) - 123/(123/123*123+1) - 123.123*321.213-1);
end

"""
        expect = r"""-40744.766"""
        self.assertTrue(TestCodeGen.test(input, expect, 130))


    def test_31(self):
        input = r"""

procedure main(); 
begin 
    putBool(True and false);
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 131))


    def test_32(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 132))


    def test_33(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and True);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 133))


    def test_34(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and false or (False and true));
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 134))


    def test_35(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and false or (False or true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 135))


    def test_36(self):
        input = r"""

procedure main(); 
begin 
    putBool(1 > 2);
    putBool(1 < 2);
    putBool(1 = 2);
    putBool(1 >= 2);
    putBool(1 <= 2);
    putBool(1 <> 2);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 136))


    def test_37(self):
        input = r"""

procedure main(); 
begin 
    putBool(2 > 2);
    putBool(2 < 2);
    putBool(2 = 2);
    putBool(2 >= 2);
    putBool(2 <= 2);
    putBool(2 <> 2);
end

"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 137))


    def test_38(self):
        input = r"""

procedure main(); 
begin 
    putBool(3 > 2);
    putBool(3 < 2);
    putBool(3 = 2);
    putBool(3 >= 2);
    putBool(3 <= 2);
    putBool(3 <> 2);
end

"""
        expect = r"""truefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 138))


    def test_39(self):
        input = r"""

procedure main(); 
begin 
    putBool(1.0 > 2);
    putBool(1.0 < 2);
    putBool(1.0 = 2);
    putBool(1.0 >= 2);
    putBool(1.0 <= 2);
    putBool(1.0 <> 2);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 139))


    def test_40(self):
        input = r"""

procedure main(); 
begin 
    putBool(1.9 > 2);
    putBool(1.9 < 2);
    putBool(1.9 = 2);
    putBool(1.9 >= 2);
    putBool(1.9 <= 2);
    putBool(1.9 <> 2);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 140))


    def test_41(self):
        input = r"""

procedure main(); 
begin 
    putBool(2.1 > 2);
    putBool(2.1 < 2);
    putBool(2.1 = 2);
    putBool(2.1 >= 2);
    putBool(2.1 <= 2);
    putBool(2.1 <> 2);
end

"""
        expect = r"""truefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 141))


    def test_42(self):
        input = r"""

procedure main(); 
begin 
    putBool(2.0 > 2);
    putBool(2.0 < 2);
    putBool(2.0 = 2);
    putBool(2.0 >= 2);
    putBool(2.0 <= 2);
    putBool(2.0 <> 2);
end

"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 142))


    def test_43(self):
        input = r"""

procedure main(); 
begin 
    putBool(2.1 > 2.1);
    putBool(2.1 < 2.1);
    putBool(2.1 = 2.1);
    putBool(2.1 >= 2.1);
    putBool(2.1 <= 2.1);
    putBool(2.1 <> 2.1);
end

"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 143))


    def test_44(self):
        input = r"""

procedure main(); 
begin 
    putBool(2 > 2.1);
    putBool(2 < 2.1);
    putBool(2 = 2.1);
    putBool(2 >= 2.1);
    putBool(2 <= 2.1);
    putBool(2 <> 2.1);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 144))


    def test_45(self):
        input = r"""

procedure main(); 
begin 
    putBool(1 + 2 > 3);
    putBool(1 + 2 < 3);
    putBool(1 + 2 = 3);
    putBool(1 + 2 >= 3);
    putBool(1 + 2 <= 3);
    putBool(1 + 2 <> 3);
end

"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 145))


    def test_46(self):
        input = r"""

procedure main(); 
begin 
    putBool(1.5 + 2 > 3);
    putBool(1.5 + 2 < 3);
    putBool(1.5 + 2 = 3);
    putBool(1.5 + 2 >= 3);
    putBool(1.5 + 2 <= 3);
    putBool(1.5 + 2 <> 3);
end

"""
        expect = r"""truefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 146))


    def test_47(self):
        input = r"""

procedure main(); 
begin
    // 1.5*2 + 2 - 5.3*2.1 = -6.13
    // 3*5 + 2*3/2 - 4*7.2/14 + 1 = 16.94
    putBool(1.5*2 + 2 - 5.3*2.1 > 3*5 + 2*3/2 - 4*7.2/14 + 1);
    putBool(1.5*2 + 2 - 5.3*2.1 < 3*5 + 2*3/2 - 4*7.2/14 + 1);
    putBool(1.5*2 + 2 - 5.3*2.1 = 3*5 + 2*3/2 - 4*7.2/14 + 1);
    putBool(1.5*2 + 2 - 5.3*2.1 >= 3*5 + 2*3/2 - 4*7.2/14 + 1);
    putBool(1.5*2 + 2 - 5.3*2.1 <= 3*5 + 2*3/2 - 4*7.2/14 + 1);
    putBool(1.5*2 + 2 - 5.3*2.1 <> 3*5 + 2*3/2 - 4*7.2/14 + 1);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 147))


    def test_48(self):
        input = r"""

procedure main(); 
begin
    // 1.5*2 + 2 - 5.3*2.1 = -6.13
    // 3*5 + 2*3/2 - 4*7.2/14 + 1 = 16.94
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) > 0);
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) < 0);
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) = 0);
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) >= 0);
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) <= 0);
    putBool(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) <> 0);
end

"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 148))


    def test_49(self):
        input = r"""

procedure main();
begin
    putIntLn(5 mod 4);
    putIntLn(15 mod 4);
    putIntLn(52 mod 6);
    putIntLn(56 mod 5);
    putIntLn(9 mod 12);
    putIntLn(1998 mod 46);
    putIntLn(1998 mod 54);
    putIntLn(1998 mod 87);
    putIntLn(1998 mod 42);
    putIntLn(1998 mod 16);
    putIntLn(1998 mod 19);
    putIntLn(1998 mod 24);
end

"""
        expect = r"""1
3
4
1
9
20
0
84
24
14
3
6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 149))


    def test_50(self):
        input = r"""

procedure main();
begin
    putIntLn(5 div 4);
    putIntLn(15 div 4);
    putIntLn(52 div 6);
    putIntLn(56 div 5);
    putIntLn(9 div 12);
    putIntLn(1998 div 46);
    putIntLn(1998 div 54);
    putIntLn(1998 div 87);
    putIntLn(1998 div 42);
    putIntLn(1998 div 16);
    putIntLn(1998 div 19);
    putIntLn(1998 div 24);
end

"""
        expect = r"""1
3
8
11
0
43
37
22
47
124
105
83
"""
        self.assertTrue(TestCodeGen.test(input, expect, 150))


    def test_51(self):
        input = r"""

procedure main();
begin
    putFloatLn(5 / 4);
    putFloatLn(15 / 4);
    putFloatLn(52 / 6);
    putFloatLn(56 / 5);
    putFloatLn(9 / 12);
    putFloatLn(1998 / 46);
    putFloatLn(1998 / 54);
    putFloatLn(1998 / 87);
    putFloatLn(1998 / 42);
    putFloatLn(1998 / 16);
    putFloatLn(1998 / 19);
    putFloatLn(1998 / 24);
end

"""
        expect = r"""1.25
3.75
8.666667
11.2
0.75
43.434784
37.0
22.965517
47.57143
124.875
105.1579
83.25
"""
        self.assertTrue(TestCodeGen.test(input, expect, 151))


    def test_52(self):
        input = r"""

procedure main();
begin
    putFloatLn(1.5*2 + 2 - 5.3*2.1);
    putFloatLn(3*5 + 2*3/2 - 4*7.2/14 + 1);
    putFloatLn(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1));
end

"""
        expect = r"""-6.13
16.942858
-23.072857
"""
        self.assertTrue(TestCodeGen.test(input, expect, 152))


    def test_53(self):
        input = r"""

procedure main();
begin
    putIntLn(1);
    putLn();
    putLn();
    putLn();
    putLn();
    putInt(2);
end

"""
        expect = r"""1




2"""
        self.assertTrue(TestCodeGen.test(input, expect, 153))


    def test_54(self):
        input = r"""

procedure main();
begin
    putIntLn(1000);
    putLn();
    putLn();
    putLn();
    putLn();
    putInt(2000);
end

"""
        expect = r"""1000




2000"""
        self.assertTrue(TestCodeGen.test(input, expect, 154))


    def test_55(self):
        input = r"""

procedure main();
begin
    putString("Hello World");
end

"""
        expect = r"""Hello World"""
        self.assertTrue(TestCodeGen.test(input, expect, 155))


    def test_56(self):
        input = r"""

procedure main();
begin
    putStringLn("Hello World 1");
    putStringLn("Hello World 2");
    putStringLn("3");
    putStringLn("4.5");
    putStringLn("-0.6");
end

"""
        expect = r"""Hello World 1
Hello World 2
3
4.5
-0.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 156))


    def test_57(self):
        input = r"""

procedure main();
begin
    putStringLn("Error: A JNI error has occurred, please check your installation and try again\nException in thread \"main\" java.lang.VerifyError: (class: MPClass, method: main signature: ([Ljava/lang/String;)V) Illegal type in constant pool");
end

"""
        expect = r"""Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.VerifyError: (class: MPClass, method: main signature: ([Ljava/lang/String;)V) Illegal type in constant pool
"""
        self.assertTrue(TestCodeGen.test(input, expect, 157))


    def test_58(self):
        input = r"""

procedure main();
begin
    PutIntLN(-1);
    PuTIntLn(-100);
    PUtFLOATLN(-1.0);
    PutfLOaTLN(-10000.0);
end

"""
        expect = r"""-1
-100
-1.0
-10000.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 158))


    def test_59(self):
        input = r"""

procedure main();
begin
    PutIntLN(--1);
    PuTIntLn(--100);
    PUtFLOATLN(--1.0);
    PutfLOaTLN(--10000.0);

    PutIntLN(---1);
    PuTIntLn(---100);
    PUtFLOATLN(---1.0);
    PutfLOaTLN(---10000.0);
end

"""
        expect = r"""1
100
1.0
10000.0
-1
-100
-1.0
-10000.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 159))


    def test_60(self):
        input = r"""

procedure main();
begin
    PutfloatLN(-(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1)));
    puTFloATLn(-(1.5*2 + 2 - 5.3*2.1) - (3*5 + 2*3/2 - 4*7.2/14 + 1));
    PUtFLOATLN(--(1.5*2 + 2 - 5.3*2.1) --- (3*5 + 2*3/2 - 4*7.2/14 + 1));
    PutfLOaTLN(-(-(-(-(1.5*2 + 2 - 5.3*2.1)))) ---- (3*5 + 2*3/2 - 4*7.2/14 + 1));
end

"""
        expect = r"""23.072857
-10.812858
-23.072857
10.812858
"""
        self.assertTrue(TestCodeGen.test(input, expect, 160))


    def test_61(self):
        input = r"""

procedure main();
begin
    putBoolLn(not false);
    PutBooLLN(not true);
    putbOOLLN(not not false);
    PUtbOOLLN(not not true);
    PutBoOLLN(not not not false);
    PutBoOLLN(not not not true);
    PutBoOLLN(not false and true);
    PutBoOLLN(not true and false);
    PutBoOLLN(not not false and not not not true or false and true);
    PutBoOLLN(not not true or false);
end

"""
        expect = r"""true
false
false
true
true
false
true
false
false
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 161))


    def test_62(self):
        input = r"""

procedure main();
begin
    putBoolLn(true and then false);
    putBoolLn(false and then true);
    putBoolLn(true and then (false and then true));
    putBoolLn(true and then (false and then true) and then false);
    
    putBoolLn(true or else false);
    putBoolLn(false or else true);
    putBoolLn(true or else (false or else true));
    putBoolLn(true or else (false or else true) or else false);
end

"""
        expect = r"""false
false
false
false
true
true
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 162))


    def test_63(self):
        input = r"""

procedure main();
begin
    putBool(false or else false or else true and then (true or else false) and (false or else true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 163))


    def test_64(self):
        input = r"""

procedure main();
var a, b: integer;
begin
    a := 1;
    putIntLn(a);
    b := 2;
    a := b;
    putIntLn(b);
    putIntLn(a);
    a := b + 1;
    putIntLn(a);
end

"""
        expect = r"""1
2
2
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 164))


    def test_65(self):
        input = r"""

procedure main();
var a, b: REAL;
begin
    a := 1.0;
    putFLOATLn(a);
    b := 2.0;
    a := b;
    putFLOATLn(b);
    putfloatln(a);
    a := b + 1;
    putFloatLn(a);
end

"""
        expect = r"""1.0
2.0
2.0
3.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 165))


    def test_66(self):
        input = r"""

procedure main();
var a, b: REAL;
begin
    a := 1;
    putFLOATLn(a);
    b := 2;
    a := b;
    putFLOATLn(b);
    putfloatln(a);
    a := b + 1;
    putFloatLn(a);
end

"""
        expect = r"""1.0
2.0
2.0
3.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 166))


    def test_67(self):
        input = r"""

procedure main();
var a, b: REAL;
    x, y: integer;
begin
    a := 1.05 * 25.4;
    putFLOATLn(a);
    b := 2.05 + a;
    putFLOATLn(b);
    a := a + 100 - b;
    putFloatLn(a);
    x := 1000;
    y := 1;
    x := x + y * 1000 div 5;
    putIntLn(x);
    putIntLn(y);
    y := x*y + x*2 + 2*x - y*2 + 2*y;
    putIntLn(y);
    x := x * y * 2 * 5;
    putIntLn(x);
    a := (a * b + x) / y + y / (a*b + 2 mod x);
    putFloatLn(a);
end

"""
        expect = r"""26.669998
28.719997
97.95
1200
1
6000
72000000
12002.601
"""
        self.assertTrue(TestCodeGen.test(input, expect, 167))


    def test_68(self):
        input = r"""

procedure main();
var a, b: REAL;
    x, y: integer;
begin
    a := 1.05 * 25.4;
    putFLOATLn(a);
    B := 2.05 + a;
    putFLOATLn(b);
    A := a + 100 - b;
    putFloatLn(a);
    x := 1000;
    y := 1;
    X := x + Y * 1000 div 5;
    putIntLn(x);
    putIntLn(Y);
    y := x*y + X*2 + 2*x - Y*2 + 2*y;
    putIntLn(Y);
    x := x * y * 2 * 5;
    putIntLn(X);
    a := (A * b + x) / y + Y / (a*B + 2 mod X);
    putFloatLn(A);
end

"""
        expect = r"""26.669998
28.719997
97.95
1200
1
6000
72000000
12002.601
"""
        self.assertTrue(TestCodeGen.test(input, expect, 168))


    def test_69(self):
        input = r"""

procedure main();
var a, b, c: REAL;
begin
    a := 5.0;
    b := 2.0;
    a := b := a + b / 2 + 1;
    putFloatLn(a);
    putFloatLn(b);

    c := a := b := (a+b)/4 + (a-b)/4 * 2 + 1;
    putFloatLn(a);
    putFloatLn(b);
    putFloatLn(c);
end

"""
        expect = r"""7.0
7.0
4.5
4.5
4.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 169))


    def test_70(self):
        input = r"""

procedure main();
var a, b: REAL;
    c: integer;
begin
    a := 5.0;
    b := 2.0;
    c := 1000;
    a := b := c + 1;
    putFloatLn(a);
    putFloatLn(b);
    putIntLn(c);
end

"""
        expect = r"""1001.0
1001.0
1000
"""
        self.assertTrue(TestCodeGen.test(input, expect, 170))


    def test_71(self):
        input = r"""

procedure main();
var a: integer;
begin
    a := 5;
    putFloat(a);
end

"""
        expect = r"""5.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 171))


    def test_72(self):
        input = r"""

procedure main();
var a: integer;
begin
    a := 5;
    putIntLn(a);
    putFloatLn(a);
    putFloatLn(a + 5.0);
end

"""
        expect = r"""5
5.0
10.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 172))


    def test_73(self):
        input = r"""

function foo(): integer;
begin
    return 100;
end

procedure main();
begin
    putInt(foo());
end

"""
        expect = r"""100"""
        self.assertTrue(TestCodeGen.test(input, expect, 173))


    def test_74(self):
        input = r"""

function foo(): integer;
var a: integer;
begin
    a := 1000;
    return a;
end

procedure main();
begin
    putInt(foo());
end

"""
        expect = r"""1000"""
        self.assertTrue(TestCodeGen.test(input, expect, 174))


    def test_75(self):
        input = r"""

procedure main();
begin
    putIntLn(fi());
    putFloatLn(ff());
    putBoolLn(fb());
end

function fi(): integer;
begin
    return 1;
end

function ff(): real;
begin
    return 5.0;
end

function fb(): boolean;
begin
    return false;
end

"""
        expect = r"""1
5.0
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 175))


    def test_76(self):
        input = r"""

procedure main();
var a: integer;
begin
    a := foo(1, 2);
    putInt(a);
end

function foo(a,b: integer): integer;
begin
    return (a + b) div 2;
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 176))


    def test_77(self):
        input = r"""

procedure main();
var a: real;
begin
    a := foo(2, false);
    putFloat(a);
end

function foo(a: real; b: boolean): real;
begin
    return a*a*a + a/2;
end

"""
        expect = r"""9.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 177))


    def test_78(self):
        input = r"""

procedure main();
begin
    a := 100;
    putInt(a);
end

var a: integer;

"""
        expect = r"""100"""
        self.assertTrue(TestCodeGen.test(input, expect, 178))


    def test_79(self):
        input = r"""

procedure main();
var a: real;
begin
    a := 100;
    putFloatLn(a);
    a := foo();
    putFloatLn(a);
    bar();
end

function foo(): integer;
begin
    a := 10;
    return a*5;
end

procedure bar();
begin
    putIntLn(a);
end

var a: integer;

"""
        expect = r"""100.0
50.0
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 179))


    def test_80(self):
        input = r"""

procedure main();
var a: real;
begin
    a := 100;
    putFloatLn(a);
    a := foo();
    putFloatLn(a);
    bar();
end

function foo(): real;
begin
    a := 10;
    return a*5;
end

procedure bar();
begin
    putFloatLn(a);
end

var a: real;

"""
        expect = r"""100.0
50.0
10.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 180))


    def test_81(self):
        input = r"""

procedure main();
var a: boolean;
begin
    a := 10 < 5;
    putBoolln(a);
    a := foo();
    putBoolln(a);
    bar();
end

function foo(): boolean;
begin
    a := 10 > 5;
    return a or else true;
end

procedure bar();
begin
    putBoolln(a);
end

var a: boolean;

"""
        expect = r"""false
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 181))


    def test_82(self):
        input = r"""

procedure main();
begin
    if 1 = 2 then putInt(100);
    else putInt(300);
end

"""
        expect = r"""300"""
        self.assertTrue(TestCodeGen.test(input, expect, 182))


    def test_83(self):
        input = r"""

procedure main();
begin
    if true then putInt(100);
    else if true then putInt(200);
    else putInt(300);

    if false then putInt(100);
    else if true then putInt(200);
    else putInt(300);

    if false then putInt(100);
    else if false then putInt(200);
    else putInt(300);
end

"""
        expect = r"""100200300"""
        self.assertTrue(TestCodeGen.test(input, expect, 183))


    def test_84(self):
        input = r"""

procedure main();
begin
    if true then begin
        putInt(100);
        if false then putInt(100);
        else if true then putInt(200);
        else putInt(300);
    end
    else if true then putInt(200);
    else putInt(300);

    if false then begin
        putInt(100);
    end
    else if true then begin
        putInt(200);
        if false then putInt(100);
        else if true then putInt(200);
        else putInt(300);
    end else putInt(300);
end

"""
        expect = r"""100200200200"""
        self.assertTrue(TestCodeGen.test(input, expect, 184))


    def test_85(self):
        input = r"""

procedure main();
var a: integer;
begin
    a := 5;
    while a > 0 do begin
        putInt(a);
        a := a-1;
    end
end

"""
        expect = r"""54321"""
        self.assertTrue(TestCodeGen.test(input, expect, 185))


    def test_86(self):
        input = r"""

procedure main();
var a, b: integer;
begin
    a := 5;
    while a > 0 do begin
        putIntLn(a);
        a := a-1;
        b := 0;
        while b < a do begin
            b := b+1;
            putInt(b);
        end
        putLn();
    end
end

"""
        expect = r"""5
1234
4
123
3
12
2
1
1

"""
        self.assertTrue(TestCodeGen.test(input, expect, 186))


    def test_87(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 5 do putInt(i);
end

"""
        expect = r"""12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 187))


    def test_88(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 5 do putInt(i);
    putInt(i);
end

"""
        expect = r"""123456"""
        self.assertTrue(TestCodeGen.test(input, expect, 188))


    def test_89(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 5 do putInt(i);
    putIntLn(i);

    for i := 1 to 1 do putInt(i);
    putIntLn(i);

    for i := 5 to 1 do putInt(i);
    putIntLn(i);
end

"""
        expect = r"""123456
12
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 189))


    def test_90(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 downto 5 do putInt(i);
    putIntLn(i);

    for i := 1 downto 1 do putInt(i);
    putIntLn(i);

    for i := 5 downto 1 do putInt(i);
    putIntLn(i);
end

"""
        expect = r"""1
10
543210
"""
        self.assertTrue(TestCodeGen.test(input, expect, 190))


    def test_91(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 10 do begin
        if i > 4 then putInt(i); else putInt(-i);
    end
end

"""
        expect = r"""-1-2-3-45678910"""
        self.assertTrue(TestCodeGen.test(input, expect, 191))


    def test_92(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 5;
    for i := a to b do begin
        for j := b downto a do begin
            putInt(i); putString(" + ");
            putInt(j); putString(" = ");
            putIntLn(i+j);
        end
    end
end

"""
        expect = r"""1 + 5 = 6
1 + 4 = 5
1 + 3 = 4
1 + 2 = 3
1 + 1 = 2
2 + 5 = 7
2 + 4 = 6
2 + 3 = 5
2 + 2 = 4
2 + 1 = 3
3 + 5 = 8
3 + 4 = 7
3 + 3 = 6
3 + 2 = 5
3 + 1 = 4
4 + 5 = 9
4 + 4 = 8
4 + 3 = 7
4 + 2 = 6
4 + 1 = 5
5 + 5 = 10
5 + 4 = 9
5 + 3 = 8
5 + 2 = 7
5 + 1 = 6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 192))


    def test_93(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 5;
    for i := a to b do begin
        for j := b downto a do begin
            putInt(i); putString(" + ");
            putInt(j); putString(" = ");
            putIntLn(i+j);
            a := a+1;
            b := b-1;
        end
    end
end

"""
        expect = r"""1 + 5 = 6
1 + 4 = 5
1 + 3 = 4
"""
        self.assertTrue(TestCodeGen.test(input, expect, 193))


    def test_94(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        i := i+1;
    end
end

"""
        expect = r"""13579"""
        self.assertTrue(TestCodeGen.test(input, expect, 194))


    def test_95(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a-b to a+b do begin
        putInt(i);
        i := i+1;
        a := a-1;
        b := b+1;
    end
end

"""
        expect = r"""-9-7-5-3-11357911"""
        self.assertTrue(TestCodeGen.test(input, expect, 195))


    def test_96(self):
        input = r"""

procedure main();
var i: integer;
begin
    i := 1;
    while true do begin
        putInt(i);
        if i = 3 then break;
        i := i+1;
    end
    putInt(i);
end

"""
        expect = r"""1233"""
        self.assertTrue(TestCodeGen.test(input, expect, 196))


    def test_97(self):
        input = r"""

procedure main();
var i: integer;
begin
    i := 1;
    while i < 10 do begin
        putInt(i);
        i := i+1;
        if i > 6 then continue;
        i := i+1;
    end
    putInt(i);
end

"""
        expect = r"""13578910"""
        self.assertTrue(TestCodeGen.test(input, expect, 197))


    def test_98(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 10 do begin
        putInt(i);
        if i > 5 then break;
    end
    putInt(i);
end

"""
        expect = r"""1234566"""
        self.assertTrue(TestCodeGen.test(input, expect, 198))


    def test_99(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 8 do begin
        if i > 5 then continue;
        putInt(i);
    end
    putInt(i);
end

"""
        expect = r"""123459"""
        self.assertTrue(TestCodeGen.test(input, expect, 199))


    def test_100(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 8 downto 1 do begin
        if i < 5 then continue;
        putInt(i);
    end
    putInt(i);
end

"""
        expect = r"""87650"""
        self.assertTrue(TestCodeGen.test(input, expect, 200))



    def test_101(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            putInt(j);
            putString(" ");
        end
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r"""1: 2 3 4 5 6 7 8 9 10 
j = 11
i = 1
2: 3 4 5 6 7 8 9 10 
j = 11
i = 2
3: 4 5 6 7 8 9 10 
j = 11
i = 3
4: 5 6 7 8 9 10 
j = 11
i = 4
5: 6 7 8 9 10 
j = 11
i = 5
6: 7 8 9 10 
j = 11
i = 6
7: 8 9 10 
j = 11
i = 7
8: 9 10 
j = 11
i = 8
9: 10 
j = 11
i = 9
10: 
j = 11
i = 10
11"""
        self.assertTrue(TestCodeGen.test(input, expect, 201))


    def test_102(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            if (j + i) * 2 > b then continue;
            putInt(j);
            putString(" ");
        end
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r"""1: 2 3 4 
j = 11
i = 1
2: 3 
j = 11
i = 2
3: 
j = 11
i = 3
4: 
j = 11
i = 4
5: 
j = 11
i = 5
6: 
j = 11
i = 6
7: 
j = 11
i = 7
8: 
j = 11
i = 8
9: 
j = 11
i = 9
10: 
j = 11
i = 10
11"""
        self.assertTrue(TestCodeGen.test(input, expect, 202))


    def test_103(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            if (j + i) * 2 > b then break;
            putInt(j);
            putString(" ");
        end
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r"""1: 2 3 4 
j = 5
i = 1
2: 3 
j = 4
i = 2
3: 
j = 4
i = 3
4: 
j = 5
i = 4
5: 
j = 6
i = 5
6: 
j = 7
i = 6
7: 
j = 8
i = 7
8: 
j = 9
i = 8
9: 
j = 10
i = 9
10: 
j = 11
i = 10
11"""
        self.assertTrue(TestCodeGen.test(input, expect, 203))


    def test_104(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            if (j + i) * 2 > b then break;
            putInt(j);
            putString(" ");
        end
        if i > 5 then continue;
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r"""1: 2 3 4 
j = 5
i = 1
2: 3 
j = 4
i = 2
3: 
j = 4
i = 3
4: 
j = 5
i = 4
5: 
j = 6
i = 5
6: 7: 8: 9: 10: 11"""
        self.assertTrue(TestCodeGen.test(input, expect, 204))


    def test_105(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            if (j + i) * 2 > b then break;
            putInt(j);
            putString(" ");
        end
        if i > 5 then break;
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r"""1: 2 3 4 
j = 5
i = 1
2: 3 
j = 4
i = 2
3: 
j = 4
i = 3
4: 
j = 5
i = 4
5: 
j = 6
i = 5
6: 6"""
        self.assertTrue(TestCodeGen.test(input, expect, 205))


    def test_106(self):
        input = r"""

procedure main();
var a, b: integer;
begin
    a := 1;
    b := 5;
    putLn();
    with a: integer; do begin
        a := 2;
        b := 10;
        putInt(a); putString(" ");
        putIntLn(b);
    end
    putInt(a); putString(" ");
    putInt(b);
end

"""
        expect = r"""
2 10
1 10"""
        self.assertTrue(TestCodeGen.test(input, expect, 206))


    def test_107(self):
        input = r"""

procedure main();
var a, b: integer;
begin
    a := 1;
    b := 5;
    putLn();
    with a,b,c: real; do begin
        a := 2;
        b := 10;
        putFloat(a); putString(" ");
        putFloatLn(b);
    end
    putInt(a); putString(" ");
    putInt(b);
end

"""
        expect = r"""
2.0 10.0
1 5"""
        self.assertTrue(TestCodeGen.test(input, expect, 207))


    def test_108(self):
        input = r"""

procedure main();
var a: array[3 .. 5] of integer;
begin
    a[5] := 10;
    putInt(a[5]);
end

"""
        expect = r"""10"""
        self.assertTrue(TestCodeGen.test(input, expect, 208))


    def test_109(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    a[0] := 1;
    a[1] := 2;
    putInt(a[0]);
    putInt(a[1]);

    i := 5;
    a[i] := 5;
    putInt(a[i]);

    i := 6;
    a[i+1] := 6;
    putInt(a[i+1]);
end

"""
        expect = r"""1256"""
        self.assertTrue(TestCodeGen.test(input, expect, 209))


    def test_110(self):
        input = r"""

procedure main();
var a: array[0 .. 8] of integer;
    i, l, r: integer;
begin
    l := 0;
    r := 8;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""1 2 3 4 5 6 7 8 9 
0: 1
1: 2
2: 3
3: 4
4: 5
5: 6
6: 7
7: 8
8: 9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 210))


    def test_111(self):
        input = r"""

procedure main();
var a: array[-8 .. 5] of integer;
    i, l, r: integer;
begin
    l := -8;
    r := 5;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""-7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 
-8: -7
-7: -6
-6: -5
-5: -4
-4: -3
-3: -2
-2: -1
-1: 0
0: 1
1: 2
2: 3
3: 4
4: 5
5: 6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 211))


    def test_112(self):
        input = r"""

procedure main();
var a: array[1000000000 .. 1000000010] of integer;
    i, l, r: integer;
begin
    l := 1000000000;
    r := 1000000010;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""1000000001 1000000002 1000000003 1000000004 1000000005 1000000006 1000000007 1000000008 1000000009 1000000010 1000000011 
1000000000: 1000000001
1000000001: 1000000002
1000000002: 1000000003
1000000003: 1000000004
1000000004: 1000000005
1000000005: 1000000006
1000000006: 1000000007
1000000007: 1000000008
1000000008: 1000000009
1000000009: 1000000010
1000000010: 1000000011
"""
        self.assertTrue(TestCodeGen.test(input, expect, 212))


    def test_113(self):
        input = r"""

procedure main();
var a: array[-1000000010 .. -1000000000] of integer;
    i, l, r: integer;
begin
    l := -1000000010;
    r := -1000000000;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""-1000000009 -1000000008 -1000000007 -1000000006 -1000000005 -1000000004 -1000000003 -1000000002 -1000000001 -1000000000 -999999999 
-1000000010: -1000000009
-1000000009: -1000000008
-1000000008: -1000000007
-1000000007: -1000000006
-1000000006: -1000000005
-1000000005: -1000000004
-1000000004: -1000000003
-1000000003: -1000000002
-1000000002: -1000000001
-1000000001: -1000000000
-1000000000: -999999999
"""
        self.assertTrue(TestCodeGen.test(input, expect, 213))


    def test_114(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    i := 0;
    a[i] := 1;
    i := a[i];
    putInt(i);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 214))


    def test_115(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    i := 0;
    i := a[i] := 1;
    putInt(i);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 215))


    def test_116(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    i := 1;
    a[i] := 1;
    a[i-1] := 2;
    i := a[i] + a[i-1];
    putInt(i);
end

"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 216))


    def test_117(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    a[0] := 1;
    a[1] := a[0];
    putInt(a[1]);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 217))


    def test_118(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    i := 1;
    a[0] := 1;
    a[i] := a[i-1];
    putInt(a[i]);
    a[i] := a[i-1] + 1;
    putInt(a[i]);
    a[i] := a[i-1] * 2 + 1;
    putInt(a[i]);
    a[i] := a[i-1] * 2 + a[i];
    putInt(a[i]);
    a[i] := a[i-1] := a[i-1] * 2 + a[i] * 3 + a[i-1] * a[i];
    putInt(a[i]);
    putInt(a[i-1]);
end

"""
        expect = r"""12352222"""
        self.assertTrue(TestCodeGen.test(input, expect, 218))


    def test_119(self):
        input = r"""

procedure main();
var a: array[0 .. 10] of integer;
    i, l, r: integer;
begin
    l := 0;
    r := 10;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putInt(a[r]);
end


"""
        expect = r"""89"""
        self.assertTrue(TestCodeGen.test(input, expect, 219))


    def test_120(self):
        input = r"""

procedure main();
var a: array[-10000 .. 10000] of integer;
    i, l, r: integer;
begin
    l := -20;
    r := 20;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putInt(a[r]);
end


"""
        expect = r"""165580141"""
        self.assertTrue(TestCodeGen.test(input, expect, 220))


    def test_121(self):
        input = r"""

procedure main();
var a: array[-10000 .. 10000] of real;
    i, l, r: integer;
begin
    l := -20;
    r := 20;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putFloat(a[r]);
end


"""
        expect = r"""1.65580128E8"""
        self.assertTrue(TestCodeGen.test(input, expect, 221))


    def test_122(self):
        input = r"""

procedure main();
var a: array[-10000 .. 10000] of real;
    i, l, r: integer;
begin
    l := -40;
    r := 40;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putFloat(a[r]);
end


"""
        expect = r"""3.788905E16"""
        self.assertTrue(TestCodeGen.test(input, expect, 222))


    def test_123(self):
        input = r"""

procedure main();
var a: array[-10000 .. 10000] of boolean;
    i, l, r: integer;
begin
    l := -40;
    r := 40;
    a[l] := True;
    a[l+1] := falsE;
    for i := l+2 to r do begin
        a[i] := a[i-1] and then not a[i-2] or else not a[i-1];
    end
    putBool(a[r]);
end


"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 223))


    def test_124(self):
        input = r"""

procedure main();
begin
    if 6/3 = foo(3,6) then putString("Ha"); 
    else putString("aH");
end

function foo(a, b: integer): integer;
var i: integer;
begin
    for i := 0 to b do begin
        if a * i = b then return i;
    end
    return -1;
end

"""
        expect = r"""Ha"""
        self.assertTrue(TestCodeGen.test(input, expect, 224))


    def test_125(self):
        input = r"""

procedure main();
begin
    if 8/3 = foo(3,9) then putString("Ha"); 
    else putString("aH");
end

function foo(a, b: integer): integer;
var i: integer;
begin
    for i := 0 to b do begin
        if a * i = b then return i;
    end
    return -1;
end

"""
        expect = r"""aH"""
        self.assertTrue(TestCodeGen.test(input, expect, 225))


    def test_126(self):
        input = r"""

var a, b: integer;

procedure main();
begin
    a := 5;
    b := 100;
    if b/a = foo(a,b) then putString("Ha"); 
    else putString("aH");
    putInt(a);
    putInt(b);
end

function foo(a, b: integer): integer;
var i: integer;
begin
    for i := 0 to b do begin
        if a * i = b then begin
            a := b := -1;
            return i;
        end
    end
    a := b := 0;
    return -1;
end

"""
        expect = r"""Ha5100"""
        self.assertTrue(TestCodeGen.test(input, expect, 226))


    def test_127(self):
        input = r"""

var a, b: integer;

procedure main();
begin
    a := 24;
    b := 100;
    if b/a = foo(a,b) then putString("Ha"); 
    else putString("aH");
    putInt(a);
    putInt(b);
end

function foo(a, b: integer): integer;
var i: integer;
begin
    for i := 0 to b do begin
        if a * i = b then begin
            a := b := -1;
            return i;
        end
    end
    a := b := 0;
    return -1;
end

"""
        expect = r"""aH24100"""
        self.assertTrue(TestCodeGen.test(input, expect, 227))


    def test_128(self):
        input = r"""

var a, b: integer;

procedure main();
begin
    putStringLn(str_ha_1());
    putStringLn(str_ha_2());
    putStringLn(str_ha_3());
    putStringLn(str_ha_4());
    putStringLn(str_ha_5());
end

function str_ha_1(): string; begin return "Ha 1"; end
function str_ha_2(): string; begin return "Ha 2"; end
function str_ha_3(): string; begin return "Ha 3"; end
function str_ha_4(): string; begin return "Ha 4"; end
function str_ha_5(): string; begin return "Ha 5"; end

"""
        expect = r"""Ha 1
Ha 2
Ha 3
Ha 4
Ha 5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 228))


    def test_129(self):
        input = r"""

var a, b: integer;

procedure main();
begin
    ha_str_proc(ha_str_func(), 9);
end

procedure ha_str_proc(ha: string; times: integer); 
var i: integer;
begin
    for i := 1 to times do begin
        putString(ha); putIntLn(i);
    end
end

function ha_str_func(): string; begin return "Ha "; end

"""
        expect = r"""Ha 1
Ha 2
Ha 3
Ha 4
Ha 5
Ha 6
Ha 7
Ha 8
Ha 9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 229))


    def test_130(self):
        input = r"""

var a, b: integer;
var x, y: real;
var u, v: boolean;

procedure main();
begin
    updateHA(5, 10);
    ha_i_space(a);
    ha_i_space(b);
    ha_f_space(x);
    ha_f_space(y);
end

procedure updateHA(ha1, ha2: integer);
begin
    a := ha1 + ha2;
    b := ha1 - ha2;
    x := a + b;
    y := a - b;
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""15 -5 10.0 20.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 230))


    def test_131(self):
        input = r"""

var a, b: integer;
var x, y: real;
var u, v: boolean;

procedure main();
var n: integer;
begin
    n := 10;
    while true do begin
        with i: integer; do begin
            a := 1;
            b := n;
            ha_i_space(n);
            for i := a to b do begin
                ha_f_space(mid(a,b));
            end
            if n = 0 then break;
        end
        n := n-1;
        putLn();
    end
end

function mid(a, b: integer): real; begin return (a + b) / 2; end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""10 5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5 
9 5.0 5.0 5.0 5.0 5.0 5.0 5.0 5.0 5.0 
8 4.5 4.5 4.5 4.5 4.5 4.5 4.5 4.5 
7 4.0 4.0 4.0 4.0 4.0 4.0 4.0 
6 3.5 3.5 3.5 3.5 3.5 3.5 
5 3.0 3.0 3.0 3.0 3.0 
4 2.5 2.5 2.5 2.5 
3 2.0 2.0 2.0 
2 1.5 1.5 
1 1.0 
0 """
        self.assertTrue(TestCodeGen.test(input, expect, 231))


    def test_132(self):
        input = r"""

var a, b: integer;
var x, y: real;
var u, v: boolean;

procedure main();
var n: integer;
begin
    ha0852_proc();
end

procedure ha0852_proc();
var i, j: integer;
begin
    for i := 1 to 10 do begin
        for j := 1 to 10 do begin
            if i = 10 and then j = 5 then return;
            ha_i_space(i);
        end
    end
end

function mid(a, b: integer): real; begin return (a + b) / 2; end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 10 10 10 10 """
        self.assertTrue(TestCodeGen.test(input, expect, 232))


    def test_133(self):
        input = r"""

var a: array[3 .. 5] of integer;
procedure main();
begin
    a[5] := 10;
    putInt(a[5]);
end

"""
        expect = r"""10"""
        self.assertTrue(TestCodeGen.test(input, expect, 233))


    def test_134(self):
        input = r"""

var a: array[0 .. 10] of integer;
procedure main();
var 
    i: integer;
begin
    a[0] := 1;
    a[1] := 2;
    putInt(a[0]);
    putInt(a[1]);

    i := 5;
    a[i] := 5;
    putInt(a[i]);

    i := 6;
    a[i+1] := 6;
    putInt(a[i+1]);
end

"""
        expect = r"""1256"""
        self.assertTrue(TestCodeGen.test(input, expect, 234))


    def test_135(self):
        input = r"""

var a: array[0 .. 8] of integer;
procedure main();
var
    i, l, r: integer;
begin
    l := 0;
    r := 8;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""1 2 3 4 5 6 7 8 9 
0: 1
1: 2
2: 3
3: 4
4: 5
5: 6
6: 7
7: 8
8: 9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 235))


    def test_136(self):
        input = r"""

var a: array[1000000000 .. 1000000010] of integer;

procedure main();
var
    i, l, r: integer;
begin
    l := 1000000000;
    r := 1000000010;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""1000000001 1000000002 1000000003 1000000004 1000000005 1000000006 1000000007 1000000008 1000000009 1000000010 1000000011 
1000000000: 1000000001
1000000001: 1000000002
1000000002: 1000000003
1000000003: 1000000004
1000000004: 1000000005
1000000005: 1000000006
1000000006: 1000000007
1000000007: 1000000008
1000000008: 1000000009
1000000009: 1000000010
1000000010: 1000000011
"""
        self.assertTrue(TestCodeGen.test(input, expect, 236))


    def test_137(self):
        input = r"""

var a: array[-1000000010 .. -1000000000] of integer;
procedure main();
var
    i, l, r: integer;
begin
    l := -1000000010;
    r := -1000000000;
    for i := l to r do begin
        a[i] := i + 1;
        putInt(a[i]); putString(" ");
    end
    putLn();
    for i := l to r do begin
        putInt(i); putString(": "); putIntLn(a[i]);
    end
end

"""
        expect = r"""-1000000009 -1000000008 -1000000007 -1000000006 -1000000005 -1000000004 -1000000003 -1000000002 -1000000001 -1000000000 -999999999 
-1000000010: -1000000009
-1000000009: -1000000008
-1000000008: -1000000007
-1000000007: -1000000006
-1000000006: -1000000005
-1000000005: -1000000004
-1000000004: -1000000003
-1000000003: -1000000002
-1000000002: -1000000001
-1000000001: -1000000000
-1000000000: -999999999
"""
        self.assertTrue(TestCodeGen.test(input, expect, 237))


    def test_138(self):
        input = r"""

var a: array[0 .. 10] of integer;
procedure main();
var i, l, r: integer;
begin
    i := 0;
    a[i] := 1;
    i := a[i];
    putInt(i);

    i := 0;
    i := a[i] := 1;
    putInt(i);

    i := 1;
    a[i] := 1;
    a[i-1] := 2;
    i := a[i] + a[i-1];
    putInt(i);

    a[0] := 1;
    a[1] := a[0];
    putInt(a[1]);

    i := 1;
    a[0] := 1;
    a[i] := a[i-1];
    putInt(a[i]);
    a[i] := a[i-1] + 1;
    putInt(a[i]);
    a[i] := a[i-1] * 2 + 1;
    putInt(a[i]);
    a[i] := a[i-1] * 2 + a[i];
    putInt(a[i]);
    a[i] := a[i-1] := a[i-1] * 2 + a[i] * 3 + a[i-1] * a[i];
    putInt(a[i]);
    putInt(a[i-1]);

    l := 0;
    r := 10;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putInt(a[r]);
end

"""
        expect = r"""11311235222289"""
        self.assertTrue(TestCodeGen.test(input, expect, 238))


    def test_139(self):
        input = r"""

var a: array[-10000 .. 10000] of integer;
procedure main();
var
    i, l, r: integer;
begin
    l := -20;
    r := 20;
    a[l] := 1;
    a[l+1] := 1;
    for i := l+2 to r do begin
        a[i] := a[i-1] + a[i-2];
    end
    putInt(a[r]);
end

"""
        expect = r"""165580141"""
        self.assertTrue(TestCodeGen.test(input, expect, 239))


    def test_140(self):
        input = r"""

procedure main();
var a: array[4 .. 10] of integer;
begin
    a[5] := 5;
    foo(4, a);
    ha_i_space(a[5]);
end

procedure foo(i: integer; a: array[4 .. 10] of integer);
begin
    ha_i_space(a[5]);
    a[5] := 8;
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""5 5 """
        self.assertTrue(TestCodeGen.test(input, expect, 240))


    def test_141(self):
        input = r"""

procedure main();
var a: array[4 .. 10] of integer;
    i: integer;
begin
    for i := 4 to 10 do begin
        a[i] := i * i;
    end
    foo(a);
    putLN();
    for i := 4 to 10 do ha_i_space(a[i]);
end

procedure foo(a: array[4 .. 10] of integer);
var i: integer;
begin
    for i := 4 to 10 do ha_i_space(a[i]);
    for i := 4 to 10 do begin
        a[i] := i + i;
    end
    for i := 4 to 10 do ha_i_space(a[i]);
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""16 25 36 49 64 81 100 8 10 12 14 16 18 20 
16 25 36 49 64 81 100 """
        self.assertTrue(TestCodeGen.test(input, expect, 241))


    def test_142(self):
        input = r"""

procedure main();
var a: array[4 .. 10] of real;
    i: integer;
begin
    for i := 4 to 10 do begin
        a[i] := i * i;
    end
    foo(a);
    putLN();
    for i := 4 to 10 do ha_f_space(a[i]);
end

procedure foo(a: array[4 .. 10] of real);
var i: integer;
begin
    for i := 4 to 10 do ha_f_space(a[i]);
    for i := 4 to 10 do begin
        a[i] := i + i;
    end
    for i := 4 to 10 do ha_f_space(a[i]);
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""16.0 25.0 36.0 49.0 64.0 81.0 100.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 242))


    def test_143(self):
        input = r"""

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
        expect = r"""true true true true true false false false false false false false true true 
true true true true true false false """
        self.assertTrue(TestCodeGen.test(input, expect, 243))


    def test_144(self):
        input = r"""

procedure main();
var a: array[4 .. 10] of integer;
    b: array[5 .. 20] of real;
    i: integer;
begin
    for i := 4 to 10 do begin
        a[i] := i * i;
        b[i+1] := i * i;
    end
    foo(b, a);
    putLN();
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
        ha_f_space(b[i+1]);
    end
end

procedure foo(
    a: array[5 .. 20] of real;
    b: array[4 .. 10] of integer
);
var i: integer;
begin
    for i := 4 to 10 do begin
        ha_f_space(a[i+1]);
        ha_f_space(b[i]);
    end
    for i := 4 to 10 do begin
        a[i+1] := b[i];
        if i+1 > 10 then continue;
        b[i+1] := (i+1) * i div 2 + 1;
    end
    putLn();
    for i := 4 to 10 do begin
        ha_f_space(a[i+1]);
        ha_f_space(b[i]);
    end
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""16.0 16.0 25.0 25.0 36.0 36.0 49.0 49.0 64.0 64.0 81.0 81.0 100.0 100.0 
16.0 16.0 11.0 11.0 16.0 16.0 22.0 22.0 29.0 29.0 37.0 37.0 46.0 46.0 
16.0 16.0 25.0 25.0 36.0 36.0 49.0 49.0 64.0 64.0 81.0 81.0 100.0 100.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 244))


    def test_145(self):
        input = r"""

function ha_arr(): array[4 .. 10] of integer;
var a: array[4 .. 10] of integer;
    i: integer;
begin
    for i := 4 to 10 do a[i] := i * i;
    return a;
end

procedure main();
begin
    foo(ha_arr());
end

procedure foo(a: array[4 .. 10] of integer);
var i: integer;
begin
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
    for i := 4 to 10 do begin
        a[i] := i + 1;
    end
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""16.0 25.0 36.0 49.0 64.0 81.0 100.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 245))


    def test_146(self):
        input = r"""

var a: array[4 .. 10] of integer;

function ha_arr(): array[4 .. 10] of integer;
var i: integer;
begin
    for i := 4 to 10 do a[i] := i * i;
    return a;
end

procedure main();
var i: integer;
begin
    putLn();
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
    putLn();
    foo(ha_arr());
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
end

procedure foo(a: array[4 .. 10] of integer);
var i: integer;
begin
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
        a[i] := i + 1;
    end
    putLn();
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 246))


    def test_147(self):
        input = r"""

var a: array[4 .. 10] of integer;

function ha_arr(): array[4 .. 10] of integer;
var i: integer;
begin
    for i := 4 to 10 do a[i] := i * i;
    return a;
end

procedure ha_arr_buff(x: array[4 .. 10] of integer); begin end

procedure main();
var i: integer;
begin
    putLn();
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
    putLn();
    foo(ha_arr());
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
    ha_arr_buff(ha_arr());
    putLn();
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
    end
end

procedure foo(x: array[4 .. 10] of integer);
var i: integer;
begin
    for i := 4 to 10 do begin
        ha_f_space(x[i]);
        x[i] := i + 1;
    end
    putLn();
    for i := 4 to 10 do begin
        ha_f_space(a[i]);
        a[i] := i - 1;
    end
    putLn();
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r"""
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 
3.0 4.0 5.0 6.0 7.0 8.0 9.0 
16.0 25.0 36.0 49.0 64.0 81.0 100.0 """
        self.assertTrue(TestCodeGen.test(input, expect, 247))


    def test_148(self):
        input = r"""

var n, m: integer;

procedure main();
var a: array[0 .. 100000] of integer;
    i: integer;
begin
    n := 10000;
    m := 1000000009;
    a[0] := 1;
    a[1] := 2;
    for i := 2 to n do a[i] := (a[i-1] + a[i-2]) mod m;
    // for i := 0 to n do putIntLn(a[i]);
    ha_i_space(indexOf(a, 1597));
    ha_i_space(indexOf(a, 10946));
    ha_i_space(indexOf(a, 1346269));
    ha_i_space(indexOf(a, 165580141));
    ha_i_space(indexOf(a, 784974805));
    ha_i_space(indexOf(a, 337007687));
    ha_i_space(indexOf(a, 807526340));
    ha_i_space(indexOf(a, 147860051));
    ha_i_space(indexOf(a, 274044507));
    ha_i_space(indexOf(a, 203070066));
    ha_i_space(indexOf(a, 150716683));
    ha_i_space(indexOf(a, 992750503));
    ha_i_space(indexOf(a, 453021451));
    ha_i_space(indexOf(a, 941642764));
    ha_i_space(indexOf(a, 163684284));
    ha_i_space(indexOf(a, 564665913));
    ha_i_space(indexOf(a, 102915696));
end

function indexOf(a: array[0 .. 100000] of integer; x: integer): integer;
var i: integer;
begin
    for i := 0 to n do begin
        if a[i] = x then return i;
    end
    return -1;
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end

"""
        expect = r"""15 19 29 39 302 318 -1 332 364 379 419 999 874 481 443 749 1000 """
        self.assertTrue(TestCodeGen.test(input, expect, 248))


    def test_149(self):
        input = r"""

var n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i: integer;
begin
    n := 50; m := 1997;
    // n := 5000; m := 1000000009;
    a[1] := 1;
    a[2] := 2;
    for i := 3 to n do a[i] := ((3 * a[i-1]) mod m - (4 * a[i-2]) mod m + m) mod m;

    ha_log_arr();
    // ha_i_space(ha_check_arr());

    sort(1, n);

    ha_log_arr();
    // ha_i_space(ha_check_arr());
end

procedure sort(l, r: integer);
var x,i,j: integer;
begin
    if l >= r then return;
    x := (l+r) div 2;
    i := l;
    j := r;
    while i <= j do begin
        while a[i] < a[x] do i := i+1;
        while a[j] > a[x] do j := j-1;
        if i <= j then begin
            with tmp: integer; do begin 
                tmp := a[i]; a[i] := a[j]; a[j] := tmp;
            end
            i := i+1;
            j := j-1;
        end
    end
    sort(l, j);
    sort(i, r);
end

function ha_check_arr(): integer;
var i: integer;
begin
    with res: integer; do begin
        res := 0;
        for i := 1 to n do res := (res + a[i] * i mod m) mod m;
        return res;
    end
end

procedure ha_log_arr();
var i: integer;
begin
    for i := 1 to n do ha_i_space(a[i]);
    putLn();
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end

"""
        expect = r"""1 2 2 1995 1983 1963 1951 1995 178 542 914 574 63 1887 1415 691 407 454 1731 1380 1210 107 1472 1991 85 279 497 375 1134 1902 1170 1893 999 1416 252 1083 244 394 206 1039 296 726 994 78 252 444 324 1193 286 80 
1 2 2 63 78 80 85 107 178 407 454 542 574 691 914 1415 1210 1380 1472 1731 1887 1951 206 252 252 279 375 286 296 324 444 497 726 994 999 1039 244 394 1083 1134 1170 1193 1416 1893 1902 1963 1983 1991 1995 1995 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 249))


    def test_150(self):
        input = r"""

var n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i: integer;
begin
    // n := 50; m := 1997;
    n := 50000; m := 1000000009;
    a[1] := 1;
    a[2] := 2;
    for i := 3 to n do a[i] := ((3 * a[i-1]) mod m - (4 * a[i-2]) mod m + m) mod m;

    // ha_log_arr();
    ha_i_space(ha_check_arr());

    sort(1, n);

    // ha_log_arr();
    ha_i_space(ha_check_arr());
end

procedure sort(l, r: integer);
var x,i,j: integer;
begin
    if l >= r then return;
    x := (l+r) div 2;
    i := l;
    j := r;
    while i <= j do begin
        while a[i] < a[x] do i := i+1;
        while a[j] > a[x] do j := j-1;
        if i <= j then begin
            with tmp: integer; do begin 
                tmp := a[i]; a[i] := a[j]; a[j] := tmp;
            end
            i := i+1;
            j := j-1;
        end
    end
    sort(l, j);
    sort(i, r);
end

function ha_check_arr(): integer;
var i: integer;
begin
    with res: integer; do begin
        res := 0;
        for i := 1 to n do res := (res + a[i] * i mod m) mod m;
        return res;
    end
end

procedure ha_log_arr();
var i: integer;
begin
    for i := 1 to n do ha_i_space(a[i]);
    putLn();
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end

"""
        expect = r"""15123137 270342704 """
        self.assertTrue(TestCodeGen.test(input, expect, 250))



    def test_151(self):
        input = r"""

var x, n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i, j: integer;
begin
    m := 10007;
    for i := 1 to 8 do begin
        with l, r: integer; do begin
            if i > 4 then begin
                l := 50; r := 55;
            end else begin
                l := 0; r := 5;
            end
            for j := l to r do begin
                ha_i_space(i); putString("^ ");
                ha_i_space(j); putString("= ");
                putIntLn(pow(i,j));
            end
        end
    end
end

function pow(x, n: integer): integer;
begin
    if n = 0 then return 1;
    with res: integer; do begin
        res := pow(x, n div 2);
        res := (res * res) mod m;
        if n mod 2 = 1 then res := (res * x) mod m;
        return res;
    end
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end


"""
        expect = r"""1 ^ 0 = 1
1 ^ 1 = 1
1 ^ 2 = 1
1 ^ 3 = 1
1 ^ 4 = 1
1 ^ 5 = 1
2 ^ 0 = 1
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16
2 ^ 5 = 32
3 ^ 0 = 1
3 ^ 1 = 3
3 ^ 2 = 9
3 ^ 3 = 27
3 ^ 4 = 81
3 ^ 5 = 243
4 ^ 0 = 1
4 ^ 1 = 4
4 ^ 2 = 16
4 ^ 3 = 64
4 ^ 4 = 256
4 ^ 5 = 1024
5 ^ 50 = 434
5 ^ 51 = 2170
5 ^ 52 = 843
5 ^ 53 = 4215
5 ^ 54 = 1061
5 ^ 55 = 5305
6 ^ 50 = 1855
6 ^ 51 = 1123
6 ^ 52 = 6738
6 ^ 53 = 400
6 ^ 54 = 2400
6 ^ 55 = 4393
7 ^ 50 = 6035
7 ^ 51 = 2217
7 ^ 52 = 5512
7 ^ 53 = 8563
7 ^ 54 = 9906
7 ^ 55 = 9300
8 ^ 50 = 2485
8 ^ 51 = 9873
8 ^ 52 = 8935
8 ^ 53 = 1431
8 ^ 54 = 1441
8 ^ 55 = 1521
"""
        self.assertTrue(TestCodeGen.test(input, expect, 251))


    def test_152(self):
        input = r"""

var x, n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i, j: integer;
begin
    m := 10007;
    ha_i_space(pow(1, 2000000000));
    ha_i_space(pow(4, 2000000000));
    ha_i_space(pow(15, 2000000000));
    ha_i_space(pow(27, 2000000000));
    ha_i_space(pow(79, 2000000000));
    ha_i_space(pow(128, 2000000000));
    ha_i_space(pow(9246, 2000000000));
    ha_i_space(pow(14942, 2000000000));
    ha_i_space(pow(29265, 2000000000));
    ha_i_space(pow(667999, 2000000000));
    ha_i_space(pow(1937815, 2000000000));
    ha_i_space(pow(6111917, 2000000000));
    ha_i_space(pow(59684905, 2000000000));
    ha_i_space(pow(793800323, 2000000000));
end

function pow(x, n: integer): integer;
begin
    if n = 0 then return 1;
    with res: integer; do begin
        res := pow(x, n div 2);
        res := (res * res) mod m;
        if n mod 2 = 1 then res := (res * x) mod m;
        return res;
    end
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end


"""
        expect = r"""1 3443 4095 9151 1264 3505 7134 1733 1738 9785 647 5510 7772 1554 """
        self.assertTrue(TestCodeGen.test(input, expect, 252))


    def test_153(self):
        input = r"""

var x, n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i, j: integer;
begin
    ha_i_space(inc(1));
    ha_i_space(inc(inc(1)));
    ha_i_space(inc(inc(inc(1))));
    ha_i_space(inc(inc(inc(inc(1)))));
    ha_i_space(inc(inc(inc(inc(inc(1))))));
    ha_i_space(inc(inc(inc(inc(inc(inc(1)))))));
end

function inc(i: integer): integer; begin return i+1; end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end


"""
        expect = r"""2 3 4 5 6 7 """
        self.assertTrue(TestCodeGen.test(input, expect, 253))


    def test_154(self):
        input = r"""

var n: integer;
var a: array[0 .. 100000] of real;

procedure main();
var i: integer;
begin
    n := 20;
    for i := 1 to n do a[i] := i * (i+1) * (i+2) / 6;
    ha_log_arr(a);
end

// function setRange(
//     a: array[0 .. 100000] of real; 
//     l, r: integer; 
//     v: real): array[0 .. 100000] of real; 
// var i: integer;
// begin
//     for i := l to r do a[i] := v;
//     return a;
// end

procedure ha_log_arr(a: array[0 .. 100000] of real);
var i: integer;
begin
    for i := 1 to n do ha_f_space(a[i]);
    putLN();
end

procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end

"""
        expect = r"""1.0 4.0 10.0 20.0 35.0 56.0 84.0 120.0 165.0 220.0 286.0 364.0 455.0 560.0 680.0 816.0 969.0 1140.0 1330.0 1540.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 254))


    def test_155(self):
        input = r"""

var n: integer;
var a: array[0 .. 100000] of real;

procedure main();
var i: integer;
begin
    n := 20;
    for i := 1 to n do a[i] := i * (i+1) * (i+2) / 6;
    ha_log_arr(a);
    ha_log_arr(SETRANGE(a, 3, 8, 1.9));
end

function setRange(
    a: array[0 .. 100000] of real; 
    l, r: integer; 
    v: real): array[0 .. 100000] of real; 
var i: integer;
begin
    for i := l to r do a[i] := v;
    return a;
end

procedure ha_log_arr(a: array[0 .. 100000] of real);
var i: integer;
begin
    for i := 1 to n do ha_f_space(a[i]);
    putLN();
end

procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end

"""
        expect = r"""1.0 4.0 10.0 20.0 35.0 56.0 84.0 120.0 165.0 220.0 286.0 364.0 455.0 560.0 680.0 816.0 969.0 1140.0 1330.0 1540.0 
1.0 4.0 1.9 1.9 1.9 1.9 1.9 1.9 165.0 220.0 286.0 364.0 455.0 560.0 680.0 816.0 969.0 1140.0 1330.0 1540.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 255))


    def test_156(self):
        input = r"""

var n: integer;
var a: array[0 .. 100000] of real;

procedure main();
var i: integer;
begin
    n := 20;
    for i := 1 to n do a[i] := i * (i+1) * (i+2) / 6;
    ha_log_arr(a);
    ha_log_arr(SETrange(SETRANGE(a, 3, 8, 1.9), 5, 15, 4.6));
end

function setRange(
    a: array[0 .. 100000] of real; 
    l, r: integer; 
    v: real): array[0 .. 100000] of real; 
var i: integer;
begin
    for i := l to r do a[i] := v;
    return a;
end

procedure ha_log_arr(a: array[0 .. 100000] of real);
var i: integer;
begin
    for i := 1 to n do ha_f_space(a[i]);
    putLN();
end

procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end

"""
        expect = r"""1.0 4.0 10.0 20.0 35.0 56.0 84.0 120.0 165.0 220.0 286.0 364.0 455.0 560.0 680.0 816.0 969.0 1140.0 1330.0 1540.0 
1.0 4.0 1.9 1.9 4.6 4.6 4.6 4.6 4.6 4.6 4.6 4.6 4.6 4.6 4.6 816.0 969.0 1140.0 1330.0 1540.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 256))


    def test_157(self):
        input = r"""

var n: integer;
var a: array[0 .. 100000] of real;

procedure main();
var i: integer;
begin
    n := 20;
    for i := 1 to n do a[i] := i * (i+1) * (i+2) / 6;
    ha_log_arr(a);
    ha_log_arr(setRange(SETrange(SETRANGE(a, 3, 8, 1.9), 5, 15, 4.6), 1, n-5, 1000.00001));
end

function setRange(
    a: array[0 .. 100000] of real; 
    l, r: integer; 
    v: real): array[0 .. 100000] of real; 
var i: integer;
begin
    for i := l to r do a[i] := v;
    return a;
end

procedure ha_log_arr(a: array[0 .. 100000] of real);
var i: integer;
begin
    for i := 1 to n do ha_f_space(a[i]);
    putLN();
end

procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end

"""
        expect = r"""1.0 4.0 10.0 20.0 35.0 56.0 84.0 120.0 165.0 220.0 286.0 364.0 455.0 560.0 680.0 816.0 969.0 1140.0 1330.0 1540.0 
1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0 816.0 969.0 1140.0 1330.0 1540.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 257))


    def test_158(self):
        input = r"""

procedure main();
begin
    with 
        i,j,k: integer;
        a,b,c: array[-1 .. 100000] of integer;
    do begin
        for i := -1 to 1000 do begin
            a[i] := i*i -i + 1000 mod (i+i*i*i-5*(i*i+4*3) mod (i+i-i*2*3*4 mod (1+2-3*4 mod 5+1)+1)+1);
        end
        for i := -1 to 50 do putInt(a[i] + b[i]);
    end
end

"""
        expect = r"""20012145244162350541342931110113211561182121012401272130613421380142014621506155216001650170217561812187019301992205621222190226023322406248225602640272228062892298030703162325633523450"""
        self.assertTrue(TestCodeGen.test(input, expect, 258))


    def test_159(self):
        input = r"""

var a: array[-1000 .. 1000] of string;

procedure main();
var a: array[-1000 .. 1000] of string;
begin
    with a: array[-1000 .. 1000] of string; do begin
    end
end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input, expect, 259))


    def test_160(self):
        input = r"""

procedure main();
var a: boolean;
begin
    a := True and then True and then False and then 5 mod 0 = 0;
    putBool(a);
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 260))


    def test_161(self):
        input = r"""

procedure main();
var a: boolean;
begin
    a := false or else true or else 5 mod 0 = 0;
    putBool(a);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 261))


    def test_162(self):
        input = r"""

procedure main();
begin
    putBoolln(retTrue() and then retTrue() and then retFalse() and then retTrue());
    putBoolln(retFalse() or else retFalse() or else retTrue() or else retFalse());
    putBoolln(retFalse() or else retFalse() or else retTrue() and then retTrue() and then retFalse() and then retTrue());
end

function retTrue(): boolean;
begin
    putString("retTrue; ");
    return true;
end

function retFalse(): boolean;
begin
    putString("retFalse; ");
    return false;
end

"""
        expect = r"""retTrue; retTrue; retFalse; false
retFalse; retFalse; retTrue; true
retFalse; retFalse; retTrue; retTrue; retFalse; false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 262))


    def test_163(self):
        input = r"""

procedure Main();
var a: integer;
begin
    a := 1;

    if a = 1 then
        with b: integer; do begin 
            putInt(a);
            b := 2;
            if b = 2 then
                with a: integer; do begin 
                    putInt(b);
                    a := 3;
                end
            else
                with b: integer; do begin 
                    putInt(a);
                    b := 4;
                end
        end
end

"""
        expect = r"""12"""
        self.assertTrue(TestCodeGen.test(input, expect, 263))


    def test_164(self):
        input = r"""

procedure Main();
begin
    FOO(10);
end

procedure FOO(x: integer);
var i: integer;
begin
    if x = 1 then return;
    else begin
        for i := x downto 1 do begin
            putIntLn(i);
            if i = 3 then return;
        end
    end
    FOO(x-1);
end

"""
        expect = r"""10
9
8
7
6
5
4
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 264))


    def test_165(self):
        input = r"""

procedure Main();
var x: array[0 .. 10] of string;
begin
    foo(x);
end

procedure FOO(a: array[0 .. 10] of string);
var i: integer;
begin
    for i := 0 to 10 do putStringLN(a[i]);
end

"""
        expect = r"""null
null
null
null
null
null
null
null
null
null
null
"""
        self.assertTrue(TestCodeGen.test(input, expect, 265))


    def test_166(self):
        input = r"""

procedure Main();
begin
    putFloatLn(1 / 0);
    putBoolLn(1/0 > 1000000000);
    putBoolLn(-1/0 > 1000000000);
end

"""
        expect = r"""Infinity
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 266))


    def test_167(self):
        input = r"""

procedure Main();
begin
    putboolln(true and then true and then 1 < 0 and then 5 div 0);
end

"""
        expect = r"""false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 267))


    def test_168(self):
        input = r"""

function getInt2(): integer; begin return 100; end
function getFloat2(): real; begin return 100.000005; end

procedure main();
var i,j,k: integer;
    main: string;
    a: array[-10000000 .. 10000000] of real;
    p,q: boolean;
begin
    j := 2; k := 3;
    for i := 1 to 5 do begin
        a[i+j*k] := a[j+i*k] := a[1] := a[0] := 5;
        putIntLN(i+j*k);
        putIntLN(j+i*k);
        for j := i+j*k downto i do begin
            p := false;
            while p do begin
                with main: integer; p: string; do begin
                    main := 5;
                    if main > j then break;
                    if getInt2() < main then continue;
                    main := getInt2();
                    putIntln(getInt2());
                    putIntLn(main);
                    with p: boolean; do begin
                        p := main < i+j*2 mod 5;
                        if i < j and then p then main := k;
                        else break;
                    end
                end
                p := false;
                break;
            end
            a[1] := getFloat2();
            putFloatLn(a[1]);
            PutFloat(GetFloat2());
        end
    end
end

"""
        expect = r"""7
5
100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.000012
6
100.00001
100.000016
10
100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.0000110
14
100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.0000114
18
100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001100.00001
100.00001"""
        self.assertTrue(TestCodeGen.test(input, expect, 268))


    def test_169(self):
        input = r"""

function getInt2(): integer; begin return 100; end
function getFloat2(): real; begin return 100.000005; end

procedure main();
var i,j,k: integer;
    main: string;
    a: array[-10000000 .. 10000000] of real;
    p,q: boolean;
begin
    i := 1; j := 2;
    for i := i+j to i+j+20 do begin
        putInt(i); putString(" "); putINtln(j);
        j := j - 1;
    end
end

"""
        expect = r"""3 2
4 1
5 0
6 -1
7 -2
8 -3
9 -4
10 -5
11 -6
12 -7
13 -8
14 -9
15 -10
16 -11
17 -12
18 -13
19 -14
20 -15
21 -16
22 -17
23 -18
24 -19
25 -20
"""
        self.assertTrue(TestCodeGen.test(input, expect, 269))


    def test_170(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function FOO(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
BEGIN
    i := x; j := y;
    while i < 1000 do begin
        a := a and then True and then False;
        putString(arr[100]);
        // if a then continue; else begin
        //     if a then return "1";
        //     else if a then return "2";
        //     else if a then return "3";
        //     else begin
        //         with a: integer; g: boolean; do begin
        //             a := x+y;
        //             g := b or else x>y;
        //             if a mod 10 = x and then b or else g then return "4";
        //             else continue;
        //         end
        //     end
        // end
        i := 1000;
        while i < 1000 do main();
        while i < 1000 do main();
        // with i: string; do begin
        //     while b do begin
        //         putString("7");
        //         break;
        //     end
        //     return foo(True, True, j,x,y);
        // end
    end
    while i < 1000 do main();
    while i < 1000 do main();
    // with i: string; do begin
    //     while b do begin
    //         putString("8");
    //         break;
    //     end
    //     return foo(True, True, j,x,y);
    // end
    return "OK";
END

"""
        expect = r"""nullOK
"""
        self.assertTrue(TestCodeGen.test(input, expect, 270))


    def test_171(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function FOO(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
BEGIN
    i := x; j := y;
    while i < 1000 do begin
        a := a and then True and then False;
        putString(arr[100]);
        // if a then continue; else begin
        //     if a then return "1";
        //     else if a then return "2";
        //     else if a then return "3";
        //     else begin
        //         with a: integer; g: boolean; do begin
        //             a := x+y;
        //             g := b or else x>y;
        //             if a mod 10 = x and then b or else g then return "4";
        //             else continue;
        //         end
        //     end
        // end
        i := 1000;
        while i < 1000 do main();
        while i < 1000 do main();
        // with i: string; do begin
        //     while b do begin
        //         putString("7");
        //         break;
        //     end
        //     return foo(True, True, j,x,y);
        // end
    end
    while i < 1000 do main();
    while i < 1000 do main();
    with i: string; do begin
        while b do begin
            putString("8");
            break;
        end
    end
    return "OK";
END

"""
        expect = r"""nullOK
"""
        self.assertTrue(TestCodeGen.test(input, expect, 271))


    def test_172(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function FOO(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
BEGIN
    i := x; j := y;
    while i < 1000 do begin
        a := a and then True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "2";
            else if a then return "3";
            else begin
                with a: integer; g: boolean; do begin
                    a := x+y;
                    g := b or else x>y;
                    // if a mod 10 = x and then b or else g then return "4";
                    // else continue;
                end
            end
        end
        i := 1000;
        while i < 1000 do main();
        while i < 1000 do main();
        // with i: string; do begin
        //     while b do begin
        //         putString("7");
        //         break;
        //     end
        //     return foo(True, True, j,x,y);
        // end
    end
    while i < 1000 do main();
    while i < 1000 do main();
    with i: string; do begin
        while b do begin
            putString("8");
            break;
        end
    end
    return "OK";
END

"""
        expect = r"""nullOK
"""
        self.assertTrue(TestCodeGen.test(input, expect, 272))


    def test_173(self):
        input = r"""

procedure main();
begin
    putint(iSqrt(5));
end

function isqrt(a: integer): integer;
begin
    with l,r,x,m: integer; do begin
        l := 1;
        r := a;
        x := -1;
        while L <= R do begin
            M := (l+r) div 2;
            if m * M <= a then begin
                x := M;
                l := m+1;
            end else begin
                r := m-1;
            end
        end
        return x;
    end
end

"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 273))


    def test_174(self):
        input = r"""

procedure main();
begin
    putintln(foo(5));
end

function foo(a: integer): integer;
begin
    while true do begin
        with i: integer; do begin
            if false then return 2;
        end
        putLN();
        break;
    end
    putLn();
    return 5;
end

"""
        expect = r"""

5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 274))


    def test_175(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function FOO(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
BEGIN
    i := x; j := y;
    while i < 1000 do begin
        a := a and then True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "2";
            else if a then return "3";
            else begin
                with a: integer; g: boolean; do begin
                    a := x+y;
                    g := b or else x>y;
                    if a mod 10 = x and then b or else g then return "4";
                    // else continue;
                end
            end
        end
        i := 1000;
        while i < 1000 do main();
        while i < 1000 do main();
        with i: string; do begin
            while b do begin
                putString("7");
                break;
            end
            return foo(True, True, j,x,y);
        end
    end
    while i < 1000 do main();
    while i < 1000 do main();
    with i: string; do begin
        while b do begin
            putString("8");
            break;
        end
    end
    return "OK";
END

"""
        expect = r"""nullnull4
"""
        self.assertTrue(TestCodeGen.test(input, expect, 275))


    def test_176(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function FOO(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
BEGIN
    i := x; j := y;
    while i < 1000 do begin
        a := a and then True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "2";
            else if a then return "3";
            else begin
                with a: integer; g: boolean; do begin
                    a := x+y;
                    g := b or else x>y;
                    if a mod 10 = x and then b or else g then return "4";
                    else begin 
                        i := 1000;
                        continue;
                    end
                end
            end
        end
        i := 1000;
        while i < 1000 do main();
        while i < 1000 do main();
        with i: string; do begin
            while b do begin
                putString("7");
                break;
            end
            return foo(True, True, j,x,y);
        end
    end
    while i < 1000 do main();
    while i < 1000 do main();
    with i: string; do begin
        while b do begin
            putString("8");
            break;
        end
    end
    return "OK";
END

"""
        expect = r"""nullOK
"""
        self.assertTrue(TestCodeGen.test(input, expect, 276))


    def test_177(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
begin
    return;
end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input, expect, 277))


    def test_178(self):
        input = r"""

procedure main();
begin
    foo();
    return;
end

procedure foo();
begin
    return;
end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input, expect, 278))


    def test_179(self):
        input = r"""

procedure main();
begin
    putInt(foo(3));
end

function foo(n: integer): integer;
begin
    if n <= 1 then return 1;
    else return n*foo(n-1);
end

"""
        expect = r"""6"""
        self.assertTrue(TestCodeGen.test(input, expect, 279))


    def test_180(self):
        input = r"""

procedure main();
begin
    putInt(foo(3));
end

function foo(n: integer): integer;
begin
    if n <= 1 then return 1;
    return 5;
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 280))



    def test_181(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
begin
    if true then begin
        while true do return 5;
    end
    return 6;
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 281))


    def test_182(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    if true then begin
        for i := 1 to 10 do return 5;
    end
    return 6;
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 282))


    def test_183(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    if true then begin
        while true do begin
            if true then begin
                return 5;
            end
        end
    end
    return 6;
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 283))


    def test_184(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    if true then begin
        while true do begin
            if true then begin
                return 5;
            end
        end
        return 6;
    end else begin
        return 7;
    end
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 284))


    def test_185(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    if true then begin
        while true do begin
            if true then begin
                return 5;
            end
        end
        return 6;
    end else begin
        while true do begin
            if true then begin
                return 7;
            end
        end
        return 8;
    end
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 285))


    def test_186(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    while true do begin
        if true then begin
            return 1;
        end else return 2;
    end
    if true then begin
        while true do begin
            if true then begin
                return 5;
            end
        end
        return 6;
    end else begin
        while true do begin
            if true then begin
                return 7;
            end
        end
        return 8;
    end
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 286))


    def test_187(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    while false do begin
        if true then begin
            return 1;
        end else return 2;
    end
    if true then begin
        while true do begin
            if true then begin
                break;
            end
        end
        return 6;
    end else begin
        while true do begin
            if true then begin
                return 7;
            end
        end
        return 8;
    end
end

"""
        expect = r"""6"""
        self.assertTrue(TestCodeGen.test(input, expect, 287))


    def test_188(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    if true then begin
        while true do begin
            with i: integer; do begin
                if true then break;
            end
        end
        with i: integer; do begin
            if true then return 5;
            else return 6;
        end
    end else begin
        return 7;
    end
end

"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 288))


    def test_189(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    for i := 1 to 10 do begin
        return 5;
    end
    return 6;
end


"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 289))


    def test_190(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 290))


    def test_191(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 291))


    def test_192(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 292))


    def test_193(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 293))


    def test_194(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 294))


    def test_195(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 295))


    def test_196(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 296))


    def test_197(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 297))


    def test_198(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 298))


    def test_199(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 299))


    def test_200(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 300))

