import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""
        
procedure main();
begin
    putBool(false or else false or else true and then (true or else false) and (false or else true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,1))