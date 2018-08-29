import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("aCBbdc", "a,C,B,bdc,<EOF>", 102))
        self.assertTrue(TestLexer.test("aAsVN", "a,A,s,V,N,<EOF>", 103))
        
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    def test_real(self):
        '''test real numbers'''
        self.assertTrue(TestLexer.test(
            '1.5 10.005 0.00001 -10000.55500 -1000.00001', 
            '1.5,10.005,0.00001,-10000.55500,-1000.00001,<EOF>', 201))
        self.assertTrue(TestLexer.test(
            '1e5 1e-5 1000e-400 -300e-411 -4e122', 
            '1e5,1e-5,1000e-400,-300e-411,-4e122,<EOF>', 202))
        self.assertTrue(TestLexer.test(
            '1.0005e5 0.00001e-1110 -0.111e113 -1234.1234e-1234', 
            '1.0005e5,0.00001e-1110,-0.111e113,-1234.1234e-1234,<EOF>', 203))
        self.assertTrue(TestLexer.test(
            '123e-4.5 e3 e4.3 3.4e3.5', 
            '123e-4,.,5,e3,e4,.,3,3.4e3,.,5,<EOF>', 204))

    def test_strings(self):
        '''test strings'''
        self.assertTrue(TestLexer.test(
            "abc 'abc' 'abc 123' '  123  abc  ' '123'   ''123'  \'",
            "abc,'abc','abc 123','  123  abc  ','123','',123,'  ',<EOF>",
            301
        ))
        self.assertTrue(TestLexer.test(
            "var s = 'hello world!'; s += ' ''Python'' --'",
            "var,s,=,'hello world!',;,s,+,=,' ''Python'' --',<EOF>",
            302
        ))