import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var a: integer;
begin
    a := 5;
    putIntLn(a);
    putFloatLn(a);
    putFloatLn(a + 5.0);
end

"""
        expect = r"""5
5.0
10.0
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