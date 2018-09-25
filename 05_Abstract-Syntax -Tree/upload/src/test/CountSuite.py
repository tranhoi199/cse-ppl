import unittest
from TestUtils import TestCount
from Count import *

class Count(unittest.TestCase):
    def test1(self):
        input = r"""
function foo(): integer;
begin end
"""
        expect = "15"
        self.assertTrue(TestCount.test(input,expect,401))

    def test2(self):
        input = r"""
procedure foo();
begin
g(3);
end
"""
        expect = "20"
        self.assertTrue(TestCount.test(input,expect,402))
    
    def test3(self):
        input = r"""
function foo(): integer;
begin
goo();
end
"""
        expect = "21"
        self.assertTrue(TestCount.test(input,expect,403))

    def test4(self):
        input = r"""
function foo():integer;
begin
g(32);
end
procedure g();
begin
println();
end
"""
        expect = "39"
        self.assertTrue(TestCount.test(input,expect,404))

    def test5(self):
        input = r"""
function foo():integer;
begin
g(32);
end
procedure g();
begin
println();
end
procedure g();
begin
println();
end
"""
        expect = "55"
        self.assertTrue(TestCount.test(input,expect,405))