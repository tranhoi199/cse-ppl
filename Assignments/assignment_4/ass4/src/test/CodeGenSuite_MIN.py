import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test_06c0aee18445cb270f14(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 101))


    def test_1723ccdd3d0c654e4082(self):
        input = r"""

procedure main(); 
begin 
    putIntLn(1);
end

"""
        expect = r"""1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 102))


    def test_290050fcc741b8d81b3a(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.5);
end

"""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 103))


    def test_1e0d85eae643dc83d9a8(self):
        input = r"""

procedure main(); 
begin 
    putFloat(0.5);
end

"""
        expect = r"""0.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 104))


    def test_822338dc3518a87abbff(self):
        input = r"""

procedure main(); 
begin 
    putFloat(0.005);
end

"""
        expect = r"""0.005"""
        self.assertTrue(TestCodeGen.test(input, expect, 105))


    def test_50c83d6f9a43bbec47f8(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1000.0001);
end

"""
        expect = r"""1000.0001"""
        self.assertTrue(TestCodeGen.test(input, expect, 106))


    def test_7dd0b3eb28254558a770(self):
        input = r"""

procedure main(); 
begin 
    putFloatLn(999.8999999);
end

"""
        expect = r"""999.9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 107))


    def test_2eedeed989e4e064fe11(self):
        input = r"""

procedure main(); 
begin 
    putBool(True);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 108))


    def test_52ff52bda82656ccf32b(self):
        input = r"""

procedure main(); 
begin 
    putBool(falSE);
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 109))


    def test_c598b2f8958152931618(self):
        input = r"""

procedure main(); 
begin 
    putBoolLn(FalSE);
end

"""
        expect = r"""false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 110))


    def test_8638f5f0ef1bbbbec33e(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2);
end

"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 111))


    def test_2940f06698a8f084cb15(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2+3+4+5);
end

"""
        expect = r"""15"""
        self.assertTrue(TestCodeGen.test(input, expect, 112))


    def test_8f57401b5ad30ceb9d1c(self):
        input = r"""

procedure main(); 
begin 
    putInt(2-1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 113))


    def test_ed0d4c3356bf290ac5ef(self):
        input = r"""

procedure main(); 
begin 
    putInt(1-2);
end

"""
        expect = r"""-1"""
        self.assertTrue(TestCodeGen.test(input, expect, 114))


    def test_c1540b8a711fed4d1ae6(self):
        input = r"""

procedure main(); 
begin 
    putInt(1+2-3+4-5+6-7-8-9);
end

"""
        expect = r"""-19"""
        self.assertTrue(TestCodeGen.test(input, expect, 115))


    def test_c12bda90a861ddbb06c4(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6);
end

"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 116))


    def test_67c1f299c7f7683e7248(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6*9*1*2);
end

"""
        expect = r"""432"""
        self.assertTrue(TestCodeGen.test(input, expect, 117))


    def test_d42063c876302af6ad87(self):
        input = r"""

procedure main(); 
begin 
    putInt(4*6*9 - 9*4*6);
end

"""
        expect = r"""0"""
        self.assertTrue(TestCodeGen.test(input, expect, 118))


    def test_4d9cf1af7dc804429901(self):
        input = r"""

procedure main(); 
begin 
    putInt(1*2*3 + 4*5*6 - 5*6 + 123-456);
end

"""
        expect = r"""-237"""
        self.assertTrue(TestCodeGen.test(input, expect, 119))


    def test_88c3964aa92c934443a4(self):
        input = r"""

procedure main(); 
begin 
    putInt(5 div 2);
end

"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 120))


    def test_b3deacceaf1856a6ccc4(self):
        input = r"""

procedure main(); 
begin 
    putInt(198 div 8);
end

"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 121))


    def test_0e59df35662ed1d39a45(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.5 + 456);
end

"""
        expect = r"""579.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 122))


    def test_ac440f5477437985cb0a(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.5 + 456.1);
end

"""
        expect = r"""579.6"""
        self.assertTrue(TestCodeGen.test(input, expect, 123))


    def test_a2d009eb23eeb94d6fb9(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.2+3.4-5.6+7.8);
end

"""
        expect = r"""6.8000007"""
        self.assertTrue(TestCodeGen.test(input, expect, 124))


    def test_574f8208ca5619399813(self):
        input = r"""

procedure main(); 
begin 
    putFloat(1.2 * 5.4);
end

"""
        expect = r"""6.4800005"""
        self.assertTrue(TestCodeGen.test(input, expect, 125))


    def test_609b614251c2a11b409d(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 2);
end

"""
        expect = r"""61.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 126))


    def test_35e68580b655f8efe1bb(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 127))


    def test_f1dc799502560257772e(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 3 + 46/5/1/1/1/2/4);
end

"""
        expect = r"""42.15"""
        self.assertTrue(TestCodeGen.test(input, expect, 128))


    def test_d5cb056a08ce17fa6718(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123 / 2.3);
end

"""
        expect = r"""53.478264"""
        self.assertTrue(TestCodeGen.test(input, expect, 129))


    def test_e68d6741c8dbc0f9d122(self):
        input = r"""

procedure main(); 
begin 
    putFloat(123.1/5 + 123/5.1 - (123*5.1 + 123.1*5) - 123/(123/123*123+1) - 123.123*321.213-1);
end

"""
        expect = r"""-40744.766"""
        self.assertTrue(TestCodeGen.test(input, expect, 130))


    def test_da10e0c1eb881e388e9c(self):
        input = r"""

procedure main(); 
begin 
    putBool(True and false);
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 131))


    def test_5406d6008a259e82dfbd(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 132))


    def test_95db8343726f3fed0737(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and True);
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 133))


    def test_d1fb9a311e9c6b9a1487(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and false or (False and true));
end

"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 134))


    def test_4c8556f44353b416b673(self):
        input = r"""

procedure main(); 
begin 
    putBool(FALSE OR TRUE and false or (False or true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 135))


    def test_d8b76217676cedaa4549(self):
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


    def test_f74cd2bd5f6c69ea4f7a(self):
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


    def test_0799ff8fee6c5dfa469f(self):
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


    def test_deef57f229e08aa8aebb(self):
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


    def test_5430f0595677cbae12e5(self):
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


    def test_b758eda00cc4ba1465fb(self):
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


    def test_ad644ff10db9d2001f43(self):
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


    def test_44cc44f31fac658bee13(self):
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


    def test_ada57044f9490b2e7185(self):
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


    def test_ceda0aad94e3f518b73d(self):
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


    def test_d84d50b091b665231aee(self):
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


    def test_3a7a5fbea3aac0579f64(self):
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


    def test_4006aac057272ce9ec87(self):
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


    def test_fe397978731a56fb3ab7(self):
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


    def test_48be4ecdfa344d55ab57(self):
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


    def test_880c57907745fd94bb06(self):
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


    def test_6da4677d2913d7435088(self):
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


    def test_23107bb512a4dc870c74(self):
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


    def test_63789dd635bb02be4034(self):
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


    def test_3f5ed12540cb596e7e95(self):
        input = r"""

