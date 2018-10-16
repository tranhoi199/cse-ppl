import unittest
from TestUtils import TestAST
from AST import *
#from AntiAST import *

class ASTGenSuite(unittest.TestCase):

    def test_parser__1(self):
        input = """
procedure arrayTest(input, output: integer);
var m : array[1 .. 5] of integer;
begin
        m[1] := 1;
        m[2] := 2;
        m[3] := 3;
        m[4] := 4;
        m[5] := 5;

        write(m[1]);
        write(m[2]);
        write(m[3]);
        write(m[4]);
        write(m[5]);
end
"""
        expect = str(Program([FuncDecl(Id(r'arrayTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'm'),ArrayType(1,5,IntType()))],[Assign(ArrayCell(Id(r'm'),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(Id(r'm'),IntLiteral(2)),IntLiteral(2)),Assign(ArrayCell(Id(r'm'),IntLiteral(3)),IntLiteral(3)),Assign(ArrayCell(Id(r'm'),IntLiteral(4)),IntLiteral(4)),Assign(ArrayCell(Id(r'm'),IntLiteral(5)),IntLiteral(5)),CallStmt(Id(r'write'),[ArrayCell(Id(r'm'),IntLiteral(1))]),CallStmt(Id(r'write'),[ArrayCell(Id(r'm'),IntLiteral(2))]),CallStmt(Id(r'write'),[ArrayCell(Id(r'm'),IntLiteral(3))]),CallStmt(Id(r'write'),[ArrayCell(Id(r'm'),IntLiteral(4))]),CallStmt(Id(r'write'),[ArrayCell(Id(r'm'),IntLiteral(5))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 201))

    def test_parser__2(self):
        input = """
procedure arrayTest(input, output: integer);
var a, b : integer;
    x : array [1 .. 5] of real;
begin
read(a);
read(b);
x[a] := 6.783;
write(a,b,x[a]);
end
"""
        expect = str(Program([FuncDecl(Id(r'arrayTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'x'),ArrayType(1,5,FloatType()))],[CallStmt(Id(r'read'),[Id(r'a')]),CallStmt(Id(r'read'),[Id(r'b')]),Assign(ArrayCell(Id(r'x'),Id(r'a')),FloatLiteral(6.783)),CallStmt(Id(r'write'),[Id(r'a'),Id(r'b'),ArrayCell(Id(r'x'),Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 202))

    def test_parser__3(self):
        input = """
var a, b: integer; c: array [1 .. 10] of strinG;

procedure arrayTest(input, output: integer);
var
    i,j:integer;
begin
        i := 0;
        if i = 0 then
                write(0);
        else if i = 1 then
                write(1);
        else if i = 2 then
                write(2);
        else write (99);

        i := 1;
        if i = 0 then
                write(0);
        else if i = 1 then
                write(1);
        else if i = 2 then
                write(2);
        else write (99);

        i := 2;
        if i = 0 then
                write(0);
        else if i = 1 then
                write(1);
        else if i = 2 then
                write(2);
        else write (99);
end
"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,10,StringType())),FuncDecl(Id(r'arrayTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[Assign(Id(r'i'),IntLiteral(0)),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[CallStmt(Id(r'write'),[IntLiteral(0)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[CallStmt(Id(r'write'),[IntLiteral(1)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(2)),[CallStmt(Id(r'write'),[IntLiteral(2)])],[CallStmt(Id(r'write'),[IntLiteral(99)])])])]),Assign(Id(r'i'),IntLiteral(1)),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[CallStmt(Id(r'write'),[IntLiteral(0)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[CallStmt(Id(r'write'),[IntLiteral(1)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(2)),[CallStmt(Id(r'write'),[IntLiteral(2)])],[CallStmt(Id(r'write'),[IntLiteral(99)])])])]),Assign(Id(r'i'),IntLiteral(2)),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[CallStmt(Id(r'write'),[IntLiteral(0)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[CallStmt(Id(r'write'),[IntLiteral(1)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(2)),[CallStmt(Id(r'write'),[IntLiteral(2)])],[CallStmt(Id(r'write'),[IntLiteral(99)])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 203))


    def test_parser__6(self):
        input = """
        function fib(n:integer) :  integer;
var
        j, k : integer;
begin
        if n = 1 then
                fib := 1;
        else if n = 2 then
                fib := 1;
        else
                fib := fib(n-1) + fib(n-2);
end

function fibTest(input, output: integer): StrinG;   {Sample tvi code here}
var
        i, done: integer;
begin
        done := 0;
        while done = 0 do begin
                read(i);
                if i = 0 then
                        done := 1;
                else begin
                        write(i);
                        i := fib(i);
                        write(i);
                end    { else part }
        end    { while }
end
"""

        expect = str(Program([FuncDecl(Id(r'fib'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'fib'),IntLiteral(1))],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(2)),[Assign(Id(r'fib'),IntLiteral(1))],[Assign(Id(r'fib'),BinaryOp(r'+',CallExpr(Id(r'fib'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1))]),CallExpr(Id(r'fib'),[BinaryOp(r'-',Id(r'n'),IntLiteral(2))])))])])],IntType()),FuncDecl(Id(r'fibTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'done'),IntType())],[Assign(Id(r'done'),IntLiteral(0)),While(BinaryOp(r'=',Id(r'done'),IntLiteral(0)),[CallStmt(Id(r'read'),[Id(r'i')]),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[Assign(Id(r'done'),IntLiteral(1))],[CallStmt(Id(r'write'),[Id(r'i')]),Assign(Id(r'i'),CallExpr(Id(r'fib'),[Id(r'i')])),CallStmt(Id(r'write'),[Id(r'i')])])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 206))

    def test_parser__7(self):
        input = """
        function fib(n:integer) :  integer;
var
        j, k : integer;
begin
    a := 1;
    b := 2;
    c := a+b+two(a,b);
    write(c);
end

function fibTest(input, output: integer): StrinG;   {Sample tvi code here}
var
        i, done: integer;
begin
        done := 0;
        while done = 0 do begin
                read(i);
                if i = 0 then
                        done := 1;
                else begin
                        write(i);
                        i := fib(i);
                        write(i);
                end    { else part }
        end    { while }
end
"""
        expect = str(Program([FuncDecl(Id(r'fib'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),IntLiteral(2)),Assign(Id(r'c'),BinaryOp(r'+',BinaryOp(r'+',Id(r'a'),Id(r'b')),CallExpr(Id(r'two'),[Id(r'a'),Id(r'b')]))),CallStmt(Id(r'write'),[Id(r'c')])],IntType()),FuncDecl(Id(r'fibTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'done'),IntType())],[Assign(Id(r'done'),IntLiteral(0)),While(BinaryOp(r'=',Id(r'done'),IntLiteral(0)),[CallStmt(Id(r'read'),[Id(r'i')]),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[Assign(Id(r'done'),IntLiteral(1))],[CallStmt(Id(r'write'),[Id(r'i')]),Assign(Id(r'i'),CallExpr(Id(r'fib'),[Id(r'i')])),CallStmt(Id(r'write'),[Id(r'i')])])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 207))

    def test_parser__8(self):
        input = """
        function fib(n:integer) :  integer;
var
        j, k : integer;
begin
read (x,y);
if x>y then write (gcd(x, y));
end

function fibTest(input, output: integer): StrinG;   {Sample tvi code here}
var
        i, done: integer;
begin
if b= 0 then gcd := a;
else begin
    x := a;
    while (x >= b) do
    begin
        x := x - b;
    end //this is a line comment
    {gcd := gcd(b,x);}
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'fib'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[CallStmt(Id(r'read'),[Id(r'x'),Id(r'y')]),If(BinaryOp(r'>',Id(r'x'),Id(r'y')),[CallStmt(Id(r'write'),[CallExpr(Id(r'gcd'),[Id(r'x'),Id(r'y')])])],[])],IntType()),FuncDecl(Id(r'fibTest'),[VarDecl(Id(r'input'),IntType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'done'),IntType())],[If(BinaryOp(r'=',Id(r'b'),IntLiteral(0)),[Assign(Id(r'gcd'),Id(r'a'))],[Assign(Id(r'x'),Id(r'a')),While(BinaryOp(r'>=',Id(r'x'),Id(r'b')),[Assign(Id(r'x'),BinaryOp(r'-',Id(r'x'),Id(r'b')))])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 208))

    def test_parser__10(self):
        input = """
        procedure that();
var h,z : real;
begin
x := y;
this (h,z);
if (9) then
if 2 then bar();
    if tRue then aaaaa();
    else foo();
end
"""
        expect = str(Program([FuncDecl(Id(r'that'),[],[VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'x'),Id(r'y')),CallStmt(Id(r'this'),[Id(r'h'),Id(r'z')]),If(IntLiteral(9),[If(IntLiteral(2),[CallStmt(Id(r'bar'),[])],[])],[]),If(BooleanLiteral(True),[CallStmt(Id(r'aaaaa'),[])],[CallStmt(Id(r'foo'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 210))

    def test_parser__11(self):
        input = """
function foo(): real;
var x, y: stRing;
begin
sum := 0;
numbers[1] := 3;
numbers[2] := 7;
numbers[3] := 2;
numbers[4] := 4;
numbers[5] := .5e-121202002;

for i := 1 to 5.e-12 do
    sum := sum + numbers[1];
writeln("sum = ", sum);
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),StringType()),VarDecl(Id(r'y'),StringType())],[Assign(Id(r'sum'),IntLiteral(0)),Assign(ArrayCell(Id(r'numbers'),IntLiteral(1)),IntLiteral(3)),Assign(ArrayCell(Id(r'numbers'),IntLiteral(2)),IntLiteral(7)),Assign(ArrayCell(Id(r'numbers'),IntLiteral(3)),IntLiteral(2)),Assign(ArrayCell(Id(r'numbers'),IntLiteral(4)),IntLiteral(4)),Assign(ArrayCell(Id(r'numbers'),IntLiteral(5)),FloatLiteral(0.0)),For(Id(r'i'),IntLiteral(1),FloatLiteral(5e-12),True,[Assign(Id(r'sum'),BinaryOp(r'+',Id(r'sum'),ArrayCell(Id(r'numbers'),IntLiteral(1))))]),CallStmt(Id(r'writeln'),[StringLiteral(r'sum = '),Id(r'sum')])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 211))

    def test_parser__12(self):
        input = """
        procedure foo();
begin

Write("Enger a number:");
readln(no);
if (no > 0) then
writeln("You enter Positive Number");
else
    if (no < 0) then
    writeln("You enter Negative number");
    else
    if (no = 0) then
    writeln("You enter Zero");
readln();
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'Write'),[StringLiteral(r'Enger a number:')]),CallStmt(Id(r'readln'),[Id(r'no')]),If(BinaryOp(r'>',Id(r'no'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'You enter Positive Number')])],[If(BinaryOp(r'<',Id(r'no'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'You enter Negative number')])],[If(BinaryOp(r'=',Id(r'no'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'You enter Zero')])],[])])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 212))

    def test_parser__13(self):
        input = """
        function fact(n: integer): real;
begin
    if (n = 0) then
        fact := 1;
    else
        fact := n * fact(n div 1);
end

procedure main(N: real);
BEGIN
    log(1000000000000000000*10-12 + -100 * 200 - 10 >= 12 - 10);
    {123 + 456
    // kljasdfjksdfj
    }
ENd
"""
        expect = str(Program([FuncDecl(Id(r'fact'),[VarDecl(Id(r'n'),IntType())],[],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(0)),[Assign(Id(r'fact'),IntLiteral(1))],[Assign(Id(r'fact'),BinaryOp(r'*',Id(r'n'),CallExpr(Id(r'fact'),[BinaryOp(r'div',Id(r'n'),IntLiteral(1))])))])],FloatType()),FuncDecl(Id(r'main'),[VarDecl(Id(r'N'),FloatType())],[],[CallStmt(Id(r'log'),[BinaryOp(r'>=',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'*',IntLiteral(1000000000000000000),IntLiteral(10)),IntLiteral(12)),BinaryOp(r'*',UnaryOp(r'-',IntLiteral(100)),IntLiteral(200))),IntLiteral(10)),BinaryOp(r'-',IntLiteral(12),IntLiteral(10)))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 213))

    def test_parser__14(self):
        input = """
        procedure foo();
var x, y: integer;
begin
x := y*12 div 100 mod 10;
write("Please type the first char: ");
readln(c1);
write("Please type the second one: ");
readln(c2);
if (upcase(c1)=lowercase(c1 div 12)) then
writeln("The first char is not a letter");
else if (upcase(c2)=lowercase(c2)) then
writeln("The second char is not a letter");
else if (upcase(c1)>upcase(c2)) then
writeln("The first letter is [",c2,"] while the second is [",c1,"].");
else
writeln("The first letter is [",c1,"] while the second is [",c2,"].");
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(Id(r'x'),BinaryOp(r'mod',BinaryOp(r'div',BinaryOp(r'*',Id(r'y'),IntLiteral(12)),IntLiteral(100)),IntLiteral(10))),CallStmt(Id(r'write'),[StringLiteral(r'Please type the first char: ')]),CallStmt(Id(r'readln'),[Id(r'c1')]),CallStmt(Id(r'write'),[StringLiteral(r'Please type the second one: ')]),CallStmt(Id(r'readln'),[Id(r'c2')]),If(BinaryOp(r'=',CallExpr(Id(r'upcase'),[Id(r'c1')]),CallExpr(Id(r'lowercase'),[BinaryOp(r'div',Id(r'c1'),IntLiteral(12))])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The first char is not a letter')])],[If(BinaryOp(r'=',CallExpr(Id(r'upcase'),[Id(r'c2')]),CallExpr(Id(r'lowercase'),[Id(r'c2')])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The second char is not a letter')])],[If(BinaryOp(r'>',CallExpr(Id(r'upcase'),[Id(r'c1')]),CallExpr(Id(r'upcase'),[Id(r'c2')])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The first letter is ['),Id(r'c2'),StringLiteral(r'] while the second is ['),Id(r'c1'),StringLiteral(r'].')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'The first letter is ['),Id(r'c1'),StringLiteral(r'] while the second is ['),Id(r'c2'),StringLiteral(r'].')])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 214))

    def test_parser__15(self):
        input = """
            procedurE foo (b : real) ;
    var
    a : array [2 .. 3] of integer;
    b: string;
    e: real;
    f: boolean;
    begin
    while (a=4   ) do
        with a,b,c:integer;b: array [1 .. 3] of StRing; do
            while(a=4) do
                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                    e:=4;
    end    procedurE foo (b : real) ;
    var
    a : array [2 .. 3] of integer;
    b: string;
    e: real;
    f: boolean;
    begin
    while (a=4   ) do
        with a,b,c:integer;b: array [1 .. 3] of StRing; do
            while(a=4) do
                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                    e:=4;
    end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(4))])])])])],VoidType()),FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(4))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 215))

    def test_parser__16(self):
        input = """
var x, y: integer;

procedure foo();
var x, y: real;
begin
    while 1 do
    begin
        if 1 > 10 - 15 mod 17 div 25 then
            break;
        else continue;
    end
    foo();
end

function bar(c: array [1 .. 1000] of real): integer;
var ahijij: real;
begin
    write("Hello world!", 1.23e12);
end
"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[While(IntLiteral(1),[If(BinaryOp(r'>',IntLiteral(1),BinaryOp(r'-',IntLiteral(10),BinaryOp(r'div',BinaryOp(r'mod',IntLiteral(15),IntLiteral(17)),IntLiteral(25)))),[Break()],[Continue()])]),CallStmt(Id(r'foo'),[])],VoidType()),FuncDecl(Id(r'bar'),[VarDecl(Id(r'c'),ArrayType(1,1000,FloatType()))],[VarDecl(Id(r'ahijij'),FloatType())],[CallStmt(Id(r'write'),[StringLiteral(r'Hello world!'),FloatLiteral(1230000000000.0)])],IntType())]))
        self.assertTrue(TestAST.test(input, expect, 216))

    def test_parser__17(self):
        input = """
        var ahihih: StRing;

