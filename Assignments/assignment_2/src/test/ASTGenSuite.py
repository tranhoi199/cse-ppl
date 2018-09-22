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
"""
        expect = str()
        self.assertTrue(TestAST.test(input,expect,300))


#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################