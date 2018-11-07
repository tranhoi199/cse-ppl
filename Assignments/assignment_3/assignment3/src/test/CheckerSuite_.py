import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""

procedure main();
begin
    ok();
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 101))


    def test_2(self):
        input = r"""

procedure main();
var a,b,c,a: integer;
begin
end

"""
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 102))


    def test_3(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,b: string;
begin
end

"""
        expect = r"""Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 103))


    def test_4(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,y: array[1 .. 2] of boolean;
begin

end

"""
        expect = r"""Redeclared Variable: y"""
        self.assertTrue(TestChecker.test(input, expect, 104))


    def test_5(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure main();
begin
end

"""
        expect = r"""Redeclared Procedure: main"""
        self.assertTrue(TestChecker.test(input, expect, 105))


    def test_6(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1();
begin
end

procedure f2();
begin
end

procedure f1();
begin
end

"""
        expect = r"""Redeclared Procedure: f1"""
        self.assertTrue(TestChecker.test(input, expect, 106))


    def test_7(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1();
begin
end

procedure f2();
begin
end

function f1(): String;
begin
    return "";
end

"""
        expect = r"""Redeclared Function: f1"""
        self.assertTrue(TestChecker.test(input, expect, 107))


    def test_8(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1(a,x,g,x: string);
begin
end

"""
        expect = r"""Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input, expect, 108))


    def test_9(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1(a,x,g: string; b,y,h: real; c,z,h: array[1 .. 2] of boolean);
begin
end

"""
        expect = r"""Redeclared Parameter: h"""
        self.assertTrue(TestChecker.test(input, expect, 109))


    def test_10(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1(a,x,g: string; b,y,h: real; c,z,t: array[1 .. 2] of boolean);
var z: boolean;
begin
end

"""
        expect = r"""Redeclared Variable: z"""
        self.assertTrue(TestChecker.test(input, expect, 110))


    def test_11(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
end

procedure f1(a,x,g: string; b,y,h: real; c,z,t: array[1 .. 2] of boolean);
var i,j,k: integer; u,v,t: real;
begin
end

"""
        expect = r"""Redeclared Variable: t"""
        self.assertTrue(TestChecker.test(input, expect, 111))


    def test_12(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
    f2();
end

procedure f1(a,x,g: string; b,y,h: real; c,z,t: array[1 .. 2] of boolean);
var i,j,k: integer; u,v,f: real;
begin
end

"""
        expect = r"""Undeclared Procedure: f2"""
        self.assertTrue(TestChecker.test(input, expect, 112))


    def test_13(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
    a := f2();
end

procedure f1(a,x,g: string; b,y,h: real; c,z,t: array[1 .. 2] of boolean);
var i,j,k: integer; u,v,f: real;
begin
end

"""
        expect = r"""Undeclared Function: f2"""
        self.assertTrue(TestChecker.test(input, expect, 113))


    def test_14(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
    f := 1;
end

procedure f1(a,x,g: string; b,y,h: real; c,z,t: array[1 .. 2] of boolean);
var i,j,k: integer; u,v,f: real;
begin
end

"""
        expect = r"""Undeclared Identifier: f"""
        self.assertTrue(TestChecker.test(input, expect, 114))


    def test_15(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
begin
    p1();
    a := f1();
    p2();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Undeclared Procedure: p2"""
        self.assertTrue(TestChecker.test(input, expect, 115))


    def test_16(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    a := getInt();
    p := getFloat();
    putInt(b);
    putFloat(k);
    putIntLn(c);
    putFloatLn(q);
    putBoolLn(g[1]);
    putString(x);
    putStringLn("H");
    putLn();
    p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Unreachable Function: f1"""
        self.assertTrue(TestChecker.test(input, expect, 116))


    def test_17(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

procedure getInt();
begin
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Redeclared Procedure: getInt"""
        self.assertTrue(TestChecker.test(input, expect, 117))


    def test_18(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

function putLn(): String;
begin
    return "";
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Redeclared Function: putLn"""
        self.assertTrue(TestChecker.test(input, expect, 118))


    def test_19(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    if 1 then p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Type Mismatch In Statement: If(IntLiteral(1),[CallStmt(Id(p1),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 119))


    def test_20(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    if a then p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Type Mismatch In Statement: If(Id(a),[CallStmt(Id(p1),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 120))


    def test_21(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    if g then p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Type Mismatch In Statement: If(Id(g),[CallStmt(Id(p1),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 121))


    def test_22(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    if a+b*c then p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Type Mismatch In Statement: If(BinaryOp(+,Id(a),BinaryOp(*,Id(b),Id(c))),[CallStmt(Id(p1),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 122))


    def test_23(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    if g[1] then p1();
    if g[1] and h[2] then p1();
    if g[1] OR h[2] AnD g[2] then p1();
    if g[1] AND thEn h[2] aNd nOt g[2] OR ElSE h[1] then p1();
    if a = 4 then p1();
    if a+b*c = 4 then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) = b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) > b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) < b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) <> b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) >= b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if a*b+c-4*(4+6+b*2-4*2*2*4*6+c) <= b*2-4*2*2*4 and then g[2] or h[1] then p1();
    if x then p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Type Mismatch In Statement: If(Id(x),[CallStmt(Id(p1),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 123))


    def test_24(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    for a := 1 to 10 do p1();
    for a := a*b+c-4*(4+6+b*2-4*2*2*4*6+c) to 10 do p1();
    for a := 10 to a*b+c-4*(4+6+b*2-4*2*2*4*6+c) do p1();
    for a := 10.0 to a*b+c-4*(4+6+b*2-4*2*2*4*6+c) do p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Type Mismatch In Statement: For(Id(a)FloatLiteral(10.0),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(*,IntLiteral(4),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(4),IntLiteral(6)),BinaryOp(*,Id(b),IntLiteral(2))),BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,IntLiteral(4),IntLiteral(2)),IntLiteral(2)),IntLiteral(4)),IntLiteral(6))),Id(c)))),True,[CallStmt(Id(p1),[])])"""
        self.assertTrue(TestChecker.test(input, expect, 124))


    def test_25(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    while g[2] do p1();
    while a*b+c-4*(4+6+b*2-4*2*2*4*6+c) = b*2-4*2*2*4 do p1();
    while a*b+c-4*(4+6+b*2-4*2*2*4*6+c) < b*2-4*2*2*4 and then g[2] or h[1] do p1();
    while g do p1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end


"""
        expect = r"""Type Mismatch In Statement: While(Id(g),[CallStmt(Id(p1),[])])"""
        self.assertTrue(TestChecker.test(input, expect, 125))


    def test_26(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    a := 1;
    p := 5.0;
    q := 1;
    k := a;
    a := b := 1;
    a := b := c := 1;
    a := b := c := a*b+c-4*(4+6+b*2-4*2*2*4*6+c);
    p := a := b := c := a*b+c-4*(4+6+b*2-4*2*2*4*6+c);
    p := q := k := a := b := c := a*b+c-4*(4+6+b*2-4*2*2*4*6+c);

    a := f1();
    k := f1();
    p := q := k := a := b := c := f1();

    p := a := k := a := b := c := f1();
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(a),Id(k))"""
        self.assertTrue(TestChecker.test(input, expect, 126))


    def test_27(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
    g[1] := True;
    h[1] := False;
    g[1] := h[2];
    g[2] := h[1] and True;
    h[1] := g[1] AND thEn h[2] aNd nOt g[2] OR ElSE h[1];
    h[2] := a*b+c-4*(4+6+b*2-4*2*2*4*6+c) = b*2-4*2*2*4;
    g[2] := g[1] AND thEn h[2] aNd nOt g[2] OR ElSE h[1];
    h[1] := a*b+c-4*(4+6+b*2-4*2*2*4*6+c) = b*2-4*2*2*4 and then g[2] or h[1];
    g[1] := g[2] := h[1] := a*b+c-4*(4+6+b*2-4*2*2*4*6+c) = b*2-4*2*2*4 and then g[2] or h[1];

    h[1] := a;
end

procedure p1();
begin
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Type Mismatch In Statement: AssignStmt(ArrayCell(Id(h),IntLiteral(1)),Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 127))


    def test_28(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

procedure p1();
begin
    return "";
end

function f1(): integer;
begin
    return 0;
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(StringLiteral()))"""
        self.assertTrue(TestChecker.test(input, expect, 128))


    def test_29(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return;
end

"""
        expect = r"""Type Mismatch In Statement: Return(None)"""
        self.assertTrue(TestChecker.test(input, expect, 129))


    def test_30(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var
    a1: array[0 .. 15] of real;
    a2: array[-5 .. 10] of string;
    a3: array[-5 .. 10] of real;
begin
    return a1;
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(Id(a1)))"""
        self.assertTrue(TestChecker.test(input, expect, 130))


    def test_31(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
begin
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var
    a1: array[0 .. 15] of real;
    a2: array[-5 .. 10] of string;
    a3: array[-5 .. 10] of real;
begin
    return a2;
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(Id(a2)))"""
        self.assertTrue(TestChecker.test(input, expect, 131))


    def test_32(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    p1();
    a := f1();
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var
    a1: array[0 .. 15] of real;
    a2: array[-5 .. 10] of string;
    a3: array[-5 .. 10] of real;
begin
    return a3;
end

"""
        expect = r"""Unreachable Function: f2"""
        self.assertTrue(TestChecker.test(input, expect, 132))


    def test_33(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    g[a] := True;
    g[a+b+c] := True;
    g[1] := g[a*b*b] := h[2] := False;
    g[1] := g["abc"] := g[2] := True;
end

"""
        expect = r"""Type Mismatch In Expression: ArrayCell(Id(g),StringLiteral(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 133))


    def test_34(self):
        input = r"""
procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    g[a] := True;
    g[a+b+c] := True;
    g[1] := g[a*b*b] := h[2] := False;
    g[1] := g[f1()] := g[2] := True;
    p := q := f2()[4] := k := 5.0;
    p := q := f2()[4] := k := 5 + b * c - a;
    p := q := f2()[4] := k := FALSE;
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var a3: array[-5 .. 10] of real;
begin
    return a3;
end

"""
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(k),BooleanLiteral(False))"""
        self.assertTrue(TestChecker.test(input, expect, 134))


    def test_35(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    g[a] := True;
    g[a+b+c] := True;
    g[1] := g[a*b*b] := h[2] := False;
    g[1] := g[f1()] := g[2] := True;
    p := q := f2()[4] := k := 5.0;
    p := q := f2()[4] := k := 5 + b * c - a;
    p := q := g[1] := f2()[4] := p := 4+2*4-4+6;
end

procedure p1();
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var a3: array[-5 .. 10] of real;
begin
    return a3;
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 135))


    def test_36(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    p1(1,b,"",x);
    p1(a*b+c-4*(4+6+b*2-4*2*2*4*6+c),getInt(),"abc",x);
    p1(getInt(),getFloat(),"abc",x);
    p1(getFloat(),getInt(),"abc",x);
end

procedure p1(a: integer; b:REAL; x,y: string);
begin
    return;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var a3: array[-5 .. 10] of real;
begin
    return a3;
end

"""
        expect = r"""Type Mismatch In Statement: CallStmt(Id(p1),[CallExpr(Id(getFloat),[]),CallExpr(Id(getInt),[]),StringLiteral(abc),Id(x)])"""
        self.assertTrue(TestChecker.test(input, expect, 136))


    def test_37(self):
        input = r"""

procedure main();
var 
    a,b,c: integer;
    x,y,z: string;
    g,h,t: array[1 .. 2] of boolean;
    p,q,k: real;
    r: array [-5 .. 10] of real;
begin
    g[1] := f3(1,b,"",x);
    g[1] := f3(a*b+c-4*(4+6+b*2-4*2*2*4*6+c),getInt(),"abc",x);
    g[1] := f3(getInt(),getFloat(),"abc",x);
    g[1] := f3(getFloat(),getInt(),"abc",x);
end

procedure p1(a: integer; b:REAL; x,y: string);
begin
    return;
end

function f3(a: integer; b:REAL; x,y: string): BOOLEAN;
begin
    return True;
end

function f1(): integer;
begin
    return 0;
end

function f2(): array [-5 .. 10] of real;
var a3: array[-5 .. 10] of real;
begin
    return a3;
end


"""
        expect = r"""Type Mismatch In Expression: CallExpr(Id(f3),[CallExpr(Id(getFloat),[]),CallExpr(Id(getInt),[]),StringLiteral(abc),Id(x)])"""
        self.assertTrue(TestChecker.test(input, expect, 137))


    def test_38(self):
        input = r"""

procedure main();
begin
end

function f1(): integer;
begin
end


"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 138))


    def test_39(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
begin
    a := 10;
    if u then return b;
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 139))


    def test_40(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else if v then return b;
        else if v then return b;
        else if v then return b;
    end
end


"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 140))


    def test_41(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then return b;
                    if a = 10 then return b;
                    if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;
                end
            end
        end
    end
end


"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 141))


    def test_42(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then return b;
                    if a = 10 then return b;
                    if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;

                    if a = 10 then begin
                        for a := 1 to 10 do return a;
                    end else begin
                        b := 1;
                        return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                    end
                end
            end
        end
    end
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 142))


    def test_43(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    break;
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then return b;
                    if a = 10 then return b;
                    if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;

                    if a = 10 then begin
                        for a := 1 to 10 do return a;
                    end else begin
                        b := 1;
                        return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                    end
                end
            end
        end
    end
end

"""
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 143))


    def test_44(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    continue;
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then return b;
                    if a = 10 then return b;
                    if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;

                    if a = 10 then begin
                        for a := 1 to 10 do return a;
                    end else begin
                        b := 1;
                        return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                    end
                end
            end
        end
    end
end

"""
        expect = r"""Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 144))


    def test_45(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then break;
        else return b;
    end
    for a := 1 to 10 do begin
        if v then return b;
        else if v then return b;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then return b;
                    if a = 10 then return b;
                    if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;

                    if a = 10 then begin
                        for a := 1 to 10 do return a;
                    end else begin
                        b := 1;
                        return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                    end
                end
            end
        end
    end
end

"""
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 145))


    def test_46(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    for a := 1 to 10 do begin
        if v then return b;
        else if v then break;
        else begin
            while a < 10 do begin
                for a := 1 to 10 do begin
                    if a = 10 then continue;
                    if a = 10 then break;
                    if a = 10 then return b;
                    else if a = 10 then break;
                    else if a = 10 then return b;
                    else if a = 10 then return b;
                    a := 10;

                    if a = 10 then begin
                        for a := 1 to 10 do continue;
                        return (1*3+1*5+3-1+5*3+1-3+5) * a+b;
                    end else begin
                        b := 1;
                        return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                    end
                end
            end
        end
    end
end


"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 146))


    def test_47(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) * a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin
        break;
    end
end

"""
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 147))


    def test_48(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) * a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            return 5.4;

        end
    end

    return 5;
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(FloatLiteral(5.4)))"""
        self.assertTrue(TestChecker.test(input, expect, 148))


    def test_49(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) / a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
        return 42;
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            return 5;

        end
    end
end


"""
        expect = r"""Type Mismatch In Statement: Return(Some(BinaryOp(+,BinaryOp(/,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLiteral(1),IntLiteral(3)),BinaryOp(*,IntLiteral(1),IntLiteral(5))),IntLiteral(3)),IntLiteral(1)),BinaryOp(*,IntLiteral(5),IntLiteral(3))),IntLiteral(1)),IntLiteral(3)),IntLiteral(5)),Id(a)),Id(b))))"""
        self.assertTrue(TestChecker.test(input, expect, 149))


    def test_50(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            return 5;

            with i: integer; do begin
                for i := 1 to 10 do begin end
            end
        end
    end
end

"""
        expect = r"""Unreachable statement: With([VarDecl(Id(i),IntType)],[For(Id(i)IntLiteral(1),IntLiteral(10),True,[])])"""
        self.assertTrue(TestChecker.test(input, expect, 150))


    def test_51(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            return 5;

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j*k to j/k do begin
                            putLn();
                        end
                    end
            end

        end
    end
end

"""
        expect = r"""Type Mismatch In Statement: For(Id(i)BinaryOp(*,Id(j),Id(k)),BinaryOp(/,Id(j),Id(k)),True,[CallStmt(Id(putLn),[])])"""
        self.assertTrue(TestChecker.test(input, expect, 151))


    def test_52(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            return 5;

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                        end
                    end
            end

        end
    end
end

"""
        expect = r"""Unreachable statement: For(Id(a)IntLiteral(1),IntLiteral(10),True,[With([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(k),IntType),VarDecl(Id(f1),BoolType),VarDecl(Id(f2),BoolType),VarDecl(Id(f3),BoolType)],[For(Id(i)BinaryOp(+,Id(j),Id(k)),BinaryOp(*,Id(j),Id(k)),True,[CallStmt(Id(putLn),[])])])])"""
        self.assertTrue(TestChecker.test(input, expect, 152))


    def test_53(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                            break;
                        end

                        return 5;
                    end
            end

        end
    end
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 153))


    def test_54(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                            break;

                            return 5;
                        end

                        return 5;
                    end
            end

        end
    end
end

"""
        expect = r"""Unreachable statement: Return(Some(IntLiteral(5)))"""
        self.assertTrue(TestChecker.test(input, expect, 154))


    def test_55(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                            if i >= 5 then break;
                            if j <= 10 then continue;
                            if i >= 0 then break;
                            else continue;
                            
                            return 5;
                        end

                        return 10;
                    end
            end

        end
    end
end

"""
        expect = r"""Unreachable statement: Return(Some(IntLiteral(5)))"""
        self.assertTrue(TestChecker.test(input, expect, 155))


    def test_56(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
var a: integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                            if i >= 5 then break;
                            if j <= 10 then continue;
                            if i >= 0 then break;
                            else return 0;

                            a := 10;
                        end
                        return a;
                    end
            end

        end
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(a),IntLiteral(10))"""
        self.assertTrue(TestChecker.test(input, expect, 156))


    def test_57(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            for a := 10 to 10 do begin
                while u do begin
                    x := 1;
                    break;
                end
                x := y := a := b := a+b;
                continue;
                break;
            end
        end
    end
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 157))


    def test_58(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            break;
            continue;
        end
    end
end

"""
        expect = r"""Unreachable statement: Continue"""
        self.assertTrue(TestChecker.test(input, expect, 158))


    def test_59(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 1 do begin
            x := 1;
            break;
        end
        x := 1;
        for b := 2 downto 10 do begin
            x := 1;
            break;
        end
        for b := 3 downto 10 do begin
            x := 1;
            for b := 4 downto 10 do begin
                x := 1;
                for b := 5 downto 10 do begin
                    x := 1;
                    break;
                    for b := 6 downto 10 do begin
                        x := 1;
                        break;
                    end
                end
                break;
            end
            break;
        end
    end
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 159))


    def test_60(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then break; else continue;
        end
        x := 1;
        y := b := a := x := 1;
    end
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 160))


    def test_61(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then break; else return;
            y := 1;
        end
        x := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 161))


    def test_62(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then break;
            else if a = 1 then return;
            else if a = 1 then break;
            else if a = 1 then return;
            else if a = 1 then break;
            else return;
            y := 1;
        end
        x := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 162))


    def test_63(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then begin
                with i: integer; do begin
                    a := 12;
                    for i := 1 to 10 do a := a + 1;
                end
                return;
            end
            else begin
                while a < 10 do begin
                    a := a + 1;
                end
                break;
            end
            y := 1;
        end
        x := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 163))


    def test_64(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then begin
                with i: integer; do begin
                    a := 12;
                    for i := 1 to 10 do a := a + 1;
                end
                return ;
            end
            else begin
                while a < 10 do begin
                    a := a + 1;
                end
                break;
            end
            y := 1;
        end
        x := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 164))


    def test_65(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then begin
                with i: integer; do begin
                    a := 12;
                    for i := 1 to 10 do a := a + 1;
                end
                break ;
            end
            else begin
                while a < 10 do begin
                    a := a + 1;
                end
                break;
            end
            y := 1;
        end
        x := 1;
    end
end
"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 165))


    def test_66(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
var a, b: integer;
begin
    for a := 1 to 10 do begin
        for b := 10 downto 10 do begin
            x := 1;
            if a = 1 then begin
                with i: integer; do begin
                    a := 12;
                    for i := 1 to 10 do a := a + 1;
                end
                return ;
            end
            else begin
                while a < 10 do begin
                    a := a + 1;
                end
                return;
            end
            y := 1;
        end
        x := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 166))


    def test_67(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure p1();
begin
end

"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 167))


    def test_68(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure p1();
begin
end

procedure p2();
begin
end

function f1(): String;
begin
    return "";
end

"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 168))


    def test_69(self):
        input = r"""

var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main(a: integer);
begin
end

"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 169))


    def test_70(self):
        input = r"""

procedure main();
begin
    p1();
    p2();
    p3();
    putStringLn(f1(False));
    putStringLn(f2(False));
    putStringLn(f3(False));
    putStringLn(f4(False));
end

procedure p1(); begin end
procedure p2(); begin end
procedure p3(); begin end
procedure p4(); begin end

function f1(x: boolean): String; begin return ""; end
function f2(x: boolean): String; begin return ""; end
function f3(x: boolean): String; begin return ""; end
function f4(x: boolean): String; begin return ""; end


"""
        expect = r"""Unreachable Procedure: p4"""
        self.assertTrue(TestChecker.test(input, expect, 170))


    def test_71(self):
        input = r"""

procedure main();
begin
    p1();
    putStringLn(f1(False));
end

procedure p1(); begin p2(); p1(); p2(); p1(); end
procedure p2(); begin p1(); p2(); p1(); p3(); main(); p3(); end
procedure p3(); begin p3(); p1(); p2(); main(); main(); end
procedure p4(); 
begin 
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
    putStringLn(f2(False));
    putStringLn(f3(False));
    putStringLn(f4(False));
end

function f1(x: boolean): String; begin putStringLn(f2(False)); return ""; end
function f2(x: boolean): String; begin putStringLn(f3(False)); return ""; end
function f3(x: boolean): String; begin putStringLn(f4(False)); return ""; end
function f4(x: boolean): String; begin return ""; end


"""
        expect = r"""Unreachable Procedure: p4"""
        self.assertTrue(TestChecker.test(input, expect, 171))


    def test_72(self):
        input = r"""

procedure main();
begin
    p1();
    putStringLn(f1(False));
end

procedure p1(); begin p2(); p1(); p2(); p1(); end
procedure p2(); begin p1(); p2(); p1(); p3(); main(); p3(); end
procedure p3(); begin p3(); p1(); p2(); main(); main(); end
procedure p4(); 
begin 
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
    putStringLn(f2(False));
    putStringLn(f3(False));
end

function f1(x: boolean): String; begin putStringLn(f2(False)); return ""; end
function f2(x: boolean): String; begin putStringLn(f3(False)); return ""; end
function f3(x: boolean): String; begin p4(); return ""; end
function f4(x: boolean): String; begin return ""; end


"""
        expect = r"""Unreachable Function: f4"""
        self.assertTrue(TestChecker.test(input, expect, 172))


    def test_73(self):
        input = r"""

procedure main();
begin
    p1();
    putStringLn(f1(False));
end

procedure p1(); begin p2(); p1(); p2(); p1(); end
procedure p2(); begin p1(); p2(); p1(); p3(); main(); p3(); end
procedure p3(); begin p3(); p1(); p2(); main(); main(); end
procedure p4(); 
begin 
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
end

function f1(x: boolean): String; begin putStringLn(f2(False)); return ""; end
function f2(x: boolean): String; begin p2(); p1(); main(); putStringLn(f3(False)); return ""; end
function f3(x: boolean): String; begin p4(); return ""; end
function f4(x: boolean): String; 
begin 
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
    return ""; 
end

"""
        expect = r"""Unreachable Function: f4"""
        self.assertTrue(TestChecker.test(input, expect, 173))


    def test_74(self):
        input = r"""

procedure main();
begin
    p1();
    putStringLn(f1(False));
end

procedure p1(); begin for a:=1 to 10 do begin p2(); p1(); p2(); p1(); end end
procedure p2(); begin for a:=1 to 10 do begin p1(); p2(); p1(); p3(); main(); p3(); end end
procedure p3(); begin for a:=1 to 10 do begin p3(); p1(); p2(); main(); main(); end end
procedure p4(); 
var a: integer;
begin
for a:=1 to 10 do
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
end

function f1(x: boolean): String; begin putStringLn(f2(False)); return ""; end
function f2(x: boolean): String; begin p2(); p1(); main(); putStringLn(f3(False)); return ""; end
function f3(x: boolean): String; begin p4(); return ""; end
function f4(x: boolean): String; 
begin 
    p1(); p2(); p3(); p4(); p4(); main(); 
    putStringLn(f1(False));
    return ""; 
end

var a: integer;

"""
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 174))


    def test_75(self):
        input = r"""

procedure main();
begin
    x := a / b;
    x := y := z := a + b * c/3;
    z := x := a := b := 4;
    a := x / y;
end

var
    a,b,c: integer;
    x,y,z: real;

"""
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,Id(x),Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 175))


    def test_76(self):
        input = r"""


procedure main();
begin
    x := a / b;
    x := y := z := a + b * c/3;
    z := x := a := b := 4;
    x := y := z := a * b + c - 3 * 2 + 1 - 6;
    x := y := z := a * b + c - 3 * 2 + 1 - 6 / 123;
    x := y := z := a := a * b + c - 3 * 2 + 1 - 6 / 123;
end

var
    a,b,c: integer;
    x,y,z: real;


"""
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(*,IntLiteral(3),IntLiteral(2))),IntLiteral(1)),BinaryOp(/,IntLiteral(6),IntLiteral(123))))"""
        self.assertTrue(TestChecker.test(input, expect, 176))


    def test_77(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
begin
    x := a / b;
    x := y := z := a + b * c/3;
    z := x := a := b := 4;
    x := y := z := a * b + c - 3 * 2 + 1 - 6;
    x := y := z := a * b + c - 3 * 2 + 1 - 6 / 123;
end

var
    a,b,c: integer;
    x,y,z: real;

"""
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 177))


    def test_78(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if p then main();
end

var
    i,j,k: string;
    p,q,r: boolean;


"""
        expect = r"""Type Mismatch In Statement: If(Id(p),[CallStmt(Id(main),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 178))


    def test_79(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if p and q then main();
end

var
    i,j,k: string;
    p,q,r: boolean;


"""
        expect = r"""Type Mismatch In Expression: BinaryOp(and,Id(p),Id(q))"""
        self.assertTrue(TestChecker.test(input, expect, 179))


    def test_80(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if (p = i) and q then main();
    if p = i and q then main();
end

var
    i,j,k: string;
    p,q,r: boolean;


"""
        expect = r"""Type Mismatch In Expression: BinaryOp(and,Id(i),Id(q))"""
        self.assertTrue(TestChecker.test(input, expect, 180))


    def test_81(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a then main();
end

var
    i,j,k: string;
    p,q,r: boolean;


"""
        expect = r"""Type Mismatch In Statement: If(Id(a),[CallStmt(Id(main),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 181))


    def test_82(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] then main();
end

var
    i,j,k: string;
    p,q,r: boolean;


"""
        expect = r"""Type Mismatch In Statement: If(ArrayCell(Id(a),IntLiteral(1)),[CallStmt(Id(main),[])],[])"""
        self.assertTrue(TestChecker.test(input, expect, 182))


    def test_83(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if a[3] + a[2] + i * (j - k / (123)) and q or else (r AND i = j) then main();
end

var
    i,j,k: string;
    p,q,r: boolean;

"""
        expect = r"""Type Mismatch In Expression: BinaryOp(/,Id(k),IntLiteral(123))"""
        self.assertTrue(TestChecker.test(input, expect, 183))


    def test_84(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if a[3] + a[2] + i * (j - p / (123)) and q or else (r AND i = j) then main();
end

var
    i,j,k: string;
    p,q,r: boolean;

"""
        expect = r"""Type Mismatch In Expression: BinaryOp(and,BinaryOp(*,Id(i),BinaryOp(-,Id(j),BinaryOp(/,Id(p),IntLiteral(123)))),Id(q))"""
        self.assertTrue(TestChecker.test(input, expect, 184))


    def test_85(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if (a[3] + a[2] + i * (j - p / (123))) > (a[3] + a[2] + i * (j - p / 1.0 * 1.0 / p)) 
        then main();
    // and q or else (r AND (i = j)) then main();

    main(1);
end

var
    i,j,k: string;
    p,q,r: boolean;

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 185))


    def test_86(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if
    (a[3] + a[2] + i * (j - p / (123))) > (a[3] + a[2] + i * (j - p / 1.0 * 1.0 / p))
    and q // or else (r AND (i = j)) then main();
        then main();
end

var
    i,j,k: string;
    p,q,r: boolean;

"""
        expect = r"""Type Mismatch In Expression: BinaryOp(and,BinaryOp(+,BinaryOp(+,ArrayCell(Id(a),IntLiteral(3)),ArrayCell(Id(a),IntLiteral(2))),BinaryOp(*,Id(i),BinaryOp(-,Id(j),BinaryOp(/,BinaryOp(*,BinaryOp(/,Id(p),FloatLiteral(1.0)),FloatLiteral(1.0)),Id(p))))),Id(q))"""
        self.assertTrue(TestChecker.test(input, expect, 186))


    def test_87(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if
    ((a[3] + a[2] + i * (j - p / (123))) > (a[3] + a[2] + i * (j - p / 1.0 * 1.0 / p)))
    and q // or else (r AND (i = j)) then main();
        then main();
    main(1);
end

var
    i,j,k: string;
    p,q,r: boolean;

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 187))


    def test_88(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    if a[1] >= i then main();
    if a[2] <= x then main();
    if
    ((a[3] + a[2] + i * (j - p / (123))) > (a[3] + a[2] + i * (j - p / 1.0 * 1.0 / p)))
    and q or else (r AND (i = j)) 
        then main();
    foo();
end

var
    i,j,k: string;
    p,q,r: boolean;

function foo(): array [-10000 .. 100000] of integer;
var main: array [-10000 .. 100000] of integer;
begin
    return main;
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 188))


    def test_89(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin 
    return nt;
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Type Mismatch In Statement: Return(Some(Id(nt)))"""
        self.assertTrue(TestChecker.test(input, expect, 189))


    def test_90(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;
"""
        expect = r"""Unreachable Function: f1"""
        self.assertTrue(TestChecker.test(input, expect, 190))


    def test_91(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1();
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;


"""
        expect = r"""Type Mismatch In Statement: AssignStmt(ArrayCell(CallExpr(Id(f1),[]),IntLiteral(2)),CallExpr(Id(f1),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 191))


    def test_92(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[a[1]];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Type Mismatch In Expression: ArrayCell(CallExpr(Id(f1),[]),ArrayCell(Id(a),IntLiteral(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 192))


    def test_93(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
    main();
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Unreachable statement: CallStmt(Id(main),[])"""
        self.assertTrue(TestChecker.test(input, expect, 193))


    def test_94(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if ij = 1 then return;
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Undeclared Identifier: ij"""
        self.assertTrue(TestChecker.test(input, expect, 194))


    def test_95(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if i = 1 then return;
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;


"""
        expect = r"""Type Mismatch In Expression: BinaryOp(=,Id(i),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 195))


    def test_96(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then return;
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Type Mismatch In Statement: Return(None)"""
        self.assertTrue(TestChecker.test(input, expect, 196))


    def test_97(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 197))


    def test_98(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then break;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 198))


    def test_99(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return f2();
    end else begin
        if r then begin
            r := false;
            return nt;
        end else return f2();
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(Id(nt)))"""
        self.assertTrue(TestChecker.test(input, expect, 199))


    def test_100(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then begin
            r := false;
            return f2();
        end
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 200))


    def test_101(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then begin
            r := false;
            return f2();
        end else begin
            while r do begin
                if R then break;
            end
        end
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 201))


    def test_102(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then begin
            r := false;
            return f2();
        end else begin
            while r do begin
                if R then break; else return f2();
            end
        end
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Function f1Not Return """
        self.assertTrue(TestChecker.test(input, expect, 202))


    def test_103(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then begin
            r := false;
            return f2();
        end else begin
            while r do begin
                if R then break; else return f2();
                return f2();
            end
        end
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Unreachable statement: Return(Some(CallExpr(Id(f2),[])))"""
        self.assertTrue(TestChecker.test(input, expect, 203))


    def test_104(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    a[1] := f1()[2];
    a[2] := f1()[1] := f1()[2];
    f1()[2] := a[1];
    f1()[1] := a[1] := a[2] := f1()[2];
    f1()[2] := f1()[i+j+i+j+i+j*2*4*6*6*4*2];
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    if r then
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end else begin
        if r then begin
            r := false;
            return f2();
        end else begin
            while r do begin
                if R then break; else return f3();
            end
            return f4();
        end
        return f1();
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

function f2(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

function f3(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

function f4(): array [ 1 .. 3 ] of real;
begin
    return nt;
end

"""
        expect = r"""Unreachable statement: Return(Some(CallExpr(Id(f1),[])))"""
        self.assertTrue(TestChecker.test(input, expect, 204))


    def test_105(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
end

var A: Real;

"""
        expect = r"""Redeclared Variable: A"""
        self.assertTrue(TestChecker.test(input, expect, 205))


    def test_106(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    I := 1;
end

procedure GETINT();
begin
end
"""
        expect = r"""Redeclared Procedure: GETINT"""
        self.assertTrue(TestChecker.test(input, expect, 206))


    def test_107(self):
        input = r"""


var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    I := 1;
end

procedure p1();
begin
end

procedure P1();
begin
end

"""
        expect = r"""Redeclared Procedure: P1"""
        self.assertTrue(TestChecker.test(input, expect, 207))


    def test_108(self):
        input = r"""

procedure main();
begin
end

var a,b,c,d,main: integer;

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 208))


    def test_109(self):
        input = r"""

var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;

procedure main();
begin
    I := 1;
end

procedure p1();
begin
end

procedure MAIN();
begin
end

"""
        expect = r"""Redeclared Procedure: MAIN"""
        self.assertTrue(TestChecker.test(input, expect, 209))


    def test_110(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure p1();
begin
end

procedure MAIN();
begin
end

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    I := 1;
end

"""
        expect = r"""Redeclared Procedure: main"""
        self.assertTrue(TestChecker.test(input, expect, 210))


    def test_111(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure p1();
begin
end

function MAIN(): String;
begin
    return "";
end

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    I := 1;
end

"""
        expect = r"""Redeclared Procedure: main"""
        self.assertTrue(TestChecker.test(input, expect, 211))


    def test_112(self):
        input = r"""

procedure main();
begin
    foo();
end

var a: integer;

procedure foo();
begin
    a := a+5*f - not ( -True OR (a <> b*"String"+"False"*False) or else fgh mOD TYR ------ 666666 *
    ("abc" <= "xyz") ) DIV FalSE MOD QUE + ---- False * "{{}}1e5" + 2e5 {  ....  };
end

"""
        expect = r"""Undeclared Identifier: f"""
        self.assertTrue(TestChecker.test(input, expect, 212))


    def test_113(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
var 
    a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;

begin
    with
        a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
    do begin
        with
            a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
        do begin
            with
                a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
            do begin
                with
                    a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
                do begin
                    return;
                end
            end
        end
    end
end

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 213))


    def test_114(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
var a: real;
begin
    a := 000000000000000000000000001.00000000001e-10000000000;
    a := 000000000000000000000000002.00000000001e-1000000000;
    a := 000000000000000000000000003.00000000001e-100000000;
    a := 000000000000000000000000004.00000000001e-10000000;
    a := 000000000000000000000000005.00000000001e-1000000;
    a := 000000000000000000000000006.00000000001e-100000;
    a := 000000000000000000000000007.00000000001e-10000;
    a := 000000000000000000000000008.00000000001e-1000;
    a := 000000000000000000000000009.00000000001e-100;
end

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 214))


    def test_115(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
var a: real;
begin
    a := 000000000000000000000000001.00000000001e-10000000000;
    a := 000000000000000000000000002.00000000001e-1000000000;
    a := 000000000000000000000000003.00000000001e-100000000;
    a := 000000000000000000000000004.00000000001e-10000000;
    a := 000000000000000000000000005.00000000001e-1000000;
    a := 000000000000000000000000006.00000000001e-100000;
    a := 000000000000000000000000007.00000000001e-10000;
    a := 000000000000000000000000008.00000000001e-1000;
    a := 000000000000000000000000009.00000000001e-100;

    a := 10000000000e-10000000000;
    a := 20000000000e-1000000000;
    a := 30000000000e-100000000;
    a := 40000000000e-10000000;
    a := 50000000000e-1000000;
    a := 60000000000e-100000;
    a := 70000000000e-10000;
    a := 80000000000e-1000;
    a := 90000000000e-100;

    a := 1.000000000000001;
    a := 2.00000000000001;
    a := 3.0000000000001;
    a := 4.000000000001;
    a := 5.00000000001;
    a := 6.0000000001;
    a := 7.000000001;
    a := 8.00000001;

    a := 10000000000e-10000000000;
    a := 20000000000e-1000000000;
    a := 30000000000e-100000000;
    a := 40000000000e-10000000;
    a := 50000000000e-1000000;
    a := 60000000000e-100000;
    a := 70000000000e-10000;
    a := 80000000000e-1000;
    a := 90000000000e-100;

    a := 2e-10000000;
    a := 3e-1000000;
    a := 4e-100000;
    a := 5e-10000;
    a := 6e-1000;
    a := 7e-100;
    a := 8e-10;

    a := 2e10;
    a := 3e100;
    a := 4e1000;
    a := 5e10000;
    a := 6e100000;

    a := 00000012345;
    a := 123456789123456789;
    a := 123456789123456789123456789;
    a := 123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789123456789;

    a := 123456789123456789123456789 + 123456789123456789123456789123456789123456789 + 123456789123456789123456789123456789123456789123456789 * 123456789123456789123456789123456789123456789123456789 - 123456789123456789123456789123456789123456789123456789 / (123456789123456789123456789123456789123456789123456789 and 1);
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 215))


    def test_116(self):
        input = r"""

procedure main();
begin
    foo(True, 2, 1, 2, 3);
end

procedure foo(a: Boolean; b: Boolean; x,y: Integer; z: Real);
begin

end

"""
        expect = r"""Type Mismatch In Statement: CallStmt(Id(foo),[BooleanLiteral(True),IntLiteral(2),IntLiteral(1),IntLiteral(2),IntLiteral(3)])"""
        self.assertTrue(TestChecker.test(input, expect, 216))


    def test_117(self):
        input = r"""


procedure main();
begin
    foo(True, False, 1, 2, 3);
end

procedure foo(a: Boolean; b: Boolean; x,y: Integer; z: Real);
begin
    main();
    main();
end

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 217))


    def test_118(self):
        input = r"""

procedure main();
begin
    foo(True, False, 1, 2, 3);
end

procedure foo(a: Boolean; b: Boolean; x,y: Integer; z: Real);
var
    a: array [1 .. 100] of String;
begin

end

"""
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 218))


    def test_119(self):
        input = r"""

procedure main();
begin
    foo(True, False, 1, 2, 3);
end

procedure foo(a: Boolean; b: Boolean; x,y: Integer; z: Real);
var
    arr: array [1 .. 100] of String;
begin

end

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 219))


    def test_120(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
end

"""
        expect = r"""Function fooNot Return """
        self.assertTrue(TestChecker.test(input, expect, 220))


    def test_121(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
    return "";
    a := True;
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(a),BooleanLiteral(True))"""
        self.assertTrue(TestChecker.test(input, expect, 221))


    def test_122(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
    if a then return 5; else return "";
end

"""
        expect = r"""Type Mismatch In Statement: Return(Some(IntLiteral(5)))"""
        self.assertTrue(TestChecker.test(input, expect, 222))


    def test_123(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
    if a then return "123"; else return "456";
end

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 223))


    def test_124(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
    if a then return "1";
    else if a then return "2";
    else if a then return "3";
    else if a then return "4";
    else if a then return "5";

    a := True;
end

"""
        expect = r"""Function fooNot Return """
        self.assertTrue(TestChecker.test(input, expect, 224))


    def test_125(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
begin
    if a then return "1";
    else if a then return "2";
    else if a then return "3";
    else if a then return "4";
    else if a then return "5";
    else return "!";

    a := True;
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(a),BooleanLiteral(True))"""
        self.assertTrue(TestChecker.test(input, expect, 225))



    def test_126(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then break; else break;

        a := b := True or False;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(b),BinaryOp(or,BooleanLiteral(True),BooleanLiteral(False)))"""
        self.assertTrue(TestChecker.test(input, expect, 226))


    def test_127(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then break; else continue;

        i := 1;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input, expect, 227))


    def test_128(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else continue;

        j := 6;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(j),IntLiteral(6))"""
        self.assertTrue(TestChecker.test(input, expect, 228))


    def test_129(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else break;

        j := 10000;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(j),IntLiteral(10000))"""
        self.assertTrue(TestChecker.test(input, expect, 229))


    def test_130(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else break;
        end

        i := 123;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(123))"""
        self.assertTrue(TestChecker.test(input, expect, 230))


    def test_131(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; do begin
                    if a then return "3";
                    else return "5";
                end
            end
        end

        i := 123;
    end
end

"""
        expect = r"""Type Mismatch In Statement: If(Id(a),[Return(Some(StringLiteral(3)))],[Return(Some(StringLiteral(5)))])"""
        self.assertTrue(TestChecker.test(input, expect, 231))


    def test_132(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else return "5";
                end
            end
        end

        i := 1000;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(1000))"""
        self.assertTrue(TestChecker.test(input, expect, 232))


    def test_133(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else break;
                end
            end
        end

        i := 1000;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(1000))"""
        self.assertTrue(TestChecker.test(input, expect, 233))


    def test_134(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else return main();
                end
            end
        end
        i := 1000;
    end
end

"""
        expect = r"""Undeclared Function: main"""
        self.assertTrue(TestChecker.test(input, expect, 234))


    def test_135(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else return foo(g, b, i,j,i*j+4-2*6);
                end
            end
        end
        i := 1000;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(1000))"""
        self.assertTrue(TestChecker.test(input, expect, 235))


    def test_136(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    for i := 1 to 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
    end
end

"""
        expect = r"""Function fooNot Return """
        self.assertTrue(TestChecker.test(input, expect, 236))


    def test_137(self):
        input = r"""

procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
    end
end

"""
        expect = r"""Function fooNot Return """
        self.assertTrue(TestChecker.test(input, expect, 237))


    def test_138(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else return foo(b,g,i,i,i);
                end
            end
        end
        i := 1000;
    end
end

"""
        expect = r"""Unreachable statement: AssignStmt(Id(i),IntLiteral(1000))"""
        self.assertTrue(TestChecker.test(input, expect, 238))


    def test_139(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
        while i < 100 do main();
        while i < 100 do main();
        with i: string; do begin
            while b do begin
                break;
            end
            putString(i);
            return foo(True, True, j,x,i);
        end
    end
end

"""
        expect = r"""Type Mismatch In Expression: CallExpr(Id(foo),[BooleanLiteral(True),BooleanLiteral(True),Id(j),Id(x),Id(i)])"""
        self.assertTrue(TestChecker.test(input, expect, 239))


    def test_140(self):
        input = r"""


procedure main();
begin
    PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
        while i < 100 do main();
        while i < 100 do main();
        with i: string; do begin
            while b do begin
                break;
            end
            putString(i);
            return foo(True, True, j,x,y);
        end
    end
end

"""
        expect = r"""Function fooNot Return """
        self.assertTrue(TestChecker.test(input, expect, 240))


    def test_141(self):
        input = r"""

procedure main();
begin
    // PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
        while i < 100 do main();
        while i < 100 do main();
        with i: string; do begin
            while b do begin
                break;
            end
            putString(i);
            return foo(True, True, j,x,y);
        end
    end
    while i < 100 do main();
    while i < 100 do main();
    with i: string; do begin
        while b do begin
            break;
        end
        putString(i);
        return foo(True, True, j,x,y);
    end
end

"""
        expect = r"""Unreachable Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 241))


    def test_142(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
begin
    for a := 1 to 10 do foo();
end

var a: integer;

"""
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 242))


    def test_143(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
begin
    for a := 1 to 10 do foo();
end

var a: real;

"""
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 243))


    def test_144(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
var a: real;
begin
    for a := 1 to 10 do foo();
end

var a: real;

"""
        expect = r"""Type Mismatch In Statement: For(Id(a)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(foo),[])])"""
        self.assertTrue(TestChecker.test(input, expect, 244))


    def test_145(self):
        input = r"""

procedure main();
begin
    foo();
end

procedure foo();
var a: integer;
begin
    for a := 1 to 10 do foo();
end

var a: real;

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 245))


    def test_146(self):
        input = r"""

procedure main();
begin
    foo(5);
end

procedure foo(a: integer);
begin
    for a := 1 to 10 do foo(a);
end

var a: real;

procedure nty(); begin end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 246))


    def test_147(self):
        input = r"""

procedure main();
var s: string;
begin
    putStringLn(s);
    s := "123";
end

"""
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(s),StringLiteral(123))"""
        self.assertTrue(TestChecker.test(input, expect, 247))


    def test_148(self):
        input = r"""

procedure main();
begin

end

var a, b, c: Integer; X,Y,Z: String;
    MaIN: boolean;

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 248))


    def test_149(self):
        input = r"""

procedure main();
var main: integer;
begin
    with main: string; do begin
        putStringLn(main);
        for main := getInt() to 10000 do begin 
            putStringLn(main);
        end
    end
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 249))


    def test_150(self):
        input = r"""

procedure main();
var i,j,k: integer;
    main: string;
    a: array[1 .. 10] of real;
    p,q: boolean;
begin
    for i := 1 to 10 do begin
        a[i+j*k] := a[j+i*k] := a[1] := a[0];
        putStringLn(main);
        for j := i+j*k to i-j*k do begin
            while p do begin
                main();
            end
        end
    end
end

"""
        expect = r"""[]"""
        self.assertTrue(TestChecker.test(input, expect, 250))


    def test_151(self):
        input = r"""

procedure main();
var i,j,k: integer;
    main: string;
    a: array[1 .. 10] of real;
    p,q: boolean;
begin
    for i := 1 to 10 do begin
        a[i+j*k] := a[j+i*k] := a[1] := a[0];
        putStringLn(main);
        for j := i+j*k to i-j*k do begin
            while p do begin
                with main: integer; p: string; do begin
                    if main > p then break;
                end
            end
        end
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 251))


    def test_152(self):
        input = r"""

procedure main();
var i,j,k: integer;
    main: string;
    a: array[1 .. 10] of real;
    p,q: boolean;
begin
    for i := 1 to 10 do begin
        a[i+j*k] := a[j+i*k] := a[1] := a[0];
        putStringLn(main);
        for j := i+j*k to i-j*k do begin
            while p do begin
                with main: integer; p: string; do begin
                    if main > j then break;
                    putStringLn(p);
                    if getInt() < main then continue;
                    main := getInt();
                    putInt(getInt());
                    putIntLn(main);
                    with p: boolean; do begin
                        if i < j and then p then putString(main);
                    end
                end
                p := false;
            end
        end
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 252))


    def test_153(self):
        input = r"""

procedure main();
var i,j,k: integer;
    main: string;
    a: array[1 .. 10] of real;
    p,q: boolean;
begin
    for i := 1 to 10 do begin
        a[i+j*k] := a[j+i*k] := a[1] := a[0];
        putStringLn(main);
        for j := i+j*k to i-j*k do begin
            while p do begin
                with main: integer; p: string; do begin
                    if main > j then break;
                    putStringLn(p);
                    if getInt() < main then continue;
                    main := getInt();
                    putInt(getInt());
                    putIntLn(main);
                    with p: boolean; do begin
                        if i < j and then p then main := k;
                        else break;
                    end
                end
                p := false;
                break;
            end
            a[1] := getFloat();
            putFloatLn(a[1]);
            PutFloat(GetFloat());
            main();
        end
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 253))


    def test_154(self):
        input = r"""

procedure main();
var main: string;
begin
    putStringLn(main);
    with main: integer; do begin
        putIntLn(main);
        with main: boolean; do begin
            if main then begin
                with main: array[1 .. 10] of real; do begin
                    main[1] := getFloat();
                    putFloatLn(main[2]);
                end
            end else begin
                main := False;
                with main: real; do begin
                    putFloat(main);
                    with main: string; do begin
                        putString(main);
                    end
                end
            end
            main := FALSE;
            for main := 1 to 1000 do begin
                putString(main);
            end
        end
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 254))


    def test_155(self):
        input = r"""

procedure main();
begin
    p1();
    p2();
    p3();
    with p1: integer; do begin
        p2();
        p3();
        with p2: string; do begin
            p3();
            with p1, p2: boolean; p3: string; do begin
                if p1 then begin 
                    if p2 then putStringLn(p3);
                end
                p3();
            end
        end
    end
end

procedure p1(); begin end
procedure p2(); begin end
procedure p3(); begin end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 255))


    def test_156(self):
        input = r"""