procedure main();
var
A,B,C,D: integer;

begin
write("A = ");
readln(A);
if (A=0) then
begin
    writeln("Not a quadratic equation.");
    halt();
end
write("B = ");
readln(B);
write("C = ");
readln(C);
D := B*B-4*A*C;
if (D=0) then
begin
    writeln("x = ",-B/2.0/A);
    halt();
end
if (D>0) then
begin
    writeln("x1 = ",(-B+Sqrt(D))/2.0/A);
    writeln("x2 = ",(-B-Sqrt(D))/2.0/A);
end
else
begin
    writeln("x1 = (",-B/2.0/A,",",Sqrt(-D)/2.0/A,")");
    writeln("x2 = (",-B/2.0/A,",",-Sqrt(-D)/2.0/A,")");
end
end
"""
        expect = str(Program([VarDecl(Id(r'ahihih'),StringType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),VarDecl(Id(r'C'),IntType()),VarDecl(Id(r'D'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r'A = ')]),CallStmt(Id(r'readln'),[Id(r'A')]),If(BinaryOp(r'=',Id(r'A'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Not a quadratic equation.')]),CallStmt(Id(r'halt'),[])],[]),CallStmt(Id(r'write'),[StringLiteral(r'B = ')]),CallStmt(Id(r'readln'),[Id(r'B')]),CallStmt(Id(r'write'),[StringLiteral(r'C = ')]),CallStmt(Id(r'readln'),[Id(r'C')]),Assign(Id(r'D'),BinaryOp(r'-',BinaryOp(r'*',Id(r'B'),Id(r'B')),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'A')),Id(r'C')))),If(BinaryOp(r'=',Id(r'D'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'x = '),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A'))]),CallStmt(Id(r'halt'),[])],[]),If(BinaryOp(r'>',Id(r'D'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'x1 = '),BinaryOp(r'/',BinaryOp(r'/',BinaryOp(r'+',UnaryOp(r'-',Id(r'B')),CallExpr(Id(r'Sqrt'),[Id(r'D')])),FloatLiteral(2.0)),Id(r'A'))]),CallStmt(Id(r'writeln'),[StringLiteral(r'x2 = '),BinaryOp(r'/',BinaryOp(r'/',BinaryOp(r'-',UnaryOp(r'-',Id(r'B')),CallExpr(Id(r'Sqrt'),[Id(r'D')])),FloatLiteral(2.0)),Id(r'A'))])],[CallStmt(Id(r'writeln'),[StringLiteral(r'x1 = ('),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A')),StringLiteral(r','),BinaryOp(r'/',BinaryOp(r'/',CallExpr(Id(r'Sqrt'),[UnaryOp(r'-',Id(r'D'))]),FloatLiteral(2.0)),Id(r'A')),StringLiteral(r')')]),CallStmt(Id(r'writeln'),[StringLiteral(r'x2 = ('),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A')),StringLiteral(r','),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',CallExpr(Id(r'Sqrt'),[UnaryOp(r'-',Id(r'D'))])),FloatLiteral(2.0)),Id(r'A')),StringLiteral(r')')])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 217))

    def test_parser__19(self):
        input = """
        procedure DrawBorder(title: String);
var
x, y: Integer;
begin
GotoXY(BORDER_START_X, 1);
Write(Title);

//Draw the top + bottom borders
for x := BORDER_START_X to BORDER_START_X + BORDER_WIDTH do
begin
    //Top
    DrawAt(x, BORDER_START_Y, BORDER_CHARACTER, White);
    DrawAt(x, BORDER_START_Y + BORDER_HEIGHT, BORDER_CHARACTER, White);
end

for y := BORDER_START_Y to BORDER_START_Y + BORDER_HEIGHT do
begin
    DrawAt(BORDER_START_X, y, BORDER_CHARACTER, White);
    DrawAt(BORDER_START_X + BORDER_WIDTH, y, BORDER_CHARACTER, White);
end
end

function GetNewLocation(originalLocation, change, lowBoundary, highBoundary: Integer): Integer;
var
newLocation: Integer;
begin
newLocation := originalLocation + change;
if (newLocation <= lowBoundary) or (newLocation >= highBoundary) then
begin
    //movement goes off screen... dont move
    result := originalLocation;
end
else
begin
    result := newLocation;
end
end
"""
        expect = str(Program([FuncDecl(Id(r'DrawBorder'),[VarDecl(Id(r'title'),StringType())],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[CallStmt(Id(r'GotoXY'),[Id(r'BORDER_START_X'),IntLiteral(1)]),CallStmt(Id(r'Write'),[Id(r'Title')]),For(Id(r'x'),Id(r'BORDER_START_X'),BinaryOp(r'+',Id(r'BORDER_START_X'),Id(r'BORDER_WIDTH')),True,[CallStmt(Id(r'DrawAt'),[Id(r'x'),Id(r'BORDER_START_Y'),Id(r'BORDER_CHARACTER'),Id(r'White')]),CallStmt(Id(r'DrawAt'),[Id(r'x'),BinaryOp(r'+',Id(r'BORDER_START_Y'),Id(r'BORDER_HEIGHT')),Id(r'BORDER_CHARACTER'),Id(r'White')])]),For(Id(r'y'),Id(r'BORDER_START_Y'),BinaryOp(r'+',Id(r'BORDER_START_Y'),Id(r'BORDER_HEIGHT')),True,[CallStmt(Id(r'DrawAt'),[Id(r'BORDER_START_X'),Id(r'y'),Id(r'BORDER_CHARACTER'),Id(r'White')]),CallStmt(Id(r'DrawAt'),[BinaryOp(r'+',Id(r'BORDER_START_X'),Id(r'BORDER_WIDTH')),Id(r'y'),Id(r'BORDER_CHARACTER'),Id(r'White')])])],VoidType()),FuncDecl(Id(r'GetNewLocation'),[VarDecl(Id(r'originalLocation'),IntType()),VarDecl(Id(r'change'),IntType()),VarDecl(Id(r'lowBoundary'),IntType()),VarDecl(Id(r'highBoundary'),IntType())],[VarDecl(Id(r'newLocation'),IntType())],[Assign(Id(r'newLocation'),BinaryOp(r'+',Id(r'originalLocation'),Id(r'change'))),If(BinaryOp(r'or',BinaryOp(r'<=',Id(r'newLocation'),Id(r'lowBoundary')),BinaryOp(r'>=',Id(r'newLocation'),Id(r'highBoundary'))),[Assign(Id(r'result'),Id(r'originalLocation'))],[Assign(Id(r'result'),Id(r'newLocation'))])],IntType())]))
        self.assertTrue(TestAST.test(input, expect, 219))

    def test_parser__20(self):
        input = """
    procedure UpdateLocation( location, change: Integer; lowBoundary, highBoundary: Integer);
begin
location := location + change;

if AtEdge(location, lowBoundary, highBoundary) then
begin
    change := -change;
end
end

//Draws and moves the ball around the screen until a key is pressed.
//
//Side Effects:
// * Draws to console (in called routines)
procedure DoBouncingBall();
var
x, y, dx, dy: Integer;
begin
x := BORDER_START_X + 1;
y := BORDER_START_Y + 1;
dx := 1;
dy := 1;

