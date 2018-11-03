import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""
 procedure main();
                var a: real;
                i,j:integer;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    continue;
                    end
                    continue;
                end
"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 101))

