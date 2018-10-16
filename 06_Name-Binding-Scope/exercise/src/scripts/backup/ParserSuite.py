import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    def test_1(self):
        """ Test Var Declare 1 line 1 var """
        input = """
var a: integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        

    def test_2(self):
        """ Test Var Declare 1 line n var """
        input = """
var a, b, c: integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        

    def test_3(self):
        """ Test Var Declare n line """
        input = """
var a, b, c: integer;
var x, y: real;
var z: string;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        

    def test_4(self):
        """ Test Var Declare array """
        input = """
var a: array[1 .. 3] of integer;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        

    def test_5(self):
        """ Test Var Declare """
        input = """
Var a, B, c: array [5 .. 1000] of Boolean ;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        

    def test_6(self):
        """ Test Var Declare """
        input = """
Var a, B, c: InTeGer;
    x, Y, Z: Boolean ;
    g: Array [4 .. 6] of REAL;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        

    def test_7(self):
        """ Test Procedure Function Declare """
        input = """
procedure foo();
var a: real;
begin

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        

    def test_8(self):
        """ Test Procedure Function Declare """
        input = """
procedure foo(x: integer);
var a, b, c: real;
begin

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        

    def test_9(self):
        """ Test Procedure Function Declare """
        input = """
procedure foo(x: integer; y, z: real; g, h: string);
var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;

begin


end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        

    def test_10(self):
        """ Test Procedure Function Declare """
        input = """
procedure foo(
    x: integer;
    y, z: real;
    g, h: string;
    arr_nodes: Array[0 .. 1000] of real
);

var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;
    dd: array[0 .. 1000005] of boolean;

begin


end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
        

    def test_11(self):
        """ Test Assign Statment """
        input = """
procedure foo();

var 
    a: real;

begin
    a := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        

    def test_12(self):
        """ Test Assign Statment """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b := c := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        

    def test_13(self):
        """ Test Assign Statment """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b [10] := foo() [3 ] := x := 1 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        

    def test_14(self):
        """ Test Assign Statment """
        input = """
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]]] + 3;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        

    def test_15(self):
        """ Test Assign Statment """
        input = """
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        

    def test_16(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n + 5 - g - 9;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        

    def test_17(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n or 4 + 5 - g or 2 - 9;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        

    def test_18(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b / 2 * n / 4 div 5 mod g and 2 * 9 / 4 mod 2;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        

    def test_19(self):
        """ Test Precedence """
        input = """
procedure foo();

var 
    a: real;

begin
    a := -5 - 6 + not 5 - 9 - not -(3 + not -5);
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        

    def test_20(self):
        """ Test Precedence """
        input = """
procedure foo();

var 
    a: real;

begin
    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        

    def test_21(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := b = c ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        

    def test_22(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        

    def test_23(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := TRUE and then 2 ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        

    def test_24(self):
        """ Test Associative """
        input = """
procedure foo();

var 
    a: real;

