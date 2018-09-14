import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    def test_1_var_decl(self):
        """ Test Var Declare 1 line 1 var """
        input = r"""
var a: integer;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        

    def test_2_var_decl(self):
        """ Test Var Declare 1 line n var """
        input = r"""
var a, b, c: integer;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        

    def test_3_var_decl(self):
        """ Test Var Declare n line """
        input = r"""
var a, b, c: integer;
var x, y: real;
var z: string;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        

    def test_4_var_decl(self):
        """ Test Var Declare array """
        input = r"""
var a: array[1 .. 3] of integer;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        

    def test_5_var_decl(self):
        """ Test Var Declare """
        input = r"""
Var a, B, c: array [5 .. 1000] of Boolean ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        

    def test_6_var_decl(self):
        """ Test Var Declare """
        input = r"""
Var a, B, c: InTeGer;
    x, Y, Z: Boolean ;
    g: Array [4 .. 6] of REAL;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        

    def test_7_proc_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
procedure foo();
var a: real;
begin

end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        

    def test_8_proc_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
procedure foo(x: integer);
var a, b, c: real;
begin

end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        

    def test_9_proc_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
procedure foo(x: integer; y, z: real; g, h: string);
var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;

begin


end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        

    def test_10_proc_func_decl(self):
        """ Test Procedure Function Declare """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 210))
        

    def test_11_assign(self):
        """ Test Assign Statment """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        

    def test_12_assign(self):
        """ Test Assign Statment """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b := c := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        

    def test_13_assign(self):
        """ Test Assign Statment """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b [10] := foo() [3 ] := x := 1 ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        

    def test_14_assign(self):
        """ Test Assign Statment """
        input = r"""
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]]] + 3;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        

    def test_15_assign(self):
        """ Test Assign Statment """
        input = r"""
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        

    def test_16_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n + 5 - g - 9;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        

    def test_17_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n or 4 + 5 - g or 2 - 9;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        

    def test_18_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b / 2 * n / 4 div 5 mod g and 2 * 9 / 4 mod 2;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        

    def test_19_precedence(self):
        """ Test Precedence """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := -5 - 6 + not 5 - 9 - not -(3 + not -5);
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        

    def test_20_precedence(self):
        """ Test Precedence """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        

    def test_12_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := b = c ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        

    def test_22_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        

    def test_23_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := TRUE and then 2 ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        

    def test_24_assoc(self):
        """ Test Associative """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := TRUE and then FALSE or     else True or      else (1 and       then 2) ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        

    def test_25_keyword(self):
        """ Test True False Keywords """
        input = r"""
procedure foo();

var 
    a: real;

begin
    a := True ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        

    def test_26_if(self):
        """ Test If Statement """
        input = r"""
procedure foo();
var a: real;
begin
    if a = 1 then ok();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        

    def test_27_if(self):
        """ Test If Statement """
        input = r"""
procedure foo();
var a: real;
begin
    if a = 1 or b = 2 and c = 3 then 
        ok();
end
"""
        expect = r"Error on line 5 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 227))
        

    def test_28_if(self):
        """ Test If Statement """
        input = r"""
procedure foo();
var a: real;
begin
    if a = 1 then
        a := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        

    def test_29_if(self):
        """ Test If Statement """
        input = r"""
procedure foo();
var a: real;
begin
    if a = 1 then begin
        a := 5;
        b := c := e * 2;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        

    def test_30_if(self):
        """ Test If Statement """
        input = r"""
procedure foo();
var a: real;
begin
    if a = 1 then ok(); else no();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        

    def test_31_if(self):
        """ Test If Statement """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        

    def test_32_if(self):
        """ Test If Statement """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 232))
        

    def test_33_while(self):
        """ Test While Statment """
        input = r"""
procedure foo();
var a: real;
begin
    While (i < 1) do i := i+1;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        

    def test_34_while(self):
        """ Test While Statement """
        input = r"""
procedure foo();
var a: real;
begin
    While i < 1 do begin
        i := i+1;
        if i = 1 then i := i - 1;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        

    def test_35_for(self):
        """ Test For Statment """
        input = r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        

    def test_36_with(self):
        """ Test With Statment """
        input = r"""
procedure foo();
var a: real;
begin
    with a: integer; do a := a + 1;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        

    def test_37_with(self):
        """ Test With Statment """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        

    def test_38_call(self):
        """ Test Call Statment """
        input = r"""
procedure foo();
var a: real;
begin
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        

    def test_39_complex(self):
        """ Test Complex Code """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        

    def test_40_complex(self):
        """ Test Success Code Statment """
        input = r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        

    def test_41_err_delc(self):
        """ Test Missing ; """
        input = r"""
