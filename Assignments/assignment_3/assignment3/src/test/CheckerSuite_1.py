import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""

procedure p2(); begin p2(); p1(); main(); end
procedure p1(); begin p2(); p1(); main(); end

procedure main();
begin
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 101))

