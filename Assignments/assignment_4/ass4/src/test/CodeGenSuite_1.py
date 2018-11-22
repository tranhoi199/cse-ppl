import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var a, b: integer;
begin
    a := 1;
    b := 5;
    putLn();
    with a,b,c: real; do begin
        a := 2;
        b := 10;
        putFloat(a); putString(" ");
        putFloatLn(b);
    end
    putInt(a); putString(" ");
    putInt(b);
end

"""
        expect = r"""
2.0 10.0
1 5"""
        self.assertTrue(TestCodeGen.test(input,expect,1))