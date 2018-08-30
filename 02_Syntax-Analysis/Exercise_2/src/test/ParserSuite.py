import unittest
from TestUtils import TestParser

def copy_template_test():
    def test_suc(self):
        input = """

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))


class ParserSuite(unittest.TestCase):
    def test_one_var(self):
        input = """
            int a;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    def test_one_var_with_space(self):
        input = """
            int   a ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_multiple_var(self):
        input = """
            int a,b,c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_multiple_var_with_space(self):
        input = """
            int     a,      b, c ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_var_complex(self):
        input = """
            int a, b, c;
            float a, b12, c9    ;
            int c; float F;     int k_123, GgYop_pq11, y__164_u1;
            float Hal4_1rte__aS126_4_26__yY3xT;
            int ttTy;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_var_miss_id(self):
        input = """
            int;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))