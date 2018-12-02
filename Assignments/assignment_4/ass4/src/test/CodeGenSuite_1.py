import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
begin
    putint(foo());
end

function foo(): integer;
var i: integer;
begin
    for i := 1 to 10 do begin
        return 5;
    end
    return 6;
end


"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input,expect,1))