import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""
var 
    a,b: integer;
    x,y: real;
    u,v: boolean;

procedure main();
begin
end

function f1(): integer;
begin
    a := 10;
    if u then return b;
    b := 1;
    if u then begin
        if v then return a;
        else if u then return 2;
    end
    if u then begin
        for a := 1 to 10 do begin
            if v then return b;
            else if v then return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
            else begin
                while a < 10 do begin
                    for a := 1 to 10 do begin
                        if a = 10 then continue;
                        if a = 10 then break;
                        if a = 10 then return b;
                        else if a = 10 then break;
                        else if a = 10 then return b;
                        else if a = 10 then return b;
                        a := 10;

                        if a = 10 then begin
                            for a := 1 to 10 do continue;
                            return (1*3+1*5+3-1+5*3+1-3+5) - a+b;
                        end else begin
                            b := 1;
                            return (2*4+6*6+4-2+4*6+4-4+6) * a+b;
                        end
                    end
                end
            end
        end
    end else begin

        if u then begin
            with i,j,k: integer; do begin
                return 5;
            end
        end else begin

            for a := 1 to 10 do begin
                with i, j, k: integer;
                    f1, f2, f3: boolean; do begin
                        for i := j+k to j*k do begin
                            putLn();
                            if i >= 5 then break;
                            if j <= 10 then continue;
                            if i >= 0 then break;
                            else return 0;

                            a := 10;
                        end
                        return a;
                    end
            end

        end
    end
end

"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 101))