begin
    a := TRUE and then FALSE or     else True or      else (1 and       then 2) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        

    def test_25(self):
        """ Test True False Keywords """
        input = """
procedure foo();

var 
    a: real;

begin
    a := True ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        

    def test_26(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        

    def test_27(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 or b = 2 and c = 3 then 
        ok();
end
"""
        expect = "Error on line 5 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 227))
        

    def test_28(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then
        a := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        

    def test_29(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then begin
        a := 5;
        b := c := e * 2;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        

    def test_30(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then ok(); else no();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        

    def test_31(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then
        if b > 3 then
            c := 5;
        else 
            d := 1;
    else
        e := 0;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        

    def test_32(self):
        """ Test If Statement """
        input = """
procedure foo();
var a: real;
begin
    if a = 1 then begin
        if b > 3 then c := 5;
        else d := 1;

        if e < 4 then ok();
    end else begin
        if h > 5 then nty(); else lyo();
        g := 5;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
        

    def test_33(self):
        """ Test While Statment """
        input = """
procedure foo();
var a: real;
begin
    While (i < 1) do i := i+1;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        

    def test_34(self):
        """ Test While Statement """
        input = """
procedure foo();
var a: real;
begin
    While i < 1 do begin
        i := i+1;
        if i = 1 then i := i - 1;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        

    def test_35(self):
        """ Test For Statment """
        input = """
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        

    def test_36(self):
        """ Test With Statment """
        input = """
procedure foo();
var a: real;
begin
    with a: integer; do a := a + 1;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        

    def test_37(self):
        """ Test With Statment """
        input = """
procedure foo();
var a: real;
begin
    with 
        a: integer;
        b, c: array [0 .. 15] of Boolean;
        x, y, z: real;
    do begin
        a := x := y := 3;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        

    def test_38(self):
        """ Test Call Statment """
        input = """
procedure foo();
var a: real;
begin
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        

    def test_39(self):
        """ Test Complex Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        

    def test_40(self):
        """ Test Success Code Statment """
        input = """
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        

    def test_41(self):
        """ Test Missing ; """
        input = """
var a: integer
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 241))
        

    def test_42(self):
        """ Test Missing ; """
        input = """
var a: integer"""
        expect = "Error on line 2 col 14: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))
        

    def test_43(self):
        """ Test Error : """
        input = """
var a:: integer;
"""
        expect = "Error on line 2 col 6: :"
        self.assertTrue(TestParser.test(input, expect, 243))
        

    def test_44(self):
        """ Test Error Type """
        input = """
var a: int
"""
        expect = "Error on line 2 col 7: int"
        self.assertTrue(TestParser.test(input, expect, 244))
        

    def test_45(self):
        """ Test Missing type """
        input = """
var a:
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 245))
        

    def test_46(self):
        """ Test Missing type """
        input = """
var a
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 246))
        

    def test_47(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var a: boolean integer
"""
        expect = "Error on line 2 col 15: integer"
        self.assertTrue(TestParser.test(input, expect, 247))
        

    def test_48(self):
        """ Test Wrong Syntax Var Declare """
        input = """
a : integer
"""
        expect = "Error on line 2 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 248))
        

    def test_49(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var real: integer;
"""
        expect = "Error on line 2 col 4: real"
        self.assertTrue(TestParser.test(input, expect, 249))
        

    def test_50(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var a integer;
"""
        expect = "Error on line 2 col 6: integer"
        self.assertTrue(TestParser.test(input, expect, 250))
        

    def test_51(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var a, b, : boolean ;
"""
        expect = "Error on line 2 col 10: :"
        self.assertTrue(TestParser.test(input, expect, 251))
        

    def test_52(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var a, b, c: boolean;
x: real
"""
        expect = "Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 252))
        

    def test_53(self):
        """ Test Wrong Syntax Var Declare """
        input = """
var a, b, c: boolean;
x, y, z: real
"""
        expect = "Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test_54(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of bool;
"""
        expect = "Error on line 4 col 26: bool"
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test_55(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of boolean
"""
        expect = "Error on line 5 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test_56(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean;
"""
        expect = "Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test_57(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of ;
"""
        expect = "Error on line 4 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test_58(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5 of boolean ;
"""
        expect = "Error on line 4 col 22: of"
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test_59(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ..] of boolean ;
"""
        expect = "Error on line 4 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test_60(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0] of boolean ;
"""
        expect = "Error on line 4 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test_61(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0  5] of boolean ;
"""
        expect = "Error on line 4 col 18: 5"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test_62(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ... 5] of boolean ;
"""
        expect = "Error on line 4 col 19: ."
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test_63(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[.. 5] of boolean ;
"""
        expect = "Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test_64(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[] of boolean ;
"""
        expect = "Error on line 4 col 15: ]"
        self.assertTrue(TestParser.test(input, expect, 264))
        

    def test_65(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array of boolean
"""
        expect = "Error on line 4 col 15: of"
        self.assertTrue(TestParser.test(input, expect, 265))
        

    def test_66(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array ;
"""
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 266))
        

    def test_67(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean ;
"""
        expect = "Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 267))
        

    def test_68(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] ;
"""
        expect = "Error on line 4 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test_69(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] with boolean ;
"""
        expect = "Error on line 4 col 23: with"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test_70(self):
        """ Test Array Declare Error """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] in boolean;
"""
        expect = "Error on line 4 col 23: in"
        self.assertTrue(TestParser.test(input, expect, 270))
        

    def test_71(self):
        """ Test Array Declare Error  """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array(0 .. 5) of boolean ;
"""
        expect = "Error on line 4 col 14: ("
        self.assertTrue(TestParser.test(input, expect, 271))
        

    def test_72(self):
        """ Test Array Declare Error  """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: arr[0 .. 5] of boolean ;
"""
        expect = "Error on line 4 col 9: arr"
        self.assertTrue(TestParser.test(input, expect, 272))
        

    def test_73(self):
        """ Test Array Declare Error  """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 .. 5] of true ;
"""
        expect = "Error on line 4 col 27: true"
        self.assertTrue(TestParser.test(input, expect, 273))
        

    def test_74(self):
        """ Test Array Declare without space dotdot """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 ..5] of boolean ;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        

    def test_75(self):
        """ Test Array Declare without space dotdot """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0.. 5] of boolean ;
"""
        expect = "Error on line 4 col 15: 0."
        self.assertTrue(TestParser.test(input, expect, 275))
        

    def test_76(self):
        """ Test Array Declare without space dotdot """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0..5] of boolean;
"""
        expect = "Error on line 4 col 15: 0."
        self.assertTrue(TestParser.test(input, expect, 276))
        

    def test_77(self):
        """ Test Negative index Array Declare """
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[-5 .. 5] of boolean;
"""
        expect = "Error on line 4 col 15: -"
        self.assertTrue(TestParser.test(input, expect, 277))
        

    def test_78(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo()
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 278))
        

    def test_79(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo ;
"""
        expect = "Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 279))
        

    def test_80(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo( ;
"""
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 280))
        

    def test_81(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo() ;
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 281))
        

    def test_82(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure 123()
"""
        expect = "Error on line 2 col 10: 123"
        self.assertTrue(TestParser.test(input, expect, 282))
        

    def test_83(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure true()
"""
        expect = "Error on line 2 col 10: true"
        self.assertTrue(TestParser.test(input, expect, 283))
        

    def test_84(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedue foo();
"""
        expect = "Error on line 2 col 0: procedue"
        self.assertTrue(TestParser.test(input, expect, 284))
        

    def test_85(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
begin
end;
"""
        expect = "Error on line 4 col 3: ;"
        self.assertTrue(TestParser.test(input, expect, 285))
        

    def test_86(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
begin
"""
        expect = "Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 286))
        

    def test_87(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var ;
begin
end
"""
        expect = "Error on line 3 col 4: ;"
        self.assertTrue(TestParser.test(input, expect, 287))
        

    def test_88(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var a;
begin
end
"""
        expect = "Error on line 3 col 5: ;"
        self.assertTrue(TestParser.test(input, expect, 288))
        

    def test_89(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var
begin
end
"""
        expect = "Error on line 4 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 289))
        

    def test_90(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var a: integer;
end
"""
        expect = "Error on line 4 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 290))
        

    def test_91(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var a: integer;
begin
begin
end
"""
        expect = "Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 291))
        

    def test_92(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo();
var a: integer;
begin
begin
end
"""
        expect = "Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 292))
        

    def test_93(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo(a: real;);
begin
end
"""
        expect = "Error on line 2 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 293))
        

    def test_94(self):
        """ Test Wrong Syntax Procedure Declare """
        input = """
procedure foo(a: real; b, c, d: boolean;);
begin
end
"""
        expect = "Error on line 2 col 40: )"
        self.assertTrue(TestParser.test(input, expect, 294))
        

    def test_95(self):
        """ Test Wrong Syntax Function Declare """
        input = """
function foo();
begin
end
"""
        expect = "Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 295))
        

    def test_96(self):
        """ Test Wrong Syntax Function Declare """
        input = """
function foo: real;
begin
end
"""
        expect = "Error on line 2 col 12: :"
        self.assertTrue(TestParser.test(input, expect, 296))
        

    def test_97(self):
        """ Test Wrong Syntax Function Declare """
        input = """
function foo(): float;
begin
end
"""
        expect = "Error on line 2 col 16: float"
        self.assertTrue(TestParser.test(input, expect, 297))
        

    def test_98(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    a = 1;
end
"""
        expect = "Error on line 4 col 6: ="
        self.assertTrue(TestParser.test(input, expect, 298))
        

    def test_99(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1:
        print('OK');
end
"""
        expect = "Error on line 4 col 12: :"
        self.assertTrue(TestParser.test(input, expect, 299))
        

    def test_100(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 {
        print('OK');
    }
end
"""
        expect = "Error on line 7 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 300))
    
    def test_101(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1
        print('OK');
end
"""
        expect = "Error on line 5 col 8: print"
        self.assertTrue(TestParser.test(input, expect, 301))
        

    def test_102(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 print('OK');
end
"""
        expect = "Error on line 4 col 13: print"
        self.assertTrue(TestParser.test(input, expect, 302))
        

    def test_103(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2; else
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 303))
        

    def test_104(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2 else begin
end
"""
        expect = "Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(input, expect, 304))
        

    def test_105(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2 else begin
        b:=2
end
"""
        expect = "Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(input, expect, 305))
        

    def test_106(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 306))
        

    def test_107(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2; else c := 3
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 307))
        

    def test_108(self):
        """ Test Error If Stmt """
        input = """
procedure foo();
begin
    if a = 1 then b := 2; else begin
        c := 4
    end;
end
"""
        expect = "Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 308))
        

    def test_109(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i = 1 to 10 do ok();
end
"""
        expect = "Error on line 4 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 309))
        

    def test_110(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 to 10: ok();
end
"""
        expect = "Error on line 4 col 20: :"
        self.assertTrue(TestParser.test(input, expect, 310))
        

    def test_111(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 .. 10 do ok();
end
"""
        expect = "Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(input, expect, 311))
        

    def test_112(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for (int i = 1; i < 10; i++) ok();
end
"""
        expect = "Error on line 4 col 8: ("
        self.assertTrue(TestParser.test(input, expect, 312))
        

    def test_113(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 down 10 do ok();
end
"""
        expect = "Error on line 4 col 15: down"
        self.assertTrue(TestParser.test(input, expect, 313))
        

    def test_114(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 to 10+5-4*e+x do ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 314))
        

    def test_115(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := f(g(h[5*t(9,1)])) to 10+5-4*e+x do ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 315))
        

    def test_116(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 to do ok();
end
"""
        expect = "Error on line 4 col 18: do"
        self.assertTrue(TestParser.test(input, expect, 316))
        

    def test_117(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := to 10 do ok();
end
"""
        expect = "Error on line 4 col 13: to"
        self.assertTrue(TestParser.test(input, expect, 317))
        

    def test_118(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 to 10 do begin
        
    end;
end
"""
        expect = "Error on line 6 col 7: ;"
        self.assertTrue(TestParser.test(input, expect, 318))
        

    def test_119(self):
        """ Test Error For Stmt """
        input = """
procedure foo();
begin
    for i := 1 to 10 do begin
        ok()
    end
end
"""
        expect = "Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 319))
        

    def test_120(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    while i do ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 320))
        

    def test_121(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    while i do ok()
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 321))
        

    def test_122(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    while i do ok
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 322))
        

    def test_123(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    while i do begin
        ok()
    end
end
"""
        expect = "Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 323))
        

    def test_124(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
"""
        expect = "Error on line 4 col 13: <"
        self.assertTrue(TestParser.test(input, expect, 324))
        

    def test_125(self):
        """ Test Error While Stmt """
        input = """
procedure foo();
begin
    loop i<4 do ok();
end
"""
        expect = "Error on line 4 col 9: i"
        self.assertTrue(TestParser.test(input, expect, 325))
        

    def test_126(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a do ok();
end
"""
        expect = "Error on line 4 col 11: do"
        self.assertTrue(TestParser.test(input, expect, 326))
        

    def test_127(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with do ok();
end
"""
        expect = "Error on line 4 col 9: do"
        self.assertTrue(TestParser.test(input, expect, 327))
        

    def test_128(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a: string do ok();
end
"""
        expect = "Error on line 4 col 19: do"
        self.assertTrue(TestParser.test(input, expect, 328))
        

    def test_129(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a:string; do ok();
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 329))
        

    def test_130(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a,b,c,d:string do ok();
end
"""
        expect = "Error on line 4 col 24: do"
        self.assertTrue(TestParser.test(input, expect, 330))
        

    def test_131(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
"""
        expect = "Error on line 4 col 35: do"
        self.assertTrue(TestParser.test(input, expect, 331))
        

    def test_132(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a,b,c,d:string; f,:integer; do ok();
end
"""
        expect = "Error on line 4 col 27: :"
        self.assertTrue(TestParser.test(input, expect, 332))
        

    def test_133(self):
        """ Test Error With Stmt """
        input = """
procedure foo();
begin
    with a,b,c,d:string; // f:integer do ok();
end
"""
        expect = "Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 333))
        

    def test_134(self):
        """ Test Error on Statement """
        input = """
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
"""
        expect = "Error on line 7 col 47: break"
        self.assertTrue(TestParser.test(input, expect, 334))
        

    def test_135(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
end
"""
        expect = "Error on line 28 col 4: ("
        self.assertTrue(TestParser.test(input, expect, 335))
        

    def test_136(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
end
"""
        expect = "Error on line 28 col 4: ("
        self.assertTrue(TestParser.test(input, expect, 336))
        

    def test_137(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    with i: integer; do begin
        for i := 4 downto -5 do h := 6
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================*)
end
"""
        expect = "Error on line 15 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 337))
        

    def test_138(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================*)
end
"""
        expect = "Error on line 8 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 338))
        

    def test_139(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
    (*
        =======================================
        Comment here
        =======================================*)
end
"""
        expect = "Error on line 31 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 339))
        

    def test_140(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
        {{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}
        *)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 340))
        

    def test_141(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        ======================================={{}}}}}}
        {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
end
"""
        expect = "Error on line 28 col 4: ("
        self.assertTrue(TestParser.test(input, expect, 341))
        

    def test_142(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================*)
        {}{
end
"""
        expect = "Error on line 32 col 10: {"
        self.assertTrue(TestParser.test(input, expect, 342))
        

    def test_143(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================*))
end
"""
        expect = "Error on line 31 col 49: )"
        self.assertTrue(TestParser.test(input, expect, 343))
        

    def test_144(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        ======================================= *)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 344))
        

    def test_145(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        ======================================= *)
end
"""
        expect = "Error on line 20 col 0: var"
        self.assertTrue(TestParser.test(input, expect, 345))
        

    def test_146(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        ======================================= *)
end
"""
        expect = "Error on line 19 col 4: return"
        self.assertTrue(TestParser.test(input, expect, 346))
        

    def test_147(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
    (*
        =======================================
        Comment here
        =======================================
        begin
    *)
end
"""
        expect = "Error on line 32 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 347))
        

    def test_148(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect = "Error on line 26 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 348))
        

    def test_149(self):
        """ Test Random Error Code """
        input = """
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect = "Error on line 22 col 0: var"
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_150(self):
        """ Test Complex Code """
        input = """
procedure foo();
begin
    a := "hello foo() \n.This is test"; // comment here
    { this is also comment
        if a = 1 then goto(4) 
        }
    for i:=1 to 10 do begin {
        if True then True()
    }
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_151(self):
        """ Test Function in Function """
        input = """
procedure foo();
begin
    function foo():real;
    begin
    end
end
"""
        expect = "Error on line 4 col 4: function"
        self.assertTrue(TestParser.test(input, expect, 351))

    
    def test_152(self):
        """ Test Compound Stmt in Compound Stmt """
        input = """
procedure foo();
begin
    begin
        begin
            ok();
        end
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 352))
        

    def test_153(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := b[3] := foo(3)[5] := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 353))
        

    def test_154(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := b[3] := foo(3) := 5;
end
"""
        expect = "Error on line 4 col 24: :="
        self.assertTrue(TestParser.test(input, expect, 354))
        

    def test_155(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := b+5 := 5;
end
"""
        expect = "Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(input, expect, 355))
        

    def test_156(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := (b+5*6)[d] := 5;
end
"""
        expect = "Error on line 4 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 356))
        

    def test_157(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := a[d][t] := 5;
end
"""
        expect = "Error on line 4 col 13: ["
        self.assertTrue(TestParser.test(input, expect, 357))
        

    def test_158(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := a[d := 5;
end
"""
        expect = "Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(input, expect, 358))
        

    def test_159(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := a[d=4] := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 359))
        

    def test_160(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := a[d<4] := 5;
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 360))
        

    def test_161(self):
        """ Test Assignment Stmt """
        input = """
procedure foo();
begin
    a := a[d:=3] := 5;
end
"""
        expect = "Error on line 4 col 12: :="
        self.assertTrue(TestParser.test(input, expect, 361))
        

    def test_162(self):
        """ Test  """
        input = """
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
"""
        expect = "Error on line 4 col 41: ["
        self.assertTrue(TestParser.test(input, expect, 362))
        

    def test_163(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 363))
        

    def test_164(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 364))
        

    def test_165(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 365))
        

    def test_166(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 366))
        

    def test_167(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 367))
        

    def test_168(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 368))
        

    def test_169(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 369))
        

    def test_170(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 370))
        

    def test_171(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 371))
        

    def test_172(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 372))
        

    def test_173(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 373))
        

    def test_174(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 374))
        

    def test_175(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 375))
        

    def test_176(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 376))
        

    def test_177(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 377))
        

    def test_178(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 378))
        

    def test_179(self):
        """ Test  """
        input = """

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 379))
        
