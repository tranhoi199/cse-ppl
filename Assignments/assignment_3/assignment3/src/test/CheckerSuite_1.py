import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""

procedure main();
begin
    // PUTSTRINGLN(foo(True, False, 1, 2, 3));
end

function foo(a: Boolean; b: Boolean; x,y: Integer; z: Real): String;
var
    arr: array [1 .. 100] of String;
    i,j: integer;
begin
    while i < 1000 do begin
        a := True and then False;
        putString(arr[100]);
        if a then continue; else begin
            if a then return "1";
            else if a then return "1";
            else if a then return "2";
            else begin
                with a: integer; g: boolean; do begin
                    if a mod 10 = x and then b or else g then return "3";
                    else main();
                end
            end
        end
        i := 1000;
        while i < 100 do main();
        while i < 100 do main();
        with i: string; do begin
            while b do begin
                break;
            end
            putString(i);
            return foo(True, True, j,x,y);
        end
    end
    while i < 100 do main();
    while i < 100 do main();
    with i: string; do begin
        while b do begin
            break;
        end
        putString(i);
        return foo(True, True, j,x,y);
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 101))

