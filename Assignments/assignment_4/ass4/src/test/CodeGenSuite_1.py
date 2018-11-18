import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""
        
procedure main();
begin
    putBoolLn(not false);
    PutBooLLN(not true);
    putbOOLLN(not not false);
    PUtbOOLLN(not not true);
    PutBoOLLN(not not not false);
    PutBoOLLN(not not not true);
    PutBoOLLN(not false and true);
    PutBoOLLN(not true and false);
    PutBoOLLN(not not false and not not not true or false and true);
    PutBoOLLN(not not true or false);
end

"""
        expect = r"""true
false
false
true
true
false
true
false
false
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,1))