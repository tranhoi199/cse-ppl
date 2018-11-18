import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

var a: integer;
procedure main();
begin
    a := 1;
    putInt(a);
end

"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input,expect,1))