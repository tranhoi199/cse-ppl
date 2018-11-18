import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""
        
procedure main();
begin
    putFloatLn(1.5*2 + 2 - 5.3*2.1);
    putFloatLn(3*5 + 2*3/2 - 4*7.2/14 + 1);
    putFloatLn(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1));
end

"""
        expect = r"""-6.13
16.942858
-23.072857
"""
        self.assertTrue(TestCodeGen.test(input,expect,1))