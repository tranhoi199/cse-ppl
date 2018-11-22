import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""


procedure main();
var a: array[2 .. 5] of integer;
begin
    a[2] := 10;
    putInt(a[2]);
end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,1))