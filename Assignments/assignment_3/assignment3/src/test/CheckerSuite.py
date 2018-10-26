import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = r"""
var a, b, c: integer;
    x, y, z: string;
var g, h, f: real;

function foo(): String;
begin
end

function goo(): String;
begin
end

procedure goo();
begin
end

function fgoo(a,b,c: string; 
    f,k,o: integer; g,h,t: Real): String;
begin
end
"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))
