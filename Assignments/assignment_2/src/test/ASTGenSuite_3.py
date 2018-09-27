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
#from AntiAST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """proceDure main() ;beGin end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """proceDure main () ;BEGIN
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'putIntLn'),[IntLiteral(4)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_wrong_miss_close(self):
        input = """proceDure main(); beGin end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_variable_declaration(self):
        input = """PROCEDURE main() ;
                  var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),ArrayType(1,5,IntType())),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_function_declaration(self):
        input = """FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_procedure_declaration(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_assign_statement1(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := 1;
                    b := a[12] ;
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_assign_statement2(self):
        input = """proCeduRe foo() ;
                  var x,y: real ;
                  BEGIN
                    a := "conga";
                    b := func(1,a+1) ;
                  END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'a'),StringLiteral(r'conga')),Assign(Id(r'b'),CallExpr(Id(r'func'),[IntLiteral(1),BinaryOp(r'+',Id(r'a'),IntLiteral(1))]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_assign_statement3(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    a := 1;
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_assign_statement4(self):
        input = """function foo(c: real): real ;
                   var x,y: array[1 .. 2] of real;
                   BEGIN
                    a[m+n] := a[m+1] ;
                    foo()[m*1] := a[a div 3] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),ArrayType(1,2,FloatType())),VarDecl(Id(r'y'),ArrayType(1,2,FloatType()))],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),Id(r'n'))),ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),IntLiteral(1)))),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),BinaryOp(r'*',Id(r'm'),IntLiteral(1))),ArrayCell(Id(r'a'),BinaryOp(r'div',Id(r'a'),IntLiteral(3))))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_assign_statement5(self):
        input = """function foo(c: real): real ;
                   var x: integer ;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),IntType())],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'div',Id(r'a'),IntLiteral(3))),BinaryOp(r'andthen',BinaryOp(r'>',Id(r'a'),Id(r'm')),BinaryOp(r'<',Id(r'b'),Id(r'n')))),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),BinaryOp(r'*',Id(r'm'),IntLiteral(1))),ArrayCell(Id(r'a'),BinaryOp(r'div',Id(r'a'),IntLiteral(3)))),Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),IntLiteral(1))),ArrayCell(CallExpr(Id(r'foo'),[]),BinaryOp(r'*',Id(r'm'),IntLiteral(1)))),Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),Id(r'n'))),ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'm'),IntLiteral(1))))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_assign_statement6(self):
        input = """function foo(c: real): real ;begin x:=a[1] ;  end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[Assign(Id(r'x'),ArrayCell(Id(r'a'),IntLiteral(1)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_if_statement1(self):
        input = """function foo(c: real): real ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else foo();
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[CallStmt(Id(r'foo'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,2);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[If(BinaryOp(r'<>',BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),BinaryOp(r'<',IntLiteral(2),IntLiteral(3))),[Assign(Id(r'x'),IntLiteral(1))],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_if_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[]),If(BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),[Assign(Id(r'x'),IntLiteral(1))],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_if_statement5(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[]),If(BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),[Assign(Id(r'x'),IntLiteral(1))],[CallStmt(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_if_statement6(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then beGin
                        a:=1 ;
                        if(1=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    end
                    END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'=',IntLiteral(1),IntLiteral(1)),[Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(1)))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(1)))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_while_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_while_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'x'),IntLiteral(1))],[]),CallStmt(Id(r'foo'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_while_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[While(IntLiteral(1),[Assign(Id(r'x'),IntLiteral(1))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_while_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                        if(a=1) then begin end
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[While(IntLiteral(1),[Assign(Id(r'x'),IntLiteral(1))]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))
    def test_with_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))
    def test_with_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b'))),CallStmt(Id(r'foo'),[]),CallStmt(Id(r'foo1'),[Id(r'a'),Id(r'b'),Id(r'c')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    def test_with_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    with a , b : integer ; do begin
                        foo2(a,b,"anc");
                    end
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b'))),CallStmt(Id(r'foo'),[]),CallStmt(Id(r'foo1'),[Id(r'a'),Id(r'b'),Id(r'c')]),With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'foo2'),[Id(r'a'),Id(r'b'),StringLiteral(r'anc')])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))
    def test_with_statement4(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; do
                        foo2(a,b,"anc");
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'foo2'),[Id(r'a'),Id(r'b'),StringLiteral(r'anc')])])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,325))
    def test_for_statement1(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do s := s + 1;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1)))])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,326))
    def test_for_statement2(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) then s:=s-1;
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1))),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r's'),BinaryOp(r'-',Id(r's'),IntLiteral(1)))],[])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,327))
    def test_for_statement3(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do beGin
                            s := s + 1;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'm'),IntLiteral(1)),IntLiteral(100),False,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1))),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r's'),BinaryOp(r'-',Id(r's'),IntLiteral(1)))],[])])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,328))
    def test_for_statement4(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[While(BinaryOp(r'>',Id(r'i'),IntLiteral(1)),[For(Id(r'i'),BinaryOp(r'+',Id(r'm'),IntLiteral(1)),IntLiteral(10),False,[While(BinaryOp(r'>',Id(r'j'),IntLiteral(1)),[Assign(Id(r'x'),CallExpr(Id(r'foo'),[IntLiteral(10)]))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))
    def test_break_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))
    def test_continue_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do continuE ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))
    def test_return_statement1(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do reTuRn ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))
    def test_return_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1) do reTuRn foo(a+1);
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Return(CallExpr(Id(r'foo'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1))]))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))
    def test_compound_statement(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1=1) do begin eND
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[While(BinaryOp(r'=',IntLiteral(1),IntLiteral(1)),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))
    def test_call_statement1(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1))]),CallStmt(Id(r'foo1'),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))
    def test_call_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1)),BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(1))]),Return(IntLiteral(1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,336))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo1();
                   END"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,337))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),CallExpr(Id(r'foo'),[CallExpr(Id(r'foo1'),[CallExpr(Id(r'foo'),[IntLiteral(2),BinaryOp(r'+',Id(r'a'),IntLiteral(1))])])])]),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_call_statement4(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    textbackground(brown); {background colour}
                    ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    return func(a(1,2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'textbackground'),[Id(r'brown')]),CallStmt(Id(r'ClrScr'),[]),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_multi1(self):
        input = """
                procedure test1() ;
                begin
                   if a=b then
                   begin
                         b := c ;
                         if(e <> f) then foo(a,c) ;
                   end
                end
                """
        expect = str(Program([FuncDecl(Id(r'test1'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),Id(r'c')),If(BinaryOp(r'<>',Id(r'e'),Id(r'f')),[CallStmt(Id(r'foo'),[Id(r'a'),Id(r'c')])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))
    def test_multi2(self):
        input = """
                procedure test2() ;
                begin
                   if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = str(Program([FuncDecl(Id(r'test2'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[While(BinaryOp(r'=',Id(r'd'),Id(r'e')),[])],[Assign(Id(r'c'),IntLiteral(1))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))
    def test_multi3(self):
        input = """
                var i: integer ;
                function f(): integer ;
                begin
                   return 200;
                end
                procedure main() ;
                var
                   main: integer ;
                begin
                   main := f() ;
                   putIntLn(main);
                   with
                        i: integer;
                        main: integer;
                        f: integer;
                   do begin
                        main := f := i:= 100;
                        putIntLn (i);
                        putIntLn (main );
                        putIntLn (f);
                   end
                   putIntLn (main);
                end
                var g: real ;
                """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'f'),[],[],[Return(IntLiteral(200))],IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'main'),IntType())],[Assign(Id(r'main'),CallExpr(Id(r'f'),[])),CallStmt(Id(r'putIntLn'),[Id(r'main')]),With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'main'),IntType()),VarDecl(Id(r'f'),IntType())],[Assign(Id(r'i'),IntLiteral(100)),Assign(Id(r'f'),Id(r'i')),Assign(Id(r'main'),Id(r'f')),CallStmt(Id(r'putIntLn'),[Id(r'i')]),CallStmt(Id(r'putIntLn'),[Id(r'main')]),CallStmt(Id(r'putIntLn'),[Id(r'f')])]),CallStmt(Id(r'putIntLn'),[Id(r'main')])],VoidType()),VarDecl(Id(r'g'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,342))
    def test_multi4(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = str(Program([FuncDecl(Id(r'Hello'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[Assign(Id(r'a'),BinaryOp(r'+',Id(r'b'),Id(r'c'))),CallStmt(Id(r'writeln'),[StringLiteral(r'Hello, world!')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_multi5(self):
        input = """
                Var
                    Num1, Num2, Sum : Integer;
                Procedure concaheo(a, c:Real);
                Begin {no semicolon}
                    Write("nhap so 1:");
                    Readln(Num1);
                    Writeln("nhap so 2:");
                    Readln(Num2);
                    Sum := Num1 + Num2; {phep cong}
                    Write(Sum);
                    Readln();
                End
        """
        expect = str(Program([VarDecl(Id(r'Num1'),IntType()),VarDecl(Id(r'Num2'),IntType()),VarDecl(Id(r'Sum'),IntType()),FuncDecl(Id(r'concaheo'),[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'Write'),[StringLiteral(r'nhap so 1:')]),CallStmt(Id(r'Readln'),[Id(r'Num1')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'nhap so 2:')]),CallStmt(Id(r'Readln'),[Id(r'Num2')]),Assign(Id(r'Sum'),BinaryOp(r'+',Id(r'Num1'),Id(r'Num2'))),CallStmt(Id(r'Write'),[Id(r'Sum')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_multi6(self):
        input = """
                Var name, surname: String;
                Procedure Main();
                Begin
                   write("Nhap ten cua ban:");
                   readln(name);
                   write("Nhap ho cua ban:");
                   readln(surname);
                   writeln();(*new line*)
                   writeln();//new line}
                   writeln("Ten day du cua ban la : ",name," ",surname);
                   readln();
                End
                """
        expect = str(Program([VarDecl(Id(r'name'),StringType()),VarDecl(Id(r'surname'),StringType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Nhap ten cua ban:')]),CallStmt(Id(r'readln'),[Id(r'name')]),CallStmt(Id(r'write'),[StringLiteral(r'Nhap ho cua ban:')]),CallStmt(Id(r'readln'),[Id(r'surname')]),CallStmt(Id(r'writeln'),[]),CallStmt(Id(r'writeln'),[]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ten day du cua ban la : '),Id(r'name'),StringLiteral(r' '),Id(r'surname')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_multi7(self):
        input = """
                Var PD, Dname, Cmodel : String;
                CostPD, TCostPD, Distance : Real;
                {real is a decimal (described later on)}
                Procedure main();
                Begin
                    textbackground(brown); {background colour}
                    ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    TextColor(lightgreen); {text colour}
                    TCostPD := 0;
                    Writeln("This program prompts you to input the cost per litre of");
                    Writeln("the petrol/diesel you spend in and the average distance you travel");
                    Writeln("with your car every week. Then, the computer calculates the total cost");
                    Writeln("you spend in fuel every week.");
                    Readkey(); {program move on as soon as a key is pressed}
                    ClrScr(); {short for clear screen}
                    GotoXy(28,3); {move to a position on the screen: x (horizontal), y (vertical)}
                    Readln();
                End
        """
        expect = str(Program([VarDecl(Id(r'PD'),StringType()),VarDecl(Id(r'Dname'),StringType()),VarDecl(Id(r'Cmodel'),StringType()),VarDecl(Id(r'CostPD'),FloatType()),VarDecl(Id(r'TCostPD'),FloatType()),VarDecl(Id(r'Distance'),FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'textbackground'),[Id(r'brown')]),CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'TextColor'),[Id(r'lightgreen')]),Assign(Id(r'TCostPD'),IntLiteral(0)),CallStmt(Id(r'Writeln'),[StringLiteral(r'This program prompts you to input the cost per litre of')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'the petrol/diesel you spend in and the average distance you travel')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'with your car every week. Then, the computer calculates the total cost')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'you spend in fuel every week.')]),CallStmt(Id(r'Readkey'),[]),CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'GotoXy'),[IntLiteral(28),IntLiteral(3)]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))
    def test_multi8(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 return ;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(10)),CallStmt(Id(r'foo'),[]),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))
    def test_multi9(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[Assign(Id(r'e'),Id(r'f'))],[Assign(Id(r'i'),IntLiteral(1))])],[Assign(Id(r'x'),IntLiteral(2))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))
    def test_multi10(self):
        input = """
                procedure main() ;
                var a: array[0 .. -1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n - 2 do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then beGin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),ArrayType(0,-1,IntType())),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),IntLiteral(0),BinaryOp(r'-',Id(r'n'),IntLiteral(2)),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp(r'>',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'temp'))],[])])]),CallStmt(Id(r'print'),[Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))
    def test_multi11(self):
        input = """
                function sum_real_array(a: array[0 .. -1] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. -1] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
                """
        expect = str(Program([FuncDecl(Id(r'sum_real_array'),[VarDecl(Id(r'a'),ArrayType(0,-1,FloatType())),VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r's'),FloatType())],[Assign(Id(r's'),FloatLiteral(0.0)),For(Id(r'i'),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),IntLiteral(0),False,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),ArrayCell(Id(r'a'),Id(r'i'))))]),Return(Id(r's'))],FloatType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),ArrayType(0,-1,FloatType())),VarDecl(Id(r'n'),IntType())],[CallStmt(Id(r'Writeln'),[BinaryOp(r'+',StringLiteral(r'Sum of real array: '),CallExpr(Id(r'sum_real_array'),[Id(r'a'),Id(r'n')]))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))
    def test_multi12(self):
        input = """
                Procedure NhapMang1C(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("So luong phan tu:");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("Nhap phan tu thu", i," ");
                        Readln( A[i] );
                    End
                End
                """
        expect = str(Program([FuncDecl(Id(r'NhapMang1C'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'Write'),[StringLiteral(r'So luong phan tu:')]),CallStmt(Id(r'Readln'),[Id(r'N')]),For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[CallStmt(Id(r'Write'),[StringLiteral(r'Nhap phan tu thu'),Id(r'i'),StringLiteral(r' ')]),CallStmt(Id(r'Readln'),[ArrayCell(Id(r'A'),Id(r'i'))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))
    def test_multi13(self):
        input = """
                Function Tong_So_Chia_Het_Cho5(A:array[0 .. 10] of integer ; N:Integer):Integer;
                Var S,i :Integer;
                Begin
                    S:=0;
                    For i:=0 to N do
                    If(A[i] mod 5=0) then
                    S := S+A[i];
                    return S;
                End
                """
        expect = str(Program([FuncDecl(Id(r'Tong_So_Chia_Het_Cho5'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'S'),IntType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'S'),IntLiteral(0)),For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',BinaryOp(r'mod',ArrayCell(Id(r'A'),Id(r'i')),IntLiteral(5)),IntLiteral(0)),[Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),ArrayCell(Id(r'A'),Id(r'i'))))],[])]),Return(Id(r'S'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,352))
    def test_multi14(self):
        input = """
                Function LaSoNT(N:Integer) :Integer;
                Var i:Integer;
                Begin
                 For i:=2 to N-1 do
                  If(N mod i = 0) then
                    return 0;
                  Else
                    return 1;
                End
                """
        expect = str(Program([FuncDecl(Id(r'LaSoNT'),[VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(2),BinaryOp(r'-',Id(r'N'),IntLiteral(1)),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'N'),Id(r'i')),IntLiteral(0)),[Return(IntLiteral(0))],[Return(IntLiteral(1))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,353))
    def test_multi15(self):
        input = """
                Function DemPtuX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=0 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = str(Program([FuncDecl(Id(r'DemPtuX'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'X'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'Count'),IntType())],[Assign(Id(r'Count'),IntLiteral(0)),For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',ArrayCell(Id(r'A'),Id(r'i')),Id(r'X')),[Assign(Id(r'Count'),BinaryOp(r'+',Id(r'Count'),IntLiteral(1)))],[])]),Return(Id(r'Count'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))
    def test_multi16(self):
        input = """
                Procedure ThayTheTatCa (A:array[0 .. 10] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { Tim thay x ==> thay the thanh y }
                  A[i] := y;
                End
                """
        expect = str(Program([FuncDecl(Id(r'ThayTheTatCa'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',ArrayCell(Id(r'A'),Id(r'i')),Id(r'x')),[Assign(ArrayCell(Id(r'A'),Id(r'i')),Id(r'y'))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))
    def test_multi17(self):
        input = """
                Procedure ThayTheBangTong(A:array[0 .. 10] of integer; N:Integer; X, Y:Integer);
                Var i,k:Integer;
                Begin
                 For i:=0 to N do
                 If( (A[i-1]+A[i]) mod 10 = 0) then
                 Begin
                  k := (A[i-1]+A[i]);
                  A[i-1] := k;
                  A[i] := k;
                 End
                End
                """
        expect = str(Program([FuncDecl(Id(r'ThayTheBangTong'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'k'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',BinaryOp(r'mod',BinaryOp(r'+',ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),ArrayCell(Id(r'A'),Id(r'i'))),IntLiteral(10)),IntLiteral(0)),[Assign(Id(r'k'),BinaryOp(r'+',ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),ArrayCell(Id(r'A'),Id(r'i')))),Assign(ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),Id(r'k')),Assign(ArrayCell(Id(r'A'),Id(r'i')),Id(r'k'))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))
    def test_multi18(self):
        input = """
                Function KtraDoiXung (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                 return flag;
                End
                """
        expect = str(Program([FuncDecl(Id(r'KtraDoiXung'),[VarDecl(Id(r'A'),ArrayType(0,10,FloatType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Flag'),BooleanLiteral(True)),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'+',BinaryOp(r'-',Id(r'N'),Id(r'i')),IntLiteral(1)))),[Assign(Id(r'Flag'),BooleanLiteral(False))],[])]),Return(Id(r'flag'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,357))
    def test_multi19(self):
        input = """
                Function KtraMangTang ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                Begin
                 Flag := True;
                 i:= 0;
                 while(i<n) do begin
                  If(A[i] < A[i-1]) Then
                   Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                  i:=i+1;
                 end
                 return Flag;
                End
                """
        expect = str(Program([FuncDecl(Id(r'KtraMangTang'),[VarDecl(Id(r'A'),ArrayType(0,10,FloatType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Flag'),BooleanLiteral(True)),Assign(Id(r'i'),IntLiteral(0)),While(BinaryOp(r'<',Id(r'i'),Id(r'n')),[If(BinaryOp(r'<',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1)))),[Assign(Id(r'Flag'),BooleanLiteral(False))],[]),Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)))]),Return(Id(r'Flag'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,358))
    def test_multi20(self):
        input = """
                Function KtraMangCapSoCong (A:Integer;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                 for i:=1 to N do
                 if(A[i] <> A[i-1] + k) then
                  flag:=false;     // Cham dut, ket qua: khong phai
                 return flag; {Ket qua kiem tra la mang cap so cong}
                End
                """
        expect = str(Program([FuncDecl(Id(r'KtraMangCapSoCong'),[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'k'),IntType())],[VarDecl(Id(r'flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'A'),Id(r'i')),BinaryOp(r'+',ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),Id(r'k'))),[Assign(Id(r'flag'),BooleanLiteral(False))],[])]),Return(Id(r'flag'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,359))
    def test_multi21(self):
        input = """
                Procedure ChenPhanTu(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
                Var i :Integer;
                Begin
                 For i:=N downto k+ 1 do
                  A[i] := A[i-1];
                 A[k] := X;
                End
                """
        expect = str(Program([FuncDecl(Id(r'ChenPhanTu'),[VarDecl(Id(r'A'),ArrayType(0,10,FloatType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'X'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),Id(r'N'),BinaryOp(r'+',Id(r'k'),IntLiteral(1)),False,[Assign(ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))))]),Assign(ArrayCell(Id(r'A'),Id(r'k')),Id(r'X'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    def test_multi22(self):
        input = """
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = str(Program([FuncDecl(Id(r'gt'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'=',Id(r'x'),IntLiteral(0)),[Return(IntLiteral(1))],[Return(BinaryOp(r'*',Id(r'x'),CallExpr(Id(r'gt'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,361))
    def test_multi23(self):
        input = """
                function fibo(x: integer): integer;
                var f1,f2: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = str(Program([FuncDecl(Id(r'fibo'),[VarDecl(Id(r'x'),IntType())],[VarDecl(Id(r'f1'),IntType()),VarDecl(Id(r'f2'),IntType())],[If(BinaryOp(r'<=',Id(r'x'),IntLiteral(2)),[Return(IntLiteral(1))],[Return(BinaryOp(r'+',CallExpr(Id(r'fibo'),[BinaryOp(r'-',Id(r'x'),IntLiteral(2))]),CallExpr(Id(r'fibo'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,362))
    def test_multi24(self):
        input = """
                function ok(i : integer):boolean;
                var k : integer;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end
                """
        expect = str(Program([FuncDecl(Id(r'ok'),[VarDecl(Id(r'i'),IntType())],[VarDecl(Id(r'k'),IntType())],[Assign(Id(r'ok'),BooleanLiteral(True)),For(Id(r'k'),IntLiteral(2),BinaryOp(r'div',Id(r'i'),IntLiteral(2)),True,[If(BinaryOp(r'=',CallExpr(Id(r'copy'),[Id(r's'),BinaryOp(r'+',BinaryOp(r'-',Id(r'i'),BinaryOp(r'*',IntLiteral(2),Id(r'k'))),IntLiteral(1)),Id(r'k')]),CallExpr(Id(r'copy'),[Id(r's'),BinaryOp(r'+',BinaryOp(r'-',Id(r'i'),Id(r'k')),IntLiteral(1)),Id(r'k')])),[Assign(Id(r'ok'),BooleanLiteral(False)),CallStmt(Id(r'exit'),[])],[])])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,363))
    def test_multi25(self):
        input = """
                Procedure Daoso(n: integer);
                Begin
                 Assign(f,fo);
                  Rewrite(f);
                 If n > 0 then
                  Begin
                  Write(f,n mod 10);
                  Daoso(n div 10);
                  End
                 Close(f);
                End
                """
        expect = str(Program([FuncDecl(Id(r'Daoso'),[VarDecl(Id(r'n'),IntType())],[],[CallStmt(Id(r'Assign'),[Id(r'f'),Id(r'fo')]),CallStmt(Id(r'Rewrite'),[Id(r'f')]),If(BinaryOp(r'>',Id(r'n'),IntLiteral(0)),[CallStmt(Id(r'Write'),[Id(r'f'),BinaryOp(r'mod',Id(r'n'),IntLiteral(10))]),CallStmt(Id(r'Daoso'),[BinaryOp(r'div',Id(r'n'),IntLiteral(10))])],[]),CallStmt(Id(r'Close'),[Id(r'f')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))
    def test_multi26(self):
        input = """
                Function UCLN(m,n:integer):integer;
                Begin
                 If(m=n) then RETURN m ;
                 else
                  If (m>n) then return UCLN(m-n,n);
                  else return UCLN(m,n-m);
                End
                """
        expect = str(Program([FuncDecl(Id(r'UCLN'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[],[If(BinaryOp(r'=',Id(r'm'),Id(r'n')),[Return(Id(r'm'))],[If(BinaryOp(r'>',Id(r'm'),Id(r'n')),[Return(CallExpr(Id(r'UCLN'),[BinaryOp(r'-',Id(r'm'),Id(r'n')),Id(r'n')]))],[Return(CallExpr(Id(r'UCLN'),[Id(r'm'),BinaryOp(r'-',Id(r'n'),Id(r'm'))]))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,365))
    def test_multi27(self):
        input = """
                Var r,dt,cv:real;
                pROCEDURE main() ;
                Begin
                 Clrscr();
                 Writeln("TINH DIEN TICH & CHU VI HINH TRON:");
                 Writeln("--------------------------------------------------");
                 Write ("Nhap ban kinh R="); readln(r);
                 dt:=pi*r*r;
                 cv:=2*pi*r;
                 Writeln("Dien tich hinh tron la:",dt);
                 Writeln("Chu vi hinh tron la:",cv);
                 Readln();
                End
                """
        expect = str(Program([VarDecl(Id(r'r'),FloatType()),VarDecl(Id(r'dt'),FloatType()),VarDecl(Id(r'cv'),FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Clrscr'),[]),CallStmt(Id(r'Writeln'),[StringLiteral(r'TINH DIEN TICH & CHU VI HINH TRON:')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'--------------------------------------------------')]),CallStmt(Id(r'Write'),[StringLiteral(r'Nhap ban kinh R=')]),CallStmt(Id(r'readln'),[Id(r'r')]),Assign(Id(r'dt'),BinaryOp(r'*',BinaryOp(r'*',Id(r'pi'),Id(r'r')),Id(r'r'))),Assign(Id(r'cv'),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(2),Id(r'pi')),Id(r'r'))),CallStmt(Id(r'Writeln'),[StringLiteral(r'Dien tich hinh tron la:'),Id(r'dt')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'Chu vi hinh tron la:'),Id(r'cv')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
    def test_multi28(self):
        input = """
                pROCEDURE main() ;
                Var a,b,x:real;
                Begin
                Clrscr();
                Writeln("GIAI PHUONG TRINH BAC NHAT: AX + B=0");
                Writeln("-------------------------------------------------------");
                Write ("Nhap a= "); readln(a);
                Write ("Nhap b= ");readln(b);
                If(a=0) then
                 If(b=0) then Writeln(" Phuong trinh co vo so nghiem");
                 Else writeln("Phuong tring vo nghiem");
                Else Writeln("Phuong trinh co nghiem x=",-b/a);
                Readln();
                End
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'x'),FloatType())],[CallStmt(Id(r'Clrscr'),[]),CallStmt(Id(r'Writeln'),[StringLiteral(r'GIAI PHUONG TRINH BAC NHAT: AX + B=0')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'-------------------------------------------------------')]),CallStmt(Id(r'Write'),[StringLiteral(r'Nhap a= ')]),CallStmt(Id(r'readln'),[Id(r'a')]),CallStmt(Id(r'Write'),[StringLiteral(r'Nhap b= ')]),CallStmt(Id(r'readln'),[Id(r'b')]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(0)),[If(BinaryOp(r'=',Id(r'b'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r' Phuong trinh co vo so nghiem')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong tring vo nghiem')])])],[CallStmt(Id(r'Writeln'),[StringLiteral(r'Phuong trinh co nghiem x='),BinaryOp(r'/',UnaryOp(r'-',Id(r'b')),Id(r'a'))])]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
    def test_multi29(self):
        input = """
                Var a,b,c,s,p: real;
                pROCEDURE main() ;
                Begin
                Clrscr();
                Writeln("BAI TOAN TAM GIAC:");
                Writeln("---------------------------------");
                Write("nhap a =");readln(a);
                Write("nhap b =");readln(b);
                Write("nhap c =");readln(c);
                If ((a+b)>c)and((b+c)>a)and((a+c)>b) then
                 Begin
                  p:=(a+b+c)/2;
                  s:=sqrt(p*(p-a)*(p-b)*(p-c));
                  Writeln("Chu vi tam giac:",2*p);
                  Writeln("Dien tich tam giac:",s);
                 End
                Else Writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
                Readln();
                End
                """
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r's'),FloatType()),VarDecl(Id(r'p'),FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Clrscr'),[]),CallStmt(Id(r'Writeln'),[StringLiteral(r'BAI TOAN TAM GIAC:')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'---------------------------------')]),CallStmt(Id(r'Write'),[StringLiteral(r'nhap a =')]),CallStmt(Id(r'readln'),[Id(r'a')]),CallStmt(Id(r'Write'),[StringLiteral(r'nhap b =')]),CallStmt(Id(r'readln'),[Id(r'b')]),CallStmt(Id(r'Write'),[StringLiteral(r'nhap c =')]),CallStmt(Id(r'readln'),[Id(r'c')]),If(BinaryOp(r'and',BinaryOp(r'and',BinaryOp(r'>',BinaryOp(r'+',Id(r'a'),Id(r'b')),Id(r'c')),BinaryOp(r'>',BinaryOp(r'+',Id(r'b'),Id(r'c')),Id(r'a'))),BinaryOp(r'>',BinaryOp(r'+',Id(r'a'),Id(r'c')),Id(r'b'))),[Assign(Id(r'p'),BinaryOp(r'/',BinaryOp(r'+',BinaryOp(r'+',Id(r'a'),Id(r'b')),Id(r'c')),IntLiteral(2))),Assign(Id(r's'),CallExpr(Id(r'sqrt'),[BinaryOp(r'*',BinaryOp(r'*',BinaryOp(r'*',Id(r'p'),BinaryOp(r'-',Id(r'p'),Id(r'a'))),BinaryOp(r'-',Id(r'p'),Id(r'b'))),BinaryOp(r'-',Id(r'p'),Id(r'c')))])),CallStmt(Id(r'Writeln'),[StringLiteral(r'Chu vi tam giac:'),BinaryOp(r'*',IntLiteral(2),Id(r'p'))]),CallStmt(Id(r'Writeln'),[StringLiteral(r'Dien tich tam giac:'),Id(r's')])],[CallStmt(Id(r'Writeln'),[Id(r'a'),StringLiteral(r', '),Id(r'b'),StringLiteral(r', '),Id(r'c'),StringLiteral(r' khong phai la ba canh cua tam giac')])]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))
    def test_multi30(self):
        input = """
                Procedure DrawLine(X : Integer; Y : Integer);
                { the declaration of the variables in brackets are called parameters }
                Var Counter : Integer; { this is called a local variable }
                Begin
                 GotoXy(X,Y); {here I use the arguments of X and Y}
                 textcolor(green);
                 For Counter := 1 to 10 do
                 Begin
                  Write(chr(196));
                 End
                End
                procedure main();
                Begin
                 DrawLine(10,5);
                 DrawLine(10,6);
                 DrawLine(10,7);
                 DrawLine(10,10);
                 Readkey();
                End
                """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'GotoXy'),[Id(r'X'),Id(r'Y')]),CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(r'DrawLine'),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    def test_multi33(self):
        input= """
                Procedure InSoLanXHcuaPTu( A:array[-11 .. -15] of REAL; N: Integer);
                Var i :Integer;
                Begin
                 For i:=0 to N do
                  Writeln( A[i],"  ===>  ", DemPtuX( A, N, A[i]));
                End"""
        expect = str(Program([FuncDecl(Id(r'InSoLanXHcuaPTu'),[VarDecl(Id(r'A'),ArrayType(-11,-15,FloatType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(0),Id(r'N'),True,[CallStmt(Id(r'Writeln'),[ArrayCell(Id(r'A'),Id(r'i')),StringLiteral(r'  ===>  '),CallExpr(Id(r'DemPtuX'),[Id(r'A'),Id(r'N'),ArrayCell(Id(r'A'),Id(r'i'))])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    def test_multi34(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,371))
    def test_multi35(self):
        input= """
                Procedure XoaPhanTu( A:array[-10 .. 10] of sTRIng; N:Integer; k:sTRIng);
                Var i :Integer;
                Begin
                 For  i:=k to N-1 do
                  A[i] := A[i+1];
                End
                """
        expect = str(Program([FuncDecl(Id(r'XoaPhanTu'),[VarDecl(Id(r'A'),ArrayType(-10,10,StringType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'k'),StringType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),Id(r'k'),BinaryOp(r'-',Id(r'N'),IntLiteral(1)),True,[Assign(ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'+',Id(r'i'),IntLiteral(1))))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
    def test_multi36(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,373))
    def test_multi37(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,374))
    def test_multi38(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,375))
    def test_multi39(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,376))
    def test_multi40(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,377))
    def test_multi41(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,378))
    def test_multi42(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,379))
    def test_multi43(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,380))
    def test_multi44(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,381))
    def test_multi45(self):
        input= """
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
        self.assertTrue(TestAST.test(input,expect,382))
    def test_multi46(self):
         input= """
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
         self.assertTrue(TestAST.test(input,expect,383))
    def test_multi47(self):
         input= """
            procedure nestedPrime();
            var
             i, j:integer;
            begin
             for i := 2 to 50 do
             begin
              for j := 2 to i do
               if (i mod j)=0 then
               break; {* if factor found, not prime *}
               if(j = i) then
               writeln(i , " is prime" );
             end
            end"""
         expect = str(Program([FuncDecl(Id(r'nestedPrime'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[For(Id(r'i'),IntLiteral(2),IntLiteral(50),True,[For(Id(r'j'),IntLiteral(2),Id(r'i'),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'i'),Id(r'j')),IntLiteral(0)),[Break()],[])]),If(BinaryOp(r'=',Id(r'j'),Id(r'i')),[CallStmt(Id(r'writeln'),[Id(r'i'),StringLiteral(r' is prime')])],[])])],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,384))
    def test_multi48(self):
         input= """
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
         self.assertTrue(TestAST.test(input,expect,385))
    def test_multi49(self):
         input= """
            procedure swap(x, y: integer);
            var
             temp: integer;
            begin
             temp := 1;
             x:= y;
             y := temp;
            end
            """
         expect = str(Program([FuncDecl(Id(r'swap'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'temp'),IntType())],[Assign(Id(r'temp'),IntLiteral(1)),Assign(Id(r'x'),Id(r'y')),Assign(Id(r'y'),Id(r'temp'))],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,386))
    def test_multi50(self):
         input= """
            procedure convertFromDemicaltoHex();
            Var
            n, k: Integer;
            CTLP: String;
            Begin
             WriteLn("Hay nhap so can doi tu he 10 sang he 16");
             ReadLn(n);
             k := n;
             While k>0 do Begin
              If k mod 16 = 0 then CTLP:="0"+CTLP ;
              Else If k mod 16 = 1 then CTLP:="1"+CTLP;
              Else If k mod 16 = 2 then CTLP:="2"+CTLP;
              Else If k mod 16 = 3 then CTLP:="3"+CTLP;
             end
            end
            """
         expect = str(Program([FuncDecl(Id(r'convertFromDemicaltoHex'),[],[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'CTLP'),StringType())],[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Hay nhap so can doi tu he 10 sang he 16')]),CallStmt(Id(r'ReadLn'),[Id(r'n')]),Assign(Id(r'k'),Id(r'n')),While(BinaryOp(r'>',Id(r'k'),IntLiteral(0)),[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'k'),IntLiteral(16)),IntLiteral(0)),[Assign(Id(r'CTLP'),BinaryOp(r'+',StringLiteral(r'0'),Id(r'CTLP')))],[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'k'),IntLiteral(16)),IntLiteral(1)),[Assign(Id(r'CTLP'),BinaryOp(r'+',StringLiteral(r'1'),Id(r'CTLP')))],[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'k'),IntLiteral(16)),IntLiteral(2)),[Assign(Id(r'CTLP'),BinaryOp(r'+',StringLiteral(r'2'),Id(r'CTLP')))],[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'k'),IntLiteral(16)),IntLiteral(3)),[Assign(Id(r'CTLP'),BinaryOp(r'+',StringLiteral(r'3'),Id(r'CTLP')))],[])])])])])],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,387))
    def test_multi51(self):
         input= """
            procedurE foo (b : real) ;
            var
             a : array [2 .. 3] of integer;
             b: real;
             e: real;
             f: boolean;
            begin
             while(a=4) and (b=6+8-9-5 or 2) do
             e:=4;
            End
            """
         expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'and',BinaryOp(r'=',Id(r'a'),IntLiteral(4)),BinaryOp(r'=',Id(r'b'),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(6),IntLiteral(8)),IntLiteral(9)),IntLiteral(5)),IntLiteral(2)))),[Assign(Id(r'e'),IntLiteral(4))])],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,388))
    def test_multi52(self):
         input= """
            procedurE foo (b : real) ;
            var
            a : array [2 .. 3] of integer;
            b: string;
            e: real;
            f: boolean;
            begin
            while(a=4) and (c=4) do
            for i:=4 downto 3+3 do
                for i:=5 to 9+9 do
                    if(a=3) and (a=True) then
                    e:=5;
            End
            """
         expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'and',BinaryOp(r'=',Id(r'a'),IntLiteral(4)),BinaryOp(r'=',Id(r'c'),IntLiteral(4))),[For(Id(r'i'),IntLiteral(4),BinaryOp(r'+',IntLiteral(3),IntLiteral(3)),False,[For(Id(r'i'),IntLiteral(5),BinaryOp(r'+',IntLiteral(9),IntLiteral(9)),True,[If(BinaryOp(r'and',BinaryOp(r'=',Id(r'a'),IntLiteral(3)),BinaryOp(r'=',Id(r'a'),BooleanLiteral(True))),[Assign(Id(r'e'),IntLiteral(5))],[])])])])],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,389))
    def test_multi53(self):
         input= """
            procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End
            """
         expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[],[Assign(ArrayCell(IntLiteral(1),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(BinaryOp(r'>=',IntLiteral(1),IntLiteral(0)),IntLiteral(2)),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',IntLiteral(2),ArrayCell(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1))),Id(r'c')),BinaryOp(r'<',StringLiteral(r'abc'),IntLiteral(0)))),Assign(ArrayCell(CallExpr(Id(r'ahihi'),[IntLiteral(1)]),BinaryOp(r'+',Id(r'm'),IntLiteral(1))),IntLiteral(3)),Assign(ArrayCell(BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),ArrayCell(Id(r'a'),IntLiteral(1))),BinaryOp(r'<',IntLiteral(1),IntLiteral(0))),IntLiteral(10)),IntLiteral(4))],VoidType())]))
         self.assertTrue(TestAST.test(input,expect,390))
    def test_multi54(self):
        """ Test Assign Statment """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),BinaryOp(r'-',BinaryOp(r'+',Id(r'f'),ArrayCell(Id(r'y'),IntLiteral(2))),BinaryOp(r'*',ArrayCell(Id(r'h'),ArrayCell(Id(r't'),BinaryOp(r'+',IntLiteral(5),Id(r'j')))),IntLiteral(4))))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 391))
    def test_multi55(self):
        """ Test Associative """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    a := b + 2 + n or 4 + 5 - g or 2 - 9;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'or',BinaryOp(r'+',BinaryOp(r'+',Id(r'b'),IntLiteral(2)),Id(r'n')),IntLiteral(4)),IntLiteral(5)),Id(r'g')),IntLiteral(2)),IntLiteral(9)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 392))
    def test_multi56(self):
        """ Test Associative """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    a := b / 2 * n / 4 div 5 mod g and 2 * 9 / 4 mod 2;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'mod',BinaryOp(r'/',BinaryOp(r'*',BinaryOp(r'and',BinaryOp(r'mod',BinaryOp(r'div',BinaryOp(r'/',BinaryOp(r'*',BinaryOp(r'/',Id(r'b'),IntLiteral(2)),Id(r'n')),IntLiteral(4)),IntLiteral(5)),Id(r'g')),IntLiteral(2)),IntLiteral(9)),IntLiteral(4)),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 393))
    def test_multi57(self):
        """ Test Precedence """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'div',BinaryOp(r'*',UnaryOp(r'not',UnaryOp(r'-',Id(r'F'))),Id(r'G')),IntLiteral(5)),BinaryOp(r'*',BinaryOp(r'and',BinaryOp(r'or',BinaryOp(r'+',BinaryOp(r'or',Id(r'I'),BinaryOp(r'and',Id(r'L'),Id(r'N'))),Id(r'Y')),BinaryOp(r'*',Id(r'Q'),UnaryOp(r'not',UnaryOp(r'-',Id(r'P'))))),IntLiteral(6)),IntLiteral(5))),BinaryOp(r'div',Id(r'O'),UnaryOp(r'not',BinaryOp(r'mod',IntLiteral(5),Id(r'T'))))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_multi58(self):
        """ Test Associative """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<=',BinaryOp(r'>=',BinaryOp(r'<',BinaryOp(r'<>',IntLiteral(5),IntLiteral(6)),BinaryOp(r'=',IntLiteral(6),IntLiteral(5))),BinaryOp(r'>',BinaryOp(r'+',IntLiteral(4),IntLiteral(5)),IntLiteral(1))),IntLiteral(1)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_multi59(self):
        """ Test Associative """
        input = """
                procedure foo();
                var
                    a: real;
                begin
                    a := TRUE and then FALSE or else True or else (1 and then 2) ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'orelse',BinaryOp(r'orelse',BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BinaryOp(r'andthen',IntLiteral(1),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_multi60(self):
        """ Test If Statement """
        input = """
                procedure foo();
                var a: real;
                begin
                    if a = 1 then begin
                        if b > 3 then c := 5;
                        else d := 1;

                        if e < 4 then ok();
                    end else begin
                        if h > 5 then nty(); else lyo();
                        g := 5;
                    end
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[If(BinaryOp(r'>',Id(r'b'),IntLiteral(3)),[Assign(Id(r'c'),IntLiteral(5))],[Assign(Id(r'd'),IntLiteral(1))]),If(BinaryOp(r'<',Id(r'e'),IntLiteral(4)),[CallStmt(Id(r'ok'),[])],[])],[If(BinaryOp(r'>',Id(r'h'),IntLiteral(5)),[CallStmt(Id(r'nty'),[])],[CallStmt(Id(r'lyo'),[])]),Assign(Id(r'g'),IntLiteral(5))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 397))
    def test_multi61(self):
        """ Test For Statment """
        input = """
                procedure foo();
                var a: real;
                begin
                    for i := 1 to 10 do begin
                        for j := i downto 1 do
                            if (i + j) mod 2 = 1 then break;
                    end
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[For(Id(r'j'),Id(r'i'),IntLiteral(1),False,[If(BinaryOp(r'=',BinaryOp(r'mod',BinaryOp(r'+',Id(r'i'),Id(r'j')),IntLiteral(2)),IntLiteral(1)),[Break()],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 398))
    def test_multi63(self):
        """ Test For Statment """
        input = """
                Function a(a:integer):real;
                Begin
                if true then
                if false then b:= b+1;
                else
                if true then a:= a+ 1;
                else
                b:= b + 1;
                end
                """
        expect = str(Program([FuncDecl(Id(r'a'),[VarDecl(Id(r'a'),IntType())],[],[If(BooleanLiteral(True),[If(BooleanLiteral(False),[Assign(Id(r'b'),BinaryOp(r'+',Id(r'b'),IntLiteral(1)))],[If(BooleanLiteral(True),[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))],[Assign(Id(r'b'),BinaryOp(r'+',Id(r'b'),IntLiteral(1)))])])],[])],FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_multi64(self):
        """ Test For Statment """
        input = """
                procedure abc ();
                var x , y : real ;
                    begin
                        if x = y then
                           a:= 1000;
                        else
                            b:= 999;
                    end
                """
        expect = str(Program([FuncDecl(Id(r'abc'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[If(BinaryOp(r'=',Id(r'x'),Id(r'y')),[Assign(Id(r'a'),IntLiteral(1000))],[Assign(Id(r'b'),IntLiteral(999))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 400))
    def test_multi65(self):
        """ Test For Statment """
        input = """
                var main:Integer;
                procedure main();
                begin
                     main := f();
                     return ;
                end
                """
        expect = str(Program([VarDecl(Id(r'main'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'main'),CallExpr(Id(r'f'),[])),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 401))