procedure main();
begin
    putIntLn(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(1)))))))))))))))))));
    putFloatLn(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(1)))))))))))))))))));
    putInt(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(fi(fr(1))))))))))))))))))));
end

function fi(r: real): integer; begin return 1; end
function fr(i: integer): real; begin return 1; end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 256))


    def test_157(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 257))


    def test_158(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure y7(); begin y7(); y7(); y7(); main(); p1(); end
procedure y6(); begin y6(); y6(); y6(); main(); end
procedure y5(); begin y5(); y5(); y5(); main(); end
procedure y4(); begin y4(); y4(); y4(); main(); end
procedure y3(); begin y3(); y3(); y3(); main(); y6(); y7(); end
procedure y2(); begin y2(); y2(); y2(); main(); y4(); y5(); end
procedure y1(); begin y1(); y1(); y1(); main(); y2(); y3(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 258))


    def test_159(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); y1(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure y7(); begin y7(); y7(); y7(); main(); end
procedure y6(); begin y6(); y6(); y6(); main(); end
procedure y5(); begin y5(); y5(); y5(); main(); end
procedure y4(); begin y4(); y4(); y4(); main(); end
procedure y3(); begin y3(); y3(); y3(); main(); y6(); y7(); end
procedure y2(); begin y2(); y2(); y2(); main(); y4(); y5(); end
procedure y1(); begin y1(); y1(); y1(); main(); y2(); y3(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 259))


    def test_160(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure y7(); begin y7(); y7(); y7(); main(); p1(); end
procedure y6(); begin y6(); y6(); y6(); main(); end
procedure y5(); begin y5(); y5(); y5(); main(); end
procedure y4(); begin y4(); y4(); y4(); main(); end
procedure y3(); begin y3(); y3(); y3(); main(); y6(); y7(); end
procedure y2(); begin y2(); y2(); y2(); main(); y4(); y5(); end
procedure y1(); begin y1(); y1(); y1(); main(); y2(); y3(); end

procedure x7(); begin x7(); x7(); x7(); main(); end
procedure x6(); begin x6(); x6(); x6(); main(); end
procedure x5(); begin x5(); x5(); x5(); main(); end
procedure x4(); begin x4(); x4(); x4(); main(); end
procedure x3(); begin x3(); x3(); x3(); main(); x6(); x7(); end
procedure x2(); begin x2(); x2(); x2(); main(); x4(); x5(); end
procedure x1(); begin x1(); x1(); x1(); main(); x2(); x3(); end

procedure main();
begin
    y1();
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 260))


    def test_161(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); x1(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure y7(); begin y7(); y7(); y7(); main(); y1(); end
procedure y6(); begin y6(); y6(); y6(); main(); end
procedure y5(); begin y5(); y5(); y5(); main(); end
procedure y4(); begin y4(); y4(); y4(); main(); end
procedure y3(); begin y3(); y3(); y3(); main(); y6(); y7(); end
procedure y2(); begin y2(); y2(); y2(); main(); y4(); y5(); end
procedure y1(); begin y1(); y1(); y1(); main(); y2(); y3(); end

procedure x7(); begin x7(); x7(); x7(); main(); x1(); end
procedure x6(); begin x6(); x6(); x6(); main(); end
procedure x5(); begin x5(); x5(); x5(); main(); end
procedure x4(); begin x4(); x4(); x4(); main(); end
procedure x3(); begin x3(); x3(); x3(); main(); x6(); x7(); end
procedure x2(); begin x2(); x2(); x2(); main(); x4(); x5(); end
procedure x1(); begin x1(); x1(); x1(); main(); x2(); x3(); end

procedure main();
begin
    y1();
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 261))


    def test_162(self):
        input = r"""

procedure p7(); begin p7(); p7(); p7(); main(); p1(); end
procedure p6(); begin p6(); p6(); p6(); main(); end
procedure p5(); begin p5(); p5(); p5(); main(); end
procedure p4(); begin p4(); p4(); p4(); main(); end
procedure p3(); begin p3(); p3(); p3(); main(); p6(); p7(); end
procedure p2(); begin p2(); p2(); p2(); main(); p4(); p5(); end
procedure p1(); begin p1(); p1(); p1(); main(); p2(); p3(); end

procedure y7(); begin y7(); y7(); y7(); main(); y1(); end
procedure y6(); begin y6(); y6(); y6(); main(); end
procedure y5(); begin y5(); y5(); y5(); main(); end
procedure y4(); begin y4(); y4(); y4(); main(); end
procedure y3(); begin y3(); y3(); y3(); main(); y6(); y7(); end
procedure y2(); begin y2(); y2(); y2(); main(); y4(); y5(); end
procedure y1(); begin y1(); y1(); y1(); main(); y2(); y3(); end

procedure x7(); begin x7(); x7(); x7(); main(); x1(); end
procedure x6(); begin x6(); x6(); x6(); main(); end
procedure x5(); begin x5(); x5(); x5(); main(); end
procedure x4(); begin x4(); x4(); x4(); main(); end
procedure x3(); begin x3(); x3(); x3(); main(); x6(); x7(); end
procedure x2(); begin x2(); x2(); x2(); main(); x4(); x5(); end
procedure x1(); begin x1(); x1(); x1(); main(); x2(); x3(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 262))


    def test_163(self):
        input = r"""

procedure p2(); begin p2(); p1(); main(); end
procedure p1(); begin p2(); p1(); main(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 263))


    def test_164(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 264))


    def test_165(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 265))


    def test_166(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 266))


    def test_167(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 267))


    def test_168(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 268))


    def test_169(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 269))


    def test_170(self):
        input = r"""

procedure main();
begin

end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 270))

