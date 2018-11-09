import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_op_1(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1))

    def test_op_2(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,2))

    def test_op_3(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,3))

    def test_op_4(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,4))

    def test_op_5(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,5))

    def test_op_6(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,6))

    def test_op_10(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,10))

    def test_op_13(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,13))

    def test_op_14(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,14))

    def test_op_15(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,15))

    def test_op_16(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,16))

    def test_op_17(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,17))

    def test_op_18(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,18))

    def test_op_19(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,19))

    def test_op_20(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,20))

    def test_op_21(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,21))

    def test_op_22(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,22))

    def test_op_23(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,23))

    def test_op_24(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,24))

    def test_op_25(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,25))

    def test_op_26(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,26))

    def test_op_27(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,27))

    def test_op_28(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,28))

    def test_op_29(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,29))

    def test_op_30(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,30))

    def test_op_31(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,31))

    def test_op_32(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,32))

    def test_op_33(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,33))

    def test_op_34(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,34))

    def test_op_35(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,35))

    def test_op_36(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,36))

    def test_op_37(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,37))

    def test_op_38(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,38))

    def test_op_39(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,39))

    def test_op_40(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,40))

    def test_op_41(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,41))

    def test_op_42(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,42))

    def test_op_43(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,43))

    def test_op_44(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,44))

    def test_op_45(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,45))

    def test_op_46(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,46))

    def test_op_47(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,47))

    def test_op_48(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,48))

    def test_op_49(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,49))

    def test_op_50(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,50))

    def test_op_51(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,51))

    def test_op_52(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,52))

    def test_op_53(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,53))

    def test_op_54(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,54))

    def test_op_55(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,55))

    def test_op_56(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,56))

    def test_op_57(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,57))

    def test_op_58(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,58))

    def test_op_59(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,59))

    def test_op_60(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,60))

    def test_op_61(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,61))

    def test_op_62(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,62))

    def test_op_63(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,63))

    def test_op_64(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,64))

    def test_op_65(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,65))

    def test_op_66(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,66))

    def test_op_67(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,67))

    def test_op_68(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,68))

    def test_op_69(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,69))

    def test_op_70(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,70))

    def test_op_71(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,71))

    def test_op_72(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,72))

    def test_op_73(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,73))

    def test_op_74(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,74))

    def test_op_75(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,75))

    def test_op_76(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,76))

    def test_op_77(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,77))

    def test_op_78(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,78))

    def test_op_79(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,79))

    def test_op_80(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,80))

    def test_op_81(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,81))

    def test_op_82(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,82))

    def test_op_83(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,83))

    def test_op_84(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,84))

    def test_op_85(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,85))

    def test_op_86(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,86))

    def test_op_87(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 + 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,87))

    def test_op_88(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 - 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,88))

    def test_op_89(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 * 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,89))

    def test_op_90(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,90))

    def test_op_91(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,91))

    def test_op_92(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,92))

    def test_op_93(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,93))

    def test_op_94(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,94))

    def test_op_95(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,95))

    def test_op_96(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,96))

    def test_op_97(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,97))

    def test_op_98(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,98))

    def test_op_99(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,99))

    def test_op_100(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,100))

    def test_op_101(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,101))

    def test_op_102(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,102))

    def test_op_103(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,103))

    def test_op_104(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,104))

    def test_op_105(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,105))

    def test_op_106(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,106))

    def test_op_107(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,107))

    def test_op_108(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,108))

    def test_op_109(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,109))

    def test_op_110(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,110))

    def test_op_111(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,111))

    def test_op_112(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,112))

    def test_op_113(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,113))

    def test_op_114(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,114))

    def test_op_115(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,115))

    def test_op_116(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,116))

    def test_op_117(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,117))

    def test_op_118(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,118))

    def test_op_119(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,119))

    def test_op_120(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,120))

    def test_op_121(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,121))

    def test_op_122(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,122))

    def test_op_123(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,123))

    def test_op_124(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,124))

    def test_op_125(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,125))

    def test_op_126(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,126))

    def test_op_127(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,127))

    def test_op_128(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,128))

    def test_op_129(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,129))

    def test_op_130(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,130))

    def test_op_131(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,131))

    def test_op_132(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,132))

    def test_op_133(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,133))

    def test_op_134(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,134))

    def test_op_135(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,135))

    def test_op_136(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,136))

    def test_op_137(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,137))

    def test_op_138(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,138))

    def test_op_139(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,139))

    def test_op_140(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,140))

    def test_op_141(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,141))

    def test_op_142(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,142))

    def test_op_143(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,143))

    def test_op_144(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,144))

    def test_op_145(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,145))

    def test_op_146(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,146))

    def test_op_147(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,147))

    def test_op_148(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,148))

    def test_op_149(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,149))

    def test_op_150(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,150))

    def test_op_151(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,151))

    def test_op_152(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,152))

    def test_op_153(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,153))

    def test_op_154(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,154))

    def test_op_155(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,155))

    def test_op_156(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,156))

    def test_op_157(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,157))

    def test_op_158(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,158))

    def test_op_159(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,159))

    def test_op_160(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= 1.0 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,160))

    def test_op_161(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,161))

    def test_op_162(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,162))

    def test_op_163(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,163))

    def test_op_164(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,164))

    def test_op_165(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,165))

    def test_op_166(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,166))

    def test_op_167(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,167))

    def test_op_168(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,168))

    def test_op_169(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,169))

    def test_op_170(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,170))

    def test_op_171(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,171))

    def test_op_172(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,172))

    def test_op_173(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,173))

    def test_op_174(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,174))

    def test_op_175(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,175))

    def test_op_176(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,176))

    def test_op_177(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,177))

    def test_op_178(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,178))

    def test_op_179(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,179))

    def test_op_180(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,180))

    def test_op_181(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,181))

    def test_op_182(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,182))

    def test_op_183(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,183))

    def test_op_184(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,184))

    def test_op_185(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,185))

    def test_op_186(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,186))

    def test_op_187(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,187))

    def test_op_188(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,188))

    def test_op_189(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,189))

    def test_op_190(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,190))

    def test_op_191(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,191))

    def test_op_192(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,192))

    def test_op_193(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,193))

    def test_op_194(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,194))

    def test_op_195(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,195))

    def test_op_196(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,196))

    def test_op_197(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,197))

    def test_op_198(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,198))

    def test_op_199(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,199))

    def test_op_200(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,200))

    def test_op_201(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,201))

    def test_op_202(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,202))

    def test_op_203(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,203))

    def test_op_204(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,204))

    def test_op_205(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,205))

    def test_op_206(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,206))

    def test_op_207(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,207))

    def test_op_208(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,208))

    def test_op_209(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,209))

    def test_op_210(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,210))

    def test_op_211(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,211))

    def test_op_212(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,212))

    def test_op_213(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,213))

    def test_op_214(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,214))

    def test_op_215(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,215))

    def test_op_216(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,216))

    def test_op_217(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,217))

    def test_op_218(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,218))

    def test_op_219(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,219))

    def test_op_220(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,220))

    def test_op_221(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,221))

    def test_op_222(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,222))

    def test_op_223(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,223))

    def test_op_224(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,224))

    def test_op_225(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,225))

    def test_op_226(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,226))

    def test_op_227(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,227))

    def test_op_228(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,228))

    def test_op_229(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,229))

    def test_op_230(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,230))

    def test_op_231(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,231))

    def test_op_232(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,232))

    def test_op_233(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,233))

    def test_op_234(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,234))

    def test_op_235(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,235))

    def test_op_236(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,236))

    def test_op_237(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,237))

    def test_op_238(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,238))

    def test_op_239(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,239))

    def test_op_240(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= "abc" or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,240))

    def test_op_241(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,241))

    def test_op_242(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,242))

    def test_op_243(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,243))

    def test_op_244(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,244))

    def test_op_245(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,245))

    def test_op_246(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,246))

    def test_op_247(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,247))

    def test_op_248(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,248))

    def test_op_249(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,249))

    def test_op_250(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,250))

    def test_op_251(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,251))

    def test_op_252(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,252))

    def test_op_253(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,253))

    def test_op_254(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,254))

    def test_op_255(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,255))

    def test_op_256(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,256))

    def test_op_257(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,257))

    def test_op_258(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,258))

    def test_op_259(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,259))

    def test_op_260(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,260))

    def test_op_261(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,261))

    def test_op_262(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,262))

    def test_op_263(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,263))

    def test_op_264(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,264))

    def test_op_265(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,265))

    def test_op_266(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,266))

    def test_op_267(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,267))

    def test_op_268(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,268))

    def test_op_269(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,269))

    def test_op_270(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,270))

    def test_op_271(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,271))

    def test_op_272(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,272))

    def test_op_273(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,273))

    def test_op_274(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,274))

    def test_op_275(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,275))

    def test_op_276(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,276))

    def test_op_277(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,277))

    def test_op_278(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,278))

    def test_op_279(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,279))

    def test_op_280(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,280))

    def test_op_281(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,281))

    def test_op_282(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,282))

    def test_op_283(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,283))

    def test_op_284(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,284))

    def test_op_285(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,285))

    def test_op_286(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,286))

    def test_op_287(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,287))

    def test_op_288(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,288))

    def test_op_289(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,289))

    def test_op_290(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,290))

    def test_op_291(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,291))

    def test_op_292(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,292))

    def test_op_293(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,293))

    def test_op_294(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,294))

    def test_op_295(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,295))

    def test_op_296(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,296))

    def test_op_297(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,297))

    def test_op_298(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,298))

    def test_op_299(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,299))

    def test_op_300(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,300))

    def test_op_301(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,301))

    def test_op_302(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,302))

    def test_op_303(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,303))

    def test_op_304(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,304))

    def test_op_305(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,305))

    def test_op_306(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,306))

    def test_op_307(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,307))

    def test_op_308(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,308))

    def test_op_309(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,309))

    def test_op_310(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,310))

    def test_op_311(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,311))

    def test_op_312(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,312))

    def test_op_313(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,313))

    def test_op_314(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,314))

    def test_op_315(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,315))

    def test_op_316(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,316))

    def test_op_317(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,317))

    def test_op_318(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,318))

    def test_op_319(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,319))

    def test_op_320(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= true or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,320))

    def test_op_321(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,321))

    def test_op_322(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,322))

    def test_op_323(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,323))

    def test_op_324(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,324))

    def test_op_325(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,325))

    def test_op_326(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,326))

    def test_op_327(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,327))

    def test_op_328(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,328))

    def test_op_329(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,329))

    def test_op_330(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,330))

    def test_op_331(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,331))

    def test_op_332(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,332))

    def test_op_333(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,333))

    def test_op_334(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,334))

    def test_op_335(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,335))

    def test_op_336(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,336))

    def test_op_337(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,337))

    def test_op_338(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,338))

    def test_op_339(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,339))

    def test_op_340(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,340))

    def test_op_341(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,341))

    def test_op_342(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,342))

    def test_op_343(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,343))

    def test_op_344(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,344))

    def test_op_345(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,345))

    def test_op_346(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,346))

    def test_op_347(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,347))

    def test_op_348(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,348))

    def test_op_349(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,349))

    def test_op_350(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,350))

    def test_op_351(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,351))

    def test_op_352(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,352))

    def test_op_353(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,353))

    def test_op_354(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,354))

    def test_op_355(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,355))

    def test_op_356(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,356))

    def test_op_357(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,357))

    def test_op_358(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,358))

    def test_op_359(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,359))

    def test_op_360(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,360))

    def test_op_361(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,361))

    def test_op_362(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,362))

    def test_op_363(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,363))

    def test_op_364(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,364))

    def test_op_365(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,365))

    def test_op_366(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,366))

    def test_op_367(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,367))

    def test_op_368(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,368))

    def test_op_369(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,369))

    def test_op_370(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,370))

    def test_op_371(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,371))

    def test_op_372(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,372))

    def test_op_373(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,373))

    def test_op_374(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,374))

    def test_op_375(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,375))

    def test_op_376(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,376))

    def test_op_377(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,377))

    def test_op_378(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,378))

    def test_op_379(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,379))

    def test_op_380(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,380))

    def test_op_381(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,381))

    def test_op_382(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,382))

    def test_op_383(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,383))

    def test_op_384(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,384))

    def test_op_385(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,385))

    def test_op_386(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,386))

    def test_op_387(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,387))

    def test_op_388(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,388))

    def test_op_389(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,389))

    def test_op_390(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,390))

    def test_op_391(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,391))

    def test_op_392(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,392))

    def test_op_393(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,393))

    def test_op_394(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,394))

    def test_op_395(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,395))

    def test_op_396(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,396))

    def test_op_397(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,397))

    def test_op_398(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,398))

    def test_op_399(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,399))

    def test_op_400(self):
        input = """
    procedure main();
    var a: integer;
    begin
        a:= false or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_op_401(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_op_402(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_op_403(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_op_404(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_op_405(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_op_406(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_op_407(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 + 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_op_408(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 - 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_op_409(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 * 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_op_410(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_op_411(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 div 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(div,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_op_412(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 mod 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(mod,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_op_413(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_op_414(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_op_415(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_op_416(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_op_417(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_op_418(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_op_419(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_op_420(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_op_421(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_op_422(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_op_423(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_op_424(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_op_425(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_op_426(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_op_427(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_op_428(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_op_429(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_op_430(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_op_431(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_op_432(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_op_433(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_op_434(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_op_435(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_op_436(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_op_437(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_op_438(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_op_439(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_op_440(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_op_441(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_op_442(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_op_443(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_op_444(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_op_445(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_op_446(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_op_447(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_op_448(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_op_449(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_op_450(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_op_451(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_op_452(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_op_453(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_op_454(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_op_455(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_op_456(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_op_457(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_op_458(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_op_459(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_op_460(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_op_461(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_op_462(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_op_463(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_op_464(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_op_465(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_op_466(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_op_467(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_op_468(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_op_469(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_op_470(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_op_471(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_op_472(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_op_473(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_op_474(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_op_475(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_op_476(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_op_477(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_op_478(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_op_479(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_op_480(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_op_481(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_op_482(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_op_483(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_op_484(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_op_485(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_op_486(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_op_487(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 + 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_op_488(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 - 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_op_489(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 * 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_op_490(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_op_491(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_op_492(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_op_493(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_op_494(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_op_495(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_op_496(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_op_497(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_op_498(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_op_499(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_op_500(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_op_501(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_op_502(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_op_503(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_op_504(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_op_505(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_op_506(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_op_507(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_op_508(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_op_509(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,509))

    def test_op_510(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,510))

    def test_op_511(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,511))

    def test_op_512(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_op_513(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,513))

    def test_op_514(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,514))

    def test_op_515(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_op_516(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,516))

    def test_op_517(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,517))

    def test_op_518(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,518))

    def test_op_519(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,519))

    def test_op_520(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,520))

    def test_op_521(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,521))

    def test_op_522(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,522))

    def test_op_523(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,523))

    def test_op_524(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,524))

    def test_op_525(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,525))

    def test_op_526(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,526))

    def test_op_527(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,527))

    def test_op_528(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,528))

    def test_op_529(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,529))

    def test_op_530(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,530))

    def test_op_531(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,531))

    def test_op_532(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,532))

    def test_op_533(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,533))

    def test_op_534(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,534))

    def test_op_535(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,535))

    def test_op_536(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,536))

    def test_op_537(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,537))

    def test_op_538(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,538))

    def test_op_539(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,539))

    def test_op_540(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,540))

    def test_op_541(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,541))

    def test_op_542(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,542))

    def test_op_543(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,543))

    def test_op_544(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,544))

    def test_op_545(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,545))

    def test_op_546(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,546))

    def test_op_547(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,547))

    def test_op_548(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,548))

    def test_op_549(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,549))

    def test_op_550(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,550))

    def test_op_551(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,551))

    def test_op_552(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,552))

    def test_op_553(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,553))

    def test_op_554(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,554))

    def test_op_555(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,555))

    def test_op_556(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,556))

    def test_op_557(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,557))

    def test_op_558(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,558))

    def test_op_559(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,559))

    def test_op_560(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= 1.0 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,560))

    def test_op_561(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,561))

    def test_op_562(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,562))

    def test_op_563(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,563))

    def test_op_564(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,564))

    def test_op_565(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,565))

    def test_op_566(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,566))

    def test_op_567(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,567))

    def test_op_568(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,568))

    def test_op_569(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,569))

    def test_op_570(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,570))

    def test_op_571(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,571))

    def test_op_572(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,572))

    def test_op_573(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,573))

    def test_op_574(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,574))

    def test_op_575(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,575))

    def test_op_576(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,576))

    def test_op_577(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,577))

    def test_op_578(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,578))

    def test_op_579(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,579))

    def test_op_580(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,580))

    def test_op_581(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,581))

    def test_op_582(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,582))

    def test_op_583(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,583))

    def test_op_584(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,584))

    def test_op_585(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,585))

    def test_op_586(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,586))

    def test_op_587(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,587))

    def test_op_588(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,588))

    def test_op_589(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,589))

    def test_op_590(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,590))

    def test_op_591(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,591))

    def test_op_592(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,592))

    def test_op_593(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,593))

    def test_op_594(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,594))

    def test_op_595(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,595))

    def test_op_596(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,596))

    def test_op_597(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,597))

    def test_op_598(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,598))

    def test_op_599(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,599))

    def test_op_600(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,600))

    def test_op_601(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,601))

    def test_op_602(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,602))

    def test_op_603(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,603))

    def test_op_604(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,604))

    def test_op_605(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,605))

    def test_op_606(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,606))

    def test_op_607(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,607))

    def test_op_608(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,608))

    def test_op_609(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,609))

    def test_op_610(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,610))

    def test_op_611(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,611))

    def test_op_612(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,612))

    def test_op_613(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,613))

    def test_op_614(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,614))

    def test_op_615(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,615))

    def test_op_616(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,616))

    def test_op_617(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,617))

    def test_op_618(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,618))

    def test_op_619(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,619))

    def test_op_620(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,620))

    def test_op_621(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,621))

    def test_op_622(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,622))

    def test_op_623(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,623))

    def test_op_624(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,624))

    def test_op_625(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,625))

    def test_op_626(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,626))

    def test_op_627(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,627))

    def test_op_628(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,628))

    def test_op_629(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,629))

    def test_op_630(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,630))

    def test_op_631(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,631))

    def test_op_632(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,632))

    def test_op_633(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,633))

    def test_op_634(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,634))

    def test_op_635(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,635))

    def test_op_636(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,636))

    def test_op_637(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,637))

    def test_op_638(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,638))

    def test_op_639(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,639))

    def test_op_640(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= "abc" or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,640))

    def test_op_641(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,641))

    def test_op_642(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,642))

    def test_op_643(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,643))

    def test_op_644(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,644))

    def test_op_645(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,645))

    def test_op_646(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,646))

    def test_op_647(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,647))

    def test_op_648(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,648))

    def test_op_649(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,649))

    def test_op_650(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,650))

    def test_op_651(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,651))

    def test_op_652(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,652))

    def test_op_653(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,653))

    def test_op_654(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,654))

    def test_op_655(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,655))

    def test_op_656(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,656))

    def test_op_657(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,657))

    def test_op_658(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,658))

    def test_op_659(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,659))

    def test_op_660(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,660))

    def test_op_661(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,661))

    def test_op_662(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,662))

    def test_op_663(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,663))

    def test_op_664(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,664))

    def test_op_665(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,665))

    def test_op_666(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,666))

    def test_op_667(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,667))

    def test_op_668(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,668))

    def test_op_669(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,669))

    def test_op_670(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,670))

    def test_op_671(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,671))

    def test_op_672(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,672))

    def test_op_673(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,673))

    def test_op_674(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,674))

    def test_op_675(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,675))

    def test_op_676(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,676))

    def test_op_677(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,677))

    def test_op_678(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,678))

    def test_op_679(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,679))

    def test_op_680(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,680))

    def test_op_681(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,681))

    def test_op_682(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,682))

    def test_op_683(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,683))

    def test_op_684(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,684))

    def test_op_685(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,685))

    def test_op_686(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,686))

    def test_op_687(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,687))

    def test_op_688(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,688))

    def test_op_689(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,689))

    def test_op_690(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,690))

    def test_op_691(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,691))

    def test_op_692(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,692))

    def test_op_693(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,693))

    def test_op_694(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,694))

    def test_op_695(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,695))

    def test_op_696(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,696))

    def test_op_697(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,697))

    def test_op_698(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,698))

    def test_op_699(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,699))

    def test_op_700(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,700))

    def test_op_701(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,701))

    def test_op_702(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,702))

    def test_op_703(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,703))

    def test_op_704(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,704))

    def test_op_705(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,705))

    def test_op_706(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,706))

    def test_op_707(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,707))

    def test_op_708(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,708))

    def test_op_709(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,709))

    def test_op_710(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,710))

    def test_op_711(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,711))

    def test_op_712(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,712))

    def test_op_713(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,713))

    def test_op_714(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,714))

    def test_op_715(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,715))

    def test_op_716(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,716))

    def test_op_717(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,717))

    def test_op_718(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,718))

    def test_op_719(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,719))

    def test_op_720(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= true or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,720))

    def test_op_721(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,721))

    def test_op_722(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,722))

    def test_op_723(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,723))

    def test_op_724(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,724))

    def test_op_725(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,725))

    def test_op_726(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,726))

    def test_op_727(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,727))

    def test_op_728(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,728))

    def test_op_729(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,729))

    def test_op_730(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,730))

    def test_op_731(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,731))

    def test_op_732(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,732))

    def test_op_733(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,733))

    def test_op_734(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,734))

    def test_op_735(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,735))

    def test_op_736(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,736))

    def test_op_737(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,737))

    def test_op_738(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,738))

    def test_op_739(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,739))

    def test_op_740(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,740))

    def test_op_741(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,741))

    def test_op_742(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,742))

    def test_op_743(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,743))

    def test_op_744(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,744))

    def test_op_745(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,745))

    def test_op_746(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,746))

    def test_op_747(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,747))

    def test_op_748(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,748))

    def test_op_749(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,749))

    def test_op_750(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,750))

    def test_op_751(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,751))

    def test_op_752(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,752))

    def test_op_753(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,753))

    def test_op_754(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,754))

    def test_op_755(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,755))

    def test_op_756(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,756))

    def test_op_757(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,757))

    def test_op_758(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,758))

    def test_op_759(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,759))

    def test_op_760(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,760))

    def test_op_761(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,761))

    def test_op_762(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,762))

    def test_op_763(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,763))

    def test_op_764(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,764))

    def test_op_765(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,765))

    def test_op_766(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,766))

    def test_op_767(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,767))

    def test_op_768(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,768))

    def test_op_769(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,769))

    def test_op_770(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,770))

    def test_op_771(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,771))

    def test_op_772(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,772))

    def test_op_773(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,773))

    def test_op_774(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,774))

    def test_op_775(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,775))

    def test_op_776(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,776))

    def test_op_777(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,777))

    def test_op_778(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,778))

    def test_op_779(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,779))

    def test_op_780(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,780))

    def test_op_781(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,781))

    def test_op_782(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,782))

    def test_op_783(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,783))

    def test_op_784(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,784))

    def test_op_785(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,785))

    def test_op_786(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,786))

    def test_op_787(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,787))

    def test_op_788(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,788))

    def test_op_789(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,789))

    def test_op_790(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,790))

    def test_op_791(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,791))

    def test_op_792(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,792))

    def test_op_793(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,793))

    def test_op_794(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,794))

    def test_op_795(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,795))

    def test_op_796(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,796))

    def test_op_797(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,797))

    def test_op_798(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,798))

    def test_op_799(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,799))

    def test_op_800(self):
        input = """
    procedure main();
    var a: string;
    begin
        a:= false or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,800))

    def test_op_801(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,801))

    def test_op_802(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,802))

    def test_op_803(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,803))

    def test_op_804(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,804))

    def test_op_805(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,805))

    def test_op_806(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,806))

    def test_op_813(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,813))

    def test_op_814(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,814))

    def test_op_815(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,815))

    def test_op_816(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,816))

    def test_op_817(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,817))

    def test_op_818(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,818))

    def test_op_819(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,819))

    def test_op_820(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,820))

    def test_op_821(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,821))

    def test_op_822(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,822))

    def test_op_827(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,827))

    def test_op_828(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,828))

    def test_op_829(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,829))

    def test_op_830(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,830))

    def test_op_831(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,831))

    def test_op_832(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,832))

    def test_op_833(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,833))

    def test_op_834(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,834))

    def test_op_835(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,835))

    def test_op_836(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,836))

    def test_op_837(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,837))

    def test_op_838(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,838))

    def test_op_839(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,839))

    def test_op_840(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,840))

    def test_op_841(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,841))

    def test_op_842(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,842))

    def test_op_843(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,843))

    def test_op_844(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,844))

    def test_op_845(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,845))

    def test_op_846(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,846))

    def test_op_847(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,847))

    def test_op_848(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,848))

    def test_op_849(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,849))

    def test_op_850(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,850))

    def test_op_851(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,851))

    def test_op_852(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,852))

    def test_op_853(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,853))

    def test_op_854(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,854))

    def test_op_855(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,855))

    def test_op_856(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,856))

    def test_op_857(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,857))

    def test_op_858(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,858))

    def test_op_859(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,859))

    def test_op_860(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,860))

    def test_op_861(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,861))

    def test_op_862(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,862))

    def test_op_863(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,863))

    def test_op_864(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,864))

    def test_op_865(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,865))

    def test_op_866(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,866))

    def test_op_867(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,867))

    def test_op_868(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,868))

    def test_op_869(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,869))

    def test_op_870(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,870))

    def test_op_871(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,871))

    def test_op_872(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,872))

    def test_op_873(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,873))

    def test_op_874(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,874))

    def test_op_875(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,875))

    def test_op_876(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,876))

    def test_op_877(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,877))

    def test_op_878(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,878))

    def test_op_879(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,879))

    def test_op_880(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,880))

    def test_op_881(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 < 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,881))

    def test_op_882(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,882))

    def test_op_883(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 > 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,883))

    def test_op_884(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 >= 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,884))

    def test_op_885(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <> 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,885))

    def test_op_886(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 = 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,886))

    def test_op_891(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,891))

    def test_op_892(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,892))

    def test_op_893(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,893))

    def test_op_894(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,894))

    def test_op_895(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,895))

    def test_op_896(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,896))

    def test_op_897(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 < 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,897))

    def test_op_898(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,898))

    def test_op_899(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 > 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,899))

    def test_op_900(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 >= 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(>=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,900))

    def test_op_901(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <> 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(<>,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,901))

    def test_op_902(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 = 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(=,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,902))

    def test_op_907(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,907))

    def test_op_908(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,908))

    def test_op_909(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,909))

    def test_op_910(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,910))

    def test_op_911(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,911))

    def test_op_912(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,912))

    def test_op_913(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,913))

    def test_op_914(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,914))

    def test_op_915(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,915))

    def test_op_916(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,916))

    def test_op_917(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,917))

    def test_op_918(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,918))

    def test_op_919(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,919))

    def test_op_920(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,920))

    def test_op_921(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,921))

    def test_op_922(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,922))

    def test_op_923(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,923))

    def test_op_924(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,924))

    def test_op_925(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,925))

    def test_op_926(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,926))

    def test_op_927(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,927))

    def test_op_928(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,928))

    def test_op_929(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,929))

    def test_op_930(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,930))

    def test_op_931(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,931))

    def test_op_932(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,932))

    def test_op_933(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,933))

    def test_op_934(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,934))

    def test_op_935(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,935))

    def test_op_936(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,936))

    def test_op_937(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,937))

    def test_op_938(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,938))

    def test_op_939(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,939))

    def test_op_940(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,940))

    def test_op_941(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,941))

    def test_op_942(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,942))

    def test_op_943(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,943))

    def test_op_944(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,944))

    def test_op_945(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,945))

    def test_op_946(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,946))

    def test_op_947(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,947))

    def test_op_948(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,948))

    def test_op_949(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,949))

    def test_op_950(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,950))

    def test_op_951(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,951))

    def test_op_952(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,952))

    def test_op_953(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,953))

    def test_op_954(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,954))

    def test_op_955(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,955))

    def test_op_956(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,956))

    def test_op_957(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,957))

    def test_op_958(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,958))

    def test_op_959(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,959))

    def test_op_960(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= 1.0 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,960))

    def test_op_961(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,961))

    def test_op_962(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,962))

    def test_op_963(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,963))

    def test_op_964(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,964))

    def test_op_965(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,965))

    def test_op_966(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,966))

    def test_op_967(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,967))

    def test_op_968(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,968))

    def test_op_969(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,969))

    def test_op_970(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,970))

    def test_op_971(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,971))

    def test_op_972(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,972))

    def test_op_973(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,973))

    def test_op_974(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,974))

    def test_op_975(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,975))

    def test_op_976(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,976))

    def test_op_977(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,977))

    def test_op_978(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,978))

    def test_op_979(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,979))

    def test_op_980(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,980))

    def test_op_981(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,981))

    def test_op_982(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,982))

    def test_op_983(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,983))

    def test_op_984(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,984))

    def test_op_985(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,985))

    def test_op_986(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,986))

    def test_op_987(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,987))

    def test_op_988(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,988))

    def test_op_989(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,989))

    def test_op_990(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,990))

    def test_op_991(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,991))

    def test_op_992(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,992))

    def test_op_993(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,993))

    def test_op_994(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,994))

    def test_op_995(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,995))

    def test_op_996(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,996))

    def test_op_997(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,997))

    def test_op_998(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,998))

    def test_op_999(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,999))

    def test_op_1000(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1000))

    def test_op_1001(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1001))

    def test_op_1002(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1002))

    def test_op_1003(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1003))

    def test_op_1004(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1004))

    def test_op_1005(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1005))

    def test_op_1006(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1006))

    def test_op_1007(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1007))

    def test_op_1008(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1008))

    def test_op_1009(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1009))

    def test_op_1010(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1010))

    def test_op_1011(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1011))

    def test_op_1012(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1012))

    def test_op_1013(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1013))

    def test_op_1014(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1014))

    def test_op_1015(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1015))

    def test_op_1016(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1016))

    def test_op_1017(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1017))

    def test_op_1018(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1018))

    def test_op_1019(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1019))

    def test_op_1020(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1020))

    def test_op_1021(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1021))

    def test_op_1022(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1022))

    def test_op_1023(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1023))

    def test_op_1024(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1024))

    def test_op_1025(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1025))

    def test_op_1026(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1026))

    def test_op_1027(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1027))

    def test_op_1028(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1028))

    def test_op_1029(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1029))

    def test_op_1030(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1030))

    def test_op_1031(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1031))

    def test_op_1032(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1032))

    def test_op_1033(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1033))

    def test_op_1034(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1034))

    def test_op_1035(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1035))

    def test_op_1036(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1036))

    def test_op_1037(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1037))

    def test_op_1038(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1038))

    def test_op_1039(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1039))

    def test_op_1040(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= "abc" or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1040))

    def test_op_1041(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1041))

    def test_op_1042(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1042))

    def test_op_1043(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1043))

    def test_op_1044(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1044))

    def test_op_1045(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1045))

    def test_op_1046(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1046))

    def test_op_1047(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1047))

    def test_op_1048(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1048))

    def test_op_1049(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1049))

    def test_op_1050(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1050))

    def test_op_1051(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1051))

    def test_op_1052(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1052))

    def test_op_1053(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1053))

    def test_op_1054(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1054))

    def test_op_1055(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1055))

    def test_op_1056(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1056))

    def test_op_1057(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1057))

    def test_op_1058(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1058))

    def test_op_1059(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1059))

    def test_op_1060(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1060))

    def test_op_1061(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1061))

    def test_op_1062(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1062))

    def test_op_1063(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1063))

    def test_op_1064(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1064))

    def test_op_1065(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1065))

    def test_op_1066(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1066))

    def test_op_1067(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1067))

    def test_op_1068(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1068))

    def test_op_1069(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1069))

    def test_op_1070(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1070))

    def test_op_1071(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1071))

    def test_op_1072(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1072))

    def test_op_1073(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1073))

    def test_op_1074(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1074))

    def test_op_1075(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1075))

    def test_op_1076(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1076))

    def test_op_1077(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1077))

    def test_op_1078(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1078))

    def test_op_1079(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1079))

    def test_op_1080(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1080))

    def test_op_1081(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1081))

    def test_op_1082(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1082))

    def test_op_1083(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1083))

    def test_op_1084(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1084))

    def test_op_1085(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1085))

    def test_op_1086(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1086))

    def test_op_1087(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1087))

    def test_op_1088(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1088))

    def test_op_1089(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1089))

    def test_op_1090(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1090))

    def test_op_1091(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1091))

    def test_op_1092(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1092))

    def test_op_1093(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1093))

    def test_op_1094(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1094))

    def test_op_1095(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1095))

    def test_op_1096(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1096))

    def test_op_1097(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1097))

    def test_op_1098(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1098))

    def test_op_1099(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1099))

    def test_op_1100(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1100))

    def test_op_1101(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1101))

    def test_op_1102(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1102))

    def test_op_1103(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1103))

    def test_op_1104(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1104))

    def test_op_1105(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1105))

    def test_op_1106(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1106))

    def test_op_1107(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1107))

    def test_op_1108(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1108))

    def test_op_1109(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1109))

    def test_op_1110(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1110))

    def test_op_1111(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1111))

    def test_op_1112(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1112))

    def test_op_1113(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1113))

    def test_op_1114(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1114))

    def test_op_1115(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1115))

    def test_op_1116(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1116))

    def test_op_1117(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1117))

    def test_op_1118(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1118))

    def test_op_1119(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1119))

    def test_op_1120(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= true or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(True),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1120))

    def test_op_1121(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1121))

    def test_op_1122(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1122))

    def test_op_1123(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1123))

    def test_op_1124(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1124))

    def test_op_1125(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1125))

    def test_op_1126(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1126))

    def test_op_1127(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1127))

    def test_op_1128(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1128))

    def test_op_1129(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1129))

    def test_op_1130(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1130))

    def test_op_1131(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1131))

    def test_op_1132(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1132))

    def test_op_1133(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1133))

    def test_op_1134(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1134))

    def test_op_1135(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1135))

    def test_op_1136(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1136))

    def test_op_1137(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1137))

    def test_op_1138(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1138))

    def test_op_1139(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1139))

    def test_op_1140(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1140))

    def test_op_1141(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1141))

    def test_op_1142(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1142))

    def test_op_1143(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1143))

    def test_op_1144(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1144))

    def test_op_1145(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1145))

    def test_op_1146(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1146))

    def test_op_1147(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1147))

    def test_op_1148(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1148))

    def test_op_1149(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1149))

    def test_op_1150(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1150))

    def test_op_1151(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1151))

    def test_op_1152(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1152))

    def test_op_1153(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1153))

    def test_op_1154(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1154))

    def test_op_1155(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1155))

    def test_op_1156(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1156))

    def test_op_1157(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1157))

    def test_op_1158(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1158))

    def test_op_1159(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1159))

    def test_op_1160(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1160))

    def test_op_1161(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1161))

    def test_op_1162(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1162))

    def test_op_1163(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1163))

    def test_op_1164(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1164))

    def test_op_1165(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1165))

    def test_op_1166(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1166))

    def test_op_1167(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1167))

    def test_op_1168(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1168))

    def test_op_1169(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1169))

    def test_op_1170(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1170))

    def test_op_1171(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1171))

    def test_op_1172(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1172))

    def test_op_1173(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1173))

    def test_op_1174(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1174))

    def test_op_1175(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1175))

    def test_op_1176(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1176))

    def test_op_1177(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1177))

    def test_op_1178(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1178))

    def test_op_1179(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1179))

    def test_op_1180(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1180))

    def test_op_1181(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1181))

    def test_op_1182(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1182))

    def test_op_1183(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and then true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1183))

    def test_op_1184(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or else true;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(True)))'
        self.assertTrue(TestChecker.test(input,expect,1184))

    def test_op_1185(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1185))

    def test_op_1186(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1186))

    def test_op_1187(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1187))

    def test_op_1188(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1188))

    def test_op_1189(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1189))

    def test_op_1190(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1190))

    def test_op_1191(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1191))

    def test_op_1192(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1192))

    def test_op_1193(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1193))

    def test_op_1194(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1194))

    def test_op_1195(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1195))

    def test_op_1196(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1196))

    def test_op_1197(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(and,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1197))

    def test_op_1198(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(or,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1198))

    def test_op_1199(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false and then false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(andthen,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1199))

    def test_op_1200(self):
        input = """
    procedure main();
    var a: real;
    begin
        a:= false or else false;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(orelse,BooleanLiteral(False),BooleanLiteral(False)))'
        self.assertTrue(TestChecker.test(input,expect,1200))

    def test_op_1207(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 + 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1207))

    def test_op_1208(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 - 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1208))

    def test_op_1209(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 * 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1209))

    def test_op_1210(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1210))

    def test_op_1211(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 div 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(div,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1211))

    def test_op_1212(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 mod 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(mod,IntLiteral(1),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1212))

    def test_op_1213(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1213))

    def test_op_1214(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1214))

    def test_op_1215(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1215))

    def test_op_1216(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1216))

    def test_op_1223(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1223))

    def test_op_1224(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1224))

    def test_op_1225(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1225))

    def test_op_1226(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,IntLiteral(1),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1226))

    def test_op_1227(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1227))

    def test_op_1228(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1228))

    def test_op_1229(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1229))

    def test_op_1230(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1230))

    def test_op_1231(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1231))

    def test_op_1232(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1232))

    def test_op_1233(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1233))

    def test_op_1234(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1234))

    def test_op_1235(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1235))

    def test_op_1236(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1236))

    def test_op_1237(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1237))

    def test_op_1238(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1238))

    def test_op_1239(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1239))

    def test_op_1240(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1240))

    def test_op_1241(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1241))

    def test_op_1242(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1242))

    def test_op_1243(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1243))

    def test_op_1244(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1244))

    def test_op_1245(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1245))

    def test_op_1246(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1246))

    def test_op_1247(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1247))

    def test_op_1248(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1248))

    def test_op_1249(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1249))

    def test_op_1250(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1250))

    def test_op_1251(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1251))

    def test_op_1252(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1252))

    def test_op_1253(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1253))

    def test_op_1254(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1254))

    def test_op_1255(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1255))

    def test_op_1256(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1256))

    def test_op_1257(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1257))

    def test_op_1258(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1258))

    def test_op_1259(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1259))

    def test_op_1260(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1260))

    def test_op_1261(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1261))

    def test_op_1262(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1262))

    def test_op_1263(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1263))

    def test_op_1264(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1264))

    def test_op_1265(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1265))

    def test_op_1266(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1266))

    def test_op_1267(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1267))

    def test_op_1268(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1268))

    def test_op_1269(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1269))

    def test_op_1270(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1270))

    def test_op_1271(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1271))

    def test_op_1272(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1272))

    def test_op_1273(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1273))

    def test_op_1274(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1274))

    def test_op_1275(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1275))

    def test_op_1276(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1276))

    def test_op_1277(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1277))

    def test_op_1278(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1278))

    def test_op_1279(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1279))

    def test_op_1280(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1280))

    def test_op_1287(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 + 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1287))

    def test_op_1288(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 - 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1288))

    def test_op_1289(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 * 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1289))

    def test_op_1290(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 / 1;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),IntLiteral(1)))'
        self.assertTrue(TestChecker.test(input,expect,1290))

    def test_op_1291(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1291))

    def test_op_1292(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1292))

    def test_op_1293(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1293))

    def test_op_1294(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1294))

    def test_op_1295(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1295))

    def test_op_1296(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1296))

    def test_op_1303(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 + 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1303))

    def test_op_1304(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 - 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1304))

    def test_op_1305(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 * 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(*,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1305))

    def test_op_1306(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 / 1.0;
    end
    """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,FloatLiteral(1.0),FloatLiteral(1.0)))'
        self.assertTrue(TestChecker.test(input,expect,1306))

    def test_op_1307(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1307))

    def test_op_1308(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1308))

    def test_op_1309(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1309))

    def test_op_1310(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1310))

    def test_op_1311(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1311))

    def test_op_1312(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1312))

    def test_op_1313(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1313))

    def test_op_1314(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1314))

    def test_op_1315(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1315))

    def test_op_1316(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1316))

    def test_op_1317(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1317))

    def test_op_1318(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1318))

    def test_op_1319(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1319))

    def test_op_1320(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1320))

    def test_op_1321(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1321))

    def test_op_1322(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1322))

    def test_op_1323(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1323))

    def test_op_1324(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1324))

    def test_op_1325(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1325))

    def test_op_1326(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1326))

    def test_op_1327(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1327))

    def test_op_1328(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1328))

    def test_op_1329(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1329))

    def test_op_1330(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1330))

    def test_op_1331(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1331))

    def test_op_1332(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1332))

    def test_op_1333(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1333))

    def test_op_1334(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1334))

    def test_op_1335(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1335))

    def test_op_1336(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1336))

    def test_op_1337(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1337))

    def test_op_1338(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1338))

    def test_op_1339(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1339))

    def test_op_1340(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1340))

    def test_op_1341(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1341))

    def test_op_1342(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1342))

    def test_op_1343(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1343))

    def test_op_1344(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1344))

    def test_op_1345(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1345))

    def test_op_1346(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1346))

    def test_op_1347(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1347))

    def test_op_1348(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1348))

    def test_op_1349(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1349))

    def test_op_1350(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1350))

    def test_op_1351(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1351))

    def test_op_1352(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1352))

    def test_op_1353(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1353))

    def test_op_1354(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1354))

    def test_op_1355(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1355))

    def test_op_1356(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1356))

    def test_op_1357(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1357))

    def test_op_1358(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1358))

    def test_op_1359(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1359))

    def test_op_1360(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= 1.0 or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,FloatLiteral(1.0),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1360))

    def test_op_1361(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1361))

    def test_op_1362(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1362))

    def test_op_1363(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1363))

    def test_op_1364(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1364))

    def test_op_1365(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1365))

    def test_op_1366(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1366))

    def test_op_1367(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1367))

    def test_op_1368(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1368))

    def test_op_1369(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1369))

    def test_op_1370(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1370))

    def test_op_1371(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1371))

    def test_op_1372(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1372))

    def test_op_1373(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1373))

    def test_op_1374(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1374))

    def test_op_1375(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1375))

    def test_op_1376(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1376))

    def test_op_1377(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1377))

    def test_op_1378(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1378))

    def test_op_1379(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1379))

    def test_op_1380(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1380))

    def test_op_1381(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1381))

    def test_op_1382(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1382))

    def test_op_1383(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1383))

    def test_op_1384(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1384))

    def test_op_1385(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1385))

    def test_op_1386(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1386))

    def test_op_1387(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1387))

    def test_op_1388(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1388))

    def test_op_1389(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1389))

    def test_op_1390(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1390))

    def test_op_1391(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1391))

    def test_op_1392(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1392))

    def test_op_1393(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1393))

    def test_op_1394(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1394))

    def test_op_1395(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1395))

    def test_op_1396(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1396))

    def test_op_1397(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1397))

    def test_op_1398(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1398))

    def test_op_1399(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1399))

    def test_op_1400(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1400))

    def test_op_1401(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1401))

    def test_op_1402(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1402))

    def test_op_1403(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1403))

    def test_op_1404(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1404))

    def test_op_1405(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1405))

    def test_op_1406(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1406))

    def test_op_1407(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1407))

    def test_op_1408(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1408))

    def test_op_1409(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1409))

    def test_op_1410(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1410))

    def test_op_1411(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1411))

    def test_op_1412(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1412))

    def test_op_1413(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1413))

    def test_op_1414(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1414))

    def test_op_1415(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1415))

    def test_op_1416(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1416))

    def test_op_1417(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1417))

    def test_op_1418(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1418))

    def test_op_1419(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1419))

    def test_op_1420(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1420))

    def test_op_1421(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1421))

    def test_op_1422(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1422))

    def test_op_1423(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and then true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1423))

    def test_op_1424(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or else true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1424))

    def test_op_1425(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1425))

    def test_op_1426(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1426))

    def test_op_1427(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1427))

    def test_op_1428(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1428))

    def test_op_1429(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1429))

    def test_op_1430(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1430))

    def test_op_1431(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1431))

    def test_op_1432(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1432))

    def test_op_1433(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1433))

    def test_op_1434(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1434))

    def test_op_1435(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1435))

    def test_op_1436(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1436))

    def test_op_1437(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1437))

    def test_op_1438(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1438))

    def test_op_1439(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" and then false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1439))

    def test_op_1440(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= "abc" or else false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,StringLiteral(abc),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1440))

    def test_op_1441(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1441))

    def test_op_1442(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1442))

    def test_op_1443(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1443))

    def test_op_1444(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1444))

    def test_op_1445(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1445))

    def test_op_1446(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1446))

    def test_op_1447(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1447))

    def test_op_1448(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1448))

    def test_op_1449(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1449))

    def test_op_1450(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1450))

    def test_op_1451(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1451))

    def test_op_1452(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1452))

    def test_op_1453(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1453))

    def test_op_1454(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1454))

    def test_op_1455(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1455))

    def test_op_1456(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1456))

    def test_op_1457(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1457))

    def test_op_1458(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1458))

    def test_op_1459(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1459))

    def test_op_1460(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1460))

    def test_op_1461(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1461))

    def test_op_1462(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1462))

    def test_op_1463(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1463))

    def test_op_1464(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1464))

    def test_op_1465(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1465))

    def test_op_1466(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1466))

    def test_op_1467(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1467))

    def test_op_1468(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1468))

    def test_op_1469(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1469))

    def test_op_1470(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1470))

    def test_op_1471(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1471))

    def test_op_1472(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1472))

    def test_op_1473(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1473))

    def test_op_1474(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1474))

    def test_op_1475(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1475))

    def test_op_1476(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1476))

    def test_op_1477(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1477))

    def test_op_1478(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1478))

    def test_op_1479(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1479))

    def test_op_1480(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1480))

    def test_op_1481(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1481))

    def test_op_1482(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1482))

    def test_op_1483(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1483))

    def test_op_1484(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1484))

    def test_op_1485(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1485))

    def test_op_1486(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1486))

    def test_op_1487(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1487))

    def test_op_1488(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(True),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1488))

    def test_op_1489(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1489))

    def test_op_1490(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1490))

    def test_op_1491(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1491))

    def test_op_1492(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1492))

    def test_op_1493(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1493))

    def test_op_1494(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1494))

    def test_op_1495(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1495))

    def test_op_1496(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1496))

    def test_op_1497(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1497))

    def test_op_1498(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1498))

    def test_op_1499(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1499))

    def test_op_1500(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1500))

    def test_op_1505(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1505))

    def test_op_1506(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1506))

    def test_op_1507(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1507))

    def test_op_1508(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1508))

    def test_op_1509(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1509))

    def test_op_1510(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1510))

    def test_op_1511(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1511))

    def test_op_1512(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1512))

    def test_op_1513(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1513))

    def test_op_1514(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1514))

    def test_op_1515(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1515))

    def test_op_1516(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= true mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(True),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1516))

    def test_op_1521(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false < 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1521))

    def test_op_1522(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1522))

    def test_op_1523(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false > 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1523))

    def test_op_1524(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false >= 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1524))

    def test_op_1525(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <> 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1525))

    def test_op_1526(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false = 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1526))

    def test_op_1527(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false + 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1527))

    def test_op_1528(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false - 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1528))

    def test_op_1529(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false * 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1529))

    def test_op_1530(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false / 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1530))

    def test_op_1531(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false div 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1531))

    def test_op_1532(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false mod 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1532))

    def test_op_1533(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1533))

    def test_op_1534(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1534))

    def test_op_1535(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and then 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1535))

    def test_op_1536(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or else 1;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),IntLiteral(1))'
        self.assertTrue(TestChecker.test(input,expect,1536))

    def test_op_1537(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false < 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1537))

    def test_op_1538(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1538))

    def test_op_1539(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false > 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1539))

    def test_op_1540(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false >= 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1540))

    def test_op_1541(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <> 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1541))

    def test_op_1542(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false = 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1542))

    def test_op_1543(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false + 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1543))

    def test_op_1544(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false - 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1544))

    def test_op_1545(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false * 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1545))

    def test_op_1546(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false / 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1546))

    def test_op_1547(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false div 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1547))

    def test_op_1548(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false mod 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1548))

    def test_op_1549(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1549))

    def test_op_1550(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1550))

    def test_op_1551(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and then 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1551))

    def test_op_1552(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or else 1.0;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),FloatLiteral(1.0))'
        self.assertTrue(TestChecker.test(input,expect,1552))

    def test_op_1553(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false < "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1553))

    def test_op_1554(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1554))

    def test_op_1555(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false > "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1555))

    def test_op_1556(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false >= "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1556))

    def test_op_1557(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <> "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1557))

    def test_op_1558(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false = "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1558))

    def test_op_1559(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false + "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1559))

    def test_op_1560(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false - "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1560))

    def test_op_1561(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false * "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1561))

    def test_op_1562(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false / "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1562))

    def test_op_1563(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false div "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1563))

    def test_op_1564(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false mod "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1564))

    def test_op_1565(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(and,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1565))

    def test_op_1566(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(or,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1566))

    def test_op_1567(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false and then "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(andthen,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1567))

    def test_op_1568(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false or else "abc";
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(orelse,BooleanLiteral(False),StringLiteral(abc))'
        self.assertTrue(TestChecker.test(input,expect,1568))

    def test_op_1569(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false < true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1569))

    def test_op_1570(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1570))

    def test_op_1571(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false > true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1571))

    def test_op_1572(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false >= true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1572))

    def test_op_1573(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <> true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1573))

    def test_op_1574(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false = true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1574))

    def test_op_1575(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false + true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1575))

    def test_op_1576(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false - true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1576))

    def test_op_1577(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false * true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1577))

    def test_op_1578(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false / true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1578))

    def test_op_1579(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false div true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1579))

    def test_op_1580(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false mod true;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(True))'
        self.assertTrue(TestChecker.test(input,expect,1580))

    def test_op_1585(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false < false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1585))

    def test_op_1586(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1586))

    def test_op_1587(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false > false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1587))

    def test_op_1588(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false >= false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1588))

    def test_op_1589(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false <> false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(<>,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1589))

    def test_op_1590(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false = false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(=,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1590))

    def test_op_1591(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false + false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1591))

    def test_op_1592(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false - false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1592))

    def test_op_1593(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false * false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1593))

    def test_op_1594(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false / false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1594))

    def test_op_1595(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false div false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1595))

    def test_op_1596(self):
        input = """
    procedure main();
    var a: boolean;
    begin
        a:= false mod false;
    end
    """
        expect = 'Type Mismatch In Expression: BinaryOp(mod,BooleanLiteral(False),BooleanLiteral(False))'
        self.assertTrue(TestChecker.test(input,expect,1596))

