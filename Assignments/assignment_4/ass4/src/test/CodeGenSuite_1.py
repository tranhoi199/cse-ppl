import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
var i: integer;
begin
    for i := 8 downto 1 do begin
        if i < 5 then continue;
        putInt(i);
    end
    putInt(i);
end

"""
        expect = r"""87650"""
        self.assertTrue(TestCodeGen.test(input,expect,1))