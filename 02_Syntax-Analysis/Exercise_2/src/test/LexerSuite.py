import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        self.assertTrue(TestLexer.test(
            "a abc abc123 BC abcABC abc123A abc_abc abc_123__AB ABc123_",
            "a,abc,abc123,BC,abcABC,abc123A,abc_abc,abc_123__AB,ABc123_,<EOF>",101))