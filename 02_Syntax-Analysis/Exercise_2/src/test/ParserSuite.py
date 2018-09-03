import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    ### Test Variable Successful
    def test_var_success(self):
        input = """
            int a;
            int     a   ;
            int a, b, c;
            int     a,      b, c ;
            float a, b12, c9    ;
            int c; float F;     int k_123, GgYop_pq11, y__164_u1;
            float Hal4_1rte__aS126_4_26__yY3xT;
            int ttTy;  int ny1lu     


            ;   float hly46e                             ;


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    ### Test Variable Error
    def test_var_miss_id(self):
        input = """
            int   ;
        """
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_var_miss_semi_one_var(self):
        input = """
            int a
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_var_miss_semi_multiple_vars(self):
        input = """
            int a, b,   c,      d
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_var_id_is_type(self):
        input = """
            int float, y, x;
        """
        expect = "Error on line 2 col 16: float"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_var_miss_complex(self):
        input = """
            int a, b, c;
            float x, y, z;
            int         float;
        """
        expect = "Error on line 4 col 24: float"
        self.assertTrue(TestParser.test(input,expect,206))



    ### Test Function Declaration Successful
    def test_func(self):
        input = """
            int foo() {}
            float goo(float a) { }
            int sum(int a, b) {}
            float min (float a, b; int x) { }

            float goo(
                int a, b, c, d; 
                int x, y, z, t;
                float gg, hh, pp) {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    ### Test Function Declaration Error
    def test_func_error_1(self):
        input = """
            int foo()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_func_error_2(self):
        input = """
            int foo() {
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_func_error_3(self):
        input = """
            int foo() }
        """
        expect = "Error on line 2 col 22: }"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_func_error_4(self):
        input = """
            int foo {}
        """
        expect = "Error on line 2 col 20: {"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_func_error_5(self):
        input = """
            int foo(int) {}
        """
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_func_error_6(self):
        input = """
            int foo(int x;) {}
        """
        expect = "Error on line 2 col 26: )"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_func_error_7(self):
        input = """
            int foo(float x,) {}
        """
        expect = "Error on line 2 col 28: )"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_func_error_8(self):
        input = """
            int foo(float x y) {}
        """
        expect = "Error on line 2 col 28: y"
        self.assertTrue(TestParser.test(input,expect,218))



    ### Test Statements in Function Successful
    def test_statement(self):
        input = """
            int main() {
                int a;
                float b;
                int a, b, c, d, e;
                float x, y, z, u, v;

                a = 1; 
                b = 2;
                c = a + b;
                x = 0.0001; y = 1e-9; z = 100.55e-4;

                u = x * y*1.0 + z - a/g + b * (c+a+12/g + x*(x+12-t*r*e/d*i/f/2.1)/(g+(h-g*4.3)));

                return 1;
                return 2.0;
                return 1e-8;
                return u;
                return u + 4;
                return (v);
                return x * y*1.0 + z - a/g + b * (c+a+12/g + x*(x+12-t*r*e/d*i/f/2.1)/(g+(h-g*4.3)));

                g = foo();
                h = min(1);
                t = max(1,2,3);
                y = sum(1.0, 2.3, 1e-5, 0.005e-7, 3e2);

                g = sum(u, v, 1, 2, h);
                t = sum(3, f, g(), t());
                h = sum( sum(sum(1, 2, 3), 4, foo(), max(1, 2, sum(1, g, y)), 34, u, p), y);
                g = sum(foo(), 6) + t * foo() - g*6/(h * goo(12, hoo(4, 3)) + yoo());

                foo();
                bar(1, 2, 3);
                foo(bar(), 12);
                foo(foo(foo()));

                return g + foo() * (g +y /4 * bar(foo(1, 2)));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    ### Test Statements in Function Error