var a: integer
"""
        expect = r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 241))
        

    def test_42_err_delc(self):
        """ Test Missing ; """
        input = r"""
var a: integer"""
        expect = r"Error on line 2 col 14: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 242))
        

    def test_43_err_delc(self):
        """ Test Error : """
        input = r"""
var a:: integer;
"""
        expect = r"Error on line 2 col 6: :"
        self.assertTrue(TestParser.test(input, expect, 243))
        

    def test_44_err_delc(self):
        """ Test Error Type """
        input = r"""
var a: int
"""
        expect = r"Error on line 2 col 7: int"
        self.assertTrue(TestParser.test(input, expect, 244))
        

    def test_45_err_delc(self):
        """ Test Missing type """
        input = r"""
var a:
"""
        expect = r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 245))
        

    def test_46_err_delc(self):
        """ Test Missing type """
        input = r"""
var a
"""
        expect = r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 246))
        

    def test_47_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var a: boolean integer
"""
        expect = r"Error on line 2 col 15: integer"
        self.assertTrue(TestParser.test(input, expect, 247))
        

    def test_48_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
a : integer
"""
        expect = r"Error on line 2 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 248))
        

    def test_49_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var real: integer;
"""
        expect = r"Error on line 2 col 4: real"
        self.assertTrue(TestParser.test(input, expect, 249))
        

    def test_50_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var a integer;
"""
        expect = r"Error on line 2 col 6: integer"
        self.assertTrue(TestParser.test(input, expect, 250))
        

    def test_51_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var a, b, : boolean ;
"""
        expect = r"Error on line 2 col 10: :"
        self.assertTrue(TestParser.test(input, expect, 251))
        

    def test_52_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var a, b, c: boolean;
x: real
"""
        expect = r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 252))
        

    def test_53_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
var a, b, c: boolean;
x, y, z: real
"""
        expect = r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test_54_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of bool;
"""
        expect = r"Error on line 4 col 26: bool"
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test_55_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of boolean
"""
        expect = r"Error on line 5 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test_56_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean;
"""
        expect = r"Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test_57_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of ;
"""
        expect = r"Error on line 4 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test_58_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5 of boolean ;
"""
        expect = r"Error on line 4 col 22: of"
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test_59_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ..] of boolean ;
"""
        expect = r"Error on line 4 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test_60_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0] of boolean ;
"""
        expect = r"Error on line 4 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test_61_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0  5] of boolean ;
"""
        expect = r"Error on line 4 col 18: 5"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test_62_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ... 5] of boolean ;
"""
        expect = r"."
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test_63_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[.. 5] of boolean ;
"""
        expect = r"Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test_64_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[] of boolean ;
"""
        expect = r"Error on line 4 col 15: ]"
        self.assertTrue(TestParser.test(input, expect, 264))
        

    def test_65_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array of boolean
"""
        expect = r"Error on line 4 col 15: of"
        self.assertTrue(TestParser.test(input, expect, 265))
        

    def test_66_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array ;
"""
        expect = r"Error on line 4 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 266))
        

    def test_67_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean ;
"""
        expect = r"Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 267))
        

    def test_68_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] ;
"""
        expect = r"Error on line 4 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test_69_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] with boolean ;
"""
        expect = r"Error on line 4 col 23: with"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test_70_err_delc(self):
        """ Test Array Declare Error """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] in boolean;
"""
        expect = r"Error on line 4 col 23: in"
        self.assertTrue(TestParser.test(input, expect, 270))
        

    def test_71_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array(0 .. 5) of boolean ;
"""
        expect = r"Error on line 4 col 14: ("
        self.assertTrue(TestParser.test(input, expect, 271))
        

    def test_72_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: arr[0 .. 5] of boolean ;
"""
        expect = r"Error on line 4 col 9: arr"
        self.assertTrue(TestParser.test(input, expect, 272))
        

    def test_73_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 .. 5] of true ;
"""
        expect = r"Error on line 4 col 27: true"
        self.assertTrue(TestParser.test(input, expect, 273))
        

    def test_74_err_delc(self):
        """ Test Array Declare without space dotdot """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 ..5] of boolean ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        

    def test_75_err_delc(self):
        """ Test Array Declare without space dotdot """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0.. 5] of boolean ;
"""
        expect = r"."
        self.assertTrue(TestParser.test(input, expect, 275))
        

    def test_76_err_delc(self):
        """ Test Array Declare without space dotdot """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0..5] of boolean;
"""
        expect = r"Error on line 4 col 15: 0."
        self.assertTrue(TestParser.test(input, expect, 276))
        

    def test_77_err_delc(self):
        """ Test Negative index Array Declare """
        input = r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[-5 .. 5] of boolean;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        

    def test_78_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo()
