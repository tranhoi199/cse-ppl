import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    def test_d66d07f9bc0b78d49f119ff5533e91(self):
        """ Test ... """
        _1=r"""
var a: integer;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,201))
        

    def test_9429bb6da60a7fcc5d5e47e1fbbc5d(self):
        """ Test ... """
        _1=r"""
var a, b, c: integer;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,202))
        

    def test_2d68c38f1e43d532d633cb72d69f8a(self):
        """ Test ... """
        _1=r"""
var a, b, c: integer;
var x, y: real;
var z: string;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,203))
        

    def test_5c9e880f81ff2fce0e7e657970c91e(self):
        """ Test ... """
        _1=r"""
var a: array[1 .. 3] of integer;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,204))
        

    def test_c2652ae49d5a27ea51cc2ba14e0751(self):
        """ Test ... """
        _1=r"""
Var a, B, c: array [5 .. 1000] of Boolean ;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,205))
        

    def test_dc1630232d055e6558c553e06b4212(self):
        """ Test ... """
        _1=r"""
Var a, B, c: InTeGer;
    x, Y, Z: Boolean ;
    g: Array [4 .. 6] of REAL;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,206))
        

    def test_e1426735443d43a2cbdb9cb0406fd5(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin

end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,207))
        

    def test_2d6d27d5dd00376d2e1ac03593054f(self):
        """ Test ... """
        _1=r"""
procedure foo(x: integer);
var a, b, c: real;
begin

end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,208))
        

    def test_baaa41678399078fc34b5c00141e2c(self):
        """ Test ... """
        _1=r"""
procedure foo(x: integer; y, z: real; g, h: string);
var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;

begin


