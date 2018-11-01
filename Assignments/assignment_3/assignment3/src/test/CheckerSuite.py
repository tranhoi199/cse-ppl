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

procedure bar();
begin
end

function tar(
    a, b, c: string; 
    f, k, o: integer; 
    g, h, t: Real): String;
begin
end

procedure main();
var d: integer; x: real; g, k, p: string;
u, v: boolean;
begin
    // u := "123" > 213;
    // u := (123.4 + x / 4) > 123 * d * a;
    // u := 1 > 2;
    // a := 1 > 2;
    // u := v := True and THEN v or else False and 5;
    // d := 1 + (2 + 3 - 4 * d) * b - f;
    // d := 1 + (2 + 3 - 4 * d) * b - 9.1;
    // a := 5;
    // g := h := 4.5;
    // g := h := a := 4;
    // g := x := y := "123";
    // a := foo();
    // foo();
    // z := y := x := foo();
    // x := foo(1, 2, 3);
    // a := bar();
    // bar();
    // p := tar("", g, p, d, 3, 4, 3.2, 4.5, x);
    // p := tar("", g, p, d, 3, 4, 3, 4.5, x);
    // p := tar("", g, p, d, 3, 4.1, 3.2, 4.5, x);
end
"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))