procedure main();
begin
    putString("Hello World");
end

"""
        expect = r"""Hello World"""
        self.assertTrue(TestCodeGen.test(input, expect, 155))


    def test_e299c13dace7ba8e5a85(self):
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


    def test_2be0986fe1a24950a1b5(self):
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


    def test_eaf79d5013db4778e55a(self):
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


    def test_e75ff488c60462318b3c(self):
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


    def test_38c1e8cec75b71e9abfd(self):
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


    def test_6fffd261237877f2c59c(self):
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


    def test_c5ca57799946e5c0fc5b(self):
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


    def test_eec51f52ead3f7e09a97(self):
        input = r"""

procedure main();
begin
    putBool(false or else false or else true and then (true or else false) and (false or else true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 163))


    def test_b4dbadb92ceed4cb38fc(self):
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


    def test_50097db3674a638cfa59(self):
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


    def test_4cea54c544a10db1b887(self):
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


    def test_c2daa2a604abf43d7cea(self):
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


    def test_080978283eec2287e743(self):
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


    def test_8209f043bcb1fc9e8a71(self):
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


    def test_77b503377ec5fbb49383(self):
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


    def test_f2f2db080870d7c9eade(self):
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


    def test_eab58593d252e3ef068e(self):
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


    def test_65e1f1c613e564a3d4c8(self):
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


    def test_ead9b774733eec7d98fd(self):
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


    def test_b989e356da7707cc3a1c(self):
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


    def test_4f6423dd3830f7b16c8c(self):
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


    def test_50ba037d851661b89482(self):
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


    def test_08838f329924e0a20589(self):
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


    def test_f3c80d676fd437d828c2(self):
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


    def test_e61431dbf3910dc6e7eb(self):
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


    def test_fd1b762bf8cf82985697(self):
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


    def test_506cb5295b64c3b7fef9(self):
        input = r"""

procedure main();
begin
    if 1 = 2 then putInt(100);
    else putInt(300);
end

"""
        expect = r"""300"""
        self.assertTrue(TestCodeGen.test(input, expect, 182))


    def test_4264f2af0ae94d252c77(self):
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


    def test_84d791dd586137a20e30(self):
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


    def test_e3c33a75f35dca4f7891(self):
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


    def test_122dd4a45b56065be5cc(self):
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


    def test_97cb6b333c48f28546f1(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 1 to 5 do putInt(i);
end

"""
        expect = r"""12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 187))


    def test_60deec6e4d45bfda4940(self):
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


    def test_9a3da5f30c8af375e040(self):
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


    def test_1acdab2adb31848afe2b(self):
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


    def test_4d9a5501d25830d7f9bb(self):
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


    def test_ee63d1d2d6daaa716653(self):
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


    def test_7605bb5cf3ba6c82644c(self):
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


    def test_5bff7ee9ee97583359df(self):
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


    def test_97815f90154f5ef99fbb(self):
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


    def test_50ed2c032fa8ebe0e522(self):
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


    def test_33fedb5eea3672935f7b(self):
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


    def test_682ab4c4818889126a3c(self):
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


    def test_7951431945c29fbaa7cd(self):
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


    def test_9b89c55fd8c2f52d1ea3(self):
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



    def test_c6d0a03d11f78ec289c2(self):
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


    def test_a15154dc87bf568f6703(self):
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


    def test_a978a163c35896bf7d0b(self):
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


    def test_e1a15d00768bce55230e(self):
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


    def test_4869156d1d9899ae2d80(self):
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


    def test_78942286ca6853c06afa(self):
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


    def test_d46d4b4cef6a59e29760(self):
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


    def test_a7d0853cfd4850e89865(self):
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


    def test_c9513c5a3aacc0416446(self):
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


    def test_35f55764fa654121d400(self):
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


    def test_4a9c8ffa1d1f5894ae47(self):
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


    def test_bdd581e556c823b286da(self):
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


    def test_e9a7d30655bf7c7fd21c(self):
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


    def test_05982a7cbd41a1e139b6(self):
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


    def test_e7854eb9abe6a9a8596f(self):
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


    def test_fd82d7af1c41dc07205d(self):
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


    def test_75c2a1d712a884602ed8(self):
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


    def test_81a425d2e079f3ed864e(self):
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


    def test_cb58ac35ceb48703707d(self):
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


    def test_f953e0bd7741544a325b(self):
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


    def test_64a2209257825616e41c(self):
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


    def test_78e1ccd32398d9fe04e9(self):
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


    def test_a513f383261c12ffcffa(self):
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


    def test_a2cea91d7cfbed48d083(self):
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


    def test_b596ad1457b5c73edec2(self):
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


    def test_ee84c0ac07051a02af7d(self):
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


    def test_b6af78021415d031e313(self):
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


    def test_62e3c412dd6b1e22beeb(self):
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


    def test_11050b13045aa349a582(self):
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


    def test_f731715cef2969b9c887(self):
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


    def test_763f741ca414852e6c93(self):
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


    def test_ca0f142153010630d210(self):
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


    def test_17fa68d028afbb177518(self):
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


    def test_b16374d45e6eca1aeb1f(self):
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


    def test_43c1a2da25489061fcdc(self):
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


    def test_dc27c0f4ebcec1658f85(self):
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


    def test_52a77e43c26906d5a6f8(self):
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


    def test_c5f3abba7bceaadec9a1(self):
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


    def test_2784831bbbc339a4b897(self):
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


    def test_b787f4955425b6a2a761(self):
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


    def test_459d25fd0446ee5790c8(self):
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


    def test_f4d65b182c0b4662ce41(self):
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


    def test_b3da9c064fef2b38080f(self):
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


    def test_3217668a550ad4de0eb9(self):
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


    def test_4f5d66003990c6a5f385(self):
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


    def test_0ae9b33c13fad98afe17(self):
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


    def test_9c88af687cb9201722fd(self):
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


    def test_a8f3ff6953977d07be4a(self):
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


    def test_568f02e1c32a295d833d(self):
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


    def test_bee43daaaecaad2059ba(self):
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



    def test_c0a12ac2e53af791e752(self):
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


    def test_5c13094a8e087b091d62(self):
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


    def test_096d849319a57e8ee0e6(self):
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


    def test_59ffe257e94ff77b077c(self):
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


    def test_eb3c146e46a65dad2c56(self):
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


    def test_7b9fab8f98a1af92b3ac(self):
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


    def test_316aca70fdb284e7e69f(self):
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


    def test_3c78599255dad2816a6c(self):
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


    def test_eab9f64d8180ae6f2801(self):
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


    def test_bb4e965fbb121080a70a(self):
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


    def test_f214abb593826b9f44fd(self):
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


    def test_dbe013275874de06a78c(self):
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


    def test_39b4f366fbb58dbfad17(self):
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


    def test_cec002d955c3f1b35501(self):
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


    def test_27937fad0cf1cfc9651a(self):
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


    def test_96b4ecae644027eb87d9(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 266))


    def test_c5f38089b6f33186dbe4(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 267))


    def test_c4ac31c565afd9755f3d(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 268))


    def test_765915906ab6675da6f5(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 269))


    def test_df05981fb7445620615b(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 270))


    def test_ac6258819faa2d6cadcc(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 271))


    def test_c996577800a7b5cce74e(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 272))


    def test_d0e442f83d3f4e2a7b2e(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 273))


    def test_8a732b117e1c25131e4f(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 274))


    def test_0c7c172b934602bf4f49(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 275))


    def test_a2ba29f922a2e5606a38(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 276))


    def test_2df125a3da0ee8184e8f(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 277))


    def test_19fd7f2e33d65657aa21(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 278))


    def test_d301dc15d71048715fdb(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 279))


    def test_bd10c443d5c5e5ed53bd(self):
        input = r"""

procedure main();
begin
    putInt(1);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 280))




    def test_065c0642cd6bd16c606b(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putBool"),[BinaryOp(">=",IntLiteral(1),IntLiteral(2))])])])
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input, expect, 281))
    def test_ff231d3aafc361c9241f(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 282))
    def test_b4786135e78168f7bb17(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 283))

    def test_1a69bf9ab6aec813b554(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 284))

    def test_56e496fe721861140ed5(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 285))
    def test_569999c36ceff02a8f2f(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 286))
    def test_8755267834feee2bdb39(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 287))
    def test_2b2c807daa362ca45fe9(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 288))
    def test_09135a4dfde291bb04cf(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 289))
    def test_10b9a548b7ab04811240(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 290))

    def test_14e780e3a3fbd6405e15(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 291))
    def test_72a8edf1dea8c0683a08(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 292))
    def test_e74ddf5aa7bb00643a68(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 293))
    def test_96275a44571c9db8b0ec(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 294))

    def test_091a38cd057383b9e833(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 295))

    def test_9b95e3f834d409a14a88(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 296))
    def test_e5cf4d9d460ec5be4449(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 297))
    def test_208fe2af376ccdf79823(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 298))

    def test_c7eb9db76006be35e846(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 299))

    def test_8c8f2e0e7aba89f4a84e(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 300))

    def test_e6fe22191c1edeee9117(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 301))

    def test_c12f97289a4199e83fd6(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 302))

    def test_29e08d2c805edd16b366(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 303))
    def test_973160917acb9eb7da32(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 304))
    def test_6217d5caa41fc8ba6b7b(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 305))
    def test_3d5b2891bcb100b4971a(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 306))

    def test_6c3e374b3e437f0d0722(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 307))

    def test_3709a54ae864da8103a5(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 308))
    def test_acc193fc4a9495154c8d(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 309))
    def test_6e5a305c362f7dafaccd(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 310))
    def test_0ad3d45578c9049e9e11(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 311))

    def test_062bc6a7cbabdf3d5053(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 312))

    def test_f4084e2fe9db74582697(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 313))
    def test_cd11a2a4529ff52f1d85(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 314))
    def test_9e7b430b0882062dd618(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 315))
    def test_43dc64197d729da91bc0(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 316))

    def test_5fb1a5a13d420afb2075(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 317))

    def test_5dbc718881e721b7bf2f(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 318))

    def test_ccfe66246867666411a4(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 319))

    def test_7f2d6fff1dc4b9365ee0(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 320))

    def test_34d91c32762dace2b3b0(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 321))

    def test_67ec963831632f0368dd(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 322))

    def test_34f48f20fe2d15fcfb14(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 323))

    def test_c967262f891a3bbd8cd4(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 324))
    def test_fb2a6c48e40e3abd6c7c(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 325))

    def test_27f7f8a9c61b8c79d78b(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 326))
    def test_e2e6ad10254fc5975043(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 327))

    def test_a2369033056cf6b56b19(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 328))

    def test_5a44aa51fbec54185e0c(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 329))

    def test_4c8b45c2fceea40ba5ed(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 330))

    def test_784904b4281580e10847(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 331))

    def test_a1a0df65625157bd7046(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 332))

    def test_49e55996ab54e4d2bdb9(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 333))

    def test_433c22310a25d9c9f221(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 334))

    def test_4d65c25b28eca36bc9bd(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 335))

    def test_291183e39547e531ccd5(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 336))

    def test_adb67ebd69b206a24573(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 337))


    def test_e0bc2b10edac4cac7829(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 338))

    def test_804fb3c558123587294a(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 339))
    def test_7b59e76288c96fefa5bf(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 340))

    def test_2b3b1259dba51ce66daf(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 341))

    def test_c79d87487b083867f299(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 342))

    def test_320ba5363336bd4bdf30(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 343))

    def test_05faf92e58a81cadbf66(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 344))

    def test_621868bdebcceb294f81(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 345))

    def test_b0ab2495fa426630ebc9(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 346))

    def test_7c9b964e95f86485e9f9(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 347))

    def test_a127bef22c7ebfcf3784(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 348))
    def test_549d1e0e0eef4002319a(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 349))

    def test_b5f321c1aab8b04ab344(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 350))

    def test_9baeeddf0c95f0a25475(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 351))

    def test_ea4d92de2b709efd409e(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 352))

    def test_ff4a508051800002fab6(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 353))

    def test_18791f61ca6182f23f94(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 354))

    def test_22413d3f58083c02c7b2(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 355))

    def test_54302586c823428e6b63(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 356))

    def test_42c08caf0a33b0df62d1(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 357))

    def test_899a34301945066d3575(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 358))

    def test_033fee82db9bb1aca8bf(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 359))

    def test_ab682f2f12234e875da8(self):
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
    	self.assertTrue(TestCodeGen.test(input, expect, 360))

    def test_0d9b8a7dc7e336a0eb51(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 361))

    def test_5dfc325d81ab4de9c461(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 362))

    def test_f0fad19709f0365756e0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 363))

    def test_e6f447b9f0963892c734(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 364))

    def test_2d68471247966739fa93(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 365))

    def test_884eab22b874f9e789db(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 366))

    def test_968b4d202d003ed7c42a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 367))

    def test_aa01d2bc26f6bce16ac1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 368))

    def test_d80c6fd895e74c9d0571(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 369))

    def test_edac3ebc3c6c802d5b27(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 370))

    def test_449a80592c918b7fafa8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 371))

    def test_743c138916394a155b18(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 372))

    def test_3aaa794f72401fe52b7d(self):
        input = """
        procedure main();
        begin
        putInt(1);
        end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 373))

    def test_de9a58f05012bb125454(self):
        input = """
        procedure main();
        begin
        putFloat(1.0);
        end
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 374))
    def test_9fcfc7c983b16f4a3340(self):
        input = """
        procedure main();
        begin
        putint(5);
        end
        """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input, expect, 375))
    def test_7048669fe05ac8cf2817(self):
        input = """
        procedure main();
        begin
        putint(6);
        end
        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 376))
    def test_12c0a0556ce1dadefc26(self):
        input = """
        procedure main();
        begin
        putint(7);
        end
        """
        expect = """7"""
        self.assertTrue(TestCodeGen.test(input, expect, 377))
    def test_ffcc8c91b9871adfc146(self):
        input = """
        procedure main();
        begin
        putint(8);
        end
        """
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input, expect, 378))
    def test_7b0a11f1e939289973c0(self):
        input = """
        procedure main();
        begin
        putint(9);
        end
        """
        expect = """9"""
        self.assertTrue(TestCodeGen.test(input, expect, 379))
    def test_8435d958849a7d7f1253(self):
        input = """
        procedure main();
        begin
        putint(10);
        end
        """
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input, expect, 380))
    def test_005c196e1bffb72e6c42(self):
        input = """
        procedure main();
        begin
        putint(11);
        end
        """
        expect = """11"""
        self.assertTrue(TestCodeGen.test(input, expect, 381))



    def test_4194dab2366442ed8b34(self):
        input = """
        procedure main();
        var a:integer;
        begin
        a := 1;
        putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 382))

    def test_037ab65e88a386b7a7fe(self):
        input = """
        procedure main();
        begin
        putFloat(100.02);
        end
        """
        expect = "100.02"
        self.assertTrue(TestCodeGen.test(input, expect, 383))

    def test_da0e72a128028914fb2e(self):
        input = """
        procedure main();
        begin
        putFloat(1.4315E7);
        end
        """
        expect = "1.4315E7"
        self.assertTrue(TestCodeGen.test(input, expect, 384))

    def test_f1b8b2b7f65f32d69b9f(self):
        input = """
        procedure main();
        begin
        putFloat(121.5E5);
        end
        """
        expect = "1.215E7"
        self.assertTrue(TestCodeGen.test(input, expect, 385))

    def test_88fd3d0600dbb2aef4c5(self):
        input = """
        procedure main();
        begin
            if (true)
                then putInt(1);
                else putInt(2);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 386))

    def test_a5fb9b6c986205b4571d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 387))

    def test_9b401b45b779e89e7761(self):
        input = """
        procedure main();
        begin
            putIntLn(000);
        end
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 388))

    def test_282c7252e1b63a0d8d1c(self):
        input = """        
        procedure main();
        begin
            putFloatLn(1.0);
        end"""
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 389))

    def test_9aae6d19f23b91e516c0(self):
        input = """
        procedure main();
        begin
            putFloatLn(10.5);
        end
        """
        expect = "10.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 390))
        
    def test_74996b63f4cf19487101(self):
        input = """
        procedure main();
        begin
            putFloatLn(100.14);
        end
        """
        expect = "100.14\n"
        self.assertTrue(TestCodeGen.test(input, expect, 391))

    def test_a2655dcddfaef2a71ebe(self):
        input = """
        procedure main();
        begin
            putBoolLn(true);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 392))

    def test_eb611a7e3a0e2429c483(self):
        input = """
        procedure main();
        begin
            putStringLn("programming");
        end
        """
        expect = "programming\n"
        self.assertTrue(TestCodeGen.test(input, expect, 393))

    def test_c8835bd33fe330716db2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 394))

    def test_30ebbf2e920f07a7070d(self):
        input =  """
        var a:array[1 .. 5] of integer;
        procedure main();
        begin
            putInt(10);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 395))
        
    def test_2a035c52861bc6033354(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 396))

    def test_1480c675e7da6c23756c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 397))

    def test_e9fd0c05a333d4c722a6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 398))


    def test_9e20bf1efb174c2212f8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 399))

    def test_7c2cb799a2ca4260a6fd(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 400))
        
    def test_a46f389ba4c8b9794995(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 401))

    def test_a73d208cb8730a75a783(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 402))

    def test_343f270d0a3433530e65(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 403))

    def test_426b7d6082c03461a49d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 404))

    def test_b4d3935af8826e7a65c1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 405))
        
    def test_f2b7e8801ebdec285f62(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 406))

    def test_a6eefb2aafcbd56573de(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 407))

    def test_3dea9f5e9504b2b02a2d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 408))

    def test_6ecc919c4effabf68086(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 409))
        
    def test_6fd31450adc0d4c1c74a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 410))

    def test_ed9c96859450f2b41fd8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 411))

    def test_c7ba1837235346f2fc5b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 412))

    def test_83f805a083c81c52d625(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 413))
        
    def test_6b0387a13184e4d5905b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 414))

    def test_d180019e7313e3f846c4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 415))

    def test_32da640ef30170001e51(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 416))

    def test_df5dccff78798972056b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 417))
        
    def test_3ee831c4cdfb24f2b4ec(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 418))

    def test_d89fda245dac744cc1c4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 419))

    def test_d8b470911a332ea8a822(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 420))

    def test_6f8e386c5c9fc2a4d56c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 421))

    def test_9743febc9330e5e5aa11(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 422))

    def test_18e55c2290dcb6a1ee4a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 423))

    def test_bdcbd6d06aa3ff572db9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 424))

    def test_73d36e5ad4c57ddd16a0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 425))
        
    def test_97e427f53fc84d2c6b67(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 426))

    def test_d56cea9f2f01b41c301f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 427))
        
    def test_d4def3de7ea2ba300edb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 428))
        
    def test_15569eff195c70fe3177(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 429))

    def test_4b78038efd65e5d6c3f0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 430))
        
    def test_c8207ee0c4289c1ca7b6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 431))

    def test_47f9fc289e93a1a55919(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 432))

    def test_4227221dd06a266dec65(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 433))
        
    def test_7049d330880a36d354c8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 434))

    def test_8ed3a0d86bac029a3abc(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 435))
        
    def test_4f3c5317bffdc7c3d931(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 436))

    def test_27e3e4b1a341d1667c38(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 437))

    def test_766df376558b78edb8b0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 438))

    def test_bd78e466107731c251ee(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 439))

    def test_9fe71302e91ebc388606(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 440))
        
    def test_d2c5196380d4c558b29f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 441))

    def test_466bbcc45f1e731ae869(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 442))

    def test_a1d0ad452c822a9af929(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 443))

    def test_b20ef714d767aeeaecb3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 444))
        
    def test_0534f0817b7fd654c7e1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 445))

    def test_ebd0134e1777eb84a8d5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 446))

    def test_5b8cb46580bb6ee7392f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 447))

    def test_80e254a3cc2bbbbe7b83(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 448))

    def test_0d1461fe6e1ead961f01(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 449))

    def test_3de5ff7a8b274d9acb4d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 450))

    def test_eca294b7a4abab9d1bef(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 451))
        
    def test_6c98736b35677ed6ad2a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 452))

    def test_f77b5aaabff3f25bd654(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 453))

    def test_c0deffdbee33b3919ba1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 454))

    def test_4a317c2429369c6addc8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 455))

    def test_9e43af5e14d48f386fb1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 456))
        
    def test_ec7461db121e5cc5c44e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 457))

    def test_8fe715b2d7816a773edc(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 458))

    def test_828cfcb4c151009edad8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 459))

    def test_8dc60dae31659e15f3f5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 460))

    def test_d67ce6b529cb19c228f6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 461))
        
    def test_9d3c8f1ca48d2912c500(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 462))

    def test_faf6e220b566fdac732a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 463))

    def test_2e9d889dfeacc5f4e9a7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 464))

    def test_3e958f8e9c76c0112e03(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 465))

    def test_00edd7764152c59e0374(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 466))
        
    def test_06be2f69ca0564778b40(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 467))

    def test_41a8521d93337b73ec0c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 468))


    def test_8c5769c141bb11913ad4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 469))

    def test_823847296873e374adc7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 470))



    def test_05ad93713102c422c399(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 471))

    def test_28368d3917fadf35a6eb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 472))

    def test_3ce1edcfa3ec1ef74751(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 473))

    def test_8d7a9f0f0acdccddad96(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 474))

    def test_7acaf293884668b2512f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 475))

    def test_3e7ccc3455227f119def(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 476))

    def test_c9ec7d9933ccf464a19f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 477))

    def test_011fd3a5550f1e9238f4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 478))

    def test_5eb5e0a9f75b45581888(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 479))

    def test_f8cdd6ed34de8421845d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 480))

    def test_13f10340fe3fc59cb20b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 481))

    def test_32cc68ab7e264f2e49bc(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 482))

    def test_252ea7e6cdc4631f25da(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 483))

    def test_8253004ff03c0738f9c9(self):
        input = """
        var a : array [0 .. 4] of integer;

        procedure main();
        begin
        end
		"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 484))

    def test_98f41790994bd5f203d8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 485))

    def test_f5440954b4f14370af6e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 486))

    def test_c69c4a0f367681d8fec4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 487))
    
    def test_52b3c5167089af370a89(self):
        input = """
        procedure main();
        begin
            putInt(1+1-2*3);
        end
		"""
        expect = "-4"
        self.assertTrue(TestCodeGen.test(input, expect, 488))

    def test_8c8701689cc9474ba316(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 489))

    def test_7950d8978e6732ece31e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 490))

    def test_f8fd62c8404685863388(self):
        input = """
        procedure main();
        begin
            putFloatLn(----------3.14e10);
            putIntLn(0 div 1);
            putFloat(-0 / -1);
        end
		"""
        expect = "3.13999995E10\n0\n-0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 491))

    def test_7cf89b2a7bd6411b34b4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 492))

    def test_ebcc7b13c8bc99053070(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 493))

    def test_34f1b3885315de962b91(self):
        input = """
        procedure main();
        begin
            putFloatLn(0);
            putBoolLn(true);
            putBool(false);
        end
		"""
        expect = "0.0\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 494))

    def test_e305d3859902c8073555(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 495))

    def test_8af73323b079d28ecfb5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 496))

    def test_03c8216571bb10c44460(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 497))

    def test_a56b5962f0866e459b81(self):
        input = """
        procedure main();
        begin
            putBool(1 > 2);
            putBool(1.0 < 2);
            putBool(-1 <= 10.0);
        end
		"""
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 498))

    def test_cfb8a8193791f1ea3ee0(self):
        input = """
        procedure main();
        begin
            putBool(-5.0 >= -5.);
            putBool(1. = 1);
            putBool(0.0 <> 0);
        end
		"""
        expect = "truetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 499))

    def test_7dad41aed37f8be25b6c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_f4c87f19e4dad8b4fe29(self):
        input = """
        var a : integer;
        procedure main();
        begin
            a := -4;
            putBool((a/8 - 3) < 0);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_53cf6e49854a463b864d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_1a13c28d6a52310f156e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_5f02899d10acad7af9ea(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_a1e93e1a9c6bb436f9cb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_aa1ec22856cfc5e312ee(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_e4e346101bcb49536155(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_3fbfc4b54edd50d68a13(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_e790f194c25ba356ac48(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_3ab6791a7177782d00c0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_faf6c6738da774feb6ff(self):
        input = """
        procedure main();
        begin
            if true then
                putString("TRUE");
        end
        """
        expect = "TRUE"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_c8265a22bc1d7b1a1028(self):
        input = """
        procedure main();
        begin
            if false then
                putString("TRUE");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_9c2dbcec048175757bf9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_08ffc2a9b0cfe6690206(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_61e15bcb394f3c1c1602(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_49f38b1c9a3502a5d78a(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            putString("ABC");
        end
        """
        expect = "ABC"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_4641e6e90501bc41e2b6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_d499b5b6b14ee59b9d58(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_a208fc7af25b3b0de62e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_aa93ccbd5017759122d5(self):
        input = """
        procedure main();
        begin
            if 1.0 >= -1.0 then
                putStringLn("1.0 >= -1.0");
            putString("Hi");
        end
        """
        expect = "1.0 >= -1.0\nHi"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_293957005b6dbe4afc1e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_76f625df519fae24e6c7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_5026d06f4c4d174f56ef(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 523))
        
    def test_9dabaa1bba03a2b2d602(self):
        input = """
        var a:array [-3 .. 3] of integer;

        procedure main();
        begin
            a[0] := 1 * (2 + (3 * 4 + (5 - 10 div (2 + 3))));
            putInt(a[0]);
        end
        """
        expect = "17"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_c06efa115e48fe3e578d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_38e37c9ddac5e74259a6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_4888d438d96e26bdf7ef(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_9b0051f629d9ddb8bae8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_8c986f2493603583b509(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_6ae3f1caeec98d7ca5cf(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_5f322364a37119db050b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_3715c2216bcd42588575(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_04a144d837c8fe9d08f0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_ca87dc6dacd237acc04c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_ba46de8371fa4a6f2efb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_9bf12e0d8a25f49a6cbf(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_2b221b8e85658bbdc393(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_f149bfcb6742adfb46b8(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 9 do
                putInt(i);
        end
        """
        expect = "123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_77eb8625dc3bcfbbd047(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -5 to -1 do
                putInt(i);
        end
        """
        expect = "-5-4-3-2-1"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_df4c020ea628d3e75c62(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_e96ba9ed05ff39781794(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_8d07bf8bbffc621994ca(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_411ae96b92e4af2f2d11(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_e7670cc12dbfcdc445ec(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_a5332835a0145b1b0713(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_68236cbc3ce7ce0e05f5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_6387cb5da4df3cd7231c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_99b7ad50aa2d4e1c2094(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_21943a2be248ad2b324c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_bdee424c169c0db4f655(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_e96cb0070ff73dff1ba1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_96a5096ac7683428394f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_aecf3965c132e29cde4e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_101e865315e926049e28(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_b6a60d60d472ff328221(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_33fd72db0db137f59809(self):
        input = """
        procedure main();
        begin
            if true then return;
            else putString("HUYTC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_e38e63e61632794d742e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_8af8331d740de7f7ce1e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_3a655bbfc846a2226cc5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_c91772cfd38a98d03673(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_a0d164009fdc039ace27(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_67f022a90283365fb8a1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_e3116eb39fc06bd96927(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_e9de324861850cf33503(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_fb33c7ff8ca869d8e16c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_4630783c43f304648f89(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_df78c53dd9a5466ea53f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_857a48d031967f938de0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_0e7903287acfbc5a918c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_48dae647464c60d1c63b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 570))



    def test_897a50d45dcc2d9347f6(self):
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

        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_7bcfab28d3fb4ad8cb4a(self):
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

        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_546410697ad0c0dc2aa7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_80ccf206c93f97f2c30e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_537cd2f98feda7d3c496(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_db111992609443154b43(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_5af8a189d74476dfa204(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_6b1c1dff7f82cdcbf7f3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_d15f8f9ecc312773bb9d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_ed25e7c797f82c6394e3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_789b51826e116669a7d5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_6802df4d134059bae51b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_b7cb25c96f77b1586163(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_6bc49e4956d8faccdbab(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_dc85f6c09cca23fefc70(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_ce6bbe7efcf1d934daf4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_3c847ad83aae235c28f3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_d39cfe27666dc4f4734d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_a171f6613ff801937cca(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_af3f6d39711c319b5263(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_f5f9959afe2f8193a1e6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_bdb92900ab320311d857(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_c9a23075563e12a5eda2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_d4b6f4b91918c0301327(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_d8151fae028587e91502(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_c4be864b812f677ec0db(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_99bb7ce3c708e8cd61f9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_6bac4d6ccac5d5a6b43d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_bdb8ac32078d0f3ef6ed(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_cb6d0cd64ce9daa42b91(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 600))


    def test_17699e2ce65d939d2760(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 601))

    def test_462570578c44c47dc345(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 602))

    def test_4e8799f26bd4ebf77a76(self):
        input = """
	   procedure main();
	   var x: array[0 .. 4] of integer;
	   i, j, temp: integer;
	   begin
			putFloatLn(2);
	   end
        """
        expect = """2.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 603))

    def test_f0c7ab72a26bf6df346a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 604))

    def test_a01af4324333189031f3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 605))

#     def test_9ff280d2c52a46fa886c(self):
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
#         self.assertTrue(TestCodeGen.test(input, expect, 606))


    def test_d48a9393911c00fbdfac(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 607))

    def test_9cf54c24b277cd6f4129(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 608))

    def test_8cff0aff204f5b7d92a2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 609))

    def test_09c8f97770c780a61f44(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 610))

    def test_b34a5a8e2eb6eaa7bbad(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 611))

    def test_c12f845765bf0551364a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 612))

    def test_799cbc9de7222154a47e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 613))

    def test_fef369afae9c1f7baae2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 614))

    def test_9d3fd78085fab4108cfe(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 615))

    def test_a4076d5f5719a60a30f1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 616))


    def test_c81df2ba63925a6742db(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 617))

    def test_19bca5349cc6aa46b7ba(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 618))

    def test_94331b44bf931b774872(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 619))

    def test_066d3082f0bbb2308c03(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 620))

    def test_0345b57d4e7886e636b1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 621))

    def test_aae9ff13513e4a78f5bd(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 622))

    def test_bd80bbb37c68032dff27(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 623))

    def test_477b1c4e8904f5d8072c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 624))

    def test_f209f213f69a227ae1a4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 625))

    def test_a9eb281e8120687437c3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 626))

    def test_14fde68a566852322816(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 627))

    def test_50734a9956f55fe26d06(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 628))

    def test_b87b3cfa0d35ba0363cb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 629))

    def test_95e2d72ae56c67c9a3f9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 630))

    def test_c95845799c4e7dd487b6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 631))

    def test_c85c2eb80b51df1013ad(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 632))

    def test_07985d6e3c00e47bfb37(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 633))

    def test_68fb0d020bd5bf3ca671(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 634))

    def test_75d0a6546941fab8a117(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 635))

    def test_6ea2f5e50f613b7c8d1f(self):
        input = """
        procedure main();
        begin
        end
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 636))


    def test_7629250f679e26c613c0(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 637))
    def test_2ced8b8afbcf2bcc15a4(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input, expect, 638))

    def test_50784fb45ba534e856ae(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.12)])])])
        expect = "5.12"
        self.assertTrue(TestCodeGen.test(input, expect, 639))

    def test_da9c6ee1e8c8a97545f9(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.12e-3)])])])
        expect = "0.00512"
        self.assertTrue(TestCodeGen.test(input, expect, 640))


    def test_fd23f914ca859f2edeed(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putBool"),[BooleanLiteral(True)])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 641))

    def test_97f7d7e02154d46c53fe(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putBool"),[
            BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False))
        ])])])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 642))
    def test_45870c0a764d5bca6db1(self):
        input = """
            procedure main();
            begin
                putBool(True And False Or True And False or True And True);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 643))

    def test_3e4c0b4b401f4dcb48a6(self):
        input = """
            procedure main();
            begin
                putFloat(1.2 + 4.5 - 2 / 5 * 4.2 - 1.2e-2 / 2 + 3);
            end
        """
        expect = '7.014'
        self.assertTrue(TestCodeGen.test(input, expect, 644))

    def test_39e5f7736262c313c93b(self):
        input = """
            procedure main();
            begin
                 putBool((10 = 5) and (3.4 <> 4) or (9.8 < 4.7 ) and (4 <= 5.6) or (10 >= 10) and (4 > 2));
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 645))

    def test_fdd6f4646dc6c01b4955(self):
        input = """
            procedure main();
            begin
                 putBool((10 = 5) and not not (3.4 <> 4) or (9.8 < 4.7 ) and not (4 <= 5.6) or (9 >= 10) and (4 > 2));
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 646))

    def test_bab5d9b6e67b29e7d5c9(self):
        input = """
            procedure main();
            begin
                putFloat(-1.2 + 4.5 -- 2 / 5 * 4.2 - - 1.2e-2 / 2 + -3);
            end
        """
        expect = "1.9860001"
        self.assertTrue(TestCodeGen.test(input, expect, 647))

    def test_106c5096714de6ed071f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 648))

    def test_071bf1508987a387f93e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 649))

    def test_99e60b62ef1b2c005f25(self):
        input = """
            procedure main();
            var a: integer ; b: real;
            begin
                putString("Hello World !");
            end
        """
        expect = "Hello World !"
        self.assertTrue(TestCodeGen.test(input, expect, 650))

    def test_42c5b89543b6d028597b(self):
        input = """
            var c,d: boolean;
            procedure main();
            var a: integer ; b: real;
            begin
                putString("Hello World !");
            end
        """
        expect = "Hello World !"
        self.assertTrue(TestCodeGen.test(input, expect, 651))

    def test_059349a10b3e4804ebc8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 652))

    def test_52d0966346e47cbcafd3(self):
        input = """
            procedure main();
            var a: integer ; b: real;
            begin
                a := 1;
                putInt(a);
            end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 653))

    def test_71a49cdcaeaa97b191f3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 654))

    def test_c8e2292915ef8bc6814e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 655))

    def test_3c4f5a10a1b7b0a94460(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 656))

    def test_0eb18d11d1648a38e3df(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 657))

    def test_4ae57bb4ed42696dfa20(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 658))

    def test_02ce33c442f5c70c1535(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 659))

    def test_beff5e2aeaa888b8f9a0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 660))

    def test_e07d6d68b82643166d63(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 661))

    def test_335f4a1c8c7fe5585e57(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 662))

    def test_5b51731532d337aed6ec(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 663))

    def test_8da5b0eea1cf2b3647e4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 664))

    def test_cb9a54d67e8a6852d875(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 665))

    def test_760afb1094037541a8dd(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 666))

    def test_f8a938c7d0c29bab0f02(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 667))

    def test_0ef2c18609a508719254(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 668))

    def test_28804838649ad7347365(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 669))
    
    def test_d50a8ece8cf13c796061(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 670))

    def test_bb0db1387e83352a8f7a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 671))

    def test_f93c2abb94f540135d48(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 672))
    
    def test_6b26a2c12f31a0702f2f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 673))
        
    def test_4993aa2c4dbf0b3617b8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 674))
    
    def test_12874fdb219ffe59d905(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 675))
        
    def test_6debe833b4b88b46eca3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 676))
        
    def test_6d33f6efeec70ce79793(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 677))
        
    def test_35ac50b10240d1303884(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 678))
        
    def test_eef3b23742df6953bef4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 679))
    
    def test_f6d0a8312f5ee7a278fe(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 680))
        
    def test_0655bf85757abdd3f9c9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 681))

    def test_e0258a09f8bf6e013ff1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 682))

    def test_c8eb6a013b814b7ca72c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 683))
        
    def test_f46dc27f1115027b7b60(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 684))
        
    def test_52d71d4aa3813f6a1bb8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 685))
        
    def test_1f2d62201961d2338e00(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 686))
        
    def test_00781648f8b48f88d48d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 687))
    
    def test_d7b28e564966800e160d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 688))
        
    def test_bed1f69c706e522bedd3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 689))
        
    def test_8f4974f839c737f45b2a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 690))
        
    def test_e046c161cf45ff3e8587(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 691))
        
    def test_b976ce251083b12e9e1c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 692))
        
    def test_39d357154fea000e9dc7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 693))
        
    def test_bf7489f11563e5066646(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 694))
        
    def test_eba46e4a5e48b3528583(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 695))
        
    def test_17848f3ddb7745f53267(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 696))
    
    def test_8cea943a32acddb707ab(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 697))
        
    def test_f309b26f806b673bed2e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 698))

    def test_31c83647ace4b770d93a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 699))
        
    def test_dd6408dc98d340d4cd06(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 700))
        
    def test_cf0d3cc2bd6149959122(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 701))
    
    def test_74f7d1d5634d1ad5f17b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 702))
    
    def test_2e33f7b796b045ebe57b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 703))
        
    def test_d0b19628d5cfbfd10bf9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 704))
        
    def test_ab957cf43116d18c3773(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 705))
        
    def test_54d47a98d63463ac7c47(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 706))
        
    def test_4d95b69b06ba613ce710(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 707))
        
    def test_19f46dd5f5bedb702eca(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 708))
        
    def test_7863041e5e15d4aee915(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 709))
        
    def test_c385fbfca18be9600095(self):
        input = r"""
        procedure main(); 
        begin 
            putFloat(123 / 3 + 46/5/2/2/2/2/4);
        end
        """
        expect = r"""41.14375"""
        self.assertTrue(TestCodeGen.test(input, expect, 710))
        
    def test_987a546a3311bad562c9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 711))
        
    def test_185b3b8f8057b81ac0b2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 712))
        
    def test_e8dd9824816df5c6b244(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 713))
        
    def test_3de4e28d4dd678993482(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 714))
        
    def test_f0d09309d02e66d8f1f1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 715))
    
    def test_f63ad78c7afd63deb397(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 716))
        
    def test_ea45cc9a6632e273b218(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 717))
        
    def test_5f13754234dadb6855bc(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 718))

    def test_abb034c7fccee8650687(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 719))
        
    def test_6010413aa68e9185a126(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 720))
    
    def test_88b19b7741da15d1baac(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 721))
        
    def test_d5d58976d49d420facc0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 722))
    
    def test_d907d866efe1a15efab6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 723))
        
    def test_c921873d50cd66b8da3e(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 724))
        
    def test_8627096f058dcf37d4e8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 725))
        
    def test_b4fac98a71d9dc11513f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 726))

    def test_31549813163e8107e6d3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 727))
    
    def test_c3159a5bacf8880122b8(self):
        input = """
            procedure main();
            begin
                putInt(49 - 1 * 12);
                putFlOatLn(- 1 / 12 + 1.2*1.2/-2);
            end
        """
        expect = "37-0.80333334\n"
        self.assertTrue(TestCodeGen.test(input, expect, 728))
        
    def test_1ced907e0e265bb604b3(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 729))
        
    def test_d06e756af9e2a8315e6e(self):
        input = """
             procedure main();
             var x: array [-1 .. 10] of integer;
             begin
                 x[-1] := 2;
                 putInt(x[-1]);
             end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 730))
        
    def test_590c8dda4942f829b096(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 731))
        
    def test_3a581f7e0f3fea4ef7ee(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 732))
        
    def test_8c8085ba87f1f813a5ae(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 733))
        
    def test_a2fea4bed55191a79a98(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 734))
        
    def test_d2d23ddcda72baa66133(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 735))
        
    def test_748183d34e3ec640bd04(self):
        input = r"""
            procedure main();
            begin
                yul := 1010;
                putInt(yul);
            end

            var yul: integer;
            """
        expect = """1010"""
        self.assertTrue(TestCodeGen.test(input, expect, 736))
        
    def test_708b65e7c3dad21fbf8f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 737))
        
    


    def test_0d061c36d1ca5bad68a8(self):
        input = """
            procedure main();
            begin
                putIntLn(100);
                putIntLn(-100);
                putInt(0);
            end
        """
        expect = "100\n-100\n0"
        self.assertTrue(TestCodeGen.test(input, expect, 738))

    def test_43066b28527fed5aa68a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 739))

    
    def test_0790755d10205c0b207c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 740))

    def test_546416b1ea8fc63bf875(self):
        input = """
            procedure main();
            begin
                putBoolLn(True);
                putBool(FalsE);
            end
        """
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 741))
    
    def test_fa8c8fdc316e06e58da0(self):
        input = """
            procedure main();
            begin
                putStringLn("PPL");
                putString("2018");
            end
        """
        expect = "PPL\n2018"
        self.assertTrue(TestCodeGen.test(input, expect, 742))

    def test_f7a5ae1fa842d7fd8287(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 743))

    def test_dd2f155b8234952978a0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 744))

    def test_752d53a9dcd1448361b4(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 745))

    def test_cae90b2bbeebe95a69e1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 746))


    def test_43037cf34dc85e6a1260(self):
        input = """
            procedure main();
            begin
                putInt(1+2+30);
            end
        """
        expect = "33"
        self.assertTrue(TestCodeGen.test(input, expect, 747))
    
    def test_e4c3a9646158605ee119(self):
        input = """
            procedure main();
            begin
                putFloat(1*45+30/12);
            end
        """
        expect = "47.5"
        self.assertTrue(TestCodeGen.test(input, expect, 748))
    
    def test_13f2a829856ef48d3e7b(self):
        input = """
            procedure main();
            begin
                putInt(100 div 3 div 2);
            end
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input, expect, 749))
    
    def test_267cdc4b402e30e2ec3d(self):
        input = """
            procedure main();
            begin
                putInt(100 - 1 * 12);
            end
        """
        expect = "88"
        self.assertTrue(TestCodeGen.test(input, expect, 750))
    
    def test_af9b10a7e708b30cd04a(self):
        input = """
            procedure main();
            begin
                putBool(FalSE and False);
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 751))
    
    def test_2c6c5bf200b281ea5632(self):
        input = """
            procedure main();
            begin
                putBool(1 <= 2);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 752))
    
    def test_d49de6a63b6d2f08f69d(self):
        input = """
            procedure main();
            begin
                putBool(1 = 2);
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 753))
    
    def test_4818fffe08fdfe8897b9(self):
        input = """
            procedure main();
            begin
                putBool(not (-10 <> 2));
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 754))
    
    def test_e1f203f2bb9621b7c660(self):
        input = """
            procedure main();
            begin
                putIntLn(-12-2);
                putFloat(-12.3+12);
            end
        """
        expect = "-14\n-0.3000002"
        self.assertTrue(TestCodeGen.test(input, expect, 755))
    
    def test_541f9b67defa9abf4466(self):
        input = """
            procedure main();
            begin
                putBool(true and then true);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 756))
    
    def test_f8ccbafb3d0752c263ad(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 757))
    
    def test_3b9cf26a303b4052305f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 758))
    
    def test_4e701402ee1d99d675d6(self):
        input = """
             procedure main();
             var x: array [-1 .. 10] of integer;
             begin
                 x[-1] := 2;
                 putInt(x[-1]);
             end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 759))

    def test_cc24c69a50624b735cc9(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 760))

    def test_899f66ed2ea965ead2dc(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 761))

    

    def test_a8e141e372e14a3f3371(self):
        input = """
             procedure main();
             var a: array [1 .. 10] of string;
             begin
                putBool(True or else (((1/0.0)/(1/0)) = 1));
             end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 762))


    #*************** TEST ARRAY ********************/

    def test_999896f2300f37a04ff6(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 763))

    def test_b907863a00ed0edbd212(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 764))

    def test_9ee47385495609e0aa5b(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 765))

    def test_4262569442029b8f7b22(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 766))


    #************************* TEST WHILE *************************#

    def test_75bf27e2d61d299072cb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 767))

    def test_2d311e056c2e4bd9bcdf(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 768))

    def test_c204cbbd9a3d00a84fa1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 769))

    #TEST CALL FUNCTION 

    def test_8119b368f77e25092c89(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 770))
    
    def test_20125756ce7a9fd30ef2(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 771))


    #TEST IF STMT 

    def test_272b20d0cdc37f6cc24a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 772))

    def test_1db555f6fbdb174a90a0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 773))

    def test_e06c25f52e0d8f97b54f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 774))

    def test_039262348878d7fecdb0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 775))

    def test_ba3e2f54318950005b8f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 776))


    def test_b35f026ba8d352ed743c(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 777))

    def test_9491b35c683536aad6ba(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 778))

    def test_16c25d45e96d05aad4e8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 779))

    def test_8d7459ecfdf82f77e4fa(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 780))

    def test_0fb2c4dbb7e2807de0e8(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 781))
    
    def test_5e4e3cc19206943f7201(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 782))

    def test_54d19aef5570a7a24e13(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 783))

    def test_36114b666685dc44e142(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 784))

    def test_e70175f94ff96f9db816(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 785))

    def test_74d8df1b0bf439a276d1(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 786))

    def test_75b92b2185a3119de5c0(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 787))

    def test_7b4f9ec08e5a01756af5(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 788))

    def test_04a2212777397b1bb8ca(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 789))

    def test_1cbc23d604b01d835d0f(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 790))

    def test_425671af7c06c0149629(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 791))

    def test_57fb423a076dbccfa081(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 792))

    
    def test_4fff7dc5fe9bcdfdc349(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 793))

    def test_3743b482f26114d5f240(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 794))

    def test_edf858025c0860d95051(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 795))

    def test_00dd561b4b7bafb9dbb7(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 796))

    def test_dd3b72b5f5af9ef2dd10(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 797))

    def test_7a50365f906bcc18d098(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 798))

    def test_ce89a63ee9d7bdf53c98(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 799))

    def test_b30d4480eb2a938acf94(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 800))


    def test_10e412ae845d0d97c435(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 801))


    def test_c5f4623ec9cbe3116803(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 802))

    def test_5a849fb3845a7ccc03e3(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 803))

    def test_145bee6738edfd6da53c(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 804))

    def test_e2123462ba917d5ce375(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 805))

    def test_1065b0db80371e93daed(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 806))

    def test_47ea40554949944952cd(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 807))

    def test_92dcb260c97d87211520(self):
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
            self.assertTrue(TestCodeGen.test(input, expect, 808))

    def test_76a0feadb60e51b71f16(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 809))

    def test_400b8c799aed5eda4b0d(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 810))

    def test_63d09345bc779ca1d643(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 811))

    def test_b8c65349c035275c4c75(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 812))

    def test_5125101eeb0fa9bbf2fb(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 813))

    def test_583f44064b2f8a98be79(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 814))

    def test_e9454b9745f224c4bd59(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 815))

    def test_2f3c5a19e044a4845060(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 816))

    def test_18f31086f3ca86e33437(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 817))

    def test_010c07d5e835bf1f0a1a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 818))

    def test_c7b08558573af9ae8005(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 819))

    def test_6e300f3328913a13eb20(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 820))

    def test_7b88c95182ff7f21e117(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 821))

    def test_bc2571458d9ed8ecfe99(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 822))

    def test_7fa05c38aeb1099a235a(self):
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
        self.assertTrue(TestCodeGen.test(input, expect, 823))
