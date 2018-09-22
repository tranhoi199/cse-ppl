#########################################################
########### Code used for Pylint to link code ###########
######    REMEMBER: Comment before submit code    #######
#########################################################

import sys
sys.path.append('../main/mp/utils')
sys.path.append('../utils')

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_1(self):
        input = """
var a: integer;
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """
var a,b: string;
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """
var x,y,z:integer; 
    g: string; 
    h,t: real;
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """
var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """
procedure foo();
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """
procedure foo(a: string);
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """
procedure foo(a: string; b: Real);
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
procedure foo(a,b,c: string);
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
procedure foo(a,b,c: string; f,k,o: integer; g,h,t: Real);
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
function foo(): String;
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """
function foo(a: string): String;
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """
function foo(a: string; b: Real): String;
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """
function foo(a,b,c: string; 
    f,k,o: integer; g,h,t: Real): String;
begin
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """
function foo(): String;
begin
continue;
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """
function foo(): String;
begin
break;
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """
function foo(): String;
begin
return;
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """
function foo(): String;
begin
return ok();
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
function foo(): String;
begin
return ok(1);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
function foo(): String;
begin
return ok(1,2);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """
function foo(): String;
begin
return ok(1,a);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """
function foo(): String;
begin
ok();
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """
function foo(): String;
begin
ok(a);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """
function foo(): String;
begin
ok(a,1);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """
function foo(): String;
begin
ok(a,"1",True,falSe);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """
function foo(): String;
begin
ok("hi", foo());
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """
function foo(): String;
begin
ok("hi", foo(bar(), 1));
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """
function foo(): String;
begin
ok(a[1]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """
function foo(): String;
begin
ok(1[1]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """
function foo(): String;
begin
ok(foo()[1]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """
function foo(): String;
begin
ok((foo())[1]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """
function foo(): String;
begin
ok(a[b]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """
function foo(): String;
begin
ok(a[foo()]);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """
function foo(): String;
begin
ok(4 and then 5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """
function foo(): String;
begin
ok(4 or else 5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """
function foo(): String;
begin
ok(4=5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """
function foo(): String;
begin
ok(4>=5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """
function foo(): String;
begin
ok(4+5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """
function foo(): String;
begin
ok(4 div 5);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """
function foo(): String;
begin
ok(-4);
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """
function foo(): String;
begin
ok(5 and then (-6 + "nt" * 3 or 5) div 7 >= a+b-(-f * not(-5*"abc")));
end
"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100(self):
        input = """

"""
        expect = str(

        )
        self.assertTrue(TestAST.test(input, expect, 400))


#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################