end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,209))
        

    def test_18d2a670c1d80804bc6f39d7c46bbc(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,210))
        

    def test_5423fe460e3f0eea66167087ebaaf1(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,211))
        

    def test_a734cbad7c5474679f075c4cb6eecf(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b := c := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,212))
        

    def test_c9ef508fa49ef862cc4eddd2e28f79(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b [10] := foo() [3 ] := x := 1 ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,213))
        

    def test_d50ed0257365188b03af33d0f7101a(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]]] + 3;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,214))
        

    def test_c5b9f690d4b20ebd6b1ab115d97696(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,215))
        

    def test_eb041417df4892fb9b1f1be68208a4(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n + 5 - g - 9;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,216))
        

    def test_403caa0ed17f1ed9857bc343f1180f(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b + 2 + n or 4 + 5 - g or 2 - 9;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,217))
        

    def test_ee1882d3d79bccab81339dbfe0c1e2(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b / 2 * n / 4 div 5 mod g and 2 * 9 / 4 mod 2;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,218))
        

    def test_88809f127f31472d824507ba439dae(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := -5 - 6 + not 5 - 9 - not -(3 + not -5);
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,219))
        

    def test_27654e73e5d67208c0aa82d5a2b939(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,220))
        

    def test_33e6696d4756532b5a51c1b8fc7097(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := b = c ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,221))
        

    def test_902ffd33cb54a365c9e7d7b894218b(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,222))
        

    def test_d829613d724a1ee7ea83298471a132(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := TRUE and then 2 ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,223))
        

    def test_49cdb99c05ca58975a0d70d5ff5d00(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := TRUE and then FALSE or     else True or      else (1 and       then 2) ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,224))
        

    def test_115fda9da080c8049e6c03c84d8d6f(self):
        """ Test ... """
        _1=r"""
procedure foo();

var 
    a: real;

begin
    a := True ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,225))
        

    def test_719f1685616661040458053143b2fc(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    if a = 1 then ok();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,226))
        

    def test_cf09732816800dd66541fa9d650ce3(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    if a = 1 or b = 2 and c = 3 then 
        ok();
end
"""
        _2=r"Error on line 5 col 18: ="
        self.assertTrue(TestParser.test(_1,_2,227))
        

    def test_0b50599781fe346cf7174decef3b23(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    if a = 1 then
        a := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,228))
        

    def test_acc5d976808ae04ec7951e6e760055(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    if a = 1 then begin
        a := 5;
        b := c := e * 2;
    end
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,229))
        

    def test_d70f1496307a825f4460e331d94833(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    if a = 1 then ok(); else no();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,230))
        

    def test_bd253942174e6aaade9f15073b99ed(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,231))
        

    def test_03b0764296f3127f479fd87e606cc2(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,232))
        

    def test_ed189b496d6e63545976dec10b14d9(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    While (i < 1) do i := i+1;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,233))
        

    def test_7fc3decf87b7f743b84a07eada2606(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    While i < 1 do begin
        i := i+1;
        if i = 1 then i := i - 1;
    end
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,234))
        

    def test_9613139067ae94ac5a5fba935eb0b9(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,235))
        

    def test_54e809815ee774fb36f02ff7ad2b12(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    with a: integer; do a := a + 1;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,236))
        

    def test_c8066a60be8ca8df29843a4f004d6c(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,237))
        

    def test_586ca166da0926ff4f40d4f75ca4b6(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,238))
        

    def test_009aad6ca79d8f0eb99b6b1280f703(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,239))
        

    def test_4e9de0e7dbba768d8b1c38e34e7ab3(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,240))
        

    def test_ed0fd4468b01dece43dc8a50480b9d(self):
        """ Test ... """
        _1=r"""
var a: integer
"""
        _2=r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,241))
        

    def test_86e32e8573aa436b8a68d0ec7801a7(self):
        """ Test ... """
        _1=r"""
var a: integer"""
        _2=r"Error on line 2 col 14: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,242))
        

    def test_1e6de462d72220219138a9a3723a4f(self):
        """ Test ... """
        _1=r"""
var a:: integer;
"""
        _2=r"Error on line 2 col 6: :"
        self.assertTrue(TestParser.test(_1,_2,243))
        

    def test_e9b0cd9460dbb84f7dd4fe066c8aa7(self):
        """ Test ... """
        _1=r"""
var a: int
"""
        _2=r"Error on line 2 col 7: int"
        self.assertTrue(TestParser.test(_1,_2,244))
        

    def test_eb2dceb14c989c40a8bf871e70bf56(self):
        """ Test ... """
        _1=r"""
var a:
"""
        _2=r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,245))
        

    def test_05ac76fa2fb0571eb63793b8126b5a(self):
        """ Test ... """
        _1=r"""
var a
"""
        _2=r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,246))
        

    def test_ea16b401fa0986029ea0432fd87d6c(self):
        """ Test ... """
        _1=r"""
var a: boolean integer
"""
        _2=r"Error on line 2 col 15: integer"
        self.assertTrue(TestParser.test(_1,_2,247))
        

    def test_1ea70ea62499644c0db543615e3beb(self):
        """ Test ... """
        _1=r"""
a : integer
"""
        _2=r"Error on line 2 col 0: a"
        self.assertTrue(TestParser.test(_1,_2,248))
        

    def test_595db737e171f0ea0173b061530d6f(self):
        """ Test ... """
        _1=r"""
var real: integer;
"""
        _2=r"Error on line 2 col 4: real"
        self.assertTrue(TestParser.test(_1,_2,249))
        

    def test_4a661108c65725c7f09879a97c886b(self):
        """ Test ... """
        _1=r"""
var a integer;
"""
        _2=r"Error on line 2 col 6: integer"
        self.assertTrue(TestParser.test(_1,_2,250))
        

    def test_af0b00babaabdb1e114a0051d11b9e(self):
        """ Test ... """
        _1=r"""
var a, b, : boolean ;
"""
        _2=r"Error on line 2 col 10: :"
        self.assertTrue(TestParser.test(_1,_2,251))
        

    def test_c194cb6036018c3eddfdacb80b80d1(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x: real
"""
        _2=r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,252))
        

    def test_151227a117676dcb02a92e7ce1e207(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real
"""
        _2=r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,253))
        

    def test_1cab2b9e4804abedf0d4668bc5b080(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of bool;
"""
        _2=r"Error on line 4 col 26: bool"
        self.assertTrue(TestParser.test(_1,_2,254))
        

    def test_e5aab06a335841805c3da1fa58b6a1(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of boolean
"""
        _2=r"Error on line 5 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,255))
        

    def test_6b75963bd6831122adccd525328623(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean;
"""
        _2=r"Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(_1,_2,256))
        

    def test_5d8748cdfa1a30a985d4e1418ca9e3(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of ;
"""
        _2=r"Error on line 4 col 26: ;"
        self.assertTrue(TestParser.test(_1,_2,257))
        

    def test_e1ec7b1e3b058cb09f59af20192727(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5 of boolean ;
"""
        _2=r"Error on line 4 col 22: of"
        self.assertTrue(TestParser.test(_1,_2,258))
        

    def test_0a2b67db26b13c06771297f02f9ac0(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ..] of boolean ;
"""
        _2=r"Error on line 4 col 19: ]"
        self.assertTrue(TestParser.test(_1,_2,259))
        

    def test_7e34f7567875ac06f07f616804ede0(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0] of boolean ;
"""
        _2=r"Error on line 4 col 16: ]"
        self.assertTrue(TestParser.test(_1,_2,260))
        

    def test_d184c56c9e2186704838b42dee7e4a(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0  5] of boolean ;
"""
        _2=r"Error on line 4 col 18: 5"
        self.assertTrue(TestParser.test(_1,_2,261))
        

    def test_fa0de14b27e58c6414c5fc7e92133e(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 ... 5] of boolean ;
"""
        _2=r"."
        self.assertTrue(TestParser.test(_1,_2,262))
        

    def test_cee124033522e12f7f2256827719ac(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[.. 5] of boolean ;
"""
        _2=r"Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(_1,_2,263))
        

    def test_bdc0c5fc74ea7ebfdb5f8c253817de(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[] of boolean ;
"""
        _2=r"Error on line 4 col 15: ]"
        self.assertTrue(TestParser.test(_1,_2,264))
        

    def test_9fa1a9b96cd5f6948571e4c8508922(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array of boolean
"""
        _2=r"Error on line 4 col 15: of"
        self.assertTrue(TestParser.test(_1,_2,265))
        

    def test_91ef0735ea0ddbfd39d9ea252773ff(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array ;
"""
        _2=r"Error on line 4 col 15: ;"
        self.assertTrue(TestParser.test(_1,_2,266))
        

    def test_3d2e76029a2de261918678dcf451f5(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] boolean ;
"""
        _2=r"Error on line 4 col 23: boolean"
        self.assertTrue(TestParser.test(_1,_2,267))
        

    def test_1e30c083351ef7b9c3180f35dfa1e9(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] ;
"""
        _2=r"Error on line 4 col 23: ;"
        self.assertTrue(TestParser.test(_1,_2,268))
        

    def test_9e280d9aecb8e6b15f198aae68fc33(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] with boolean ;
"""
        _2=r"Error on line 4 col 23: with"
        self.assertTrue(TestParser.test(_1,_2,269))
        

    def test_32e265c3ad02525f0a11eee84ad0a8(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] in boolean;
"""
        _2=r"Error on line 4 col 23: in"
        self.assertTrue(TestParser.test(_1,_2,270))
        

    def test_7dd63725ed8ad24ae47f408249c0a5(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array(0 .. 5) of boolean ;
"""
        _2=r"Error on line 4 col 14: ("
        self.assertTrue(TestParser.test(_1,_2,271))
        

    def test_c126d9f685d346bab1765250304a9e(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: arr[0 .. 5] of boolean ;
"""
        _2=r"Error on line 4 col 9: arr"
        self.assertTrue(TestParser.test(_1,_2,272))
        

    def test_ba07a03d2ff227fb6bc0f66c13bf86(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 .. 5] of true ;
"""
        _2=r"Error on line 4 col 27: true"
        self.assertTrue(TestParser.test(_1,_2,273))
        

    def test_63658303132b68e78c178f6086f817(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array [0 ..5] of boolean ;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,274))
        

    def test_e17429a08a206e286c971a5ad4b679(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0.. 5] of boolean ;
"""
        _2=r"."
        self.assertTrue(TestParser.test(_1,_2,275))
        

    def test_8b507856351d288487880dd15e0437(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0..5] of boolean;
"""
        _2=r"Error on line 4 col 17: .5"
        self.assertTrue(TestParser.test(_1,_2,276))
        

    def test_9c2567ae109cd440a3b9e4018b9b26(self):
        """ Test ... """
        _1=r"""
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[-5 .. 5] of boolean;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,277))
        

    def test_bf50285e7d4e6eca89368a347f1e8a(self):
        """ Test ... """
        _1=r"""
procedure foo()
"""
        _2=r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,278))
        

    def test_093126b26c03c454a7618eed38d4f4(self):
        """ Test ... """
        _1=r"""
procedure foo ;
"""
        _2=r"Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(_1,_2,279))
        

    def test_ba687d5fd5a4c55d70177753aafc90(self):
        """ Test ... """
        _1=r"""
procedure foo( ;
"""
        _2=r"Error on line 2 col 15: ;"
        self.assertTrue(TestParser.test(_1,_2,280))
        

    def test_4388557dfd52b36e0dd475c8bc1879(self):
        """ Test ... """
        _1=r"""
procedure foo() ;
"""
        _2=r"Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,281))
        

    def test_907ea5e11513b3fc28926e2ba36fb5(self):
        """ Test ... """
        _1=r"""
procedure 123()
"""
        _2=r"Error on line 2 col 10: 123"
        self.assertTrue(TestParser.test(_1,_2,282))
        

    def test_18c9c4efac2166e5fbf6c6436c2042(self):
        """ Test ... """
        _1=r"""
procedure true()
"""
        _2=r"Error on line 2 col 10: true"
        self.assertTrue(TestParser.test(_1,_2,283))
        

    def test_71a31dc3f55bb2a78513abed28ce87(self):
        """ Test ... """
        _1=r"""
procedue foo();
"""
        _2=r"Error on line 2 col 0: procedue"
        self.assertTrue(TestParser.test(_1,_2,284))
        

    def test_3e6827d538df3906d88c0824fbbf6f(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
end;
"""
        _2=r"Error on line 4 col 3: ;"
        self.assertTrue(TestParser.test(_1,_2,285))
        

    def test_86e0461660239233b118874034705d(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
"""
        _2=r"Error on line 4 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,286))
        

    def test_836624a43431ef4b31e39a82adc189(self):
        """ Test ... """
        _1=r"""
procedure foo();
var ;
begin
end
"""
        _2=r"Error on line 3 col 4: ;"
        self.assertTrue(TestParser.test(_1,_2,287))
        

    def test_d6e67c9a092591e35924ce7c211d5a(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a;
begin
end
"""
        _2=r"Error on line 3 col 5: ;"
        self.assertTrue(TestParser.test(_1,_2,288))
        

    def test_f8505dc936be4ae694bb160f4cf78f(self):
        """ Test ... """
        _1=r"""
procedure foo();
var
begin
end
"""
        _2=r"Error on line 4 col 0: begin"
        self.assertTrue(TestParser.test(_1,_2,289))
        

    def test_4c90c81713dccaee709867efe91d4b(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: integer;
end
"""
        _2=r"Error on line 4 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,290))
        

    def test_a2fba9b0da439ef70fa2686deaeeed(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: integer;
begin
begin
end
"""
        _2=r"Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,291))
        

    def test_0f6c6af9e717e5835ee7d77bffbff6(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: integer;
begin
begin
end
"""
        _2=r"Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(_1,_2,292))
        

    def test_78b058e0652c9321b55b8aa9474033(self):
        """ Test ... """
        _1=r"""
procedure foo(a: real;);
begin
end
"""
        _2=r"Error on line 2 col 22: )"
        self.assertTrue(TestParser.test(_1,_2,293))
        

    def test_c7ce31216fa6ee176b873e42a9fc78(self):
        """ Test ... """
        _1=r"""
procedure foo(a: real; b, c, d: boolean;);
begin
end
"""
        _2=r"Error on line 2 col 40: )"
        self.assertTrue(TestParser.test(_1,_2,294))
        

    def test_dbf0e933d448f1d5f4dad8e600dbe6(self):
        """ Test ... """
        _1=r"""
function foo();
begin
end
"""
        _2=r"Error on line 2 col 14: ;"
        self.assertTrue(TestParser.test(_1,_2,295))
        

    def test_8b20472d6d94f40d792aa47ea7bd55(self):
        """ Test ... """
        _1=r"""
function foo: real;
begin
end
"""
        _2=r"Error on line 2 col 12: :"
        self.assertTrue(TestParser.test(_1,_2,296))
        

    def test_7f32c513301ca8f997406bf5842545(self):
        """ Test ... """
        _1=r"""
function foo(): float;
begin
end
"""
        _2=r"Error on line 2 col 16: float"
        self.assertTrue(TestParser.test(_1,_2,297))
        

    def test_b887c962fa39da039179e31f3d1bc1(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a = 1;
end
"""
        _2=r"Error on line 4 col 6: ="
        self.assertTrue(TestParser.test(_1,_2,298))
        

    def test_ad31acd21c30964bc7cb181df010cd(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1:
        print('OK');
end
"""
        _2=r"Error on line 4 col 12: :"
        self.assertTrue(TestParser.test(_1,_2,299))
        

    def test_e799fd12ab6cdc44b1a7435e1e4a24(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 {
        print('OK');
    }
end
"""
        _2=r"Error on line 7 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,300))
    
    def test_d853f06d4e2f0e174befef717cefc3(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1
        print('OK');
end
"""
        _2=r"Error on line 5 col 8: print"
        self.assertTrue(TestParser.test(_1,_2,301))
        

    def test_84c992cdc1084a6e73e264bbdd3592(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 print('OK');
end
"""
        _2=r"Error on line 4 col 13: print"
        self.assertTrue(TestParser.test(_1,_2,302))
        

    def test_b5b260b75f41b88fe1ede20c3b7980(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2; else
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,303))
        

    def test_2d50d2f9d91328e1d93f835335ef78(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2 else begin
end
"""
        _2=r"Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(_1,_2,304))
        

    def test_7b760b7ff218e68624e827b0e7ea0a(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2 else begin
        b:=2
end
"""
        _2=r"Error on line 4 col 25: else"
        self.assertTrue(TestParser.test(_1,_2,305))
        

    def test_c1d3b763ff8ecdd6743d38feeebfe9(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,306))
        

    def test_1aadb4be23d0788831b07b03f6edaa(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,307))
        

    def test_63dd8d14a4263958deead5d3af3956(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    if a = 1 then b := 2; else begin
        c := 4
    end;
end
"""
        _2=r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(_1,_2,308))
        

    def test_db3d1745f3b822f2d6da0a141e2cd8(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i = 1 to 10 do ok();
end
"""
        _2=r"Error on line 4 col 10: ="
        self.assertTrue(TestParser.test(_1,_2,309))
        

    def test_919601de0b8a6eada5524f45471b1d(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 to 10: ok();
end
"""
        _2=r"Error on line 4 col 20: :"
        self.assertTrue(TestParser.test(_1,_2,310))
        

    def test_25d9e7468e6fddebe5d378b702515b(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 .. 10 do ok();
end
"""
        _2=r"Error on line 4 col 15: .."
        self.assertTrue(TestParser.test(_1,_2,311))
        

    def test_2fd73b64865ab48a73e2cbb472c09e(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for (int i = 1; i < 10; i++) ok();
end
"""
        _2=r"Error on line 4 col 8: ("
        self.assertTrue(TestParser.test(_1,_2,312))
        

    def test_f10be47a99f319911aae6431a1d35c(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 down 10 do ok();
end
"""
        _2=r"Error on line 4 col 15: down"
        self.assertTrue(TestParser.test(_1,_2,313))
        

    def test_067237dc08e3cedec8193885824ad3(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 to 10+5-4*e+x do ok();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,314))
        

    def test_7236fe091234a4ac16b83ca69c333b(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := f(g(h[5*t(9,1)])) to 10+5-4*e+x do ok();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,315))
        

    def test_e9b7b2bd319bcab85c30629392046a(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 to do ok();
end
"""
        _2=r"Error on line 4 col 18: do"
        self.assertTrue(TestParser.test(_1,_2,316))
        

    def test_0765ab3e4936fbeaf7b5f1f15c5604(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := to 10 do ok();
end
"""
        _2=r"Error on line 4 col 13: to"
        self.assertTrue(TestParser.test(_1,_2,317))
        

    def test_63171e2edcb0dd302a99128c8e72b5(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        
    end;
end
"""
        _2=r"Error on line 6 col 7: ;"
        self.assertTrue(TestParser.test(_1,_2,318))
        

    def test_d74745cd06955bf04c4eb597e404b1(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        ok()
    end
end
"""
        _2=r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(_1,_2,319))
        

    def test_26b5d2cd24629dd306e032e017ea47(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    while i do ok();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,320))
        

    def test_9fc5aa624d59c36cb1abad4f709672(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    while i do ok()
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,321))
        

    def test_97268b61836cc35b1a33127d27ddf8(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    while i do ok
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,322))
        

    def test_7415eaac2c9cbc72d66e368883941c(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    while i do begin
        ok()
    end
end
"""
        _2=r"Error on line 6 col 4: end"
        self.assertTrue(TestParser.test(_1,_2,323))
        

    def test_cdc2796ff957b831d4834d81db5445(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
"""
        _2=r"Error on line 4 col 13: <"
        self.assertTrue(TestParser.test(_1,_2,324))
        

    def test_d8b0a37d041af19f642a730249a34e(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    loop i<4 do ok();
end
"""
        _2=r"Error on line 4 col 9: i"
        self.assertTrue(TestParser.test(_1,_2,325))
        

    def test_bb364d8a1367ccf567f1a487b63d34(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a do ok();
end
"""
        _2=r"Error on line 4 col 11: do"
        self.assertTrue(TestParser.test(_1,_2,326))
        

    def test_e1dbbe6efa142dba44bbf0a278b1ed(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with do ok();
end
"""
        _2=r"Error on line 4 col 9: do"
        self.assertTrue(TestParser.test(_1,_2,327))
        

    def test_fa5c779987af0de277c8d37252ea2d(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a: string do ok();
end
"""
        _2=r"Error on line 4 col 19: do"
        self.assertTrue(TestParser.test(_1,_2,328))
        

    def test_96f9de001eede93f2725ce408365dc(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a:string; do ok();
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,329))
        

    def test_f335af63636822bb4f4bbcdc0f4556(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a,b,c,d:string do ok();
end
"""
        _2=r"Error on line 4 col 24: do"
        self.assertTrue(TestParser.test(_1,_2,330))
        

    def test_072cf1fb58fe045230a0f3914e264b(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
"""
        _2=r"Error on line 4 col 35: do"
        self.assertTrue(TestParser.test(_1,_2,331))
        

    def test_d97e1725f922e859ab26aed42cd93f(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a,b,c,d:string; f,:integer; do ok();
end
"""
        _2=r"Error on line 4 col 27: :"
        self.assertTrue(TestParser.test(_1,_2,332))
        

    def test_1c789445c05a7d3e2e88b9df14bfab(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    with a,b,c,d:string; // f:integer do ok();
end
"""
        _2=r"Error on line 5 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,333))
        

    def test_8990bddfecc48a04819ae6bec5ea47(self):
        """ Test ... """
        _1=r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
"""
        _2=r"Error on line 7 col 47: break"
        self.assertTrue(TestParser.test(_1,_2,334))
        

    def test_b1a7260eb29fb1aeabd5d63638d8fb(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(_1,_2,335))
        

    def test_2ec819975b7bba7308bc5cbe345fe0(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(_1,_2,336))
        

    def test_33392dbcf089c8a5fcde06abb2daab(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 15 col 4: end"
        self.assertTrue(TestParser.test(_1,_2,337))
        

    def test_9ac40f190df8481b019eac8520f94d(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 8 col 0: begin"
        self.assertTrue(TestParser.test(_1,_2,338))
        

    def test_a30a0a1ed90a82b9399e34a12f98d3(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 31 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,339))
        

    def test_d896ae4958954a7ec4fff99bea9e77(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,340))
        

    def test_b303046dc52117a4b7535014700777(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(_1,_2,341))
        

    def test_0ddaa74ba9a08dd39c583b5b7e9f09(self):
        """ Test ... """
        _1=r"""
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
        _2=r"}"
        self.assertTrue(TestParser.test(_1,_2,342))
        

    def test_3a64d54c3dfdeb8b9958fe2271419c(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 31 col 49: )"
        self.assertTrue(TestParser.test(_1,_2,343))
        

    def test_a09b2c2349d2dbcd54a4f0b49666e2(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,344))
        

    def test_6423f14d6e3824ed0f7f0b81aba645(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 20 col 0: var"
        self.assertTrue(TestParser.test(_1,_2,345))
        

    def test_aa1bc69609d605a4b75191dd7e4008(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 19 col 4: return"
        self.assertTrue(TestParser.test(_1,_2,346))
        

    def test_79e959927732feb27108776356add9(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 32 col 0: end"
        self.assertTrue(TestParser.test(_1,_2,347))
        

    def test_8494c761f23d4d97edc4a68b47254f(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 26 col 0: begin"
        self.assertTrue(TestParser.test(_1,_2,348))
        

    def test_b88b99f10837cf200fc234caaced90(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 22 col 0: var"
        self.assertTrue(TestParser.test(_1,_2,349))

    def test_5d6b3afd346918924a5389f14edcb3(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,350))

    def test_2956ce8eb643bf898341de9d091bbf(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    function foo():real;
    begin
    end
end
"""
        _2=r"Error on line 4 col 4: function"
        self.assertTrue(TestParser.test(_1,_2,351))

    
    def test_a7d858d8ab9da65f03c2e6ae4e8529(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    begin
        begin
            ok();
        end
    end
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,352))
        

    def test_c665743ad51be896b36e8e69891eba(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := b[3] := foo(3)[5] := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,353))
        

    def test_dee384d48983a678a5d5876fb78cf5(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := b[3] := foo(3) := 5;
end
"""
        _2=r"Error on line 4 col 24: :="
        self.assertTrue(TestParser.test(_1,_2,354))
        

    def test_d1c298f6ffdc12554935d0007bd278(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := b+5 := 5;
end
"""
        _2=r"Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(_1,_2,355))
        

    def test_7153116aa9fe91652cdd3294a28ab2(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := (b+5*6)[d] := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,356))
        

    def test_3f060ebc0f22217fb1bfd781f685fd(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d][t] := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,357))
        

    def test_0562c31de059378c63fc7a5941c4d9(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d := 5;
end
"""
        _2=r"Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(_1,_2,358))
        

    def test_cabb63fb2c61821dbfe97071dac61e(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d=4] := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,359))
        

    def test_e5468d31963fb4c1428c1aec0ef751(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d<4] := 5;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,360))
        

    def test_ded3c3abe31f5954b79323d2721b75(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d:=3] := 5;
end
"""
        _2=r"Error on line 4 col 12: :="
        self.assertTrue(TestParser.test(_1,_2,361))
        

    def test_b617c5b9128dca939d331bf60a3883(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,362))
        

    def test_29c68006918917afaaba31091f60c7(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    ok();
    break();
end
"""
        _2=r"Error on line 5 col 9: ("
        self.assertTrue(TestParser.test(_1,_2,363))
        

    def test_178e750a165cbfb2102af26e6a1056(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,364))
        

    def test_f04eccdedea229ae228ab5fc48d978(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,365))
        

    def test_21e613a106dba2047d11642ad1244f(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,366))
        

    def test_26f593a3c1947060d22ab4a7e34684(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 8 col 15: return"
        self.assertTrue(TestParser.test(_1,_2,367))
        

    def test_1573f4f560545192656e27a8837c0b(self):
        """ Test ... """
        _1=r"""
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
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,368))
        

    def test_4cfad09364d183cb408d5742182911(self):
        """ Test ... """
        _1=r"""
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
        _2=r"Error on line 8 col 15: break"
        self.assertTrue(TestParser.test(_1,_2,369))
        

    def test_99c66940eeb9770923a8bcaa4a2bcd(self):
        """ Test ... """
        _1=r"""
procedure f();
begin
    a := -------------5.e4;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,370))
        

    def test_71c0bdb380ea0627008cdbd4b8cffc(self):
        """ Test ... """
        _1=r"""
{
    // Line Comment
    (* Block Comment *)
}
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,371))
        

    def test_7f57473ba80f177ae50c2a248fbe93(self):
        """ Test ... """
        _1=r"""
// Line Comment { Block Comment }
// Line Comment (* Block Comment *)
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,372))
        

    def test_7592440e6e8f7ef64f87933166cadb(self):
        """ Test ... """
        _1=r"""
var a: array[1-2 .. 5+4 ] of integer;
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,373))
        

    def test_909f430805f86d169cced599e50cfe(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := (1 + 2 * 3 - 4 / 5 and 6 or then 7)[(1+2+3)-(4+5*6/abc and then (123))] := a[(((-5)))] := (((-5)))[a] := 0;
end
"""
        _2=r"Error on line 4 col 37: then"
        self.assertTrue(TestParser.test(_1,_2,374))
        

    def test_c2c52b5b17a475103ac406bf4eec72(self):
        """ Test ... """
        _1=r"""
procedure foo();
begin
    a := (1 + 2 * 3 - 4 / 5 and 6 or else 7)[(1+2+3)-(4+5*6/abc and then (123))] := a[(((-5)))] := (((-5)))[a] := 0;
end
"""
        _2=r"successful"
        self.assertTrue(TestParser.test(_1,_2,375))