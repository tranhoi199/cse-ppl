import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,1))


"""
procedure foo(
    a, b: Integer;
    x, y: String;
    u, v: Boolean
);
var e, f: Real;
    i, j: integer;
begin

end
"""