while KeyPressed() do
begin
    DrawAt(x, y, BALL_CHARACTER, Yellow);
    Delay(100);
    DrawAt(x, y, " ", White);

    UpdateLocation(x, dx, BORDER_START_X, BORDER_START_X + BORDER_WIDTH);
    UpdateLocation(y, dy, BORDER_START_Y, BORDER_START_Y + BORDER_HEIGHT);
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'UpdateLocation'),[VarDecl(Id(r'location'),IntType()),VarDecl(Id(r'change'),IntType()),VarDecl(Id(r'lowBoundary'),IntType()),VarDecl(Id(r'highBoundary'),IntType())],[],[Assign(Id(r'location'),BinaryOp(r'+',Id(r'location'),Id(r'change'))),If(CallExpr(Id(r'AtEdge'),[Id(r'location'),Id(r'lowBoundary'),Id(r'highBoundary')]),[Assign(Id(r'change'),UnaryOp(r'-',Id(r'change')))],[])],VoidType()),FuncDecl(Id(r'DoBouncingBall'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'dx'),IntType()),VarDecl(Id(r'dy'),IntType())],[Assign(Id(r'x'),BinaryOp(r'+',Id(r'BORDER_START_X'),IntLiteral(1))),Assign(Id(r'y'),BinaryOp(r'+',Id(r'BORDER_START_Y'),IntLiteral(1))),Assign(Id(r'dx'),IntLiteral(1)),Assign(Id(r'dy'),IntLiteral(1)),While(CallExpr(Id(r'KeyPressed'),[]),[CallStmt(Id(r'DrawAt'),[Id(r'x'),Id(r'y'),Id(r'BALL_CHARACTER'),Id(r'Yellow')]),CallStmt(Id(r'Delay'),[IntLiteral(100)]),CallStmt(Id(r'DrawAt'),[Id(r'x'),Id(r'y'),StringLiteral(r' '),Id(r'White')]),CallStmt(Id(r'UpdateLocation'),[Id(r'x'),Id(r'dx'),Id(r'BORDER_START_X'),BinaryOp(r'+',Id(r'BORDER_START_X'),Id(r'BORDER_WIDTH'))]),CallStmt(Id(r'UpdateLocation'),[Id(r'y'),Id(r'dy'),Id(r'BORDER_START_Y'),BinaryOp(r'+',Id(r'BORDER_START_Y'),Id(r'BORDER_HEIGHT'))])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 220))

    def test_parser__21(self):
        input = """
        procedure Main();
begin
CursorOff();

DrawBorder("Bouncing Ball");
DoBouncingBall();

CursorOn();
end
"""
        expect = str(Program([FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'CursorOff'),[]),CallStmt(Id(r'DrawBorder'),[StringLiteral(r'Bouncing Ball')]),CallStmt(Id(r'DoBouncingBall'),[]),CallStmt(Id(r'CursorOn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 221))

    def test_parser__22(self):
        input = """
        procedure Test();
VAR
x : REAL;
i : INTEGER;
j : INTEGER;
BEGIN
    x := 12.449;
    i := 10;
    j := -300;
    WRITE("This is some text");
    WRITELN("Unformatted integer ",i);
    WRITELN("Unformatted integer computation ",i*i);
    WRITELN("formatted integer",i/4);
    WRITELN("formatted integer",j/4);
    WRITELN("Unformatted real ",x);
    WRITE("Formatted real");
    WRITE(x/8/2);
    WRITELN("all in one line");
END
"""
        expect = str(Program([FuncDecl(Id(r'Test'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[Assign(Id(r'x'),FloatLiteral(12.449)),Assign(Id(r'i'),IntLiteral(10)),Assign(Id(r'j'),UnaryOp(r'-',IntLiteral(300))),CallStmt(Id(r'WRITE'),[StringLiteral(r'This is some text')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Unformatted integer '),Id(r'i')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Unformatted integer computation '),BinaryOp(r'*',Id(r'i'),Id(r'i'))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'formatted integer'),BinaryOp(r'/',Id(r'i'),IntLiteral(4))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'formatted integer'),BinaryOp(r'/',Id(r'j'),IntLiteral(4))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Unformatted real '),Id(r'x')]),CallStmt(Id(r'WRITE'),[StringLiteral(r'Formatted real')]),CallStmt(Id(r'WRITE'),[BinaryOp(r'/',BinaryOp(r'/',Id(r'x'),IntLiteral(8)),IntLiteral(2))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'all in one line')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 222))

    def test_parser__23(self):
        input = """

VAR
radius: REAL;

FUNCTION CircleArea(r : REAL): REAL;
BEGIN
    CircleArea := 3.1415 * r * r;
END

procedure main();
var x, y : string;
    a: array [1 .. 1000000] of integer;
BEGIN
    WRITE("Area of circle with radius 2.0: ");
    WRITELN(CircleArea(2.0)/6/1);
    WRITE("Area of circle with radius 5.0: ");
    WRITELN(CircleArea(5.0)/6/1);
    WRITE("Enter your own radius: ");
    READLN(radius);
    WRITE("Area of circle with radius ", radius/3/1,": ");
    WRITELN(CircleArea(radius));   { ugly - formatting missing for real }
    radius := 5.0;
    radius := CircleArea(radius);
    WRITELN(radius);               { can you guess the output ? }
END
"""
        expect = str(Program([VarDecl(Id(r'radius'),FloatType()),FuncDecl(Id(r'CircleArea'),[VarDecl(Id(r'r'),FloatType())],[],[Assign(Id(r'CircleArea'),BinaryOp(r'*',BinaryOp(r'*',FloatLiteral(3.1415),Id(r'r')),Id(r'r')))],FloatType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'x'),StringType()),VarDecl(Id(r'y'),StringType()),VarDecl(Id(r'a'),ArrayType(1,1000000,IntType()))],[CallStmt(Id(r'WRITE'),[StringLiteral(r'Area of circle with radius 2.0: ')]),CallStmt(Id(r'WRITELN'),[BinaryOp(r'/',BinaryOp(r'/',CallExpr(Id(r'CircleArea'),[FloatLiteral(2.0)]),IntLiteral(6)),IntLiteral(1))]),CallStmt(Id(r'WRITE'),[StringLiteral(r'Area of circle with radius 5.0: ')]),CallStmt(Id(r'WRITELN'),[BinaryOp(r'/',BinaryOp(r'/',CallExpr(Id(r'CircleArea'),[FloatLiteral(5.0)]),IntLiteral(6)),IntLiteral(1))]),CallStmt(Id(r'WRITE'),[StringLiteral(r'Enter your own radius: ')]),CallStmt(Id(r'READLN'),[Id(r'radius')]),CallStmt(Id(r'WRITE'),[StringLiteral(r'Area of circle with radius '),BinaryOp(r'/',BinaryOp(r'/',Id(r'radius'),IntLiteral(3)),IntLiteral(1)),StringLiteral(r': ')]),CallStmt(Id(r'WRITELN'),[CallExpr(Id(r'CircleArea'),[Id(r'radius')])]),Assign(Id(r'radius'),FloatLiteral(5.0)),Assign(Id(r'radius'),CallExpr(Id(r'CircleArea'),[Id(r'radius')])),CallStmt(Id(r'WRITELN'),[Id(r'radius')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 223))

    def test_parser__24(self):
        input = """
        {****************************************}
PROCEDURE DoTheConversion();
{ This procedure converts the number     }
{ contained in UserInput to the degree   }
{ according to the user"s menu choice.   }
BEGIN
    IF (UserChoice = "a") THEN
        answer := ToFahrenheit(UserInput);
    IF (UserChoice = "b") THEN
        answer := ToCelcius(UserInput);
end
{****************************************}
PROCEDURE DisplayTheAnswer();
{ This procedure displays the answer in  }
{ a nice numerical format. It switches   }
{ the title of the table displaying the  }
{ answer depending on the user"s menu    }
{ choice.                                }
BEGIN
    WRITELN();
    WRITELN("        Degree");
    IF (UserChoice = "a") THEN
        WRITELN("Celcius    | Fahrenheit");
    IF (UserChoice = "b") THEN
        WRITELN("FahrenHeit |   Celcius");
    WRITELN("------------------------");
    WRITE(UserInput/8/2);
    WRITE("   |   ");
    WRITE(Answer/8/2);
    WRITELN();
    WRITELN();
end
"""
        expect = str(Program([FuncDecl(Id(r'DoTheConversion'),[],[],[If(BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'a')),[Assign(Id(r'answer'),CallExpr(Id(r'ToFahrenheit'),[Id(r'UserInput')]))],[]),If(BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'b')),[Assign(Id(r'answer'),CallExpr(Id(r'ToCelcius'),[Id(r'UserInput')]))],[])],VoidType()),FuncDecl(Id(r'DisplayTheAnswer'),[],[],[CallStmt(Id(r'WRITELN'),[]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'        Degree')]),If(BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'a')),[CallStmt(Id(r'WRITELN'),[StringLiteral(r'Celcius    | Fahrenheit')])],[]),If(BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'b')),[CallStmt(Id(r'WRITELN'),[StringLiteral(r'FahrenHeit |   Celcius')])],[]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'------------------------')]),CallStmt(Id(r'WRITE'),[BinaryOp(r'/',BinaryOp(r'/',Id(r'UserInput'),IntLiteral(8)),IntLiteral(2))]),CallStmt(Id(r'WRITE'),[StringLiteral(r'   |   ')]),CallStmt(Id(r'WRITE'),[BinaryOp(r'/',BinaryOp(r'/',Id(r'Answer'),IntLiteral(8)),IntLiteral(2))]),CallStmt(Id(r'WRITELN'),[]),CallStmt(Id(r'WRITELN'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 224))

    def test_parser__25(self):
        input = """
        procedure main();
BEGIN
UserChoice := "q";
WHILE (UserChoice <> "x") DO
    BEGIN
        ShowTheMenu();
        GetUserChoice();
        IF (UserChoice = "a") OR
            (UserChoice = "b") THEN
        BEGIN
            GetNumberToConvert();
            DoTheConversion();
            DisplayTheAnswer();
            Wait();
        END
    END

    with x: integer; y: array [1 .. 12] of real; do
        BEGIN
        foo();
        with x: integer; do foo[2] := foo + foo;
        end
END
"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'UserChoice'),StringLiteral(r'q')),While(BinaryOp(r'<>',Id(r'UserChoice'),StringLiteral(r'x')),[CallStmt(Id(r'ShowTheMenu'),[]),CallStmt(Id(r'GetUserChoice'),[]),If(BinaryOp(r'OR',BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'a')),BinaryOp(r'=',Id(r'UserChoice'),StringLiteral(r'b'))),[CallStmt(Id(r'GetNumberToConvert'),[]),CallStmt(Id(r'DoTheConversion'),[]),CallStmt(Id(r'DisplayTheAnswer'),[]),CallStmt(Id(r'Wait'),[])],[])]),With([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),ArrayType(1,12,FloatType()))],[CallStmt(Id(r'foo'),[]),With([VarDecl(Id(r'x'),IntType())],[Assign(ArrayCell(Id(r'foo'),IntLiteral(2)),BinaryOp(r'+',Id(r'foo'),Id(r'foo')))])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 225))

    def test_parser__26(self):
        input = """
        Function Weird(A : Integer) : Integer;

Var
S : Integer;

Begin
S := A/2;

If S < 10 Then
Weird := 1;

S := S + 9;

If S >= 10 Then
Weird := 0;

Weird := 2;
End
"""
        expect = str(Program([FuncDecl(Id(r'Weird'),[VarDecl(Id(r'A'),IntType())],[VarDecl(Id(r'S'),IntType())],[Assign(Id(r'S'),BinaryOp(r'/',Id(r'A'),IntLiteral(2))),If(BinaryOp(r'<',Id(r'S'),IntLiteral(10)),[Assign(Id(r'Weird'),IntLiteral(1))],[]),Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),IntLiteral(9))),If(BinaryOp(r'>=',Id(r'S'),IntLiteral(10)),[Assign(Id(r'Weird'),IntLiteral(0))],[]),Assign(Id(r'Weird'),IntLiteral(2))],IntType())]))
        self.assertTrue(TestAST.test(input, expect, 226))

    def test_parser__27(self):
        input = """

function tarea(b1,b2,h:real):real;
begin
    tarea:=(b1+b2)*(h/2);
end

{Gauss Function, to be integrated}
function gauss(x:real):real;
begin
    gauss:=(exp(-(x*x)/2))/sqrt(2*pi);
end

procedure main();
var t,p0,epsilon,IP,IA:real;
    isNeg:boolean;
    i:integer;
    n_data:integer;

    begin
    writeln("Tabulate Gauss Function");
    writeln("Enter t to compute P(|X <= t|) ");

    { setting boolean to track (t<0) }
    read(t);
    if t < 0 then
    begin
        t:=-t;
        isNeg:=true;
    end
    else isNeg:=false;

    writeln("Enter integration step");
    read(p0);

    writeln("Enter accuracy");
    read(epsilon);

    p0:=p0*2;
    IA:=0;

    while (abs(IP-IA) < epsilon) do
    begin
        IP:=IA;
        p0:=p0/2;
        writeln("Current integration step ",p0);
        n_data:=trunc((t/p0))+1;
            if ((0+n_data*p0))> t then n_data:=n_data-1;
        IA:=0;
            for i:=0 to n_data-1 do
                IA:=IA+tarea(gauss((0+i*p0)),gauss(0+(i+1)*p0),p0);
        IA:=IA+0.5;
            if isNeg then IA:=1-IA;
    end

    writeln("Result: ",IA/5);
end
"""
        expect = str(Program([FuncDecl(Id(r'tarea'),[VarDecl(Id(r'b1'),FloatType()),VarDecl(Id(r'b2'),FloatType()),VarDecl(Id(r'h'),FloatType())],[],[Assign(Id(r'tarea'),BinaryOp(r'*',BinaryOp(r'+',Id(r'b1'),Id(r'b2')),BinaryOp(r'/',Id(r'h'),IntLiteral(2))))],FloatType()),FuncDecl(Id(r'gauss'),[VarDecl(Id(r'x'),FloatType())],[],[Assign(Id(r'gauss'),BinaryOp(r'/',CallExpr(Id(r'exp'),[BinaryOp(r'/',UnaryOp(r'-',BinaryOp(r'*',Id(r'x'),Id(r'x'))),IntLiteral(2))]),CallExpr(Id(r'sqrt'),[BinaryOp(r'*',IntLiteral(2),Id(r'pi'))])))],FloatType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'p0'),FloatType()),VarDecl(Id(r'epsilon'),FloatType()),VarDecl(Id(r'IP'),FloatType()),VarDecl(Id(r'IA'),FloatType()),VarDecl(Id(r'isNeg'),BoolType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'n_data'),IntType())],[CallStmt(Id(r'writeln'),[StringLiteral(r'Tabulate Gauss Function')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Enter t to compute P(|X <= t|) ')]),CallStmt(Id(r'read'),[Id(r't')]),If(BinaryOp(r'<',Id(r't'),IntLiteral(0)),[Assign(Id(r't'),UnaryOp(r'-',Id(r't'))),Assign(Id(r'isNeg'),BooleanLiteral(True))],[Assign(Id(r'isNeg'),BooleanLiteral(False))]),CallStmt(Id(r'writeln'),[StringLiteral(r'Enter integration step')]),CallStmt(Id(r'read'),[Id(r'p0')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Enter accuracy')]),CallStmt(Id(r'read'),[Id(r'epsilon')]),Assign(Id(r'p0'),BinaryOp(r'*',Id(r'p0'),IntLiteral(2))),Assign(Id(r'IA'),IntLiteral(0)),While(BinaryOp(r'<',CallExpr(Id(r'abs'),[BinaryOp(r'-',Id(r'IP'),Id(r'IA'))]),Id(r'epsilon')),[Assign(Id(r'IP'),Id(r'IA')),Assign(Id(r'p0'),BinaryOp(r'/',Id(r'p0'),IntLiteral(2))),CallStmt(Id(r'writeln'),[StringLiteral(r'Current integration step '),Id(r'p0')]),Assign(Id(r'n_data'),BinaryOp(r'+',CallExpr(Id(r'trunc'),[BinaryOp(r'/',Id(r't'),Id(r'p0'))]),IntLiteral(1))),If(BinaryOp(r'>',BinaryOp(r'+',IntLiteral(0),BinaryOp(r'*',Id(r'n_data'),Id(r'p0'))),Id(r't')),[Assign(Id(r'n_data'),BinaryOp(r'-',Id(r'n_data'),IntLiteral(1)))],[]),Assign(Id(r'IA'),IntLiteral(0)),For(Id(r'i'),IntLiteral(0),BinaryOp(r'-',Id(r'n_data'),IntLiteral(1)),True,[Assign(Id(r'IA'),BinaryOp(r'+',Id(r'IA'),CallExpr(Id(r'tarea'),[CallExpr(Id(r'gauss'),[BinaryOp(r'+',IntLiteral(0),BinaryOp(r'*',Id(r'i'),Id(r'p0')))]),CallExpr(Id(r'gauss'),[BinaryOp(r'+',IntLiteral(0),BinaryOp(r'*',BinaryOp(r'+',Id(r'i'),IntLiteral(1)),Id(r'p0')))]),Id(r'p0')])))]),Assign(Id(r'IA'),BinaryOp(r'+',Id(r'IA'),FloatLiteral(0.5))),If(Id(r'isNeg'),[Assign(Id(r'IA'),BinaryOp(r'-',IntLiteral(1),Id(r'IA')))],[])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Result: '),BinaryOp(r'/',Id(r'IA'),IntLiteral(5))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 227))

    def test_parser__28(self):
        input = """
        function Egcd(a,b:integer):integer;

begin
    if (a=0) or (b=0) then Epgcd:=0;
    else
        while (a<>b) do
            if (a>b) then a:=a-b; else b:=b-a;
    Egcd:=a;
end
"""
        expect = str(Program([FuncDecl(Id(r'Egcd'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[If(BinaryOp(r'or',BinaryOp(r'=',Id(r'a'),IntLiteral(0)),BinaryOp(r'=',Id(r'b'),IntLiteral(0))),[Assign(Id(r'Epgcd'),IntLiteral(0))],[While(BinaryOp(r'<>',Id(r'a'),Id(r'b')),[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),BinaryOp(r'-',Id(r'a'),Id(r'b')))],[Assign(Id(r'b'),BinaryOp(r'-',Id(r'b'),Id(r'a')))])])]),Assign(Id(r'Egcd'),Id(r'a'))],IntType())]))
        self.assertTrue(TestAST.test(input, expect, 228))

    def test_parser__29(self):
        input = """
        function isPrime(n:integer):boolean;
var i:integer;
    isDiv:boolean;
begin
    if (n=1) then isPrime:=false;
    else
        begin
        isDiv:=false;
            for i:=2 to trunc(sqrt(n)) do
            if ((n mod i)=0) then isDiv:=true;
            if (isDiv) then isPrime:=false;
            else isPrime:=true;
        end
end
"""
        expect = str(Program([FuncDecl(Id(r'isPrime'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'isDiv'),BoolType())],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'isPrime'),BooleanLiteral(False))],[Assign(Id(r'isDiv'),BooleanLiteral(False)),For(Id(r'i'),IntLiteral(2),CallExpr(Id(r'trunc'),[CallExpr(Id(r'sqrt'),[Id(r'n')])]),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'n'),Id(r'i')),IntLiteral(0)),[Assign(Id(r'isDiv'),BooleanLiteral(True))],[])]),If(Id(r'isDiv'),[Assign(Id(r'isPrime'),BooleanLiteral(False))],[Assign(Id(r'isPrime'),BooleanLiteral(True))])])],BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 229))

    def test_parser__30(self):
        input = """
        function foo(): integer;
var n,a,b,i:integer;
begin
    writeln("Enter n");
    read(n);
    if ((n mod 2)<>0) then writeln(n, "is not a prime number!");
    else
        for i:=1 to (n div 2) do  begin
        a:=i;  b:=n-i;
        if isPrime(a) and isPrime(b) then writeln(n," = ",a," + ",b);
        end
end

function bar(): real;
begin
    log("...");
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'writeln'),[StringLiteral(r'Enter n')]),CallStmt(Id(r'read'),[Id(r'n')]),If(BinaryOp(r'<>',BinaryOp(r'mod',Id(r'n'),IntLiteral(2)),IntLiteral(0)),[CallStmt(Id(r'writeln'),[Id(r'n'),StringLiteral(r'is not a prime number!')])],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'div',Id(r'n'),IntLiteral(2)),True,[Assign(Id(r'a'),Id(r'i')),Assign(Id(r'b'),BinaryOp(r'-',Id(r'n'),Id(r'i'))),If(BinaryOp(r'and',CallExpr(Id(r'isPrime'),[Id(r'a')]),CallExpr(Id(r'isPrime'),[Id(r'b')])),[CallStmt(Id(r'writeln'),[Id(r'n'),StringLiteral(r' = '),Id(r'a'),StringLiteral(r' + '),Id(r'b')])],[])])])],IntType()),FuncDecl(Id(r'bar'),[],[],[CallStmt(Id(r'log'),[StringLiteral(r'...')])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 230))

    def test_parser__31(self):
        input = """
        function foo(): real;
begin
    found:=0;
    current_num:=1;
    while found = 4 do begin
        sum_div:=0;
        for i:=1 to (current_num-1) do
            if ((current_num mod i)=0) then sum_div:=sum_div+i;
            if (current_num = sum_div) then begin
                writeln(current_num);
                found:=found+1;
            end
        current_num:=current_num+1;
    end
end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'found'),IntLiteral(0)),Assign(Id(r'current_num'),IntLiteral(1)),While(BinaryOp(r'=',Id(r'found'),IntLiteral(4)),[Assign(Id(r'sum_div'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),BinaryOp(r'-',Id(r'current_num'),IntLiteral(1)),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'current_num'),Id(r'i')),IntLiteral(0)),[Assign(Id(r'sum_div'),BinaryOp(r'+',Id(r'sum_div'),Id(r'i')))],[])]),If(BinaryOp(r'=',Id(r'current_num'),Id(r'sum_div')),[CallStmt(Id(r'writeln'),[Id(r'current_num')]),Assign(Id(r'found'),BinaryOp(r'+',Id(r'found'),IntLiteral(1)))],[]),Assign(Id(r'current_num'),BinaryOp(r'+',Id(r'current_num'),IntLiteral(1)))])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 231))

    def test_parser__32(self):
        input = """
        procedure aaaaaaaaa(c: array [1 .. 10] of string);
