import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

var a: array[3 .. 5] of integer;

procedure main();
begin
    a[5] := 10;
    putInt(a[5]);
end

"""
        expect = r"""10"""
        self.assertTrue(TestCodeGen.test(input,expect,1))


"""



"""