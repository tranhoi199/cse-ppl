import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

var a, b: integer;
var x, y: real;
var u, v: boolean;

procedure main();
var n: integer;
begin

end

function mid(a, b: integer): real; begin return (a + b) / 2; end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,1))


"""

procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    for i := 0 to 10 do a[i] := i;
    foo(a);
end

procedure foo(a: array[0 .. 10] of integer);
begin
end


procedure main();
var a: array[0 .. 10] of integer;
    i: integer;
begin
    for i := 0 to 10 do a[i] := i;
    putInt(find(a, 5));
end

function find(a: array[0 .. 10] of integer; x: integer): integer;
var i: integer;
begin
    for i := 0 to 10 do begin
        if a[i] = x then return i;
    end
    return -1;
end

"""