"""
        expect = r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 278))
        

    def test_79_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo ;
"""
        expect = r"Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 279))
        

    def test_80_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo( ;
"""
        expect = r"Error on line 2 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 280))
        

    def test_81_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo() ;
"""
        expect = r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 281))
        

    def test_82_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure 123()
"""
        expect = r"Error on line 2 col 10: 123"
        self.assertTrue(TestParser.test(input, expect, 282))
        

    def test_83_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure true()
"""
        expect = r"Error on line 2 col 10: true"
        self.assertTrue(TestParser.test(input, expect, 283))
        

    def test_84_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedue foo();
"""
        expect = r"Error on line 2 col 0: procedue"
        self.assertTrue(TestParser.test(input, expect, 284))
        

    def test_85_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
begin
end;
"""
        expect = r"Error on line 4 col 3: ;"
        self.assertTrue(TestParser.test(input, expect, 285))
        

    def test_86_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
begin
"""
        expect = r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 286))
        

    def test_87_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var ;
begin
end
"""
        expect = r"Error on line 3 col 4: ;"
        self.assertTrue(TestParser.test(input, expect, 287))
        

    def test_88_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var a;
begin
end
"""
        expect = r"Error on line 3 col 5: ;"
        self.assertTrue(TestParser.test(input, expect, 288))
        

    def test_89_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var
begin
end
"""
        expect = r"Error on line 4 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 289))
        

    def test_90_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var a: integer;
end
"""
        expect = r"Error on line 4 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 290))
        

    def test_91_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var a: integer;
begin
begin
end
"""
        expect = r"Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 291))
        

    def test_92_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo();
var a: integer;
begin
begin
end
"""
        expect = r"Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 292))
        

    def test_93_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo(a: real;);
begin
end
"""
        expect = r"Error on line 2 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 293))
        

    def test_94_err_delc(self):
        """ Test Wrong Syntax Procedure Declare """
        input = r"""
procedure foo(a: real; b, c, d: boolean;);
begin
end
"""
        expect = r"Error on line 2 col 40: )"
        self.assertTrue(TestParser.test(input, expect, 294))
        

    def test_95_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
function foo();
begin
end
"""
        expect = r"Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 295))
        

    def test_96_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
function foo: real;
begin
end
"""
        expect = r"Error on line 2 col 12: :"
        self.assertTrue(TestParser.test(input, expect, 296))
        

    def test_97_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
function foo(): float;
begin
end
"""
        expect = r"Error on line 2 col 16: float"
        self.assertTrue(TestParser.test(input, expect, 297))
        

    def test_98_err_delc(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    a = 1;
end
"""
        expect = r"Error on line 4 col 6: ="
        self.assertTrue(TestParser.test(input, expect, 298))
        

    def test_99_err_stmt(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1:
        print('OK');
end
"""
        expect = r"Error on line 4 col 12: :"
        self.assertTrue(TestParser.test(input, expect, 299))
        

    def test_100_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 {
        print('OK');
    }
end
"""
        expect = r"Error on line 7 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 300))
    
    def test_101_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1
        print('OK');
end
"""
        expect = r"Error on line 5 col 8: print"
        self.assertTrue(TestParser.test(input, expect, 301))
        

    def test_102_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 print('OK');
end
"""
        expect = r"Error on line 4 col 13: print"
        self.assertTrue(TestParser.test(input, expect, 302))
        

    def test_103_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2; else
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 303))
        

    def test_104_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2 else begin
end
"""
        expect = r"Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(input, expect, 304))
        

    def test_105_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2 else begin
        b:=2
end
"""
        expect = r"Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(input, expect, 305))
        

    def test_106_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 306))
        

    def test_107_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 307))
        

    def test_108_err_if(self):
        """ Test Error If Stmt """
        input = r"""
procedure foo();
begin
    if a = 1 then b := 2; else begin
        c := 4
    end;
end
"""
        expect = r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 308))
        

    def test_109_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i = 1 to 10 do ok();
end
"""
        expect = r"Error on line 4 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 309))
        

    def test_110_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 to 10: ok();
end
"""
        expect = r"Error on line 4 col 20: :"
        self.assertTrue(TestParser.test(input, expect, 310))
        

    def test_111_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 .. 10 do ok();
end
"""
        expect = r"Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(input, expect, 311))
        

    def test_112_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for (int i = 1; i < 10; i++) ok();
end
"""
        expect = r"Error on line 4 col 8: ("
        self.assertTrue(TestParser.test(input, expect, 312))
        

    def test_113_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 down 10 do ok();
