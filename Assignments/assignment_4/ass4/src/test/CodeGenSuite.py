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
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 101))


    def test_2(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 102))


    def test_3(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 103))


    def test_4(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 104))


    def test_5(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 105))


    def test_6(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 106))


    def test_7(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 107))


    def test_8(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 108))


    def test_9(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 109))


    def test_10(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 110))


    def test_11(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 111))


    def test_12(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 112))


    def test_13(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 113))


    def test_14(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 114))


    def test_15(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 115))


    def test_16(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 116))


    def test_17(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 117))


    def test_18(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 118))


    def test_19(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 119))


    def test_20(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 120))


    def test_21(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 121))


    def test_22(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 122))


    def test_23(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 123))


    def test_24(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 124))


    def test_25(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 125))


    def test_26(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 126))


    def test_27(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 127))


    def test_28(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 128))


    def test_29(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 129))


    def test_30(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 130))


    def test_31(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 131))


    def test_32(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 132))


    def test_33(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 133))


    def test_34(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 134))


    def test_35(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 135))


    def test_36(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 136))


    def test_37(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 137))


    def test_38(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 138))


    def test_39(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 139))


    def test_40(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 140))


    def test_41(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 141))


    def test_42(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 142))


    def test_43(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 143))


    def test_44(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 144))


    def test_45(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 145))


    def test_46(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 146))


    def test_47(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 147))


    def test_48(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 148))


    def test_49(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 149))


    def test_50(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 150))


    def test_51(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 151))


    def test_52(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 152))


    def test_53(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 153))


    def test_54(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 154))


    def test_55(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 155))


    def test_56(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 156))


    def test_57(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 157))


    def test_58(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 158))


    def test_59(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 159))


    def test_60(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 160))


    def test_61(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 161))


    def test_62(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 162))


    def test_63(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 163))


    def test_64(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 164))


    def test_65(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 165))


    def test_66(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 166))


    def test_67(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 167))


    def test_68(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 168))


    def test_69(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 169))


    def test_70(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 170))


    def test_71(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 171))


    def test_72(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 172))


    def test_73(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 173))


    def test_74(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 174))


    def test_75(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 175))


    def test_76(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 176))


    def test_77(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 177))


    def test_78(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 178))


    def test_79(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 179))


    def test_80(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 180))


    def test_81(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 181))


    def test_82(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 182))


    def test_83(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 183))


    def test_84(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 184))


    def test_85(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 185))


    def test_86(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 186))


    def test_87(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 187))


    def test_88(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 188))


    def test_89(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 189))


    def test_90(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 190))


    def test_91(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 191))


    def test_92(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 192))


    def test_93(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 193))


    def test_94(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 194))


    def test_95(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 195))


    def test_96(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 196))


    def test_97(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 197))


    def test_98(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 198))


    def test_99(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 199))


    def test_100(self):
        input = r"""

procedure main();
begin 
    putInt(1);
end

"""
        expect = "1"
        self.assertTrue(TestChecker.test(input, expect, 200))

