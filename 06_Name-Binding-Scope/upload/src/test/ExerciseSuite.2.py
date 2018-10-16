import unittest
from TestUtils import TestExercise
from AST import *
from NameExercise import RedeclaredException

class ExerciseSuite(unittest.TestCase):
    def test_1(self):
        input = Program([
            VarDecl(Id('a'),IntType)
        ])
        expect = True
        self.assertTrue(TestExercise.test(input,expect,301))
    
    def test_2(self):
        input = Program([
            VarDecl(Id('a'),IntType),
            VarDecl(Id('b'),IntType)
        ])
        expect = True
        self.assertTrue(TestExercise.test(input,expect,302))
    
    def test_3(self):
        input = Program([
            VarDecl(Id('a'),IntType),
            VarDecl(Id('b'),IntType),
            VarDecl(Id('a'),IntType)
        ])
        expect = RedeclaredException('a')
        self.assertTrue(TestExercise.test(input,expect,303))
    
    def test_4(self):
        input = Program([
            VarDecl(Id('a'),IntType),
            VarDecl(Id('c'),IntType),
            VarDecl(Id('c'),IntType),
            FuncDecl(
                Id('a'),
                [VarDecl(Id('c'),IntType)], 
                [VarDecl(Id('c'),IntType)],
                []
            )
        ])
        expect = RedeclaredException('c')
        self.assertTrue(TestExercise.test(input,expect,304))