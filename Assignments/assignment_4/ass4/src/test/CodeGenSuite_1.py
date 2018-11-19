import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var a, b: integer;
    x, y: STRING;
begin
    a := 1;
end

"""
        expect = r"""1"""
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