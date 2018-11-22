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
    for i := a to b do begin
        putInt(i);
        putString(": ");
        for j := i+1 to b do begin
            if (j + i) * 2 > b then break;
            putInt(j);
            putString(" ");
        end
        if i > 5 then break;
        putLn();
        putString("j = ");
        putIntLn(j);
        putString("i = "); 
        putIntLn(i);
    end
    putInt(i);
end

"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,1))