end
"""
        expect = r"Error on line 4 col 15: down"
        self.assertTrue(TestParser.test(input, expect, 313))
        

    def test_114_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 to 10+5-4*e+x do ok();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 314))
        

    def test_115_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := f(g(h[5*t(9,1)])) to 10+5-4*e+x do ok();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 315))
        

    def test_116_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 to do ok();
end
"""
        expect = r"Error on line 4 col 18: do"
        self.assertTrue(TestParser.test(input, expect, 316))
        

    def test_117_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := to 10 do ok();
end
"""
        expect = r"Error on line 4 col 13: to"
        self.assertTrue(TestParser.test(input, expect, 317))
        

    def test_118_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        
    end;
end
"""
        expect = r"Error on line 6 col 7: ;"
        self.assertTrue(TestParser.test(input, expect, 318))
        

    def test_119_err_for(self):
        """ Test Error For Stmt """
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        ok()
    end
end
"""
        expect = r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 319))
        

    def test_120_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    while i do ok();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 320))
        

    def test_121_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    while i do ok()
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 321))
        

    def test_122_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    while i do ok
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 322))
        

    def test_123_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    while i do begin
        ok()
    end
end
"""
        expect = r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 323))
        

    def test_124_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
"""
        expect = r"Error on line 4 col 13: <"
        self.assertTrue(TestParser.test(input, expect, 324))
        

    def test_125_err_while(self):
        """ Test Error While Stmt """
        input = r"""
procedure foo();
begin
    loop i<4 do ok();
end
"""
        expect = r"Error on line 4 col 9: i"
        self.assertTrue(TestParser.test(input, expect, 325))
        

    def test_126_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a do ok();
end
"""
        expect = r"Error on line 4 col 11: do"
        self.assertTrue(TestParser.test(input, expect, 326))
        

    def test_127_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with do ok();
end
"""
        expect = r"Error on line 4 col 9: do"
        self.assertTrue(TestParser.test(input, expect, 327))
        

    def test_128_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a: string do ok();
end
"""
        expect = r"Error on line 4 col 19: do"
        self.assertTrue(TestParser.test(input, expect, 328))
        

    def test_129_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a:string; do ok();
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 329))
        

    def test_130_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a,b,c,d:string do ok();
end
"""
        expect = r"Error on line 4 col 24: do"
        self.assertTrue(TestParser.test(input, expect, 330))
        

    def test_131_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
"""
        expect = r"Error on line 4 col 35: do"
        self.assertTrue(TestParser.test(input, expect, 331))
        

    def test_132_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a,b,c,d:string; f,:integer; do ok();
end
"""
        expect = r"Error on line 4 col 27: :"
        self.assertTrue(TestParser.test(input, expect, 332))
        

    def test_133_err_with(self):
        """ Test Error With Stmt """
        input = r"""
procedure foo();
begin
    with a,b,c,d:string; // f:integer do ok();
end
"""
        expect = r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 333))
        

    def test_134_err_complex(self):
        """ Test Error on Statement """
        input = r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
"""
        expect = r"Error on line 7 col 47: break"
        self.assertTrue(TestParser.test(input, expect, 334))
        

    def test_135_err_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(input, expect, 335))
        

    def test_136_err_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(input, expect, 336))
        

    def test_137_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 15 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 337))
        

    def test_138_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 8 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 338))
        

    def test_139_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 31 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 339))
        

    def test_140_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 340))
        

    def test_141_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(input, expect, 341))
        

    def test_142_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        {{{{}}{{}}}{}
end
"""
        expect = r"}"
        self.assertTrue(TestParser.test(input, expect, 342))
        

    def test_143_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 31 col 49: )"
        self.assertTrue(TestParser.test(input, expect, 343))
        

    def test_144_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 344))
        

    def test_145_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 20 col 0: var"
        self.assertTrue(TestParser.test(input, expect, 345))
        

    def test_146_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 19 col 4: return"
        self.assertTrue(TestParser.test(input, expect, 346))
        

    def test_147_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 32 col 0: end"
        self.assertTrue(TestParser.test(input, expect, 347))
        

    def test_148_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 26 col 0: begin"
        self.assertTrue(TestParser.test(input, expect, 348))
        

    def test_149_complex(self):
        """ Test Random Error Code """
        input = r"""
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
        expect = r"Error on line 22 col 0: var"
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_150_complex(self):
        """ Test Complex Code """
        input = r"""
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_151_func_in_func(self):
        """ Test Function in Function """
        input = r"""
procedure foo();
begin
    function foo():real;
    begin
    end
end
"""
        expect = r"Error on line 4 col 4: function"
        self.assertTrue(TestParser.test(input, expect, 351))

    
    def test_152_compound(self):
        """ Test Compound Stmt in Compound Stmt """
        input = r"""
procedure foo();
begin
    begin
        begin
            ok();
        end
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 352))
        

    def test_153_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3)[5] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 353))
        

    def test_154_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3) := 5;
