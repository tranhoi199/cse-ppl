import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """var a: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))