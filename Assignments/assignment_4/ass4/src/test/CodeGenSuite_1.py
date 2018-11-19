import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

function foo(): integer;
begin
    return 100;
end

procedure main();
begin
    putInt(foo());
end

"""
        expect = r"""100"""
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