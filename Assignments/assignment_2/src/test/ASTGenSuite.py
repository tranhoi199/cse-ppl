#########################################################
########### Code used for Pylint to link code ###########
######    REMEMBER: Comment before submit code    #######
#########################################################

import sys
sys.path.append('../main/mp/utils')
sys.path.append('../utils')

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;
"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,300))

"""
var x,y,z:integer; g: string; h,t: real;

function main(a: integer): string;
begin
end

procedure foo();
begin
end

procedure foo(a: string);
begin
end

procedure foo(a: string; b: Real);
begin
end

procedure foo(a,b,c: string);
begin
end

procedure foo(a,b,c: string; f,k,o: integer; g,h,t: Real);
begin
end

function foo(): String;
begin
end

function foo(a: string): String;
begin
end

function foo(a: string; b: Real): String;
begin
end

function foo(a,b,c: string; f,k,o: integer; g,h,t: Real): String;
begin
end

function foo(): String;
begin
continue;
end

function foo(): String;
begin
break;
end

function foo(): String;
begin
return;
end

function foo(): String;
begin
return ok();
end

function foo(): String;
begin
return ok(1);
end

function foo(): String;
begin
return ok(1,2);
end

function foo(): String;
begin
return ok(1,a);
end

function foo(): String;
begin
ok();
end

function foo(): String;
begin
ok(a);
end

function foo(): String;
begin
ok(a,1);
end

function foo(): String;
begin
ok(a,"1",True,falSe);
end

function foo(): String;
begin
ok("hi", foo());
end

function foo(): String;
begin
ok("hi", foo(bar(), 1));
end

function foo(): String;
begin
ok(a[1]);
end

function foo(): String;
begin
ok(1[1]);
end

function foo(): String;
begin
ok(foo()[1]);
end

function foo(): String;
begin
ok((foo())[1]);
end

function foo(): String;
begin
ok(a[b]);
end

function foo(): String;
begin
ok(a[foo()]);
end

function foo(): String;
begin
ok(4 and then 5);
end

function foo(): String;
begin
ok(4 or else 5);
end

function foo(): String;
begin
ok(4=5);
end

function foo(): String;
begin
ok(4>=5);
end

function foo(): String;
begin
ok(4+5);
end

function foo(): String;
begin
ok(4 div 5);
end

function foo(): String;
begin
ok(-4);
end

function foo(): String;
begin
ok(5 and then (-6 + "nt" * 3 or 5) div 7 >= a+b-(-f * not(-5*"abc")));
end

var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;
"""

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################