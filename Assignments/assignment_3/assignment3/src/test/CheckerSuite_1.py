import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""

var
    a,b,c: integer;
    x,y,z: real;

procedure main();
var 
    i,j,p: integer;
    a : array [ 1 .. 5 ] of real;
begin
    
end

function f1(): array [ 1 .. 3 ] of real;
var nt: array [ 1 .. 3] of string;
begin
    with nt: array [ 1 .. 3 ] of real; do begin
        return nt;
    end
end

var
    i,j,k: string;
    p,q,r: boolean;

var nt: array [ 1 .. 3 ] of real;

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 101))

