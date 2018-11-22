import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

// var a: array[2 .. 5] of integer;

procedure main();
var a: array[5 .. 15] of integer;
begin
    a[6] := 4;
end

"""
        expect = r"""
2.0 10.0
1 5"""
        self.assertTrue(TestCodeGen.test(input,expect,1))