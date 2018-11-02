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
    bar();
    bar();
    bar();
    return "1";
end

function rft(a: integer; b,c: String): boolean;
begin
    bar();
    return False;
end

procedure bar();
begin
    bar();
    bar();
end

function tar(
    a, b, c: string; 
    f, k, o: integer; 
    g, h, t: Real 
    ): array[-4 .. 5] of boolean;
var 

    f1: array[-1 .. 2] of boolean;
    f2: array[-1 .. 5] of boolean;
    f3: array[-4 .. 5] of string;
    f4: array[-4 .. 5] of boolean;
begin
    // return f1;
    // return f2;
    // return f3;
    
    if (f = 2) then return f4;

    with i,j,k: integer; 
        g: String;
        h,p,t: BooLean;
    do begin
        g := "123";
        if t then i := 1; else t := false;
    end
    
    for f := 1 to 10 do k := 4;

    for f := f * k + 4 to 14+5-f do begin
        k := 5;
        // break;
        if k = 5 then break;
        if k = 5 then continue;
        k := 5;
    end

    // if k = 5 then return f4; else return f4;


    if k = 5 then begin
        k := 5;
        if k = 5 then begin
            k := 5;
            if k = 5 then
                for k :=  1 to 10 do break;
            return f4;
        end else begin
            k := 5;
            // if k = 5 break;
            // return f4;
            if k = 5 then begin
                return f4;
            end
            else if k = 5 then return f4;
            else if k = 5 then return f4;
            else if k = 5 then return f4;
            else return f4;
        end
    end else begin
        return f4;
    end 
    
    // if (f = 2) then continue;
    // break;
    // return f4;
    
    // foo();
    // a := foo();
end


procedure main();
var a: integer; x: boolean;
begin
    // bar();
    putStringLn(foo());
    // x := rft(1, "", "");
end

procedure nty();
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