var inC,outC,nGen:integer;
    randX,randY:string;

begin
    Randomize();
    write("How many generations ? ");
    readln(nGen);
    inC:=0;
    outC:=0;
    while (nGen <= 0) do
    begin
        randX:=random(100)/100;
        randY:=random(100)/100;
        nGen:=nGen-1;
            if ((randX-0.5)*(randX-0.5)+(randY-0.5)*(randY-0.5)<0.5*0.5) Then
                inC:= inC+1;
            else outC:=outC+1;
        writeln("Generations fell the circle: ",inC," Total : ",(inC+outC));
        writeln("Current Pi Evaluation : ",(inC/(outC+inC))*4);
        writeln();
    end
end
        """
        expect = str(Program([FuncDecl(Id(r'aaaaaaaaa'),[VarDecl(Id(r'c'),ArrayType(1,10,StringType()))],[VarDecl(Id(r'inC'),IntType()),VarDecl(Id(r'outC'),IntType()),VarDecl(Id(r'nGen'),IntType()),VarDecl(Id(r'randX'),StringType()),VarDecl(Id(r'randY'),StringType())],[CallStmt(Id(r'Randomize'),[]),CallStmt(Id(r'write'),[StringLiteral(r'How many generations ? ')]),CallStmt(Id(r'readln'),[Id(r'nGen')]),Assign(Id(r'inC'),IntLiteral(0)),Assign(Id(r'outC'),IntLiteral(0)),While(BinaryOp(r'<=',Id(r'nGen'),IntLiteral(0)),[Assign(Id(r'randX'),BinaryOp(r'/',CallExpr(Id(r'random'),[IntLiteral(100)]),IntLiteral(100))),Assign(Id(r'randY'),BinaryOp(r'/',CallExpr(Id(r'random'),[IntLiteral(100)]),IntLiteral(100))),Assign(Id(r'nGen'),BinaryOp(r'-',Id(r'nGen'),IntLiteral(1))),If(BinaryOp(r'<',BinaryOp(r'+',BinaryOp(r'*',BinaryOp(r'-',Id(r'randX'),FloatLiteral(0.5)),BinaryOp(r'-',Id(r'randX'),FloatLiteral(0.5))),BinaryOp(r'*',BinaryOp(r'-',Id(r'randY'),FloatLiteral(0.5)),BinaryOp(r'-',Id(r'randY'),FloatLiteral(0.5)))),BinaryOp(r'*',FloatLiteral(0.5),FloatLiteral(0.5))),[Assign(Id(r'inC'),BinaryOp(r'+',Id(r'inC'),IntLiteral(1)))],[Assign(Id(r'outC'),BinaryOp(r'+',Id(r'outC'),IntLiteral(1)))]),CallStmt(Id(r'writeln'),[StringLiteral(r'Generations fell the circle: '),Id(r'inC'),StringLiteral(r' Total : '),BinaryOp(r'+',Id(r'inC'),Id(r'outC'))]),CallStmt(Id(r'writeln'),[StringLiteral(r'Current Pi Evaluation : '),BinaryOp(r'*',BinaryOp(r'/',Id(r'inC'),BinaryOp(r'+',Id(r'outC'),Id(r'inC'))),IntLiteral(4))]),CallStmt(Id(r'writeln'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 232))

    def test_parser__33(self):
        input = """
        {Computes x^y}
{(*t this is a fucking
//line commnet
no, i's body comment)}
function power(x:real;y:integer):real;
var p:real;
    i:integer;
begin
    p:=1;
    for i:=1 to y do p:=p*x;
    power:=p;
end

function mainr(x:real;y:integer):real;
var p:real;
    i:integer;
begin
    p:=1;
    for i:=1 to y do p:=p*x;
    power:=p;
end
"""
        expect = str(Program([FuncDecl(Id(r'power'),[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'p'),FloatType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'p'),IntLiteral(1)),For(Id(r'i'),IntLiteral(1),Id(r'y'),True,[Assign(Id(r'p'),BinaryOp(r'*',Id(r'p'),Id(r'x')))]),Assign(Id(r'power'),Id(r'p'))],FloatType()),FuncDecl(Id(r'mainr'),[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'p'),FloatType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'p'),IntLiteral(1)),For(Id(r'i'),IntLiteral(1),Id(r'y'),True,[Assign(Id(r'p'),BinaryOp(r'*',Id(r'p'),Id(r'x')))]),Assign(Id(r'power'),Id(r'p'))],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 233))

    def test_parser__34(self):
        input = """
        function isPrime(n:integer):boolean;
var i:integer;
    isDiv:boolean;
begin
    if (n=1) then isPrime:=false;
    else
        begin
        isDiv:=false;
            for i:=2 to trunc(sqrt(n)) do
            if ((n mod i)=0) then isDiv:=true;
            if (isDiv) then isPrime:=false;
            else isPrime:=true;
        end
end
        """
        expect = str(Program([FuncDecl(Id(r'isPrime'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'isDiv'),BoolType())],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'isPrime'),BooleanLiteral(False))],[Assign(Id(r'isDiv'),BooleanLiteral(False)),For(Id(r'i'),IntLiteral(2),CallExpr(Id(r'trunc'),[CallExpr(Id(r'sqrt'),[Id(r'n')])]),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'n'),Id(r'i')),IntLiteral(0)),[Assign(Id(r'isDiv'),BooleanLiteral(True))],[])]),If(Id(r'isDiv'),[Assign(Id(r'isPrime'),BooleanLiteral(False))],[Assign(Id(r'isPrime'),BooleanLiteral(True))])])],BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 234))

    def test_parser__35(self):
        input = """
    procedure get();
var a:array[1 .. 100] of integer;
    i,g:integer;

Begin
g := 0;
for i:= 1 to 5 do
                    begin
                    writeln("Enter Number: ");
                    readln(a[i]);
                    end

for i := 1 to 5 do
    if g < a[i] then
    g := a[i];
writeln("Biggest Number is: ",g);
readln();
end
        """
        expect = str(Program([FuncDecl(Id(r'get'),[],[VarDecl(Id(r'a'),ArrayType(1,100,IntType())),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'g'),IntType())],[Assign(Id(r'g'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(r'writeln'),[StringLiteral(r'Enter Number: ')]),CallStmt(Id(r'readln'),[ArrayCell(Id(r'a'),Id(r'i'))])]),For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[If(BinaryOp(r'<',Id(r'g'),ArrayCell(Id(r'a'),Id(r'i'))),[Assign(Id(r'g'),ArrayCell(Id(r'a'),Id(r'i')))],[])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Biggest Number is: '),Id(r'g')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 235))

    def test_parser__36(self):
        input = """
        function reverse(AString: string): string;
var
i, h, l, len:integer;

begin
len := Length;
if (len < 2) then
begin
    result := AString;
end
else
begin
    l :=  Low(AString);
    h :=  High(AString);
    SetString(result, PChar(nil), len);
    for i := l to h do
    result[i] := Chars[h-i];
end
end
        """
        expect = str(Program([FuncDecl(Id(r'reverse'),[VarDecl(Id(r'AString'),StringType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'l'),IntType()),VarDecl(Id(r'len'),IntType())],[Assign(Id(r'len'),Id(r'Length')),If(BinaryOp(r'<',Id(r'len'),IntLiteral(2)),[Assign(Id(r'result'),Id(r'AString'))],[Assign(Id(r'l'),CallExpr(Id(r'Low'),[Id(r'AString')])),Assign(Id(r'h'),CallExpr(Id(r'High'),[Id(r'AString')])),CallStmt(Id(r'SetString'),[Id(r'result'),CallExpr(Id(r'PChar'),[Id(r'nil')]),Id(r'len')]),For(Id(r'i'),Id(r'l'),Id(r'h'),True,[Assign(ArrayCell(Id(r'result'),Id(r'i')),ArrayCell(Id(r'Chars'),BinaryOp(r'-',Id(r'h'),Id(r'i'))))])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 236))

    def test_parser__37(self):
        input = """
        function fib(n: integer): integer;
var
x, z, y, i: integer;
begin
x := 0;
y := 1;
writeln(x);
writeln(y);
for i := 1 to n do
begin
z:= y + x;
y := x;
x := z ;
writeln(z);
end
end
"""
        expect = str(Program([FuncDecl(Id(r'fib'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'x'),IntLiteral(0)),Assign(Id(r'y'),IntLiteral(1)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'writeln'),[Id(r'y')]),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[Assign(Id(r'z'),BinaryOp(r'+',Id(r'y'),Id(r'x'))),Assign(Id(r'y'),Id(r'x')),Assign(Id(r'x'),Id(r'z')),CallStmt(Id(r'writeln'),[Id(r'z')])])],IntType())]))
        self.assertTrue(TestAST.test(input, expect, 237))

    def test_parser__38(self):
        input = """
        procedure xxa();
var
i,j,n : integer;
A : Array[1 .. 6] of Integer;
begin
n := 6;
for i:=1 to n do
begin
    for j:=1 to i do
    begin
        if (j=1) or (i=j) then
        begin
            A[i]:=1;
        end
        else
        begin
            A[i] := A[i-1] + A[i-11];
        end
    end
end
for i:=1 to n do
begin
    Gotoxy(41-i,i);
    for j:=1 to i do
        write(A[i]);
end
readln();
end
        """
        expect = str(Program([FuncDecl(Id(r'xxa'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'A'),ArrayType(1,6,IntType()))],[Assign(Id(r'n'),IntLiteral(6)),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[For(Id(r'j'),IntLiteral(1),Id(r'i'),True,[If(BinaryOp(r'or',BinaryOp(r'=',Id(r'j'),IntLiteral(1)),BinaryOp(r'=',Id(r'i'),Id(r'j'))),[Assign(ArrayCell(Id(r'A'),Id(r'i')),IntLiteral(1))],[Assign(ArrayCell(Id(r'A'),Id(r'i')),BinaryOp(r'+',ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(11)))))])])]),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[CallStmt(Id(r'Gotoxy'),[BinaryOp(r'-',IntLiteral(41),Id(r'i')),Id(r'i')]),For(Id(r'j'),IntLiteral(1),Id(r'i'),True,[CallStmt(Id(r'write'),[ArrayCell(Id(r'A'),Id(r'i'))])])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 238))

    def test_parser__39(self):
        input = """
        Var Counter : Integer;

procedure main();
Begin
    textcolor(green);

    GotoXy(10,5);
    For Counter := 1 to 10 do
    Begin
        Write(chr(196));
    End

    GotoXy(10,6);
    For Counter := 1 to 10 do
    Begin
        Write(chr(16));
    End

    GotoXy(10,7);
    For Counter := 1 to 10 do
    Begin
        Write(chr(196));
    End

    GotoXy(10,10);
    For Counter := 1 to 10 do
    Begin
        Write(chr(196));
    End

    Readkey();
End
"""
        expect = str(Program([VarDecl(Id(r'Counter'),IntType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'textcolor'),[Id(r'green')]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(5)]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(6)]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(16)])])]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(7)]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])]),CallStmt(Id(r'GotoXy'),[IntLiteral(10),IntLiteral(10)]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])]),CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 239))

    def test_parser__40(self):
        input = """
        Procedure EnterUserInfo(TxtCol : real; TxtBck : string);
Begin
    textcolor(TxtCol);
    textbackground(TxtBck);
    continue;
    Write("Your Name: ");
    Readln(UName);
    Write("Your Surname : ");
    Readln(USurn);
    Write("Country : ");
    Readln(UCoun);
    Write("E-Mail Address: ");
    Readln(UMail);
    Write(" Thank you for entering your personal information!!");
    break;
End
        """
        expect = str(Program([FuncDecl(Id(r'EnterUserInfo'),[VarDecl(Id(r'TxtCol'),FloatType()),VarDecl(Id(r'TxtBck'),StringType())],[],[CallStmt(Id(r'textcolor'),[Id(r'TxtCol')]),CallStmt(Id(r'textbackground'),[Id(r'TxtBck')]),Continue(),CallStmt(Id(r'Write'),[StringLiteral(r'Your Name: ')]),CallStmt(Id(r'Readln'),[Id(r'UName')]),CallStmt(Id(r'Write'),[StringLiteral(r'Your Surname : ')]),CallStmt(Id(r'Readln'),[Id(r'USurn')]),CallStmt(Id(r'Write'),[StringLiteral(r'Country : ')]),CallStmt(Id(r'Readln'),[Id(r'UCoun')]),CallStmt(Id(r'Write'),[StringLiteral(r'E-Mail Address: ')]),CallStmt(Id(r'Readln'),[Id(r'UMail')]),CallStmt(Id(r'Write'),[StringLiteral(r' Thank you for entering your personal information!!')]),Break()],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 240))

    def test_parser__41(self):
        input = """
function foo(): real;
begin
    foo();
end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 241))

    def test_parser__42(self):
        input = """
                Procedure InSoLanXHcuaPTu( A:array[1 .. 15] of REAL; N: Integer);
                Var i :Integer;
                Begin
                For i:=0 to N do
                Writeln( A[i],"  ===>  ", DemPtuX( A, N, A[i]));
                End"""
        expect = str(Program([FuncDecl(Id(r'InSoLanXHcuaPTu'),[VarDecl(Id(r'A'),ArrayType(1,15,FloatType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[CallStmt(Id(r'Writeln'),[ArrayCell(Id(r'A'),Id(r'i')),StringLiteral(r'  ===>  '),CallExpr(Id(r'DemPtuX'),[Id(r'A'),Id(r'N'),ArrayCell(Id(r'A'),Id(r'i'))])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 242))

    def test_parser__43(self):
        input = """
                Procedure SxepDuongTangAmGiam ( A:array[1 .. 10] of integer; N:Integer );
                Var i ,j ,k:Integer;
                Begin
                For i:=1 to N do
                For j:=1 to N  do
                If (((i<j)and (A[i] > A[j]) and (A[i]>0) and (A[j]>0)) or
                ((i<j) and ( A[i] < A[j] ) and ( A[i]<0) and ( A[j]<0))) then
                    Begin
                    k := A[i];      { Tien hanh hoan doi gia tri A[i], A[j]}
                    A[i] := A[j];             { thong qua bien tam k }
                    A[j] := k;
                    End
                End
                """
        expect = str(Program([FuncDecl(Id(r'SxepDuongTangAmGiam'),[VarDecl(Id(r'A'),ArrayType(1,10,IntType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[For(Id(r'j'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'or',BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'<',Id(r'i'),Id(r'j')),BinaryOp(r'>',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),Id(r'j')))),BinaryOp(r'>',ArrayCell(Id(r'A'),Id(r'i')),IntLiteral(0))),BinaryOp(r'>',ArrayCell(Id(r'A'),Id(r'j')),IntLiteral(0))),BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'<',Id(r'i'),Id(r'j')),BinaryOp(r'<',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),Id(r'j')))),BinaryOp(r'<',ArrayCell(Id(r'A'),Id(r'i')),IntLiteral(0))),BinaryOp(r'<',ArrayCell(Id(r'A'),Id(r'j')),IntLiteral(0)))),[Assign(Id(r'k'),ArrayCell(Id(r'A'),Id(r'i'))),Assign(ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),Id(r'j'))),Assign(ArrayCell(Id(r'A'),Id(r'j')),Id(r'k'))],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 243))

    def test_parser__44(self):
        input = """
                Procedure XoaPhanTu( A:array[1 .. 10] of sTRIng; N:Integer; k:sTRIng);
                Var i :Integer;
                Begin
                For  i:=k to N-1 do
                A[i] := A[i+1];
                End
                """
        expect = str(Program([FuncDecl(Id(r'XoaPhanTu'),[VarDecl(Id(r'A'),ArrayType(1,10,StringType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'k'),StringType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),Id(r'k'),BinaryOp(r'-',Id(r'N'),IntLiteral(1)),True,[Assign(ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'+',Id(r'i'),IntLiteral(1))))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 244))

    def test_parser__45(self):
        input = """
                pROCEDURE main();
                Var A:array[1 .. 100] of integer;
                N,i,S:Integer;
                Begin
                {nhap mang}
                Write("Nhap N="); Readln(N);
                For i:=1 To N Do
                Begin
                Write("A[",i,"]="); Readln(A[i]);
                End
                {tinh tong}
                S:=0;
                For i:=1 To N Do
                If A[i]<0 Then S:=S+A[i]*A[i];
                {Xuat ket qua ra man hinh}
                Writeln("S= ", S);
                Readln();
                End
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),ArrayType(1,100,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'S'),IntType())],[CallStmt(Id(r'Write'),[StringLiteral(r'Nhap N=')]),CallStmt(Id(r'Readln'),[Id(r'N')]),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[CallStmt(Id(r'Write'),[StringLiteral(r'A['),Id(r'i'),StringLiteral(r']=')]),CallStmt(Id(r'Readln'),[ArrayCell(Id(r'A'),Id(r'i'))])]),Assign(Id(r'S'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'<',ArrayCell(Id(r'A'),Id(r'i')),IntLiteral(0)),[Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),BinaryOp(r'*',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),Id(r'i')))))],[])]),CallStmt(Id(r'Writeln'),[StringLiteral(r'S= '),Id(r'S')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 245))

    def test_parser__46(self):
        input = """
                procedure UCLN_BCNN();
                Var a, b :integer; // Khai bao bien su dung
                Begin
                Write("Nhap vao so a:"); // Thong bao nhap lieu
                Readln(a); // Nhap gtri a (voi &a, la lay d/c bien a,)
                Write("Nhap vao so b:");  // Thong bao nhap lieu
                Readln(b);  // Nhap gtri b (voi &b, la lay d/c bien b,)
                For i:=a downto 1 do
                If((a mod i = 0) and (b mod i = 0)) then  // Kiem tra a, b co chia het
                Break;
                Writeln("USCLN (",a,",",b,"):", i);  // Xuat ket qua USCLN(a, b)
                Writeln("BSCNN (",a,",",b,"):", a*b div i); // Xuat ket qua USCLN(a, b)
                Readln();
                End
                """
        expect = str(Program([FuncDecl(Id(r'UCLN_BCNN'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'Write'),[StringLiteral(r'Nhap vao so a:')]),CallStmt(Id(r'Readln'),[Id(r'a')]),CallStmt(Id(r'Write'),[StringLiteral(r'Nhap vao so b:')]),CallStmt(Id(r'Readln'),[Id(r'b')]),For(Id(r'i'),Id(r'a'),IntLiteral(1),False,[If(BinaryOp(r'and',BinaryOp(r'=',BinaryOp(r'mod',Id(r'a'),Id(r'i')),IntLiteral(0)),BinaryOp(r'=',BinaryOp(r'mod',Id(r'b'),Id(r'i')),IntLiteral(0))),[Break()],[])]),CallStmt(Id(r'Writeln'),[StringLiteral(r'USCLN ('),Id(r'a'),StringLiteral(r','),Id(r'b'),StringLiteral(r'):'),Id(r'i')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'BSCNN ('),Id(r'a'),StringLiteral(r','),Id(r'b'),StringLiteral(r'):'),BinaryOp(r'div',BinaryOp(r'*',Id(r'a'),Id(r'b')),Id(r'i'))]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 246))

    def test_parser__47(self):
        input = """
                procedure MaxOfThreeNumber();
                var  a, b, c, max: real;
                begin
                write("Nhap a = "); readln(a);
                write("Nhap b = "); readln(b);
                write("Nhap c = "); readln(c);
                max:=a;
                if max<b then max:=b;
                if max<c then max:=c;
                writeln("So lon nhat trong 3 so la: ", max);
                readln();
                end
                """
        expect = str(Program([FuncDecl(Id(r'MaxOfThreeNumber'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'max'),FloatType())],[CallStmt(Id(r'write'),[StringLiteral(r'Nhap a = ')]),CallStmt(Id(r'readln'),[Id(r'a')]),CallStmt(Id(r'write'),[StringLiteral(r'Nhap b = ')]),CallStmt(Id(r'readln'),[Id(r'b')]),CallStmt(Id(r'write'),[StringLiteral(r'Nhap c = ')]),CallStmt(Id(r'readln'),[Id(r'c')]),Assign(Id(r'max'),Id(r'a')),If(BinaryOp(r'<',Id(r'max'),Id(r'b')),[Assign(Id(r'max'),Id(r'b'))],[]),If(BinaryOp(r'<',Id(r'max'),Id(r'c')),[Assign(Id(r'max'),Id(r'c'))],[]),CallStmt(Id(r'writeln'),[StringLiteral(r'So lon nhat trong 3 so la: '),Id(r'max')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 247))

    def test_parser__48(self):
        input = """
                procedure ptb2() ;
                VAR a,b,c,x1,x2,d:REAL;
                BEGIN
                clrscr();
                while(1) do begin
                write("Nhap cac he so a, b, c: ");
                readln(a,b,c);
                if(a<>0) then break;
                end
                d:=sqr(b)-4*a*c;
                IF d<0 THEN write("Phuong trinh vo nghiem!");
                ELSE BEGIN
                x1:=(-b-sqrt(d))/(2*a);
                x2:=(-b+sqrt(d))/(2*a);
                IF d=0 THEN writeln("Phuong trinh co nghiem kep x = ",x1);
                ELSE writeln("Phuong trinh co 2 nghiem phan biet: ",x1,x2);
                END
                readln();
                END
            """
        expect = str(Program([FuncDecl(Id(r'ptb2'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x1'),FloatType()),VarDecl(Id(r'x2'),FloatType()),VarDecl(Id(r'd'),FloatType())],[CallStmt(Id(r'clrscr'),[]),While(IntLiteral(1),[CallStmt(Id(r'write'),[StringLiteral(r'Nhap cac he so a, b, c: ')]),CallStmt(Id(r'readln'),[Id(r'a'),Id(r'b'),Id(r'c')]),If(BinaryOp(r'<>',Id(r'a'),IntLiteral(0)),[Break()],[])]),Assign(Id(r'd'),BinaryOp(r'-',CallExpr(Id(r'sqr'),[Id(r'b')]),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'a')),Id(r'c')))),If(BinaryOp(r'<',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'write'),[StringLiteral(r'Phuong trinh vo nghiem!')])],[Assign(Id(r'x1'),BinaryOp(r'/',BinaryOp(r'-',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),Assign(Id(r'x2'),BinaryOp(r'/',BinaryOp(r'+',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),If(BinaryOp(r'=',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co nghiem kep x = '),Id(r'x1')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co 2 nghiem phan biet: '),Id(r'x1'),Id(r'x2')])])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 248))

    def test_parser__49(self):
        input = """
                procedure main();
                var i: integer;
                S: integer;
                begin
                S:= 0;
                i:= 1;
                while i <= 100 do begin
                S:= S + i;
                i:= i +1;
                end
                write("Tong tu 1 den 100 la: ",S);
                readln();
                end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'S'),IntType())],[Assign(Id(r'S'),IntLiteral(0)),Assign(Id(r'i'),IntLiteral(1)),While(BinaryOp(r'<=',Id(r'i'),IntLiteral(100)),[Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),Id(r'i'))),Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)))]),CallStmt(Id(r'write'),[StringLiteral(r'Tong tu 1 den 100 la: '),Id(r'S')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 249))

    def test_parser__50(self):
        input = """
                procedure SquareRoot();
                VAR Value, SqRoot:REAL;
                Finished:String;
                BEGIN
                Finished := "N";
                WHILE Finished <> "Y" DO
                BEGIN {WHILE LOOP}
                READLN(Value);
                IF Value >= 0 THEN
                BEGIN
                SqRoot := SQRT(Value);
                WRITELN(Value,SqRoot);
                END
                ELSE WRITELN(Value," IS A NEGATIVE NUMBER");
                WRITELN("Are you Done entering data ");
                READLN(Finished);
                END {WHILE LOOP}
                END
            """
        expect = str(Program([FuncDecl(Id(r'SquareRoot'),[],[VarDecl(Id(r'Value'),FloatType()),VarDecl(Id(r'SqRoot'),FloatType()),VarDecl(Id(r'Finished'),StringType())],[Assign(Id(r'Finished'),StringLiteral(r'N')),While(BinaryOp(r'<>',Id(r'Finished'),StringLiteral(r'Y')),[CallStmt(Id(r'READLN'),[Id(r'Value')]),If(BinaryOp(r'>=',Id(r'Value'),IntLiteral(0)),[Assign(Id(r'SqRoot'),CallExpr(Id(r'SQRT'),[Id(r'Value')])),CallStmt(Id(r'WRITELN'),[Id(r'Value'),Id(r'SqRoot')])],[CallStmt(Id(r'WRITELN'),[Id(r'Value'),StringLiteral(r' IS A NEGATIVE NUMBER')])]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Are you Done entering data ')]),CallStmt(Id(r'READLN'),[Id(r'Finished')])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 250))

    def test_parser__51(self):
        input = """
                Function LuyThua(a, k: Integer): integer;
                Begin
                If k = 1 then return a;
                Else return LuyThua(a, k-1) * a;
                End
                procedure main();
                Var
                A: Array [1 .. 10] of Integer;
                i, n: Integer;
                Begin
                WriteLn("Hay nhap so phan tu cua day so");
                ReadLn(n);
                {Nhap day so}
                For i := 1 to n do begin
                WriteLn("Hay nhap phan tu thu ", i);
                ReadLn(A[i]);
                End
                {In ra gia tri luy thua cua 2}
                For i := 1 to n do
                Write(LuyThua(2, A[i]));
                ReadLn();
                End
            """
        expect = str(Program([FuncDecl(Id(r'LuyThua'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'k'),IntType())],[],[If(BinaryOp(r'=',Id(r'k'),IntLiteral(1)),[Return(Id(r'a'))],[Return(BinaryOp(r'*',CallExpr(Id(r'LuyThua'),[Id(r'a'),BinaryOp(r'-',Id(r'k'),IntLiteral(1))]),Id(r'a')))])],IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),ArrayType(1,10,IntType())),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'n'),IntType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap so phan tu cua day so')]),CallStmt(Id(r'ReadLn'),[Id(r'n')]),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap phan tu thu '),Id(r'i')]),CallStmt(Id(r'ReadLn'),[ArrayCell(Id(r'A'),Id(r'i'))])]),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'LuyThua'),[IntLiteral(2),ArrayCell(Id(r'A'),Id(r'i'))])])]),CallStmt(Id(r'ReadLn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 251))

    def test_parser__52(self):
        input = """
                procedure convertBinaryToDemical();
                Var
                So: Integer;
                LT, STP: integer;
                CNP: String;
                Begin
                WriteLn("Hay nhap chuoi can doi tu he 2 sang he 10");
                ReadLn(CNP);
                LT := 1;
                For i:=Length(CNP) downto 1 do Begin
                If CNP[i] = "0" then So :=0 ;
                Else So := 1;
                STP := STP + So;
                LT := LT * 2;
                End
                WriteLn("Chuoi ", CNP, " trong he 2 doi sang he 10 la ", STP);
                ReadLn();
                End
                """
        expect = str(Program([FuncDecl(Id(r'convertBinaryToDemical'),[],[VarDecl(Id(r'So'),IntType()),VarDecl(Id(r'LT'),IntType()),VarDecl(Id(r'STP'),IntType()),VarDecl(Id(r'CNP'),StringType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap chuoi can doi tu he 2 sang he 10')]),CallStmt(Id(r'ReadLn'),[Id(r'CNP')]),Assign(Id(r'LT'),IntLiteral(1)),For(Id(r'i'),CallExpr(Id(r'Length'),[Id(r'CNP')]),IntLiteral(1),False,[If(BinaryOp(r'=',ArrayCell(Id(r'CNP'),Id(r'i')),StringLiteral(r'0')),[Assign(Id(r'So'),IntLiteral(0))],[Assign(Id(r'So'),IntLiteral(1))]),Assign(Id(r'STP'),BinaryOp(r'+',Id(r'STP'),Id(r'So'))),Assign(Id(r'LT'),BinaryOp(r'*',Id(r'LT'),IntLiteral(2)))]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Chuoi '),Id(r'CNP'),StringLiteral(r' trong he 2 doi sang he 10 la '),Id(r'STP')]),CallStmt(Id(r'ReadLn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 252))

    def test_parser__53(self):
        input = """
            procedure convertDemicalToBinary();
            Var
            n, k: Integer;
            CNP: String;
            Begin
            WriteLn("Hay nhap so can doi tu he 10 sang he 2");
            ReadLn(n);
            k := n;
            While k>0 do Begin
            If k mod 2 = 0 then CNP:="0" + CNP ;
            Else CNP := "1" + CNP;
            k := k div 2;
            End
            WriteLn("So ", n, " trong he 10 doi sang he 2 la ", CNP);
            ReadLn();
            End
            """
        expect = str(Program([FuncDecl(Id(r'convertDemicalToBinary'),[],[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'CNP'),StringType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap so can doi tu he 10 sang he 2')]),CallStmt(Id(r'ReadLn'),[Id(r'n')]),Assign(Id(r'k'),Id(r'n')),While(BinaryOp(r'>',Id(r'k'),IntLiteral(0)),[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'k'),IntLiteral(2)),IntLiteral(0)),[Assign(Id(r'CNP'),BinaryOp(r'+',StringLiteral(r'0'),Id(r'CNP')))],[Assign(Id(r'CNP'),BinaryOp(r'+',StringLiteral(r'1'),Id(r'CNP')))]),Assign(Id(r'k'),BinaryOp(r'div',Id(r'k'),IntLiteral(2)))]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'So '),Id(r'n'),StringLiteral(r' trong he 10 doi sang he 2 la '),Id(r'CNP')]),CallStmt(Id(r'ReadLn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 253))

    def test_parser__56(self):
        input = """
            procedurE foo (b : real) ;
    var
    a : array [2 .. 3] of integer;
    b: string;
    e: real;
    f: boolean;
    begin
    while (a=4   ) do
        with a,b,c:integer;b: array [1 .. 3] of StRing; do
            while(a=4) do
                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                    e:=4;
    end    procedurE foo (b : real) ;
    var
    a : array [2 .. 3] of integer;
    b: string;
    e: real;
    f: boolean;
    begin
    while (a=4   ) do
        with a,b,c:integer;b: array [1 .. 3] of StRing; do
            while(a=4) do
                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                    e:=4;
    end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(4))])])])])],VoidType()),FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(4))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 256))


    def test_parser__57(self):
        input = """
            procedure example_String();
            var
            str1, str2, str3 : string;
            str4: string;
            len: integer;
            begin
            str1 := "Hello ";
            str2 := "There!";
            (* copy str1 into str3 *)
            str3 := str1;
            writeln("appendstr( str3, str1) : ", str3 );
            (* concatenates str1 and str2 *)
            appendstr(str1, str2);
            writeln("appendstr( str1, str2) " , str1);
            str4 := str1 + str2;
            writeln("Now str4 is: ", str4);
            (* total lenghth of str4 after concatenation *)
            writeln("Length of the final string str4: ", len);
            end
            """
        expect = str(Program([FuncDecl(Id(r'example_String'),[],[VarDecl(Id(r'str1'),StringType()),VarDecl(Id(r'str2'),StringType()),VarDecl(Id(r'str3'),StringType()),VarDecl(Id(r'str4'),StringType()),VarDecl(Id(r'len'),IntType())],[Assign(Id(r'str1'),StringLiteral(r'Hello ')),Assign(Id(r'str2'),StringLiteral(r'There!')),Assign(Id(r'str3'),Id(r'str1')),CallStmt(Id(r'writeln'),[StringLiteral(r'appendstr( str3, str1) : '),Id(r'str3')]),CallStmt(Id(r'appendstr'),[Id(r'str1'),Id(r'str2')]),CallStmt(Id(r'writeln'),[StringLiteral(r'appendstr( str1, str2) '),Id(r'str1')]),Assign(Id(r'str4'),BinaryOp(r'+',Id(r'str1'),Id(r'str2'))),CallStmt(Id(r'writeln'),[StringLiteral(r'Now str4 is: '),Id(r'str4')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Length of the final string str4: '),Id(r'len')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 257))

    def test_parser__58(self):
        input = """
            procedure tongChuSoTanCung();
            Var
            Tong, n, i: Integer;
            Begin
            WriteLn("Hay nhap so");
            ReadLn(n);
            WriteLn("Muon tinh tong bao nhieu chu so tan cung");
            ReadLn(k);
            {Tinh tong k chu so tan cung}
            i := 1;
            While i <= k do Begin
            Tong := Tong + n mod 10;
            n := n div 10;
            Inc(i);
            End
            {In ket qua}
            WriteLn("Tong ", k, " chu so tan cung trong so ", n, " la ", Tong);
            ReadLn();
            End
            """
        expect = str(Program([FuncDecl(Id(r'tongChuSoTanCung'),[],[VarDecl(Id(r'Tong'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap so')]),CallStmt(Id(r'ReadLn'),[Id(r'n')]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Muon tinh tong bao nhieu chu so tan cung')]),CallStmt(Id(r'ReadLn'),[Id(r'k')]),Assign(Id(r'i'),IntLiteral(1)),While(BinaryOp(r'<=',Id(r'i'),Id(r'k')),[Assign(Id(r'Tong'),BinaryOp(r'+',Id(r'Tong'),BinaryOp(r'mod',Id(r'n'),IntLiteral(10)))),Assign(Id(r'n'),BinaryOp(r'div',Id(r'n'),IntLiteral(10))),CallStmt(Id(r'Inc'),[Id(r'i')])]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Tong '),Id(r'k'),StringLiteral(r' chu so tan cung trong so '),Id(r'n'),StringLiteral(r' la '),Id(r'Tong')]),CallStmt(Id(r'ReadLn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 258))

    def test_parser__59(self):
        input = """
            procedure nested_ifelseChecking(k:integer);
            var
            { local variable definition }
            a, b : integer;
            begin
            a := 100;
            b:= 200;
            (* check the boolean condition *)
            if (a = 100) then
            (* if condition is true then check the following *)
            if ( b = 200 ) then
            (* if nested if condition is true then print the following *)
            writeln("Value of a is 100 and value of b is 200");
            writeln("Exact value of a is: ",a);
            writeln("Exact value of b is: ", b );
            end"""
        expect = str(Program([FuncDecl(Id(r'nested_ifelseChecking'),[VarDecl(Id(r'k'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(100)),Assign(Id(r'b'),IntLiteral(200)),If(BinaryOp(r'=',Id(r'a'),IntLiteral(100)),[If(BinaryOp(r'=',Id(r'b'),IntLiteral(200)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Value of a is 100 and value of b is 200')])],[])],[]),CallStmt(Id(r'writeln'),[StringLiteral(r'Exact value of a is: '),Id(r'a')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Exact value of b is: '),Id(r'b')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 259))

    def test_parser__60(self):
        input = """
            procedure tongChuSoTanCung();
            Var
            Tong, n, i: Integer;
            Begin
            WriteLn("Hay nhap so");
            ReadLn(n);
            WriteLn("Muon tinh tong bao nhieu chu so tan cung");
            ReadLn(k);
            {Tinh tong k chu so tan cung}
            i := 1;
            While i <= k do Begin
            Tong := Tong + n mod 10;
            n := n div 10;
            Inc(i);
            End
            {In ket qua}
            WriteLn("Tong ", k, " chu so tan cung trong so ", n, " la ", Tong);
            ReadLn();
            End
            """
        expect = str(Program([FuncDecl(Id(r'tongChuSoTanCung'),[],[VarDecl(Id(r'Tong'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap so')]),CallStmt(Id(r'ReadLn'),[Id(r'n')]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Muon tinh tong bao nhieu chu so tan cung')]),CallStmt(Id(r'ReadLn'),[Id(r'k')]),Assign(Id(r'i'),IntLiteral(1)),While(BinaryOp(r'<=',Id(r'i'),Id(r'k')),[Assign(Id(r'Tong'),BinaryOp(r'+',Id(r'Tong'),BinaryOp(r'mod',Id(r'n'),IntLiteral(10)))),Assign(Id(r'n'),BinaryOp(r'div',Id(r'n'),IntLiteral(10))),CallStmt(Id(r'Inc'),[Id(r'i')])]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Tong '),Id(r'k'),StringLiteral(r' chu so tan cung trong so '),Id(r'n'),StringLiteral(r' la '),Id(r'Tong')]),CallStmt(Id(r'ReadLn'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 260))

    def test_parser__61(self):
        input = """
        funcTion foo(): real;
var x,y: inTeger;
begin
sum := 0;
writeln(sum);
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(Id(r'sum'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'sum')])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 261))

    def test_parser_62(self):
        input = """
        procedurE fooabczys (b : real;h:string) ;
var
a : array [2 .. 3] of integer;
b: string;
e: real;
f: boolean;
begin
while(a=4) do
e:="abded";
End
"""
        expect = str(Program([FuncDecl(Id(r'fooabczys'),[VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'h'),StringType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[Assign(Id(r'e'),StringLiteral(r'abded'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 262))

    def test_parser_63(self):
        input = """
        procedurE a2b_3(b : real) ;
var
a : array [2 .. 3] of integer;
b: string;
e: real;
f: boolean;
begin
while(a=4) do
e:=u:=a[4+2+3]:=6;
End
"""
        expect = str(Program([FuncDecl(Id(r'a2b_3'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',IntLiteral(4),IntLiteral(2)),IntLiteral(3))),IntLiteral(6)),Assign(Id(r'u'),ArrayCell(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',IntLiteral(4),IntLiteral(2)),IntLiteral(3)))),Assign(Id(r'e'),Id(r'u'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 263))

    def test_parser_64(self):
        input = """
        function foo (b : real) : arraY [2 .. 3] of StrinG ;
var
a : array [2 .. 3] of integer;
begin
with a , b :integer ; c: array [1 .. 2] of real ; do
d := c[a] + b;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType()))],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])],ArrayType(2,3,StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 264))

    def test_parser_65(self):
        input = """
        procedurE foo (b : real) ;
var
a : array [2 .. 3] of integer;
b: string;
e: real;
f: boolean;
begin
while(a=4) and (b=6) do
e:=4;
End
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'and',BinaryOp(r'=',Id(r'a'),IntLiteral(4)),BinaryOp(r'=',Id(r'b'),IntLiteral(6))),[Assign(Id(r'e'),IntLiteral(4))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 265))

    def test_parser__66(self):
        input = """
        function foo (b : REal) : arraY [2 .. 3] of StrinG ;
var
a : array [2 .. 3] of integer;
begin
for i:=0 doWnTo 2 dO
    a:=b:=e:=f:=5; (*               jaskldfj;sjfd; *)
end
    """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType()))],[For(Id(r'i'),IntLiteral(0),IntLiteral(2),False,[Assign(Id(r'f'),IntLiteral(5)),Assign(Id(r'e'),Id(r'f')),Assign(Id(r'b'),Id(r'e')),Assign(Id(r'a'),Id(r'b'))])],ArrayType(2,3,StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 266))

    def test_parser_69(self):
        input = """
        function foo (b : integer) : array [2 .. 3] of real ;
var
a : array [2 .. 3] of real;
begin
while (2=3) do return foo(2,3,4); //CORRECT
end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'a'),ArrayType(2,3,FloatType()))],[While(BinaryOp(r'=',IntLiteral(2),IntLiteral(3)),[Return(CallExpr(Id(r'foo'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))])],ArrayType(2,3,FloatType()))]))
        self.assertTrue(TestAST.test(input, expect, 269))

    def test_parser_70(self):
        input = """
        function foo (b : integer) : array [2 .. 3] of real ;
var
a : array [2 .. 3] of real;
begin
while (2=3) do return foo(2,3,4); //CORRECT
end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'a'),ArrayType(2,3,FloatType()))],[While(BinaryOp(r'=',IntLiteral(2),IntLiteral(3)),[Return(CallExpr(Id(r'foo'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))])],ArrayType(2,3,FloatType()))]))
        self.assertTrue(TestAST.test(input, expect, 270))

    def test_parser_71(self):
        input = """
    (*   //Draw the top + bottom borders
for x := BORDER_START_X to BORDER_START_X + BORDER_WIDTH do
begin
    //Top
    DrawAt(x, BORDER_START_Y, BORDER_CHARACTER, White);
    DrawAt(x, BORDER_START_Y + BORDER_HEIGHT, BORDER_CHARACTER, White);
end

for y := BORDER_START_Y to BORDER_START_Y + BORDER_HEIGHT do
begin
    DrawAt(BORDER_START_X, y, BORDER_CHARACTER, White);
    DrawAt(BORDER_START_X + BORDER_WIDTH, y, BORDER_CHARACTER, White);
end *)
var a : integer;
"""

        expect = str(Program([VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input, expect, 271))

    def test_parser_72(self):
        input = """
        proCedure temp();
        begin
                i := 2;
        if i = 0 then
                write(0);
        else if i = 1 then
                write(1);
        else if i mod 2 then
                write(2);
        else write (99);
        end
"""
        expect = str(Program([FuncDecl(Id(r'temp'),[],[],[Assign(Id(r'i'),IntLiteral(2)),If(BinaryOp(r'=',Id(r'i'),IntLiteral(0)),[CallStmt(Id(r'write'),[IntLiteral(0)])],[If(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[CallStmt(Id(r'write'),[IntLiteral(1)])],[If(BinaryOp(r'mod',Id(r'i'),IntLiteral(2)),[CallStmt(Id(r'write'),[IntLiteral(2)])],[CallStmt(Id(r'write'),[IntLiteral(99)])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 272))

    def test_parser_73(self):
        input = """
        Procedure Temperaturerrechnung (input, output: stRing);
var
C: real;
F: real;
begin
    writeln("Insert Fahrenheit", F);
    readln(F);
    C:= (5 * (F - 32)) / 9  ;
    writeln("The temperature is C: ", C)  ;
end

        """
        expect = str(Program([FuncDecl(Id(r'Temperaturerrechnung'),[VarDecl(Id(r'input'),StringType()),VarDecl(Id(r'output'),StringType())],[VarDecl(Id(r'C'),FloatType()),VarDecl(Id(r'F'),FloatType())],[CallStmt(Id(r'writeln'),[StringLiteral(r'Insert Fahrenheit'),Id(r'F')]),CallStmt(Id(r'readln'),[Id(r'F')]),Assign(Id(r'C'),BinaryOp(r'/',BinaryOp(r'*',IntLiteral(5),BinaryOp(r'-',Id(r'F'),IntLiteral(32))),IntLiteral(9))),CallStmt(Id(r'writeln'),[StringLiteral(r'The temperature is C: '),Id(r'C')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 273))

    def test_parser_74(self):
        input = """
                procedure Test();
VAR
x : REAL;
j : INTEGER;
BEGIN
    x := 12.449;
    i := 10;
    j := -300;
    WRITE("This is some text");
    WRITELN("Unformatted integer ",i);
    WRITELN("Unformatted integer computation ",a[1] + b[a[c]*2]/12 - c[a[4]/c[12]]);
    WRITELN("formatted integer",i/4);
    WRITELN("formatted integer",j/4);
END
"""
        expect = str(Program([FuncDecl(Id(r'Test'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'j'),IntType())],[Assign(Id(r'x'),FloatLiteral(12.449)),Assign(Id(r'i'),IntLiteral(10)),Assign(Id(r'j'),UnaryOp(r'-',IntLiteral(300))),CallStmt(Id(r'WRITE'),[StringLiteral(r'This is some text')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Unformatted integer '),Id(r'i')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'Unformatted integer computation '),BinaryOp(r'-',BinaryOp(r'+',ArrayCell(Id(r'a'),IntLiteral(1)),BinaryOp(r'/',ArrayCell(Id(r'b'),BinaryOp(r'*',ArrayCell(Id(r'a'),Id(r'c')),IntLiteral(2))),IntLiteral(12))),ArrayCell(Id(r'c'),BinaryOp(r'/',ArrayCell(Id(r'a'),IntLiteral(4)),ArrayCell(Id(r'c'),IntLiteral(12)))))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'formatted integer'),BinaryOp(r'/',Id(r'i'),IntLiteral(4))]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'formatted integer'),BinaryOp(r'/',Id(r'j'),IntLiteral(4))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 274))

    def test_parser_75(self):
        input = """
        function AverageSystem(): real ;

Var
Number1 : Integer ;
Number2 : Integer ;
Sum : Real ;
Average : Real ;

Begin { AverageSystem }

break;

Write ("Type a first number: ") ;
Readln (Number1) ;

Write ("Type a second number: ") ;
Readln (Number2) ;

Sum :=Number1 + Number2 ;
Average := Sum / 2 ;

End { AverageSystem }
"""
        expect = str(Program([FuncDecl(Id(r'AverageSystem'),[],[VarDecl(Id(r'Number1'),IntType()),VarDecl(Id(r'Number2'),IntType()),VarDecl(Id(r'Sum'),FloatType()),VarDecl(Id(r'Average'),FloatType())],[Break(),CallStmt(Id(r'Write'),[StringLiteral(r'Type a first number: ')]),CallStmt(Id(r'Readln'),[Id(r'Number1')]),CallStmt(Id(r'Write'),[StringLiteral(r'Type a second number: ')]),CallStmt(Id(r'Readln'),[Id(r'Number2')]),Assign(Id(r'Sum'),BinaryOp(r'+',Id(r'Number1'),Id(r'Number2'))),Assign(Id(r'Average'),BinaryOp(r'/',Id(r'Sum'),IntLiteral(2)))],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 275))



    def test_parser_82(self):
        input = """

procedure main();
var
A,B,C,D: integer;

begin
write("A = ");
readln(A);
D := B*B-4*A*C;
if (D=0) then
begin
    writeln("x = ",-B/2.0/A);
    halt();
end
end
"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),VarDecl(Id(r'C'),IntType()),VarDecl(Id(r'D'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r'A = ')]),CallStmt(Id(r'readln'),[Id(r'A')]),Assign(Id(r'D'),BinaryOp(r'-',BinaryOp(r'*',Id(r'B'),Id(r'B')),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'A')),Id(r'C')))),If(BinaryOp(r'=',Id(r'D'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'x = '),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A'))]),CallStmt(Id(r'halt'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 282))


    def test_parser_84(self):
        input = """

procedure main();
var
A,B,C,D: integer;

begin
write("A = ");
readln(A);
D := B*B-4*A*C;
if (D=0 - 10 /100 * 1000000 - 0.1e1212 * 1.0000e12) then
begin
    writeln("x = ",-B/2.0/A);
    halt();
end
end
"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),VarDecl(Id(r'C'),IntType()),VarDecl(Id(r'D'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r'A = ')]),CallStmt(Id(r'readln'),[Id(r'A')]),Assign(Id(r'D'),BinaryOp(r'-',BinaryOp(r'*',Id(r'B'),Id(r'B')),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'A')),Id(r'C')))),If(BinaryOp(r'=',Id(r'D'),BinaryOp(r'-',BinaryOp(r'-',IntLiteral(0),BinaryOp(r'*',BinaryOp(r'/',IntLiteral(10),IntLiteral(100)),IntLiteral(1000000))),BinaryOp(r'*',FloatLiteral(inf),FloatLiteral(1000000000000.0)))),[CallStmt(Id(r'writeln'),[StringLiteral(r'x = '),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A'))]),CallStmt(Id(r'halt'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 284))

    def test_parser_85(self):
        input = """

procedure main();
var
A,B,C,D: integer;

begin
write("A = ");
readln(A);
D := B*B-4*A*C;
if (D=0 - 10 /100 * 1000000 - 0.1e1212 * 1.0000e12) then
begin
    writeln("x\\t \\f \\n = ",-B/2.0/A);
    halt();
end
end
"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'B'),IntType()),VarDecl(Id(r'C'),IntType()),VarDecl(Id(r'D'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r'A = ')]),CallStmt(Id(r'readln'),[Id(r'A')]),Assign(Id(r'D'),BinaryOp(r'-',BinaryOp(r'*',Id(r'B'),Id(r'B')),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'A')),Id(r'C')))),If(BinaryOp(r'=',Id(r'D'),BinaryOp(r'-',BinaryOp(r'-',IntLiteral(0),BinaryOp(r'*',BinaryOp(r'/',IntLiteral(10),IntLiteral(100)),IntLiteral(1000000))),BinaryOp(r'*',FloatLiteral(inf),FloatLiteral(1000000000000.0)))),[CallStmt(Id(r'writeln'),[StringLiteral(r'x\t \f \n = '),BinaryOp(r'/',BinaryOp(r'/',UnaryOp(r'-',Id(r'B')),FloatLiteral(2.0)),Id(r'A'))]),CallStmt(Id(r'halt'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 285))





    def test_parser_90(self):
        input = """
        procedure main();
    var t,p0,epsilon,IP,IA:real;
        isNeg:boolean;
        i:integer;

        begin
        writeln("Tabulate Gauss Function");
        writeln("Enter t to compute P(|X <= t|) ahahaha");

        { setting boolean to track (t<0) }
        read(t);
        if t < 0 then break;
        else continue;
    end
    """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'p0'),FloatType()),VarDecl(Id(r'epsilon'),FloatType()),VarDecl(Id(r'IP'),FloatType()),VarDecl(Id(r'IA'),FloatType()),VarDecl(Id(r'isNeg'),BoolType()),VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'writeln'),[StringLiteral(r'Tabulate Gauss Function')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Enter t to compute P(|X <= t|) ahahaha')]),CallStmt(Id(r'read'),[Id(r't')]),If(BinaryOp(r'<',Id(r't'),IntLiteral(0)),[Break()],[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 290))

    def test_parser_91(self):
        input = """
        procedure main();
    begin
    i := 1;
    x := 5;
    While (I <= 5) and 11111111e122102200202-122 or (x <= 75) do
    begin
        w [i] := x;
        x := w[i] * 20.5;
        i := 1 + 1 ;
    end
    read (x,y);
    if x>y then write (gcd(x, y));
    else if 1 then foo();
    else write (gcd (h,z));
    w[gcd(x,y)] := 23e10;
    this (w,z);
    this (w[w[i]],gcd(x,y));
    i := 1;
    while (i <= 5) do
        begin
        write(w[i]);
        i := 1 + 1;
        end
    write(h,i,x,y,z);
    end
    """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'i'),IntLiteral(1)),Assign(Id(r'x'),IntLiteral(5)),While(BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'and',BinaryOp(r'<=',Id(r'I'),IntLiteral(5)),FloatLiteral(inf)),IntLiteral(122)),BinaryOp(r'<=',Id(r'x'),IntLiteral(75))),[Assign(ArrayCell(Id(r'w'),Id(r'i')),Id(r'x')),Assign(Id(r'x'),BinaryOp(r'*',ArrayCell(Id(r'w'),Id(r'i')),FloatLiteral(20.5))),Assign(Id(r'i'),BinaryOp(r'+',IntLiteral(1),IntLiteral(1)))]),CallStmt(Id(r'read'),[Id(r'x'),Id(r'y')]),If(BinaryOp(r'>',Id(r'x'),Id(r'y')),[CallStmt(Id(r'write'),[CallExpr(Id(r'gcd'),[Id(r'x'),Id(r'y')])])],[If(IntLiteral(1),[CallStmt(Id(r'foo'),[])],[CallStmt(Id(r'write'),[CallExpr(Id(r'gcd'),[Id(r'h'),Id(r'z')])])])]),Assign(ArrayCell(Id(r'w'),CallExpr(Id(r'gcd'),[Id(r'x'),Id(r'y')])),FloatLiteral(230000000000.0)),CallStmt(Id(r'this'),[Id(r'w'),Id(r'z')]),CallStmt(Id(r'this'),[ArrayCell(Id(r'w'),ArrayCell(Id(r'w'),Id(r'i'))),CallExpr(Id(r'gcd'),[Id(r'x'),Id(r'y')])]),Assign(Id(r'i'),IntLiteral(1)),While(BinaryOp(r'<=',Id(r'i'),IntLiteral(5)),[CallStmt(Id(r'write'),[ArrayCell(Id(r'w'),Id(r'i'))]),Assign(Id(r'i'),BinaryOp(r'+',IntLiteral(1),IntLiteral(1)))]),CallStmt(Id(r'write'),[Id(r'h'),Id(r'i'),Id(r'x'),Id(r'y'),Id(r'z')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 291))







    def test_parser_97(self):
        input = """
        procedure main();
        var x : array [1 .. -3] of real;
    begin
    i := 1;
    x := 5;
    While (I <= 5) and (i) or (x <= 75.0000e1212) do
    begin
        w [i] := x;
        x := w[i] * 20.5e1818111;
        i := 1 + 1 ;
    end
    read (x,y);
    if x>y then write (gcd(x, y));
    else gg();
    end
    """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'x'),ArrayType(1,-3,FloatType()))],[Assign(Id(r'i'),IntLiteral(1)),Assign(Id(r'x'),IntLiteral(5)),While(BinaryOp(r'or',BinaryOp(r'and',BinaryOp(r'<=',Id(r'I'),IntLiteral(5)),Id(r'i')),BinaryOp(r'<=',Id(r'x'),FloatLiteral(inf))),[Assign(ArrayCell(Id(r'w'),Id(r'i')),Id(r'x')),Assign(Id(r'x'),BinaryOp(r'*',ArrayCell(Id(r'w'),Id(r'i')),FloatLiteral(inf))),Assign(Id(r'i'),BinaryOp(r'+',IntLiteral(1),IntLiteral(1)))]),CallStmt(Id(r'read'),[Id(r'x'),Id(r'y')]),If(BinaryOp(r'>',Id(r'x'),Id(r'y')),[CallStmt(Id(r'write'),[CallExpr(Id(r'gcd'),[Id(r'x'),Id(r'y')])])],[CallStmt(Id(r'gg'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 297))



    def test_parser_100(self):
        input = """
var a, b, c: boolean;
x, y, z: real ;
g, h, i: array[0 .. 5] of boolean ;
procedure main();
begin
    a := 1[2][1] + (1>2-"string")[4][112 - "string"];
end
"""
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'g'),ArrayType(0,5,BoolType())),VarDecl(Id(r'h'),ArrayType(0,5,BoolType())),VarDecl(Id(r'i'),ArrayType(0,5,BoolType())),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',ArrayCell(ArrayCell(IntLiteral(1),IntLiteral(2)),IntLiteral(1)),ArrayCell(ArrayCell(BinaryOp(r'>',IntLiteral(1),BinaryOp(r'-',IntLiteral(2),StringLiteral(r'string'))),IntLiteral(4)),BinaryOp(r'-',IntLiteral(112),StringLiteral(r'string')))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