end
"""
        expect = r"Error on line 4 col 24: :="
        self.assertTrue(TestParser.test(input, expect, 354))
        

    def test_155_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b+5 := 5;
end
"""
        expect = r"Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(input, expect, 355))
        

    def test_156_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := (b+5*6)[d] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 356))
        

    def test_157_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d][t] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 357))
        

    def test_158_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d := 5;
end
"""
        expect = r"Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(input, expect, 358))
        

    def test_159_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d=4] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 359))
        

    def test_160_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d<4] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 360))
        

    def test_161_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d:=3] := 5;
end
"""
        expect = r"Error on line 4 col 12: :="
        self.assertTrue(TestParser.test(input, expect, 361))
        

    def test_162_assign(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 362))
        

    def test_163_call_proc(self):
        """ Test Break Func call """
        input = r"""
procedure foo();
begin
    ok();
    break();
end
"""
        expect = r"Error on line 5 col 9: ("
        self.assertTrue(TestParser.test(input, expect, 363))
        

    def test_164_stmt(self):
        """ Test Statements """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        continue;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 364))
        

    def test_165_stmt(self):
        """ Test Return in Compound """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return 15 * 6 - 3;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 365))
        

    def test_166_stmt(self):
        """ Test Return multiple times """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return;
        return 15 * 6 - 3;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 366))
        

    def test_167_return_return(self):
        """ Test Return in Return """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return return 15 * 6 - 3;
    end
end
"""
        expect = r"Error on line 8 col 15: return"
        self.assertTrue(TestParser.test(input, expect, 367))
        

    def test_168_stmt(self):
        """ Test  """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return ;
    end
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 368))
        

    def test_169_return_break(self):
        """ Test Return Break """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return break;
    end
end
"""
        expect = r"Error on line 8 col 15: break"
        self.assertTrue(TestParser.test(input, expect, 369))
        

    def test_170_exp_real(self):
        """ Test  """
        input = r"""
procedure f();
begin
    a := -------------5.e4;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 370))
        

    def test_171_comment(self):
        """ Test Comment Line in Block """
        input = r"""
{
    // Line Comment
    (* Block Comment *)
}
"""
        expect = r"Error on line 6 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 371))
        

    def test_172_comment(self):
        """ Test Comment Block in Line """
        input = r"""
// Line Comment { Block Comment }
// Line Comment (* Block Comment *)
"""
        expect = r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 372))
        

    def test_173_arr_subscript(self):
        """ Test Supscript Array is expression """
        input = r"""
var a: array[1-2 .. 5+4 ] of integer;
"""
        expect = r"Error on line 2 col 14: -"
        self.assertTrue(TestParser.test(input, expect, 373))
        

    def test_174_idx_exp(self):
        """ Test Index Expression with or else """
        input = r"""
procedure foo();
begin
    a := (1 + 2 * 3 - 4 / 5 and 6 or then 7)[(1+2+3)-(4+5*6/abc and then (123))] := a[(((-5)))] := (((-5)))[a] := 0;
end
"""
        expect = r"Error on line 4 col 37: then"
        self.assertTrue(TestParser.test(input, expect, 374))
        

    def test_175_idx_exp(self):
        """ Test Index Expression """
        input = r"""
procedure foo();
begin
    a := (1 + 2 * 3 - 4 / 5 and 6 or else 7)[(1+2+3)-(4+5*6/abc and then (123))] := a[(((-5)))] := (((-5)))[a] := 0;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 375))

    def test_176_empty_prog(self):
        """ Test Empty Program """
        input = r""""""
        expect = r"Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 376))

    def test_177_arr_subscript(self):
        """ Test Array Subscript """
        input = r"""
var a : array[5 + (1 * 4/ 2) .. 14] of string;
"""
        expect = r"Error on line 2 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 377))
    
    def test_178_arr_subscript(self):
        """ Test Array Subscript """
        input = r"""
var a : array[1      .. 14] of string;
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 378))

    def test_179_if_else(self):
        """ Test If Else Again """
        input = r"""
procedure abc ();
var x , y : real ; 
    begin
        if x = y then
            a:= 1000;
        else;
            b:= 999;
    end
"""
        expect = r"Error on line 7 col 12: ;"
        self.assertTrue(TestParser.test(input, expect, 379))