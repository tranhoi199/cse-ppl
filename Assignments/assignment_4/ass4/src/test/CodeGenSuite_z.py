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
