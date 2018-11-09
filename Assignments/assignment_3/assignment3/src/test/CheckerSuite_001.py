import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_redeclared_variable_otr0(self):
        input = '''
            procedure main();
            begin
            end
            var a, ab, ba, b: integer;
                ba: string;
                c: real;
        '''
        expect = "Redeclared Variable: ba"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_redeclared_variable_otr1(self):
        input = '''
            procedure main();
            begin end
            var OTR, __otr__, otr: real;
        '''
        expect = "Redeclared Variable: otr"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redeclared_variable_otr2(self):
        input = '''
            VAR luan, otr: integer;
                oTr, __trluan__: boolean;
            procedure main();
            begin end
        '''
        expect = "Redeclared Variable: oTr"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_variable_otr3(self):
        input = '''
            procedure main();
            var x1, x2: integer;
                y1, y2, y3, X1: real;
            begin end
        '''
        expect = "Redeclared Variable: X1"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_redeclared_variable_otr4(self):
        input = '''
            procedure foo(otr:integer;a:string;c:boolean);
            var a, x, y: array[0 .. 2] of integer;
            begin
                putIntLn(x[10]);
            end
            procedure main();
            begin
                foo(1, "2", true);
            end
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_redeclared_variable_otr5(self):
        input = '''
            var x, y, z: array [1 .. -1] of integer;
                c: integer;
            function oanhtrinh(x, y, t:string): integer;
            var T, E, S: boolean;
            begin
                return 11111999;
            end
            procedure main();
            begin
                c := oanhtrinh("1", "2", "3");
                return;
            end
        '''
        expect = "Redeclared Variable: T"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_redeclared_variable_otr6(self):
        input = '''
            procedure main();
            begin end
            var MAIN: integer;
                LUAN: array[0 .. 4] of real;
        '''
        expect = "Redeclared Variable: MAIN"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_redeclared_variable_otr7(self):
        input = '''
            procedure main();
            begin
                putBoolLn(layer());
            end
            FUNCTION layer(): BOOLEAN;
            begin
                return false;
            end
            var myBear, layER: Boolean;
        '''
        expect = "Redeclared Variable: layER"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_redeclared_parameter_otr8(self):
        input = '''
            procedure main();
            begin
                foo(11111999, 16111998);
            end
            procedure foo(p, p:integer);
            begin
            end
        '''
        expect = "Redeclared Parameter: p"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_redeclared_parameter_otr9(self):
        input = '''
            var P, Q, R, pqrST: integer;
            procedure main();
            begin
                foo(0, 0, 0.1, TRUE);
            end
            procedure foo(p, pqrst:integer; x:real; P:boolean);
            begin
            end
        '''
        expect = "Redeclared Parameter: P"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_redeclared_procedure_otr10(self):
        input = '''
            var oanhtrinh, trongluan: array[0 .. 9] of STRING;
            procedure main();
            begin
                return;
            end
            procedure oanhtrinh();
            begin
            end
        '''
        expect = "Redeclared Procedure: oanhtrinh"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_redeclared_procedure_otr11(self):
        input = '''
            procedure main();
            begin
                oanhtrinh();
            end
            procedure oanhtrinh();
            begin
            end
            PROCEDURE OANHTRINH();
            var i, am, luan: boolean;
            begin
            end
        '''
        expect = "Redeclared Procedure: OANHTRINH"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_redeclared_procedure_otr12(self):
        input = '''
            function oanhtrinh(a,b,c:integer):integer;
            begin
                return 4102018;
            end
            procedure OaNhTrInH(a, b, c:integer);
            begin
            end
            procedure main();
            begin
                putFloat(oanhtring(0, 1, 2));
                return;
            end
        '''
        expect = "Redeclared Procedure: OaNhTrInH"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_redeclared_function_otr13(self):
        input = '''
            procedure main();
            begin end
            function foo():real;
            begin
                return foo1();
            end
            function foo1():real;
            begin
                return foo();
            end
            function FOO(a,b,c:boolean):array[0 .. -1] of integer;
            begin end
        '''
        expect = "Redeclared Function: FOO"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_redeclared_function_otr14(self):
        input = '''
            var oanhtrinh: array[9 .. 10] of boolean;
                foo: integer;
            procedure main();
            begin
                foo := LUAN(oanhtrinh);
            end
            var luan: array[10 .. 11] of real;
            function LUAN(oanhtrinh: array[9 .. 10] of boolean): integer;
            begin end
        '''
        expect = "Redeclared Function: LUAN"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_no_entry_point_otr15(self):
        input = '''
            procedure oanhtrinh();
            begin
                trongluan();
            end
            procedure trongluan();
            begin
                oanhtrinh();
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_no_entry_point_otr16(self):
        input = '''
            VAR list, tuple, set, dict, str: array[0 .. 100] of integer;
                pytagonas, euler, fermat: String;
                right, wrong: Boolean;
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_no_entry_point_otr17(self):
        input = '''
            var a, b, c: array[0 .. -10] of boolean;
            var x, y, z: array[0 .. -10] of string;
            function foo1(a,b:integer):integer;
            begin
                return foo2(getInt(), 11);
            end
            FUNCTION FOO2(A,B:INTEGER):INTEGER;
            BEGIN
                RETURN FOO1(11, getInt());
            END
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_no_entry_point_otr18(self):
        input = '''
            procedure main(ab, bc, ca: real);
            begin
                foo();
                main(getFloat(), 1.5/ (getFloat() + 3) / 4, ab);
                return;
            end
            procedure foo();
            begin
                main(2.5, 2, 3);
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_no_entry_point_otr19(self):
        input = '''
            function main():real;
            begin
                putStringLn("Huynh Thi Oanh Trinh");
                return foo() + 4.5;
            end
            function sub():real;
            begin
                putIntLn(1611931);
                return main() / 3 * 4 + 5;
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_no_entry_point_otr20(self):
        input = '''
            function MAIN(x, y: integer):integer;
            begin
                return x - 1611931 + fx();
            end
            function fx():integer;
            begin
                return MAIN(0, 0);
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_undeclared_identifier_otr21(self):
        input = '''
            var luan, __otr__: integer;
            var khang, minh, truyen, luong: String;
            procedure main();
            begin
                otr := 1 + 2 - 5 div 6;
                __otr__ := luan + 2 mod 5;
            end
        '''
        expect = "Undeclared Identifier: otr"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_undeclared_identifier_otr22(self):
        input = '''
            function otr(param: real):real;
            begin
                param := param + 1;
                return .11111999;
            end
            PROCEDURE Main();
            var x: real;
            begin
                x := (not (otr(otr(otr(otr(otr)))) mod 2) and FALSE OR TRUE) * 1.1111999;
                putInt(x);
                return;
            end
        '''
        expect = "Undeclared Identifier: otr"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_undeclared_identifier_otr23(self):
        input = '''
            function foo(x:string; y: boolean; z:array [0 .. 5] of string):real;
            var abc, def: integer;
            begin
                if (y and then y) or FALSE then
                begin
                    putstringln(x);
                    abc := def * 5 - 4;
                end
                else
                begin
                    return otr;
                end
                return abc;
            end
            procedure main();
            var mnp:real;
                qr: array[0 .. 5] of string;
            begin
                mnp := foo("1", true, qr);
                return;
            end
        '''
        expect = "Undeclared Identifier: otr"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_redeclared_procedure_otr24(self):
        input = '''
            procedure PUTSTRING(p:integer;q:real);
            begin
                putSTring("abc");
                return;
            end
            procedure main();
            begin
            end
        '''
        expect = "Redeclared Procedure: PUTSTRING"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_undeclared_identifier_otr25(self):
        input = '''
            procedure main();
            var otr: integer;
                x: array[0 .. 100] of integer;
            begin
                OTr := fOO();
                otr_trl(X, foo(), foo * 1.0);
            end
            function foo():integer;
            var i,j:integer;
                stack: array[0 .. 100] of integer;
            begin
                otr_trl(stack, i + j, j + 1);
                return 1 - 6 - 1 - 1 - 9 - 3 - 1;
            end
            procedure otr_trl(s:array[0 .. 100] of integer; m,n:real);
            begin
                putStringLn("I love you Oanh Trinh");
                putBool(False and True OR False);
                putIntLn(s[11111999]);
            end
        '''
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_undeclared_function_otr26(self):
        input = '''
            var otr, trl: array [1 .. 0] of integer;
            procedure maIN();
            begin
                putFloat(trl[10]);
                putFloatLn(otr(trl));
                putStringLn("False");
            end
        '''
        expect = "Undeclared Function: otr"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_undeclared_identifier_otr27(self):
        input = '''
            procedure otr();
            begin
            end
            procedure main();
            begin
                if otr = (-2.5 - 1.5) then
                    return;
                else
                    otr();
                return;
            end
        '''
        expect = "Undeclared Identifier: otr"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_undeclared_identifier_otr28(self):
        input = '''
            var i,j,k:integer;
            procedure main();
            begin
                for i := j + k to (k / h / j / j) div i do
                begin
                    putStringLn("I love Oanh Trinh");
                end
            end
        '''
        expect = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_undeclared_function_otr29(self):
        input = '''
            function abc(x:integer):real;
            var m: real;
            begin
                m := abc(1) + m;
                m := m MOD xyz(abc(2), 1.5, getFloat(), getInt(), "oanhtrinhcute") / 11.111999;
                return m;
            end
            procedure main();
            var n:real;
            begin
                n := n / abc(123) * 4;
            end
        '''
        expect = "Undeclared Function: xyz"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_undeclared_procedure_otr30(self):
        input = '''
            procedure KTRolster(Smeb, Score, Ucal, Deft, Mata: String);
            begin
                putString("KTRolster members: ");
                print(Smeb, ", ");
                print(Score, ", ");
                print(Ucal, ", ");
                print(Deft, ", ");
                print(Mata, ", ");
                return;
            end
            procedure main();
            var i,j,k: integer;
            begin
                KTRolster("Smeb", "Score", "Ucal", "Deft", "Mata");
                if i > k then
                    if j > k then
                        putBoolLn(False);
                    else
                        if k <> i then
                            putFloatLn(11+12+13+14);
            end
        '''
        expect = "Undeclared Procedure: print"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_undeclared_identifier_otr31(self):
        input = '''
            procedure main();
            begin
                while 2 <> (3.5 / 4 / Getfloat moD 0) do
                begin
                    begin
                        begin end
                    end
                end
            end
        '''
        expect = "Undeclared Identifier: Getfloat"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_undeclared_function_otr32(self):
        input = '''
            procedure count();
            begin
                Main();
            end
            procedure main();
            var foo: integer;
            begin
                COUNT();
                foo := 1.5 * ((count(foo, foo * 2) div 5) and 4) / 7 + 2;
                return;
            end
        '''
        expect = "Undeclared Function: count"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_undeclared_procedure_otr33(self):
        input = '''
            procedure main();
            var i,l,o,v,e,u:boolean;
                love: string;
            begin
                u := i and l or o and then v and __init__(__init__(__init__(e))) or u;
                putBoolLn(u);
                if u and i then
                    __init__(i, love, u);
                return;
            end
            function __init__(self:boolean):boolean;
            begin
                PUTSTRING("I am Luan Nguyen Trong");
                return self and then self or self and self or else self;
            end
        '''
        expect = "Undeclared Procedure: __init__"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_undeclared_procedure_otr34(self):
        input = '''
            var otr, trl: string;
            procedure main();
            var love: boolean;
            begin
                if love and True then
                begin
                    putSTRINGLN("Oanh Trinh, I love you");
                    return;
                end
                else
                    putSTRING("Oanh Trinh, I still love you");
                trl(trl, love, otr);
                while love do
                begin
                    while love do begin main(); end
                end
            end
        '''
        expect = "Undeclared Procedure: trl"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_typemismatchstatement_if_otr35(self):
        input = '''
            var girl, boy, gay: boolean;
            procedure MAIN();
            var gay: array[1 .. 10] of real;
            begin
                IF gay then 
                begin
                    PutString("You are are a gay");
                    PutString("Please afk");
                end
                putStringLn("You are are not gay");
                putStringLn("Come here");
            end
        '''
        expect = "Type Mismatch In Statement: If(Id(gay),[CallStmt(Id(PutString),[StringLiteral(You are are a gay)]),CallStmt(Id(PutString),[StringLiteral(Please afk)])],[])"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_typemismatchstatement_if_otr36(self):
        input = '''
            procedure main();
            var frac: real;
            begin
                frac := fraction(11111999);
                if (frac > 0) and (1 <= 2) and then (3 <> 4) then
                    putString("Large number");
                else
                    putString("Small number");
            end
            function fraction(n:integer):integer;
            begin
                if n then return n * fraction(n - 1);
                return 1;
            end
        '''
        expect = "Type Mismatch In Statement: If(Id(n),[Return(Some(BinaryOp(*,Id(n),CallExpr(Id(fraction),[BinaryOp(-,Id(n),IntLiteral(1))]))))],[])"
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_typemismatchstatement_while_otr37(self):
        input = '''
            procedure main();
            var a,b: boolean;
            begin
                with a:integer; do
                begin
                    while a do
                        a := a - 1;
                end
            end
        '''
        expect = "Type Mismatch In Statement: While(Id(a),[AssignStmt(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_typemismatchstatement_while_otr38(self):
        input = '''
            procedure main();
            begin
                while getName() do
                begin
                    if (2 = 2) or (3 = 3) then
                        putStringLn("Oanh Trinh");
                    else
                        putStringLn("Trong Luan");
                    break;
                end
            end
            function getName():String;
            var name: string;
            begin
                return name;
            end
        '''
        expect = "Type Mismatch In Statement: While(CallExpr(Id(getName),[]),[If(BinaryOp(or,BinaryOp(=,IntLiteral(2),IntLiteral(2)),BinaryOp(=,IntLiteral(3),IntLiteral(3))),[CallStmt(Id(putStringLn),[StringLiteral(Oanh Trinh)])],[CallStmt(Id(putStringLn),[StringLiteral(Trong Luan)])]),Break])"
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_typemismatchstatement_while_otr39(self):
        input = '''
            var arr: array[0 .. 1] of boolean;
                x, y, z: integer;
            
            function number(n:string):integer;
            begin
                return number(n);
            end
            
            function str(n:integer):string;
            begin
                return str(n);
            end

            function isnumber(n:string):boolean;
            begin
                if number(n) = number(str(number(n))) then
                    return true;
                return false;
            end

            procedure main();
            begin
                if isnumber("123") then
                    x := number("123");
                else
                    return;

                while arr[x + y + z] do
                begin
                    with arr: array[0 .. 1] of real; do
                    begin
                        while arr[x + y + z] do
                        begin
                            return;
                        end
                        x := y := z := GetInt();
                    end
                    continue;
                end
            end
        '''
        expect = "Type Mismatch In Statement: While(ArrayCell(Id(arr),BinaryOp(+,BinaryOp(+,Id(x),Id(y)),Id(z))),[Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_typemismatchstatement_for_otr40(self):
        input = '''
            var i, j, k: integer;
            procedure printrange(n: integer);
            begin
                for i := ((j + k div j + 10 - i) / 2) - 1 to n do
                    putIntLn(i);
            end
            procedure main();
            begin
                printRange(10);
            end
        '''
        expect = "Type Mismatch In Statement: For(Id(i)BinaryOp(-,BinaryOp(/,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(j),BinaryOp(div,Id(k),Id(j))),IntLiteral(10)),Id(i)),IntLiteral(2)),IntLiteral(1)),Id(n),True,[CallStmt(Id(putIntLn),[Id(i)])])"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_typemismatchstatement_for_otr41(self):
        input = '''
            var i:integer;
            procedure main();
            var i:boolean;
            begin
                for i := getInt() to (getInt() + 1000) do
                begin
                    i := (((1 >= 2) and (2 > 4)) or else (5 < 6)) and then (9 <= 10);
                    putboolLn(i);
                    return;
                end
            end
        '''
        expect = "Type Mismatch In Statement: For(Id(i)CallExpr(Id(getInt),[]),BinaryOp(+,CallExpr(Id(getInt),[]),IntLiteral(1000)),True,[AssignStmt(Id(i),BinaryOp(andthen,BinaryOp(orelse,BinaryOp(and,BinaryOp(>=,IntLiteral(1),IntLiteral(2)),BinaryOp(>,IntLiteral(2),IntLiteral(4))),BinaryOp(<,IntLiteral(5),IntLiteral(6))),BinaryOp(<=,IntLiteral(9),IntLiteral(10)))),CallStmt(Id(putboolLn),[Id(i)]),Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_typemismatchstatement_for_otr42(self):
        input = '''
            procedure main();
            var i: integer;
                arr: array [0 .. 1] of integer;
            begin
                for i := arr[0] to arr[10] do
                begin
                    with j,k: real; do
                    begin
                        for i := arr[1] to arr[2] do putString("I love OT");
                    end
                    with i,j,k: real; do
                    begin
                        for i := arr[1] to arr[2] do
                        begin 
                            putString("I love OT");
                            break;
                        end
                    end
                end
                return;
            end
        '''
        expect = "Type Mismatch In Statement: For(Id(i)ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2)),True,[CallStmt(Id(putString),[StringLiteral(I love OT)]),Break])"
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test_typemismatchstatement_for_otr43(self):
        input = '''
            procedure main();
            begin
                HCMUT(getINT(), GETint(), gETInt());
                HCMUT(getint(), GETINT(), gEtInT());
            end
            procedure HCMUT(a,b,c:integer);
            begin
                for a := b + c downTO b <= c do
                begin
                    break;
                end
                return;
            end
        '''
        expect = "Type Mismatch In Statement: For(Id(a)BinaryOp(+,Id(b),Id(c)),BinaryOp(<=,Id(b),Id(c)),False,[Break])"
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_typemismatchstatement_assign_otr44(self):
        input = '''
            function isPrime(main:integer):boolean;
            var i: integer;
            begin
                if main < 2 then
                    return NOT TRUE;
                else 
                begin
                    if main = 2 then
                        return TRUE;
                    else
                    begin
                        for i := 2 to main - 1 do
                            if (main mod i) = 0 then
                                return FALSE;
                        return TRUE;
                    end
                end
            end
            procedure main();
            var x, y: integer;
            begin
                x := getInt();
                y := isPrime(x);
                putString("Finish");
            end
        '''
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),CallExpr(Id(isPrime),[Id(x)]))"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_typemismatchstatement_assign_otr45(self):
        input = '''
            var abc: string;
            procedure main();
            begin
                abc := "I love OT";
            end
        '''
        expect = "Type Mismatch In Statement: AssignStmt(Id(abc),StringLiteral(I love OT))"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_typemismatchstatement_assign_otr46(self):
        input = '''
            function getArray(x:array[0 .. 0] of integer):array[0 .. 0] of integer;
            begin
                return x;
            end
            procedure main();
            var y: array [0 .. 0] of integer;
            begin
                y := getArray(y);
                return;
            end
        '''
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),CallExpr(Id(getArray),[Id(y)]))"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_typemismatchstatement_assign_otr47(self):
        input = '''
            var x, y, z: real;
                t, u: integer;
                k: boolean;
            procedure main();
            var u:boolean;
            begin
                u := u and k or u or k;
                z := t div 2 mod t;
                x := ((x + y * z) / t) + (t div t);
                t := ((t + 2 * t) / 3) + (t div 100);
                y := t / 0;
                k := (x > y) or else (y < z);
            end
        '''
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),BinaryOp(+,BinaryOp(/,BinaryOp(+,Id(t),BinaryOp(*,IntLiteral(2),Id(t))),IntLiteral(3)),BinaryOp(div,Id(t),IntLiteral(100))))"
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_typemismatchstatement_assign_otr48(self):
        input = '''
            PROCEDURE __init__(i:integer;r,q,p:real);
            var arr: ARRAY [0 .. 0] of REAL;
                brr: ARRAY [0 .. 0] of INTEGER;
            begin
                i := brr[1] := brr[0];
                brr[1] := brr[brr[brr[brr[brr[brr[0]]]]] div 4] - 10 div 5;
                i := r := q := p := arr[3] := brr[brr[brr[11]] - i div 2];
            end
            procedure main();
            var z:integer;
            begin
                for z := 0 DOWNTO 100 do
                    __init__(0, 0, 0, 0);
                return;
            end
        '''
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),Id(r))"
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_typemismatchstatement_return_otr49(self):
        input = '''
            procedure main();
            begin
                skt("Lee sang-hyoek");
            end
            procedure SKT(faker:string);
            var isFaker: boolean;
            begin
                if isFaker then
                    return faker;
                else
                    putString(faker);
                return;
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(faker)))"
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_typemismatchstatement_return_otr50(self):
        input = '''
            procedure main();
            begin end
            procedure MT16TN(leader:String);
            var isBao: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isBao then break;
                    return leader;
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(leader)))"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_typemismatchstatement_return_otr51(self):
        input = '''
            procedure main();
            begin
                if 2 > 3 then
                begin
                    if 2 > 4 then
                        return;
                    return;
                end
                while True do
                begin
                    if 10 < 11 then return;
                    return;
                end
                return (getInt() > getFloat()) and (16111998 < 11111999);
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(BinaryOp(and,BinaryOp(>,CallExpr(Id(getInt),[]),CallExpr(Id(getFloat),[])),BinaryOp(<,IntLiteral(16111998),IntLiteral(11111999)))))"
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_typemismatchstatement_return_otr52(self):
        input = '''
            var t: array[1 .. 2] of integer;
            procedure main();
            var foo: real;
            begin
                foo := func(t);
            end
            function Func(ab: array[1 .. 2] of integer):integer;
            var t: integer;
            begin
                ab[ab[10]] := t := 10;
                return ab[ab[t]] > ab[t];
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(BinaryOp(>,ArrayCell(Id(ab),ArrayCell(Id(ab),Id(t))),ArrayCell(Id(ab),Id(t)))))"
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_typemismatchstatement_return_otr53(self):
        input = '''
            var t: array[1 .. 2] of real;
            procedure main();
            var foo: real;
            begin
                foo := f(1);
                foo := func(t);
            end
            function f(bc:integer):real;
            begin
                return bc;
            end
            function Func(ab: array[1 .. 2] of real):integer;
            begin
                return ab[10];
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(ArrayCell(Id(ab),IntLiteral(10))))"
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_typemismatchstatement_return_otr54(self):
        input = '''
            procedure main();
            var T: integer;
            begin
                T := foo()[0];
                return;
            end
            function foo():array [1 .. 10] of integer;
            var x: array[1 .. 11] of integer;
            begin
                return x;
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_typemismatchstatement_return_otr55(self):
        input = '''
            function foo():array [1 .. 10] of real;
            var b: array[1 .. 10] of integer;
            begin
                return b;
            end
            procedure MAIN();
            var T: real;
            begin
                T := foo()[0];
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_typemismatchstatement_return_otr56(self):
        input = '''
            function foo():array [1 .. 10] of real;
            var b: array[2 .. 0] of string;
            begin
                return b;
            end
            procedure MAIN();
            var T: real;
            begin
                T := foo()[0];
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_typemismatchstatement_return_otr57(self):
        input = '''
            function foo():array [1 .. 10] of real;
            var b: array[1 .. 10] of real;
            begin
                return b;
            end
            function foo1():real;
            begin
                return foo2();
            end
            function foo2():integer;
            begin
                return foo1();
            end
            procedure MAIN();
            var T:real;
            begin
                T := foo()[0];
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(CallExpr(Id(foo1),[])))"
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_typemismatchstatement_return_otr58(self):
        input = '''
            function foo():integer;
            begin
                if True then 
                begin
                    PutSTring("abc");
                    return 1;
                end
                else
                begin
                    putString("xyz");
                    return;
                end
            end
            procedure main();
            var x:integer;
            begin
                x := foo();
            end
        '''
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_typemismatchstatement_return_otr59(self):
        input = '''
            function foo():integer;
            var i: integer;
            begin
                for i := 1 to 10 do
                begin
                    putInt(getInt());
                    putFloat(getInt());
                    return;
                end
                return 123;
            end
            procedure main();
            var x:integer;
            begin
                x := foo();
            end
        '''
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_typemismatchstatement_param_otr60(self):
        input = '''
            procedure Oanhtrinh(a:integer);
            begin
                putIntLn(a);
            end
            procedure main();
            begin
                Oanhtrinh(16111998);
                Oanhtrinh();
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[])"
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_typemismatchstatement_param_otr61(self):
        input = '''
            procedure Oanhtrinh(a:integer;b:real);
            begin
                putIntLn(a);
                putFloatLn(b);
            end
            procedure main();
            begin
                Oanhtrinh(0, 0.1);
                Oanhtrinh(1, 1.2, 10);
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[IntLiteral(1),FloatLiteral(1.2),IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_typemismatchstatement_param_otr62(self):
        input = '''
            procedure Oanhtrinh(a:integer; b:real);
            begin
                putIntLn(a);
                putFloatLn(b);
            end
            procedure main();
            var x: String;
            begin
                Oanhtrinh(1, 1.2);
                Oanhtrinh(x, 1.2);
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[Id(x),FloatLiteral(1.2)])"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_typemismatchstatement_param_otr63(self):
        input = '''
            procedure Oanhtrinh(a:real;b:integer;c:string;d:boolean);
            begin
                putFloatLn(a);
                putIntLn(b);
                putStringLn(c);
                putBoolLn(d);
            end
            procedure main();
            begin
                Oanhtrinh(9.75, 9, "Oanhtrinh", True);
                Oanhtrinh(0, 9, "oanhtrinh", False);
                Oanhtrinh(0, 9, False, 10);
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[IntLiteral(0),IntLiteral(9),BooleanLiteral(False),IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_typemismatchstatement_param_otr64(self):
        input = '''
            procedure Oanhtrinh(x:array[0 .. 10] of integer);
            begin
                putIntLn(x[1]);
            end
            procedure main();
            var a: array[-0 .. 10] of integer;
                b: array[-0 .. 10] of real;
            begin
                Oanhtrinh(a);
                Oanhtrinh(b);
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_typemismatchstatement_param_otr65(self):
        input = '''
            procedure Oanhtrinh(x:array[0 .. 10] of real);
            begin
                putFloatLn(x[1]);
            end
            procedure main();
            var a: array[-0 .. -10] of real;
                b: array[-0 .. 10] of real;
            begin
                Oanhtrinh(b);
                Oanhtrinh(a);
            end
        '''
        expect = "Type Mismatch In Statement: CallStmt(Id(Oanhtrinh),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_typemismatchexpression_arraycell_otr66(self):
        input = '''
            var t: integer;
            procedure main();
            var x: array[0 .. 1] of integer;
            begin
                if x[1.5] + 100 * 10 then
                    return; 
            end
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_typemismatchexpression_arraycell_otr67(self):
        input = '''
            var t: integer;
            procedure main();
            var x: array[0 .. 1] of integer;
            begin
                t := x[1 + 1 - 2 div 43];
                t := 2 + 1[2] div 1.5;
            end
        '''
        expect = "Type Mismatch In Expression: ArrayCell(IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_typemismatchexpression_arraycell_otr68(self):
        input = '''
            var t: integer;
            function foo():integer;
            begin
                return 1;
            end
            procedure main();
            begin
                t := (foo() + 3)[foo() + 3] / 4 / 5;
            end
        '''
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(3)),BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_typemismatchexpression_operator_otr69(self):
        input = '''
            procedure main();
            var a: real;
                b: integer;
            begin
                a := (10 div 11) + 12 / 13;
                for b := 1 downto ((-b + a) div (10 > 5)) do
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(div,BinaryOp(+,UnaryOp(-,Id(b)),Id(a)),BinaryOp(>,IntLiteral(10),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_typemismatchexpression_operator_otr70(self):
        input = '''
            procedure main();
            var a: real;
                b: integer;
            begin
                while not ("otr" + "trl") and ((2 mod 3) > (4 / 5)) do
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(otr),StringLiteral(trl))"
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_typemismatchexpression_operator_otr71(self):
        input = '''
            procedure main();
            begin
                with a,b:integer; c:boolean; d:string; do
                begin
                    c := ((-a----b) <> a) and then c;
                    a := (a Div b) mod 11 - 11 * 1999;
                    d := (a / b) DiV (a);
                end
                return;
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(DiV,BinaryOp(/,Id(a),Id(b)),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_typemismatchexpression_funcall_otr72(self):
        input = '''
            function sum(a,b,c:integer):integer;
            begin
                return a + b + c;
            end
            procedure main();
            begin
                if sum(11, 11) then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(11),IntLiteral(11)])"
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_typemismatchexpression_funcall_otr73(self):
        input = '''
            function sum(a,b,c:integer):integer;
            begin
                return a + b + c;
            end
            procedure main();
            begin
                while sum(11, 11, 1999, 16, 11, 1998) do
                    break;
                return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(11),IntLiteral(11),IntLiteral(1999),IntLiteral(16),IntLiteral(11),IntLiteral(1998)])"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_typemismatchexpression_funcall_otr74(self):
        input = '''
            function sum(a,b:integer;c:real):real;
            begin
                return a + b + c;
            end
            procedure main();
            begin
                if not sum(11, 11.5, 1999) then
                    return;
                if sum(11, 11, 19.99) = 1 then
                    return;
                if sum(11, 11, 1999) = 2 then
                    return;
                if sum(1, 2, 3) = 3 then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(11),FloatLiteral(11.5),IntLiteral(1999)])"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_typemismatchexpression_funcall_otr75(self):
        input = '''
            function sum(a, b:integer):integer;
            begin
                return a + b;
            end
            procedure main();
            begin
                if sum("abc", True) then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[StringLiteral(abc),BooleanLiteral(True)])"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_typemismatchexpression_funcall_otr76(self):
        input = '''
            function sum(x:array [1 .. 10] of real):real;
            var i:integer;
                S:real;
            begin
                S := 0;
                for i := 0 to 10 do
                    S := S + x[i];
                return S;
            end
            procedure main();
            var y:array[1 .. 10] of string;
            begin
                if sum(y) then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_typemismatchexpression_funcall_otr77(self):
        input = '''
            function sum(x:array [0 .. 10] of real):real;
            var i:integer;
                S:real;
            begin
                S := 0;
                for i := 0 to 10 do
                    S := S + x[i];
                return S;
            end
            procedure main();
            var y:array[-0 .. 10] of real;
                z:array[-1 .. 9] of real;
            begin
                if sum(y) > 0 then
                    return;
                if sum(z) then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[Id(z)])"
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_breaknotinloop_otr78(self):
        input = '''
            procedure MAIN();
            begin
                if True then
                begin
                    if false then
                    begin
                        putStringLn("Luan Nguyen Trong");
                        break;
                    end
                end
                return;
            end
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_breaknotinloop_otr78(self):
        input = '''
            procedure MAIN();
            begin
                WITH x,y:integer;a,b:real; do
                begin
                    for x := y to y + 10 do
                        break;
                    break;
                end
            end
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_breaknotinloop_otr79(self):
        input = '''
            function foo(n:integer):integer;
            var x: integer;
            begin
                while x > 10 do
                begin
                    x := x - 1;
                    if x < 4 then
                        break;
                end
                for x := 0 to 90 do
                begin
                    putIntLn(x);
                    if x = 67 then
                        break;
                    else
                        break;
                end
                if x <> 67 then
                    break;
                else
                    putStringLn("Oanh Trinh");
                return n;
            end
            procedure MAIN();
            var number:integer;
            begin
                number := foo(foo(foo(foo(10))));
            end
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_continuenotinloop_otr80(self):
        input = '''
            procedure MAIN();
            var a:array [10 .. -1] of string;
            begin
                WITH x,y:integer;a,b:real; do
                begin
                    while x < y do
                    begin
                        a := b := x := y + 100;
                        continue;
                    end
                end
                continue;
                putStringLn(a[11111999]);
                putStringLn(a[16111998]);
            end
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_continuenotinloop_otr81(self):
        input = '''
            procedure main();
            begin
                cseHcmut();
            end
            procedure cseHcmut();
            var otr: integer;
            begin
                for otr := 100 downto 0 do
                begin
                    if otr > otr + 1 then
                        break;
                    while otr < otr + 1 do
                    begin
                        putString("Oanh trinh");
                        putStringLn("Oanh trinh");
                        continue;
                    end
                    if otr = 10 then
                        continue;
                    else
                        putInt(100);
                end
                if otr = 10 then
                begin
                    putBoolLn(True);
                    continue;
                end
                putStringLn("SK Telecom T1");
                return;
            end
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_function_notreturn_otr82(self):
        input = '''
            function FOO(a,b:integer;c:real):integer;
            begin
                putStringLn("Hello, this is FOO function");
                c := a := b := 10;
                if a = b then
                    return 0;
                for a := b to a + b do
                    return 0;
                while a < 10 do
                    return 0;
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo(0, 8, 7.5);
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_function_notreturn_otr83(self):
        input = '''
            function FOO():integer;
            var x, y, i: integer;
            begin
                if x <> y then
                begin
                    for i := 0 to 55 do
                    begin
                        x := getINt();
                        putIntLn(x);
                        break;
                    end
                    return 0;
                end
                else
                begin
                    if x = y then
                    begin
                        main();
                        return 0;
                    end
                end
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_function_notreturn_otr84(self):
        input = '''
            function FOO():integer;
            var x,y:integer;
            begin
                IF x <> y then
                    IF x < 10 then
                    begin
                        putStringLn("Hello world!");
                        return 0;
                    END
                    ELSE
                    begin
                        putStringLn("Hello Luan!");
                        putStringLn("Hello Otrinh!");
                        return 0;
                    end
                ELSE
                begin
                    IF y > 10 THEN
                    begin
                        IF x * y > 10 THEN
                        begin
                            putStringLn("Hello PPL!");
                            if x = 0 then
                                return 0;
                            return 0;
                        end
                        else
                        BEGIN
                            if y <> 5 then
                            begin
                                if y = 1 then
                                    return 0;
                                else
                                    return 2;
                            end
                            else
                            begin
                                if y = 2 then
                                    return 0;
                                putStringLn("Hello BKU!");
                            end
                        END
                    end
                    ELSE
                    begin
                        if y - y = 0 then
                        begin
                            return 0;
                        end
                        else
                        begin
                            if x < y then
                                return 100;
                            else 
                                return 0;
                        end
                    end
                end
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_function_notreturn_otr85(self):
        input = '''
            function FOO():integer;
            var x,y,i: integer;
            begin
                IF true THEN
                BEGIN
                    FOR i := 0 to 100 do
                    begin
                        if i = 20 then
                            break;
                        if i = x + y then
                        begin
                            putIntLn(i);
                            putStringLn("Hello Python!");
                            return 0;
                        end
                        else
                        begin
                            main();
                            return 0;
                        end
                    end
                END
                ELSE
                BEGIN
                    with a,b:integer; do
                    begin
                        while x <> y do
                        begin
                            a := b := x := y := 0;
                            if x = y then
                                break;
                            else
                                putStringLn("Hello C++");
                            return 0;
                        end
                        if x <> y then
                            return 0;
                        else
                            return a + b + y + x;
                    end
                END
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_function_notreturn_otr86(self):
        input = '''
            function FOO():integer;
            var x, y: integer;
            begin
                while x <> y do
                begin
                    FOR x := 0 to 99 do 
                    begin
                        putString("Hello Java!");
                        if x * y <> 0 then
                            putStringLn("Hello Scala!");
                        else
                            break;
                        with a,b: integer; do
                        begin
                            if x * y <> 0 then
                                continue;
                            else
                                putStringLn("Hello Ocaml!");
                            return 0;
                        end
                    end
                    return 0;
                end
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_function_notreturn_otr87(self):
        input = '''
            function FOO():integer;
            var x, y: integer;
            begin
                for x:= 0 to 99 do
                begin
                    while x <> y do 
                    begin
                        putString("Hello Java!");
                        if x * y <> 0 then
                            putStringLn("Hello Scala!");
                        else
                            break;
                        with a,b: integer; do
                        begin
                            if x * y <> 0 then
                                continue;
                            else
                                putStringLn("Hello Ocaml!");
                            return 0;
                        end
                    end
                    return 0;
                end
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,487))
    
    def test_function_notreturn_otr88(self):
        input = '''
            function FOO1():integer;
            begin
                with a,b:real;c:integer; do
                begin
                    while a + c > b do
                    begin
                        putStringLn("Hello C!");
                        return 0;
                    end
                    putStringLn("Hello C#!");
                    if a = b then
                    begin
                        putStringLn("Hello Ada!");
                        return 0;
                    end
                    else
                        return 0;
                end
            end
            function FOO():integer;
            var x, y: integer;
            begin
                if (x MOD y) = 2 then
                begin
                    putStringLn("Hello PHP!");
                    return 1;
                end
                else
                    putStringLn("Hello HTML!");
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_function_notreturn_otr89(self):
        input = '''
            function FOO1():integer;
            var x,y:integer;
            begin
                IF x <> y then
                    IF x < 10 then
                    begin
                        putStringLn("Hello world!");
                        return 0;
                    END
                    ELSE
                    begin
                        putStringLn("Hello Luan!");
                        putStringLn("Hello Otrinh!");
                        return 0;
                    end
                ELSE
                begin
                    IF y > 10 THEN
                    begin
                        IF x * y > 10 THEN
                        begin
                            putStringLn("Hello PPL!");
                            if x = 0 then
                                return 0;
                            return 0;
                        end
                        else
                        BEGIN
                            if y <> 5 then
                            begin
                                if y = 1 then
                                    return 0;
                                else
                                    return 2;
                            end
                            else
                            begin
                                if y = 2 then
                                    return 0;
                                putStringLn("Hello BKU!");
                                return 0;
                            end
                        END
                    end
                    ELSE
                    begin
                        if y - y = 0 then
                        begin
                            return 0;
                        end
                        else
                        begin
                            if x < y then
                                return 100;
                            else 
                                return 0;
                        end
                    end
                end
            end
            function FOO():integer;
            var x, y: integer;
            begin
                with a,b:integer; do
                begin
                    for a:= 0 to b do
                        return 0;
                    if a > b then
                        return 0;
                    while a <> 1 do
                        return 0;
                end
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_function_notreturn_otr90(self):
        input = '''
            function FOO1():integer;
            var x,y: integer;
            begin
                if x = y then
                begin
                    with a:integer; do
                    begin
                        for a := 0 to 10 do
                        begin
                            putStringLn("Hello CSS!");
                            if a <> 10 then
                                a := a + 1;
                            if a <> 5 then
                                continue;
                        end
                        if a = 1 then
                        begin
                            with x:real; do
                            begin
                                putFloatLn(x);
                                return 0;
                            end 
                        end
                        return 1;
                    end
                end
                else 
                BEGIN
                    with a:integer; do
                    begin
                        if a <> 0 then
                            return 0;
                        else
                        begin
                            for a := 0 to 100 do
                                return 0;
                            return 1;
                        end
                    end
                END
            end
            function FOO():integer;
            var x, y: integer;
            begin
                if x < y then
                begin
                    x := x + 1;
                    for x := 0 to 100 do
                        return 0;
                end
                else
                    while y <> 0 do return 0;
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_function_notreturn_otr91(self):
        input = '''
            function FOO1():integer;
            var x, y: integer;
            begin
                if x <> y then
                    return 0;
                for x := x div y to x mod y do
                    return 0;
                while x = y do begin
                    return 0;
                end
                with a:integer; do
                begin
                    return a;
                end
            end
            function FOO():integer;
            var x, y: integer;
            begin
                x := y + 1;
                putStringLn("Hello Javascript!");
                putIntLn(0);
                putFloatLn(x + y);
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = "Function FOONot Return "
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_function_notreturn_otr92(self):
        input = '''
            function FOO1():integer;
            begin
                if True then if false then if true then if false then if true then if true then if false then if false then return 0;
            end
            function FOO():integer;
            begin
                if True then if false then if true then if false then if true then if true then if false then if false then return 0;
                return 0;
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = "Function FOO1Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_unreachable_function_otr93(self):
        input = '''
            function foo():integer;
            begin
                return 0;
            end
            procedure main();
            begin
            end
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_unreachable_function_otr94(self):
        input = '''
            procedure foo();
            begin
            end
            function foo1():integer;
            begin
                foo();
                return 0;
            end
            procedure main();
            begin
            end
        '''
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_unreachable_function_otr95(self):
        input = '''
            function foo():integer;
            begin
                putIntLn(foo());
                return 0;
            end
            procedure main();
            begin
            end
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_unreachable_function_otr96(self):
        input = '''
            procedure main();
            var i:integer;
            begin
                for i := skt() + getInt() to 100 do
                begin
                    if i <> 5 then
                        i := i + skt();
                    else
                        i := i - skt();
                end
            end
            function kt():integer;
            begin
                return skt();
            end
            function skt():integer;
            begin
                putIntLn(skt());
                return 0;
            end
        '''
        expect = "Unreachable Function: kt"
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_unreachable_procedure_otr97(self):
        input = '''
            procedure main();
            begin
            end
            procedure otr1();
            begin
                otr2();
            end
            procedure otr2();
            begin
                otr3();
            end
            procedure otr3();
            begin
                otr4();
            end
            procedure otr4();
            begin
                main();
            end
        '''
        expect = "Unreachable Procedure: otr1"
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_unreachable_procedure_otr98(self):
        input = '''
            procedure main();
            begin
            end
            procedure otr();
            begin
                otr();
            end
        '''
        expect = "Unreachable Procedure: otr"
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_unreacable_statement_otr99(self):
        input = '''
            procedure main();
            var i:integer;
            begin
                for i := 0 to 100 do
                begin
                    break;
                    continue;
                end
            end
        '''
        expect = "Unreachable statement: Continue"
        self.assertTrue(TestChecker.test(input,expect,499))
    
    def test_unreacable_statement_otr100(self):
        input = '''
            procedure main();
            var c:boolean;
            begin
                if c then
                begin
                    if True then
                        return;
                    return;
                end
                else
                begin
                    putStringLn("Hello Lua!");
                    return;
                end
                putStringLn("Hello Ruby!");
            end
        '''
        expect = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello Ruby!)])"
        self.assertTrue(TestChecker.test(input,expect,500))
    
    def test_unreacable_statement_otr101(self):
        input = '''
            procedure main();
            var i:integer;
            begin
                i := 0;
                while i < 100 do
                begin
                    putIntLn(i);
                    i := i + 1;
                    if i = 60 then
                        return;
                    putStringLn("Hello Haskell!");
                    if i = 70 then
                        break;
                    else
                        continue;
                    putStringLn("Hello Smalltalk!");
                end 
            end
        '''
        expect = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello Smalltalk!)])"
        self.assertTrue(TestChecker.test(input,expect,501))
    
    def test_unreacable_statement_otr102(self):
        input = '''
            procedure main();
            var i:integer;
            begin
                i := 20;
                while i <> 1 do
                begin
                    i := i - 1;
                    if i = 3 then
                        break;
                    putStringLn("Hello Perl!");
                end
                for i := 0 to 100 do
                begin
                    putStringLn("Hello Pascal!");
                    if i = 50 then
                        return;
                    else
                        continue;
                end
                with otr:real; do
                begin
                    putFloatLn(otr);
                    putStringLn("Hello MP!");
                    if otr > i then
                        return;
                    else
                    begin
                        putStringLn("Hello Objective-C!");
                        return;
                    end
                end
                if i = 1 then
                    putFloatLn(i);
                else
                    putStringLn("Hello BASIC!");
                putStringLn("Hello COBOL!");
            end
        '''
        expect = "Unreachable statement: If(BinaryOp(=,Id(i),IntLiteral(1)),[CallStmt(Id(putFloatLn),[Id(i)])],[CallStmt(Id(putStringLn),[StringLiteral(Hello BASIC!)])])"
        self.assertTrue(TestChecker.test(input,expect,502))
    
    def test_unreacable_statement_otr503(self):
        input = '''
            procedure OANHTRINH();
            begin
                if True then
                    if False then
                        if True then
                            if False then
                                if True then
                                    return;
                putStringLn("Hello Clojure!");
            end
            function f(): integer;
            var x, y: integer;
            begin
                OANHTRINH();
                IF x <> y then
                    IF x < 10 then
                    begin
                        putStringLn("Hello world!");
                        return 0;
                    END
                    ELSE
                    begin
                        putStringLn("Hello Luan!");
                        putStringLn("Hello Otrinh!");
                        return 0;
                    end
                ELSE
                begin
                    IF y > 10 THEN
                    begin
                        IF x * y > 10 THEN
                        begin
                            putStringLn("Hello PPL!");
                            if x = 0 then
                                return 0;
                            return 0;
                        end
                        else
                        BEGIN
                            if y <> 5 then
                            begin
                                if y = 1 then
                                    return 0;
                                else
                                    return 2;
                            end
                            else
                            begin
                                if y = 2 then
                                    return 0;
                                putStringLn("Hello BKU!");
                                return 0;
                            end
                        END
                    end
                    ELSE
                    begin
                        if y - y = 0 then
                        begin
                            return 0;
                        end
                        else
                        begin
                            if x < y then
                                return 100;
                            else 
                                return 0;
                        end
                    end
                end
                putStringLn("Hello Fortran!");
                return 11111999;
            end
            procedure Main();
            var liss: integer;
            begin
                liss := f();
            end
        '''
        expect = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello Fortran!)])"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_unreacable_statement_otr104(self):
        input = '''
            procedure main();
            var i:integer;
            begin
                while i < 100 do 
                begin
                    for i := 0 to 99 do
                    begin
                        putStringLn("Hello Go!");
                        if i <= 60 then
                            putStringLn("Hello Kotlin!");
                        else
                            continue;
                        putStringLn("Hello Lisp!");
                    end
                    if i <= 20 then
                        break;
                    else
                        putStringLn("Hello Prolog!");
                    putStringLn("Hello F#!");
                end
                putStringLn("Hello R!");
                with otr:integer; do
                begin
                    putFloatLn(otr);
                    if i < 0 then
                        return;
                    return;
                end
                putStringLn("Hello R++!");
            end
        '''
        expect = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello R++!)])"
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_unreacable_statement_otr105(self):
        input = '''
            procedure oanhtrinh();
            var i: integer;
            begin
                i := 0;
                while i < 100 do
                begin
                    if i = 70 then
                    begin
                        if i = 50 then
                        begin
                            for i := 0 to 99 do
                            begin
                                putStringLn("Hello MIIS!");
                                if 1 < 2 then
                                    break;
                                else
                                    putStringLn("Hello Maple!");
                                return;
                            end
                            return;
                        end
                        else
                        begin
                            if 2 < 6 then
                                return;
                            else
                            begin
                                with a:real; do
                                    return;
                            end
                        end
                    end
                    else
                    begin
                        return;
                    end
                    putStringLn("Hello Lynx!");
                end 
            end
            procedure main();
            var i:integer;
            begin
                oanhtrinh();
                i := 0;
                while i < 100 do
                begin
                    if i = 70 then
                    begin
                        if i = 50 then
                        begin
                            for i := 0 to 99 do
                            begin
                                putStringLn("Hello Sodility!");
                                if 1 < 2 then
                                    break;
                                else
                                    putStringLn("Hello RSL!");
                                return;
                            end
                            return;
                        end
                        else
                        begin
                            if 2 < 6 then
                                return;
                        end
                    end
                    else
                    begin
                        return;
                    end
                    putStringLn("Hello OpenCL!");
                end 
            end
        '''
        expect = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello Lynx!)])"
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_unreacable_statement_otr106(self):
        input = '''
            procedure main();
            begin
                if True then
                    if False then
                        if True then
                            if False then
                                if False then
                                    if True then
                                        return;
                else return;
                    else return;
                        else return;
                            else return;
                                else return;
                putStringLn("Hello MATLAB!");
                with a:integer; do
                    with a:real; do
                        with a:boolean; do
                            with a:string; do
                                with a:array[0 .. 1] of real; do
                                    return;
                while True do
                    putStringLn("Hello JScript!");
            end
        '''
        expect = "Unreachable statement: While(BooleanLiteral(True),[CallStmt(Id(putStringLn),[StringLiteral(Hello JScript!)])])"
        self.assertTrue(TestChecker.test(input,expect,506))

    
