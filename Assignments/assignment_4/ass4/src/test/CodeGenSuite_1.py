import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var i, j, a, b: integer;
begin
    a := 1;
    b := 10;
    for i := a-b to a+b do begin
        putInt(i);
        i := i+1;
        a := a-1;
        b := b+1;
    end
end

"""
        expect = r"""-9-7-5-3-11357911"""
        self.assertTrue(TestCodeGen.test(input,expect,1))