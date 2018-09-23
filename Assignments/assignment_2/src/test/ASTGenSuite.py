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
    
    def test_1(self):
        input = r"""
procedure foo();
begin
    with i: real;
    do begin
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect = str(
        )
        self.assertTrue(TestAST.test(input, expect, 301))

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################