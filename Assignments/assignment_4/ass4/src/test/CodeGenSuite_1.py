import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure Main();
var x: array[0 .. 10] of string;
begin
    foo(x);
end

procedure FOO(a: array[0 .. 10] of string);
var i: integer;
begin
    for i := 0 to 10 do putStringLN(a[i]);
end

"""
        expect = r"""null
null
null
null
null
null
null
null
null
null
null
"""
        self.assertTrue(TestCodeGen.test(input,expect,1))