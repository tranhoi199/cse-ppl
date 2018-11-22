import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var i: integer;
begin
    i := 1;
    //for i := 1 to 8 do begin
    //end
end

"""
        expect = r"""
2.0 10.0
1 5"""
        self.assertTrue(TestCodeGen.test(input,expect,1))