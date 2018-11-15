import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""
        
procedure main(); 
begin 
    putBool(FALSE OR TRUE and false or (False or true));
end

"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,1))