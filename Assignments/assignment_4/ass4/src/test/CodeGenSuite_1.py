import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = r"""
        
procedure main();
begin 
    putInt(1);
end

"""
        expect = r"1"
        self.assertTrue(TestCodeGen.test(input,expect,1))