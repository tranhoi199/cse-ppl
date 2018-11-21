import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
begin
    if 5*2 + 3 - 5*2 - 3 = 0 then begin
        putInt(100);
        putFloat(100);
        if true then putInt(101); else putInt(102);
    end else begin
        putInt(200);
        putFloat(200);
        if true then putInt(201); else putInt(202);
    end
end

"""
        expect = r"""100100.0101"""
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