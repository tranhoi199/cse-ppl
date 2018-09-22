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
function foo(aa,b,c: string; f,k,o: integer; g,h,t: Real): String;
begin
end
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
"""

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################