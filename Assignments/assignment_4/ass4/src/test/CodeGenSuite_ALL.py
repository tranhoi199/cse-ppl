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

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 266))


    def test_167(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 267))


    def test_168(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 268))


    def test_169(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 269))


    def test_170(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 270))


    def test_171(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 271))


    def test_172(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 272))


    def test_173(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 273))


    def test_174(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 274))


    def test_175(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 275))


    def test_176(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 276))


    def test_177(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 277))


    def test_178(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 278))


    def test_179(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 279))


    def test_180(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 280))




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



    def test_500(self):
        input = """
        var x:integer;
        procedure main();
        begin
            x := 1;
            foo(x, 1.0);
            putInt(x);
        end

        procedure foo(i: integer; f: real);
        var bar:boolean;
        begin
            bar := true;
            putBool(bar);
            i := 2;
            putInt(i);
        end
        """
        expect = "true21"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_with_501(self):
        input = """
        var i:integer;
        procedure main();
        begin
            i := 1;
            with i:integer; do
            begin
                i := 2;
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_if_502(self):
        input = """
        procedure main();
        begin
            if true then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_if_503(self):
        input = """
        procedure main();
        begin
            if false then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_for_504(self):
        input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_array_505(self):
        input = """
        var a:array[-1 .. 1] of integer;
        var b:array[3 .. 5] of real;
        procedure main();
        begin
            a[0] := 1;
            b[4] := 2.0;
            putInt(a[0]);
            putFloat(b[4]);
        end
        """
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_array_khoa_506(self):
        input = """
		procedure main();
		var x: array [1 .. 5] of integer;
		begin
			x[2] := 3;
			putInt(x[2]);
			return;
		end
		"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_binop_507(self):
        input = """
		procedure main();
		begin
			putIntLn(1+2);
            putIntLn(1-2);
            putIntLn(1*2);
            putIntLn(1 div 2);
            putIntLn(31 mod 4);
            putFloatLn(1/2);
            putBoolLn(1 > 2);
            putBoolLn(1 < 2);
            putBoolLn(1 <= 2);
			return;
		end
		"""
        expect = "3\n-1\n2\n0\n3\n0.5\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_binop_508(self):
        input = """
		procedure main();
		begin
            // same result as AND
			putBoolLn(true and then false);
            putBoolLn(true and then true);
            putBoolLn(false and then true);
            putBoolLn(false and then false);
            // skip evaluation of the second operand --> no error
            putBoolLn(false and then 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_binop_509(self):
        input = """
		procedure main();
		begin
            // same result as OR
			putBoolLn(false or else false);
            putBoolLn(false or else true);
            putBoolLn(true or else true);
            putBoolLn(true or else false);
            // skip evaluation of the second operand --> no error
            putBoolLn(true or else 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_binop_510(self):
        input = """
        function foo():real;
        begin
            return 1;
        end

		procedure main();
		begin
            putFloat(foo());
		end
		"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_array_511(self):
        input = """
        function foo(): array [-2 .. 2] of string;
        var x: array [-2 .. 2] of string;
        i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "HELLO";
            return x;
        end

        procedure printArray(a : array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                putStringLn(a[i]);
        end

		procedure main();
		begin
            printArray(foo());
		end
		"""
        expect = "HELLO\nHELLO\nHELLO\nHELLO\nHELLO\n"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_array_512(self):
        input = """
        procedure hello(x: array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "HELLO";
        end

        procedure goodbye(x: array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                x[i] := "GOODBYE";
        end

        procedure printArray(a : array [-2 .. 2] of string);
        var i:integer;
        begin
            for i := -2 to 2 do
                putStringLn(a[i]);
        end

		procedure main();
        var arr : array[-2 .. 2] of string;
        i:integer;
		begin
            // Init array
            for i := -2 to 2 do
                arr[i] := "HI"; 
            hello(arr);
            printArray(arr);
            goodbye(arr);
            printArray(arr);
		end
		"""
        expect = "HI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\nHI\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_global_array_init_513(self):
        input = """
        var a : array [0 .. 4] of integer;

        procedure main();
        begin
        end
		"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_while_514(self):
        input = """
        procedure main();
        var i:integer;
        begin
            i := 0;
            while i < 5 do
            begin
                putInt(i);
                i := i + 1;
            end
        end
		"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_while_515(self):
        input = """
        procedure main();
        var i:integer;
        begin
            i := 0;
            while true do
            begin
                if i = 5 then break;
                putInt(i);
                i := i + 1;
            end
        end
		"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_array_516(self):
        input = """
        procedure main();
        var a:array [1 .. 3] of integer;
        i:integer;
        begin
            for i:=1 to 3 do
            begin
                a[i] := i;
                putInt(a[i]);
            end     
        end
		"""
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_exp_517(self):
        input = """
        procedure main();
        begin
            putInt(1+1-2*3);
        end
		"""
        expect = "-4"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_exp_518(self):
        input = """
        procedure main();
        begin
            putFloatLn(-2/5);
            putIntLn((27 mod 8));
            putIntLn(27 div -3);
            putInt(-28 div -3);
        end
		"""
        expect = "-0.4\n3\n-9\n9"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_exp_519(self):
        input = """
        procedure main();
        begin
            putFloatLn(1/1);
            putFloatLn(1./1);
            putFloatLn(1/1.);
            putFloatLn(1./1.);
            putFloat(1./1. - 1/1);
        end
		"""
        expect = "1.0\n1.0\n1.0\n1.0\n0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_exp_520(self):
        input = """
        procedure main();
        begin
            putFloatLn(----------3.14e10);
            putIntLn(0 div 1);
            putFloat(-0 / -1);
        end
		"""
        expect = "3.13999995E10\n0\n-0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_exp_521(self):
        input = """
        procedure main();
        var x,y,z:integer;
        begin
            x := 1;
            y := 2;
            z := -5;
            putInt(x+y-z*3);
        end
		"""
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_exp_522(self):
        input = """
        procedure main();
        var x,y,z:integer;
        f,r:real;
        begin
            x := 1;
            y := 2;
            z := -5;
            f := x + y;
            r := f/2;
            putIntLn(x+y-z*3);
            putFloat(f*r*x);
        end
		"""
        expect = "18\n4.5"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_exp_523(self):
        input = """
        procedure main();
        begin
            putFloatLn(0);
            putBoolLn(true);
            putBool(false);
        end
		"""
        expect = "0.0\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_exp_524(self):
        input = """
        procedure main();
        begin
            putBool(true or false);
            putBool(true or true);
            putBool(false or true);
            putBool(false or false);
        end
		"""
        expect = "truetruetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_exp_525(self):
        input = """
        procedure main();
        begin
            putBool(true and false);
            putBool(true and true);
            putBool(false and true);
            putBool(false and false);
        end
		"""
        expect = "falsetruefalsefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_exp_526(self):
        input = """
        procedure main();
        begin
            putBool(not true);
            putBool(not false);
            putBool(not not true);
            putBool(not not false);
            putBool(not not not not (true and true));
        end
		"""
        expect = "falsetruetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_exp_527(self):
        input = """
        procedure main();
        begin
            putBool(1 > 2);
            putBool(1.0 < 2);
            putBool(-1 <= 10.0);
        end
		"""
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_exp_528(self):
        input = """
        procedure main();
        begin
            putBool(-5.0 >= -5.);
            putBool(1. = 1);
            putBool(0.0 <> 0);
        end
		"""
        expect = "truetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_exp_529(self):
        input = """
        procedure main();
        begin
            putBool(1-1 = 0);
            putBool(not (1 > 2));
            putBoolLn(1.*1 <> 1/1);
            putBoolLn(1 div 1 <> 1*1);
            putFloatLn(1.*1);
            putFloatLn(1/1);
        end
		"""
        expect = "truetruefalse\nfalse\n1.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_exp_530(self):
        input = """
        var a : integer;
        procedure main();
        begin
            a := -4;
            putBool((a/8 - 3) < 0);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_exp_531(self):
        input = """
        var a : integer;
        procedure main();
        begin
            a := -4;
            putBool(a = a);
            putBool(a = a*1.);
        end
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_exp_532(self):
        input = """
        var a : array [-100 .. 100] of real;
        procedure main();
        begin
            a[99] := 1;
            a[-99] := -1;
            putBool(1234567 = 1234567);
            putBool(a[99] + a[-99] = 0.0*2e10);
            putFloat(a[99]*a[99]-a[-99]-2);
        end
        """
        expect = "truetrue0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_exp_533(self):
        input = """
        var a : array [-100 .. 100] of real;
        b : array[0 .. 3] of integer;
        procedure main();
        begin
            b[0] := 0;
            b[1] := b[0] + 1;
            b[2] := b[1] + 1;
            b[3] := b[2] + 1;
            a[b[b[1]]] := b[b[0]] + 666;
            putFloat(a[1]);
        end
        """
        expect = "666.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_exp_534(self):
        input = """
        var a : array [1 .. 2] of real;
        b : array[0 .. 3] of integer;

        procedure main();
        begin
            b[1] := floatToInt(1.0);
            b[2] := floatToInt(2.5);
            putIntLn(b[1]);
            putIntLn(b[2]);
        end

        function intToFloat(i : integer) : real;
        begin
            return i * 1.0;
        end

        function floatToInt(f : real) : integer;
        var i, sign : integer;
        begin
            i := 0;
            if f >= 0 then
                sign := 1;
            else
                sign := -1;
            f := f * sign;
            while f >= 1 do
            begin
                f := f - 1;
                i := i + 1;
            end
            return i * sign;
        end
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_exp_535(self):
        input = """
        var a : array [1 .. 2] of real;
        b : array[0 .. 3] of integer;

        procedure main();
        begin
            b[1] := floatToInt(-5.0);
            b[2] := floatToInt(-3.9);
            putIntLn(b[1]);
            putIntLn(b[2]);
        end

        function intToFloat(i : integer) : real;
        begin
            return i * 1.0;
        end

        function floatToInt(f : real) : integer;
        var i, sign : integer;
        begin
            i := 0;
            if f >= 0 then
                sign := 1;
            else
                sign := -1;
            f := f * sign;
            while f >= 1 do
            begin
                f := f - 1;
                i := i + 1;
            end
            return i * sign;
        end
        """
        expect = "-5\n-3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_exp_536(self):
        input = """
        var a : array [1 .. 2] of real;
        b : array[0 .. 3] of integer;

        procedure main();
        begin
            putFloat(intToFloat(123));
            a[2] := a[1] := 0.001;
            putBool(a[1]*a[2] <> 0);
        end

        function intToFloat(i : integer) : real;
        begin
            return i * 1.0;
        end

        function floatToInt(f : real) : integer;
        var i, sign : integer;
        begin
            i := 0;
            if f >= 0 then
                sign := 1;
            else
                sign := -1;
            f := f * sign;
            while f >= 1 do
            begin
                f := f - 1;
                i := i + 1;
            end
            return i * sign;
        end
        """
        expect = "123.0true"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_exp_537(self):
        input = """
        procedure main();
        begin
            putboolln(T());
            putboolln(F());
            putboolln(T() and then foo());
            putboolln(F() and then foo());
        end

        function T():boolean;
        begin
            return TRUE;
        end

        function F():boolean;
        begin
            return FALSE;
        end

        function FOO():boolean;
        begin
            putString("FOO!");
            return false;
        end
        """
        expect = "true\nfalse\nFOO!false\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_exp_538(self):
        input = """
        var INTMAX, INTMIN:integer;
        procedure main();
        begin
            INTMAX := 2147483647;
            INTMIN := INTMAX*-1-1;
            putIntLn(INTMAX);
            putIntLn(INTMIN);
            putIntLn(INTMAX + INTMIN);
        end
        """
        expect = "2147483647\n-2147483648\n-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_array_539(self):
        input = """
            function func(x: array [1 .. 2] of real; i,j: integer; z: real): array [1 .. 2] of real;
            var t: integer;
            begin
                for t := i to j do 
                    x[t] := x[t] * 2 * z;
                return x; 
            end    

            procedure print(x: array [1 .. 2] of real);
            var i : integer;
            begin 
                for i := 1 to 2 do 
                    putFloatLn(x[i]);
            end 

            procedure main();
            var x: array [1 .. 2] of real; i : integer;
            begin 
                for i := 1 to 2 do 
                    x[i] := i;
                print(func(func(x,1,2,3),1,2,-1));
            end 
        """
        expect = "-12.0\n-24.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_if_540(self):
        input = """
        procedure main();
        begin
            if true then
                putString("TRUE");
        end
        """
        expect = "TRUE"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_if_541(self):
        input = """
        procedure main();
        begin
            if false then
                putString("TRUE");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_if_542(self):
        input = """
        procedure foo(i:integer);
        begin
            if i >= 0 then
                putStringLn("POSITIVE");
            else
                putStringLn("NEGATIVE");
        end

        procedure main();
        begin
            foo(100);
            foo(0);
            foo(-1);
        end
        """
        expect = "POSITIVE\nPOSITIVE\nNEGATIVE\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_if_543(self):
        input = """
        function abs(i:integer):integer;
        begin
            if i >= 0 then
                return i;
            else
                return -i;
        end

        procedure main();
        begin
            putIntLn(abs(167));
            putIntLn(abs(-167));
            putIntLn(abs(167)-abs(-167));
        end
        """
        expect = "167\n167\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_if_544(self):
        input = """
        function absFloat(i:integer):real;
        begin
            if i >= 0 then
                return i*1.;
            else
                return -i*1.;
        end

        procedure main();
        begin
            putFloatLn(absFloat(167));
            putFloatLn(absFloat(-167));
            putFloatLn(absFloat(167)-absFloat(-167));
        end
        """
        expect = "167.0\n167.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_if_545(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            putString("ABC");
        end
        """
        expect = "ABC"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_if_546(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            else
                putString("ABC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_if_547(self):
        input = """
        procedure main();
        begin
            if 10 = 10 then
            begin
                putString("10 = 10"); 
            end
            else
                putString("10 <> 10");
        end
        """
        expect = "10 = 10"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_if_548(self):
        input = """
        procedure main();
        begin
            if 10 <> 10 then
            begin end
            else
                putString("10 <> 10");
        end
        """
        expect = "10 <> 10"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_if_549(self):
        input = """
        procedure main();
        begin
            if 1.0 >= -1.0 then
                putStringLn("1.0 >= -1.0");
            putString("Hi");
        end
        """
        expect = "1.0 >= -1.0\nHi"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_assign_550(self):
        input = """
        var globalInt:integer;
        globalFloat:real;
        globalBool:boolean;

        procedure main();
        var localInt:integer;
        localFloat:real;
        localBool:boolean;
        begin
            globalInt := localInt := 0;
            globalFloat := localFloat := 1;
            localBool := globalBool := not not not true;
            putIntLn(globalInt);
            putIntLn(localInt);
            putFloatLn(globalFloat);
            putFloatLn(localFloat);
            putBoolLn(localBool);
            putBoolLn(globalBool);
        end
        """
        expect = "0\n0\n1.0\n1.0\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_assign_551(self):
        input = """
        var globalInt:integer;
        globalFloat:real;
        globalBool:boolean;
        globalArray:array [1 .. 5] of real;

        procedure main();
        var localInt:integer;
        localFloat:real;
        localBool:boolean;
        localArray:array [1 .. 5] of real;
        begin
            globalArray[1] := localArray[2] := localFloat := globalInt := (-1*-2 + 1) mod 3;
            putFloatLn(globalArray[1]);
            putFloatLn(localArray[2]);
            putFloatLn(localFloat);
            putIntLn(globalInt);
        end
        """
        expect = "0.0\n0.0\n0.0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_assign_552(self):
        input = """
        var a:array [-3 .. 3] of boolean;

        procedure main();
        begin
            a[-3] := A[3] := true;
            a[-2] := not a[-3];
            putBool(A[-3]);
            putBool(A[-2]);
        end
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 552))
        
    def test_assign_553(self):
        input = """
        var a:array [-3 .. 3] of integer;

        procedure main();
        begin
            a[0] := 1 * (2 + (3 * 4 + (5 - 10 div (2 + 3))));
            putInt(a[0]);
        end
        """
        expect = "17"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_assign_554(self):
        input = """
        var a:array [-3 .. 3] of integer;

        procedure main();
        begin
            a[0] := 1 * (2 + (3 * 4 + (5 - 10 div (2 + 3))));
            a[1] := -2 * - a[0] * 3;
            putInt(a[1]);
        end
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_assign_555(self):
        input = """
        procedure main();
        begin
            x := 37 div 5;
            x := x := x := x;
            putInt(x);
        end

        var x : integer;
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_assign_556(self):
        input = """
        procedure main();
        begin
            a := -1000000;
            b := 1000000;
            // swap
            t := a;
            a := b;
            b := t;
            putIntLn(a);
            putIntLn(b);
        end

        var a,b,t : integer;
        """
        expect = "1000000\n-1000000\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_while_557(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            while i < 5 do
            begin
                i := i + 1;
            end
            putInt(i);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_while_558(self):
        input = """
        procedure main();
        var i : integer;
        begin
            while FALSE do
                putString("FALSE");
            while -256 > -1 do
            begin
                putString("-256 > -1");
            end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_while_559(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 10;
            while i = 10 do
            begin
                putIntLn(i);
                i := 11;
            end
            putIntLn(i);
        end
        """
        expect = "10\n11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_while_560(self):
        input = """
        procedure main();
        var b : BOOLEAN;
        begin
            b := true;
            while B do
            begin
                b := not b;
                putBool(b);
            end
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_while_561(self):
        input = """
        procedure main();
        var a, b : real;
        begin
            a := 100;
            b := -100;
            while a <> b do
            begin
                a := -1 + a;
                b := 1 + b;
            end
            putFloat(a - b);
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_while_562(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            while i mod 3 = 0 do
            begin
                i := i + 3;
                if i = 99 then i := i + 1;
            end
            putInt(i);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_while_563(self):
        input = """
        function isPositive(i:integer):boolean;
        begin
            return i >= 0;
        end

        function getMaxInt():integer;
        var i: integer;
        begin
            i := 0;
            while isPositive(i) and isPositive(i + 1) do
            begin
                i := i + 1;
            end
            return i;
        end

        procedure main();
        var i : integer;
        begin
            putInt(getMaxInt());
        end
        """
        expect = "2147483647"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_while_564(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    j := j + 1;
                    counter := counter + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_while_565(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    k := 0;
                    while k < 5 do
                    begin
                        k := k + 1;
                        counter := counter + 1;
                    end
                    j := j + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        expect = "60"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_while_566(self):
        input = """
        procedure main();
        begin
            while not true do
                while not false do
                    while true do
                        WHILE TRUE and TRUE do
                            putInt(-999);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_for_567(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 9 do
                putInt(i);
        end
        """
        expect = "123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_for_568(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -5 to -1 do
                putInt(i);
        end
        """
        expect = "-5-4-3-2-1"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_for_569(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 3 do
            begin end
            putInt(i);
        end
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_for_570(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 9 downto 1 do
            begin
                putInt(i);
            end
        end
        """
        expect = "987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_for_571(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -1 downto -4 do
            begin
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "-1-2-3-4-5"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_for_572(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 0 to 10 do
            begin
                if i mod 2 = 0 then
                    putInt(i);
            end
        end
        """
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_for_573(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i := 0 to 10 do
                for j := 0 to 10 do
                    counter := counter + 1;
            putInt(counter);
        end
        """
        expect = "121"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_for_574(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            counter := 0;
            for i := 9 downto 1 do
                for j := 8 downto 1 do
                    for k:= 7 downto 1 do
                        counter := counter + 1;
            putBool(counter = 7*8*9);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_for_575(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i:= 10 div 10 to 9 * 19 div 10 do
                while 5 > i do
                begin
                    putInt(i);
                    i := i + 1;
                end
            putStringLn("");
            putInt(i);
        end
        """
        expect = "1234\n18"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_for_576(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i:= 1 to 20000 do
                for j := 20000 downto 1 do
                    counter := counter - 1;
            putInt(counter);
        end
        """
        expect = "-400000000"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_for_577(self):
        input = """
        procedure main();
        var i : integer;
        a : array[0 .. 5] of integer;
        begin
            for i := 0 to 5 do
                a[i] := i*100;
            for i := a[1] downto 95 do
                putIntLn(i);
            putIntLn(i);
        end
        """
        expect = "100\n99\n98\n97\n96\n95\n94\n"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_for_578(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=9 downto 5 do
                if i mod 3 = 0 then
                    putfloatln(i div 3);
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_for_579(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=-100 to 100 do
                for i:= 0 to 100 do begin end
            putInt(i);
        end
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_break_continue_580(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:= 0 to 10 do
                if i > 5 then break;
            putIntLn(i);

            for i:= 0 to 100 do
            begin
                if i >= 10 then continue;
                else putInt(i);
            end
        end
        """
        expect = "6\n0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_break_continue_581(self):
        input = """
        var i,j:integer;
        procedure main();
        begin
            while TRUE do
            begin
                putStringLn("LOOPING...");
                break;
            end
            for i:= 1 to 100 do
            begin
                while not not not false do
                    break;
                for j := -9 to -1 do
                begin
                    putInt(-(j*i));
                end
                break;
            end
        end
        """
        expect = "LOOPING...\n987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_break_continue_582(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_break_continue_583(self):
        input = """
        procedure main();
        var i: integer;
        begin
            while True do
            begin
                while true do
                begin
                    while not false do
                        break;
                    break;
                end
                break;
            end
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_break_continue_584(self):
        input = """
        var i : integer;
        procedure main();
        begin
            for i:=90 downto 0 do
                if i mod 10 <> 0 then continue;
                else
                    putFloatLn(i / 10);
        end
        """
        expect = "9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_return_585(self):
        input = """
        procedure main();
        begin
            if true then return;
            else putString("HUYTC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_return_586(self):
        input = """
        function fib(n:integer):integer; //calculate the nth Fibonacci number
        begin
            if n < 0 then return -1;
            else if n = 0 then return 0;
            else if n = 1 then return 1;
            else return fib(n - 1) + fib(n - 2);
        end

        procedure main();
        var i : integer;
        begin
            putIntLn(fib(-100));
            for i := 0 to 10 do
                putIntLn(fib(i));
        end
        """
        expect = "-1\n0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_return_587(self):
        input = """
        procedure foo(i:integer);
        begin
            if i >= 0 then
            begin
                putStringLn("POSITIVE");
                return;
            end
            putStringLn("NEGATIVE");
        end

        procedure main();
        begin
            foo(1);
            foo(2);
            foo(3);
            foo(-3);
            foo(-2);
            foo(0);
        end
        """
        expect = "POSITIVE\nPOSITIVE\nPOSITIVE\nNEGATIVE\nNEGATIVE\nPOSITIVE\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_with_588(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:integer; do
            begin
                i := 8;
                putIntLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_with_589(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:real; do
            begin
                i := 8;
                putFloatLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8.0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_with_590(self):
        input = """
        var i : integer;
        procedure foo();
        begin
            i := 0;
            putint(i);
            with i:integer; do
                with f,i:real; do
                    with i:boolean; do
                    begin
                        i := 1 > -5;
                        putBool(i);
                    end
        end

        procedure main();
        var i : integer;
        begin
            i := -1;
            putint(i);
            foo();
            putint(i);
        end
        """
        expect = "-10true-1"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_call_591(self):
        input = """
        procedure printSum(a,b,c:integer);
        begin
            putIntLn(a+b+c);
            a := 0;
            b := 0;
            c := 0;
        end

        procedure main();
        var a : integer;
        begin
            a := 1;
            printSum(a, 6, 7);
            putIntLn(a);
        end
        """
        expect = "14\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_call_592(self):
        input = """
        procedure foo(a:array [1 .. 5] of integer);
        begin
            with i:integer; do
            begin
                for i:= 1 to 5 do
                    a[i] := i;
            end
        end

        procedure main();
        var arr:array [1 .. 5] of integer;
        i:integer;
        begin
            for i:= 1 to 5 do
                arr[i] := 0;
            foo(arr);
            for i:= 1 to 5 do
                putInt(arr[i]);
        end
        """
        expect = "00000"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_call_593(self):
        input = """
        function newArray():array [-1 .. 1] of boolean;
        var a:array [-1 .. 1] of boolean;
        begin
            a[-1] := a[1] := true;
            a[0] := not a[-1];
            return a;
        end

        procedure printArray(a: array [-1 .. 1] of boolean);
        begin
            with i:integer; do
                for i:= -1 to 1 do
                    putBoolLn(a[i]);
        end

        procedure main();
        begin
            putBoolLn(newArray()[0]);
            printArray(newArray());
        end
        """
        expect = "false\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_call_594(self):
        input = """
        function newArray():array [0 .. 50] of integer;
        var a:array [0 .. 50] of integer;
        begin
            with i:integer; do
                for i:=0 to 50 do
                    a[i] := i;
            return a;
        end

        function sumArray(a: array [0 .. 50] of integer):integer;
        begin
            with i,sum:integer; do
            begin
                sum := 0;
                for i:= 0 to 50 do
                    sum := sum + a[i];
                return sum;
            end
        end

        procedure main();
        begin
            putInt(sumArray(newArray()));
        end
        """
        expect = "1275"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_call_595(self):
        input = """
        function sum(a,b:integer):integer;
        begin
            return a + b;
        end

        procedure main();
        begin
            putInt(sum(1,10) - sum(10,1));
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_call_596(self):
        input = """
        // Ascending bubble sort
        function sortArray(a: array [0 .. 9] of integer): array [0 .. 9] of integer;
        var i,j,temp : integer;
        begin
            for i := 0 to 8 do
                for j := 0 to 8 do
                    if a[j] > a[j+1] then
                    begin
                        temp := a[j];
                        a[j] := a[j+1];
                        a[j+1] := temp;
                    end
            return a;
        end

        procedure printArray(a: array [0 .. 9] of integer);
        var i:integer;
        begin
            for i:= 0 to 9 do
                putIntLn(a[i]);
        end

        procedure main();
        var myArray : array [0 .. 9] of integer;
        begin
            myArray[0] := 50;
            myArray[1] := 70;
            myArray[2] := 0;
            myArray[3] := 10;
            myArray[4] := 90;
            myArray[5] := 60;
            myArray[6] := 30;
            myArray[7] := 20;
            myArray[8] := 40;
            myArray[9] := 80;

            printArray(sortArray(myArray));
        end
        """
        expect = "0\n10\n20\n30\n40\n50\n60\n70\n80\n90\n"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_call_597(self):
        input = """
        // Ascending bubble sort
        function sortArray(a: array [0 .. 9] of integer): array [0 .. 9] of integer;
        var i,j,temp : integer;
        begin
            for i := 0 to 8 do
                for j := 0 to 8 do
                    if a[j] > a[j+1] then
                    begin
                        temp := a[j];
                        a[j] := a[j+1];
                        a[j+1] := temp;
                    end
            return a;
        end

        procedure printArray(a: array [0 .. 9] of integer);
        var i:integer;
        begin
            for i:= 0 to 9 do
                putIntLn(a[i]);
        end

        procedure main();
        var myArray : array [0 .. 9] of integer;
        begin
            myArray[0] := 50;
            myArray[1] := 70;
            myArray[2] := 0;
            myArray[3] := 10;
            myArray[4] := 90;
            myArray[5] := 60;
            myArray[6] := 30;
            myArray[7] := 20;
            myArray[8] := 40;
            myArray[9] := 80;

            printArray(sortArray(myArray));
            printArray(myArray);
        end
        """
        expect = "0\n10\n20\n30\n40\n50\n60\n70\n80\n90\n50\n70\n0\n10\n90\n60\n30\n20\n40\n80\n"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_call_598(self):
        input = """
        procedure print(s:string);
        begin
            putStringLn(s);
        end

        function helloWorld():String;
        begin
            return "HELLO WORLD";
        end

        procedure main();
        begin
            print("TEST");
            print(helloWorld());
        end
        """
        expect = "TEST\nHELLO WORLD\n"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_call_599(self):
        input = """
        function finalTest():real;
        begin
            return 420/420;
        end

        procedure main();
        begin
            putFloatLn(100*finalTest()*100 - 1e4);
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))



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
