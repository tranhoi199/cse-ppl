import unittest
from TestUtils import TestExercise
from AST import *

class ExerciseSuite(unittest.TestCase):
    def test_1(self):
        input = Program([
            VarDecl(Id('a'),IntType),
            VarDecl(Id('c'),IntType),
            FuncDecl(
                Id('a'),
                [VarDecl(Id('c'),IntType)], 
                [VarDecl(Id('c'),IntType)],
                []
            )
        ])
        expect = [VarDecl(Id('a'),IntType), VarDecl(Id('c'),IntType)]
        self.assertTrue(TestExercise.test(input,expect,301))