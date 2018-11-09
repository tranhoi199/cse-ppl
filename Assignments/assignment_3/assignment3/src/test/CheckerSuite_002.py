import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclared_variable1(self):
        """test_redeclared_variable1"""
        input = """
procedure main();
var A,a:integer;  // error
begin
end
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable2(self):
        """test_redeclared_variable2"""
        input = """
procedure main();
var a,b:integer;
    a:real;  // error
begin
end
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable3(self):
        """test_redeclared_variable3"""
        input = """
procedure Main();
var a,b:integer;
begin
end

var main:real;  // error
"""
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable4(self):
        """test_redeclared_variable4"""
        input = """
function FOO():integer;
begin
    return 0;
end

var foo:string;  // error

var temp:integer;

procedure main();
begin
    temp := foo();
end
"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable5(self):
        """test_redeclared_variable5"""
        input = """
function foo(a:real):integer;
var foo:string;
    A: integer;  // error
begin
    return 0;
end

procedure main();
var x:real;
    y:integer;
begin
    y := foo(x);
end
"""
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable6(self):
        """test_redeclared_variable6"""
        input = """
procedure main();
begin
    with
        a,b:integer;
        A:string;  // error
    do
        b:=0;
end
"""
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable7(self):
        """test_redeclared_variable7"""
        input = """
var a:integer;
procedure main();
var a:integer;
begin
    with
        a,Main:integer;
    do
        with
            a,MAIN:real;
            main:integer;  // error
        do
            return;
end
"""
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable8(self):
        """test_redeclared_variable8"""
        input = """
procedure main();
var putIntLn: array[1 .. 3] of real;
begin 
end
var putfloatln:real;  // error
"""
        expect = "Redeclared Variable: putfloatln"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_function1(self):
        """test_redeclared_function1"""
        input = """
procedure main();
var putIntLn: array[1 .. 3] of real;
begin
    call();
end

function MaIn(a,b:integer;c,d:real):real;  // error
begin
    return 1.1;
end

procedure call();
var s:real;
begin
    s:=main(1,2,1.1,2.2);
end
"""
        expect = "Redeclared Function: MaIn"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_procedure1(self):
        """test_redeclared_procedure1"""
        input = """
procedure main();
var a: real;
begin
    with
        a: integer;
    do
        with
            a:string;
        do
            begin
            end
end

procedure MAIN();  // error
begin
end
"""
        expect = "Redeclared Procedure: MAIN"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_identifier1(self):
        """test_undeclared_identifier1"""
        input = """
procedure main();
var a:integer;
begin
    putIntLn(1);
    a:= 1998;
    b:=1998;  // error
end
"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_identifier2(self):
        """test_undeclared_identifier2"""
        input = """
var x:integer;
    
function foo():real;
begin
    return x;
end

procedure main();
var x:real;
begin
    x:=foo();
    x:= foo + 1;  // error
end
"""
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_function1(self):
        """test_undeclared_function1"""
        input = """
procedure main();
var x:integer;
begin
    x:=getint();
    x:=foo(1,2.2,x,y);  // error
end
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_function2(self):
        """test_undeclared_function2"""
        input = """
var boolFunc:boolean;

procedure main();
begin
    putintln(1);
    if boolFunc() then  // error
        return;
    else
        putstringln("hello world !");
end
"""
        expect = "Undeclared Function: boolFunc"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_procedure(self):
        """test_undeclared_procedure"""
        input = """
procedure main();
var x:real;
begin
    x := getfloat();
    putfloat(x);
    x(1);  // error
end
"""
        expect = "Undeclared Procedure: x"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_if_condition_must_be_boolean(self):
        """test_if_condition_must_be_boolean"""
        input = """
procedure main();
var x:real;
begin
    if false then
        if x then  // error
            begin
            end
end
"""
        expect = "Type Mismatch In Statement: If(Id(x),[],[])"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_id_in_for_must_be_integer(self):
        """test_id_in_for_must_be_integer"""
        input = """
procedure main();
var x:real;
    y:integer;
begin
    for y:=0 to 10 do
        for x:=0 to 10 do  // error
            begin
            end
end
"""
        expect = "Type Mismatch In Statement: For(Id(x)IntLiteral(0),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_expr1_in_for_must_be_integer(self):
        """test_expr1_in_for_must_be_integer"""
        input = """
procedure main();
var x:integer;
begin
    for x:=0 to 10 do
        for x:=0.5 to 10 do  // error
            begin
            end
end
"""
        expect = "Type Mismatch In Statement: For(Id(x)FloatLiteral(0.5),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_expr2_in_for_must_be_integer(self):
        """test_expr2_in_for_must_be_integer"""
        input = """
procedure main();
var x:integer;
begin
    for x:=0 to 10 do
        for x:=0 to 10.5 do  // error
            begin
            end
end
"""
        expect = "Type Mismatch In Statement: For(Id(x)IntLiteral(0),FloatLiteral(10.5),True,[])"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_id_in_for_must_be_local(self):
        """test_id_in_for_must_be_local"""
        input = """
var x:integer;

procedure main();
var y:integer;
    z:real;
begin
    for y:=0 to 10 do
        for x:=0 to 10 do
            for y:=z to x do  // error
                begin
                end
end
"""
        expect = "Type Mismatch In Statement: For(Id(y)Id(z),Id(x),True,[])"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_condition_in_while_must_be_boolean(self):
        """test_condition_in_while_must_be_boolean"""
        input = """
procedure main();
begin
    while TRUE do
        begin
        end

    while 1 do  // error
        begin
        end
end
"""
        expect = "Type Mismatch In Statement: While(IntLiteral(1),[])"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_return_proc_must_no_expr(self):
        """test_return_proc_must_no_expr"""
        input = """
procedure proc();
begin
    return;
end

procedure main();
begin
    proc();
    return 0;  // error
end
"""
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_return_func_must_expr_with_proper_type1(self):
        """test_return_func_must_expr_with_proper_type1"""
        input = """
procedure main();
var ret:integer;
begin
    ret:=foo();
    ret:=foo1();
end

function foo1():integer;
begin
    return 1;
end

function foo():integer;
begin
    return 1.1;  // error
end
"""
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_return_func_must_expr_with_proper_type2(self):
        """test_return_func_must_expr_with_proper_type2"""
        input = """
procedure main();
var ret:real;
    b:boolean;
begin
    ret:=foo();
    b:=foo1();
end

function foo():real;
begin
    return 2*3-5;
end

function foo1():boolean;
begin
    return 0;  // error
end
"""
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_assign_stmt_lhs_must_not_string_type(self):
        """test_assign_stmt_lhs_must_not_string_type"""
        input = """
procedure MAIN();
var s:string;
    a:integer;
begin
    a:=1;
    s:="random string";  // error
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(s),StringLiteral(random string))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_assign_stmt_lhs_must_not_arr_type(self):
        """test_assign_stmt_lhs_must_not_arr_type"""
        input = """
function foo():array[0 .. 5] of string;
var arr:array[0 .. 5] of string;
begin
    return arr;
end

procedure MaIn();
var arr:array[0 .. 5] of string;
begin
    arr := foo();  // error
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_assign_stmt_type_lhs_and_rhs_must_be_compa(self):
        """test_assign_stmt_type_lhs_and_rhs_must_be_compa"""
        input = """
procedure MAIN();
var a,b:integer;
    c:real;
begin
    a:=b;
    c:=a;
    a:=c;  // error
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_assign_stmt_type_lhs_and_rhs_must_be_compa2(self):
        """test_assign_stmt_type_lhs_and_rhs_must_be_compa2"""
        input = """
procedure MAIN();
var a,b:integer;
    c:real;
begin
    a:=b;
    c:=a:=b;
    a:=c:=a;  // error
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_call_stmt_id_must_be_proc(self):
        """test_call_stmt_id_must_be_proc"""
        input = """
function foo():integer;
begin
    return 0;
end

procedure proc();
begin
end

procedure MaIn();
begin
    proc();
    foo();  // error
end
"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_call_stmt_param_len_must_be_the_same(self):
        """test_call_stmt_param_len_must_be_the_same"""
        input = """
procedure proc(a,b:integer);
begin
end

procedure MaIn();
begin
    proc(1 , 0);
    proc(1);  // error
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(proc),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_call_stmt_param_list_must_be_type_comp(self):
        """test_call_stmt_param_list_must_be_type_comp"""
        input = """
procedure proc(a,b:real);
begin
end

procedure MaIn();
begin
    proc(1.2 , 3);
    proc(1.2 , "string");  // error
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(proc),[FloatLiteral(1.2),StringLiteral(string)])"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_expr1_arr_must_be_array_type(self):
        """test_expr1_arr_must_be_array_type"""
        input = """
procedure MaIn();
var a:integer;
    arr:array[0 .. 4] of integer;
begin
    arr[0]:=1;
    a[0]:=1;  // error
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_expr2_arr_must_be_int_type(self):
        """test_expr2_arr_must_be_int_type"""
        input = """
procedure MaIn();
var a:array[0 .. 4] of real;
begin
    a[0]:=1.1;
    a[0.5]:=1.1;  // error
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(0.5))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_binary_expr1(self):
        """test_type_operand_expr1"""
        input = """
procedure MaIn();
var b,c:boolean;
begin
    b:= true and false;
    b:= b and then c;
    c:= b or c or else true;
    c:= b and 0;  // error
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_binary_expr2(self):
        """test_type_operand_expr2"""
        input = """
procedure MaIn();
var a,b:integer;
    c: real;
    d:boolean;
begin
    c:= b + 1;
    b:= 5 - 1;
    c:= b * c;
    c:= b div a;
    c:= b mod a;
    c:= c/b;
    d:= (a>=b) and (c<=b) or (a=c);
    a:= d + 0;  // error
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(d),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_binary_expr3(self):
        """test_type_operand_expr3"""
        input = """
procedure MaIn();
var b:integer;
    c: real;
begin
    b:= b div c;  // error
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(div,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_binary_expr4(self):
        """test_type_operand_expr4"""
        input = """
procedure foo(s:string);
begin
    return ;
end

procedure MaIn();
var a: integer;
begin
    foo("ss");
    foo("s"*2);  // error
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(*,StringLiteral(s),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_unary_expr1(self):
        """test_type_unary_expr1"""
        input = """
procedure MaIn();
var s: string;
    a: integer;
begin
    putintln(-a);
    putstring(-s);  // error
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(s))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_unary_expr2(self):
        """test_type_unary_expr2"""
        input = """
procedure MaIn();
var b: boolean;
    a: integer;
begin
    a:=-a;
    b:=b;
    b:=-b;  // error
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_unary_expr3(self):
        """test_type_unary_expr3"""
        input = """
procedure MaIn();
var b: boolean;
    a: integer;
begin
    b:=not b;
    a:=not a;  // error
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_unary_expr4(self):
        """test_type_unary_expr4"""
        input = """
procedure MaIn();
var b: boolean;
    s: sTRING;
begin
    b:=not B;
    putstring(not S);  // error
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(S))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_call_expr_id_must_be_func(self):
        """test_call_expr_id_must_be_func"""
        input = """
function foo():integer;
begin
    return getint();
end

procedure MaIn();
var a:integer;
begin
    a:=foo();
    a:=main();  // error
end
"""
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_call_expr_param_len_must_be_the_same(self):
        """test_call_expr_param_len_must_be_the_same"""
        input = """
function foo():real;
var a:integer;
begin
    return a;
end

procedure MaIn();
var a:real;
begin
    a := foo();
    a := foo(1,2,3);  // error
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_call_expr_param_list_must_be_type_comp(self):
        """test_call_expr_param_list_must_be_type_comp"""
        input = """
function foo(a:integer;b:real;c:strinG):boolean;
begin
    return (a*b - a/b) <= ((b / a+1) *getint());
end

procedure MaIn();
var a:boolean;
begin
    a := foo(1,2,"15gg");
    a := foo(1,2,3);  // error
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_func_not_return1(self):
        """test_func_not_return1"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo1();
end
        
function foo():boolean;
begin
    return 5*getint()/getfloat()>=1998.0;  //# return here
end

function foo1():boolean;  // error
begin
end
"""
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_func_not_return2(self):
        """test_func_not_return2"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo2();
end
        
function foo():boolean;
begin
    if True then
        return falsE;  //# return here
    else
        return true;  //# return here
end

function foo2():boolean;  // error
begin
    if True then
        return falsE;
    else  //# no return
        begin
        end
end
"""
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_func_not_return3(self):
        """test_func_not_return3"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo3();
end
        
function foo():boolean;
begin
    if True then
        return falsE;  //# return here
    else
        return true;  //# return here
end

function foo3():boolean;  // error
begin
    if True then  //# no return
        begin
        end
    else
        return True;
end
"""
        expect = "Function foo3Not Return "
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_func_not_return4(self):
        """test_func_not_return4"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo4();
end
        
function foo():boolean;
var a:integer;
begin
    if True then
        begin
        end
    else
        begin
        end
    a:=1;
    return true aNd THEN faLse;  //# return here
end

function foo4():boolean;  // error
var a:integer;
begin
    if True then
        begin
        end
    else
        begin
        end
    a:=1;
end
"""
        expect = "Function foo4Not Return "
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_func_not_return5(self):
        """test_func_not_return5"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo5();
end
        
function foo():boolean;
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return a=9.9;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return 1.2<=1.20;  //# return here
        end
end

function foo5():boolean;  // error
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return a=9.9;
        end
    else  //# no return
        begin
            a:=0;
            putintln(69);
        end
end
"""
        expect = "Function foo5Not Return "
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_func_not_return6(self):
        """test_func_not_return6"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo6();
end
        
function foo():boolean;
var a:integer;
begin
    with
        a,b:real;
        c:string;
    do
        begin
            a:=b;
            putstring(c);
            return a > b/2;  //# return here
        end
end

function foo6():boolean;  // error
var a:integer;
begin
    with
        a,b:real;
        c:string;
    do
        begin
            a:=b;
            putstring(c);
        end
end
"""
        expect = "Function foo6Not Return "
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_func_not_return7(self):
        """test_func_not_return7"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo7();
end
        
function foo():boolean;
var a:integer;
begin
    while foo() do
        return True or else a = 0;
    return false;  //# return here
end

function foo7():boolean;  // error
var a:real;
begin
    while foo() do  //# no return
        return True or else a = 0;
end
"""
        expect = "Function foo7Not Return "
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_func_not_return8(self):
        """test_func_not_return8"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo8();
end

function foo():boolean;
var i:integer;
    f:real;
begin
    while foo() do
        begin
            i:=getint();
            f:=i/1;
            f:=getfloat();
            return True or else i = 0;
        end
    return True;  //# return here
end

function foo8():boolean;  // error
var i:integer;
    f:real;
begin
    while foo() do  //# no return
        begin
            i:=getint();
            f:=i/1;
            f:=getfloat();
            return True or else i = 0;
        end
end
"""
        expect = "Function foo8Not Return "
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_func_not_return9(self):
        """test_func_not_return9"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo9();
end

function foo():boolean;
var i:integer;
    f:real;
begin
    for i:=0 downtO -100 do
        return i=1998;
    return True;  //# return here
end

function foo9():boolean;  // error
var i:integer;
    f:real;
begin
    for i:=0 downtO -100 do  //# no return
        return i=1998;
end
"""
        expect = "Function foo9Not Return "
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_func_not_return10(self):
        """test_func_not_return10"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo10();
end

function foo():boolean;
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            while True do
                break;
                
            return false;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return 1.2<=1.20;  //# return here
        end
end

function foo10():boolean;  // error
var a:integer;
begin
    if True then  //# no return
        begin
            a:=a;
            putintln(a);
            while True do
                return true;

            for a:=0 downto a do
                begin
                    return false;
                end
        end
    else
        begin
            a:=0;
            putintln(69);
            return 1.2<=1.20;
        end
end
"""
        expect = "Function foo10Not Return "
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_func_not_return11(self):
        """test_func_not_return11"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo11();
end

function foo():boolean;
var a:integer;
begin
    while a = 1 do
        begin
            a:=0;
            if not (a=0) THEn
                return falSE;
            else
                return false or false;
        end
    return foo();  //# return here
end

function foo11():boolean;  // error
var a:integer;
begin
    while a = 1 do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end
end
"""
        expect = "Function foo11Not Return "
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_func_not_return12(self):
        """test_func_not_return12"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo12();
end

function foo():boolean;
var a:integer;
begin
    for a:=a to a do
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end
    return foo();  //# return here
end

function foo12():boolean;  // error
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end
end
"""
        expect = "Function foo12Not Return "
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_func_not_return13(self):
        """test_func_not_return13"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo13();
end

function foo():boolean;
var a:integer;
begin
    for a:=a to a do
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                continue;
                        end
                end
            return trUE;
        end
    return FALsE;  //# return here
end

function foo13():boolean;  // error
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                continue;
                        end
                end
            return trUE;
        end
end
"""
        expect = "Function foo13Not Return "
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_break_not_in_loop1(self):
        """test_break_not_in_loop1"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        break;
    
    for a:=a doWNtO 0 do
        break;
end

procedure MaIn();
begin
    foo();
    break;  // error
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_break_not_in_loop2(self):
        """test_break_not_in_loop2"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        if (1=2) or (a>=0.000000001000000000001) then
            break;
    
    for a:=a doWNtO 0 do
        if true or FalSe then
            break;
end

procedure MaIn();
begin
    foo();
    if (0.6/5>7) or not false then
        break;  // error
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_break_not_in_loop3(self):
        """test_break_not_in_loop3"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        with a:booleaN; do
            break;
    
    for a:=a doWNtO 0 do
        with a:booleaN; do
            break;
end

procedure MaIn();
begin
    foo();
    with a:booleaN; do
        break;  // error
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_break_not_in_loop4(self):
        """test_break_not_in_loop4"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        if 6*7-42>1 then
            with a:booleaN; do
                break;
    
    for a:=a doWNtO 0 do
        if 0mod 0>1 then
            with a:booleaN; do
                break;
end

procedure MaIn();
begin
    foo();
    if (3div 4=0) or (6=6.00) then
        with a:booleaN; do
            break;  // error
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_break_not_in_loop5(self):
        """test_break_not_in_loop5"""
        input = """
procedure MaIn();
begin
    if -5=0-5/1*3.14/ 3.14 then
        while getINT()=1.998 do
            begin
                break;
            end
    else
        begin
            with a:integer; do
                begin
                    for a:=getint() to getINT() do
                        break ;
                    begin
                        putINT(a);
                        break;  // error
                    end
                end
            return;
        end
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_continue_not_in_loop1(self):
        """test_continue_not_in_loop1"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        continue;
    
    for a:=a doWNtO 0 do
        continue;
end

procedure MaIn();
begin
    foo();
    continue;  // error
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_continue_not_in_loop2(self):
        """test_continue_not_in_loop2"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        if (1=2) or (a>=0.000000001000000000001) then
            Continue;
    
    for a:=a doWNtO 0 do
        if true or FalSe then
            Continue;
end

procedure MaIn();
begin
    foo();
    if (0.6/5>7) or not false then
        Continue;  // error
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_continue_not_in_loop3(self):
        """test_continue_not_in_loop3"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        with a:booleaN; do
            Continue;
    
    for a:=a doWNtO 0 do
        with a:booleaN; do
            Continue;
end

procedure MaIn();
begin
    foo();
    with a:booleaN; do
        Continue;  // error
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_continue_not_in_loop4(self):
        """test_continue_not_in_loop4"""
        input = """
procedure foo();
var a:integer;
begin
    while trUE do
        if 6*7-42>1 then
            with a:booleaN; do
                Continue;
    
    for a:=a doWNtO 0 do
        if 0mod 0>1 then
            with a:booleaN; do
                Continue;
end

procedure MaIn();
begin
    foo();
    if (3div 4=0) or (6=6.00) then
        with a:booleaN; do
            Continue;  // error
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_continue_not_in_loop5(self):
        """test_continue_not_in_loop5"""
        input = """
procedure MaIn();
begin
    if -5=0-5/1*3.14/ 3.14 then
        while getINT()=1.998 do
            begin
                Continue;
            end
    else
        begin
            with a:integer; do
                begin
                    for a:=getint() to getINT() do
                        Continue ;
                    begin
                        putINT(a);
                        Continue;  // error
                    end
                end
            return;
        end
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_continue_not_in_loop6(self):
        """test_continue_not_in_loop6"""
        input = """
var a:boolEAN;
procedure main();
begin
    a:=MaIn1();
    a:=maiN2();
end

function main2():booleaN;
var a: integer;
begin
    while true do
        begin
            if a=6.9 then
                begin
                    with
                        a,b: real;
                        C:array[1 .. 4] of integeR;
                        D:integer;
                    do
                        begin
                            a:=b/3;
                            b:=-b;
                            for d:=c[D] to D mod 0 do
                                break;
                            continue;
                        end
                end
            else
                begin
                end
        end
    return falSE;
end

function main1():booleaN;
var a: integer;
begin
    while true do
        begin
            if a=6.9 then
                begin
                    with
                        a,b: real;
                        C:array[1 .. 4] of integeR;
                        D:integer;
                    do
                        begin
                            a:=b/3;
                            b:=-b;
                            for d:=c[D] to D mod 0 do
                                break;
                            continue;
                        end
                end
            else
                begin
                end
        end
    continue;  // error
    return falSE;
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_no_entry_point1(self):
        """test_no_entry_point1"""
        input = """
var a:boolEAN;
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_no_entry_point2(self):
        """test_no_entry_point2"""
        input = """
var a:boolEAN;

function foo():boolean;
begin
    return foo2();
end

function foo2():boolean;
begin
    return foo();
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_no_entry_point3(self):
        """test_no_entry_point3"""
        input = """
var a:boolEAN;

function main():boolean;
begin
    return MAIN3();
end

function main3():boolean;
begin
    return MAIN();
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_no_entry_point4(self):
        """test_no_entry_point4"""
        input = """
var a:boolEAN;

procedure MAIN(a:integer);
begin  
    main4(1);
end

procedure MAIN4(a:integer);
begin
    maIN(2);
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_no_entry_point5(self):
        """test_no_entry_point5"""
        input = """
var a:boolEAN;
var arr:array[0 .. 1998] of string;

procedure main(a:array[0 .. 1998] of string);
begin
    MaIn5(arr);
end

procedure main5(a:array[0 .. 1998] of string);
begin
    MaIn(arr);
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_no_entry_point6(self):
        """test_no_entry_point6"""
        input = """
var MaIN:boolEAN;
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_no_entry_point7(self):
        """test_no_entry_point7"""
        input = """
var main:integer;
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_no_entry_point8(self):
        """test_no_entry_point8"""
        input = """
var main:integer;

function foo(a:array[0 .. 1998] of string):array [0 .. 1998] of string;
var main:real;
begin
    with
        main:string;
    do
        with
            main:array[0 .. -1] of integer;
        do
            with 
                main:booleAN;
            do
                begin
                    return foo(foo8());
                end
end

function foo8():array [0 .. 1998] of string;
var main:real;
begin
    with
        main:string;
    do
        with
            main:array[0 .. -1] of integer;
        do
            with 
                main:booleAN;
            do
                begin
                    return foo(foo8());
                end
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_no_entry_point9(self):
        """test_no_entry_point9"""
        input = """
function main(main:array[0 .. 1998] of string):array [0 .. 1998] of string;
begin
    with
        main:string;
    do
        with 
            main:booleAN;
        do
            with
                main:array[0 .. 1998] of string;
            do
                begin
                    return call(main);
                end
end

function call(call:array[0 .. 1998] of string):array [0 .. 1998] of string;
begin
    return main(call);
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_func_not_return14(self):
        """test_func_not_return14"""
        input = """
procedure main();
var i:real;
begin
    i:=foo();
    i:=foo14();
end

function foo():integer;
begin
    if true then
        return - 0;
    return - 0 - 1;  //# return here
end

function foo14():integer;  // error
begin
    if true then
        return - 0;
end
"""
        expect = "Function foo14Not Return "
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_unreachable_stmt1(self):
        """test_unreachable_stmt1"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo1();
end

function foo():boolean;
begin
    return true;
end
        
function foo1():boolean;
begin
    return 5*getint()/getfloat()>=1998.0;  //# return here
    return False;  // error
end
"""
        expect = "Unreachable statement: Return(Some(BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_unreachable_stmt2(self):
        """test_unreachable_stmt2"""
        input = """
procedure MaIn();
var a:boolean;
begin
    foo();
    foo2();
end

var x:boolean;
        
procedure foo();
begin
    if True then
        return;
    else  //# no return
        begin
        end
    while true do
        begin
            foo2();
            return ;
        end
end

procedure foo2();
begin
    if True then
        return ;  //# return here
    else
        return ;  //# return here
    while FALSE do  // error
        begin
            foo();
            return ;
        end
end
"""
        expect = "Unreachable statement: While(BooleanLiteral(False),[CallStmt(Id(foo),[]),Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_unreachable_stmt3(self):
        """test_unreachable_stmt3"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo3();
end

function foo():boolean;
begin
    if True then  //# no return
        begin
        end
    else
        return True;
    with
        a:integer;
        b,c:real;
        d:boolean;
    do
        begin
            a:=1;
            b:=a+c;
            d:=a=c;
            return false;
        end
end
        
function foo3():boolean;
begin
    if True then
        return falsE;  //# return here
    else
        return true;  //# return here
    with  // error
        A:integer;
        B,C:real;
        d:boolean;
    do
        begin
            a:=1;
            b:=a+c;
            d:=a=c;
            return false;
        end
end
"""
        expect = "Unreachable statement: With([VarDecl(Id(A),IntType),VarDecl(Id(B),FloatType),VarDecl(Id(C),FloatType),VarDecl(Id(d),BoolType)],[AssignStmt(Id(a),IntLiteral(1)),AssignStmt(Id(b),BinaryOp(+,Id(a),Id(c))),AssignStmt(Id(d),BinaryOp(=,Id(a),Id(c))),Return(Some(BooleanLiteral(False)))])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_unreachable_stmt4(self):
        """test_unreachable_stmt4"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo4();
end
      
function foo():boolean;
var a:integer;
begin
    if True then
        begin
        end
    else
        begin
        end
    a:=1;
    begin
        return true and false;
    end
end
  
function foo4():boolean;
var a:integer;
begin
    if True then
        begin
        end
    else
        begin
        end
    a:=1;
    return true aNd THEN faLse;  //# return here
    begin
        return TRUE;  // error
    end
end
"""
        expect = "Unreachable statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_unreachable_stmt5(self):
        """test_unreachable_stmt5"""
        input = """
procedure MaIn();
var a:boolean;
begin
    foo();
    foo5();
end
        
procedure foo();
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return ;
        end
    else  //# no return
        begin
            a:=0;
            putintln(69);
        end
    a:=0;
end

procedure foo5();
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return ;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return ;  //# return here
        end
    A:=0;  // error
end
"""
        expect = "Unreachable statement: AssignStmt(Id(A),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachable_stmt6(self):
        """test_unreachable_stmt6"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo6();
end
        
function foo():boolean;
var a:integer;
begin
    with
        a,b:real;
        c:string;
    do
        begin
            a:=b;
            putstring(c);
        end
    begin
        a:=getint();
        putfloat(a/2);
        return true;
    end
end

function foo6():boolean;
var a:integer;
begin
    with
        a,b:real;
        c:string;
    do
        begin
            a:=b;
            putstring(c);
            return a > b/2;  //# return here
        end

    begin
        A:=GETint();  // error
    end
end
"""
        expect = "Unreachable statement: AssignStmt(Id(A),CallExpr(Id(GETint),[]))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachable_stmt7(self):
        """test_unreachable_stmt7"""
        input = """
procedure MaIn();
begin
    foo();
    foo7();
end
        
procedure foo();
var a:real;
    i:integer;
begin
    while true do  //# no return
        return;

    for i:=0 to 10 do
        begin
            i:=-(-(i-1));
            return;
        end
end

procedure foo7();
var i:integer;
begin
    while false do
        return ;
    return ;  //# return here

    for I:=0 to 10 do  // error
        begin
            i:=-(-(i-1));
            return ;
        end
end
"""
        expect = "Unreachable statement: For(Id(I)IntLiteral(0),IntLiteral(10),True,[AssignStmt(Id(i),UnaryOp(-,UnaryOp(-,BinaryOp(-,Id(i),IntLiteral(1))))),Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachable_stmt8(self):
        """test_unreachable_stmt8"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo8();
end

function foo():boolean;
var i:integer;
    f:real;
begin
    while foo() do  //# no return
        begin
            i:=getint();
            f:=i/1;
            f:=getfloat();
            return True or else i = 0;
        end
    return false;
end

function foo8():boolean;
var i:integer;
    f:real;
begin
    while foo() do
        begin
            i:=getint();
            f:=i/1;
            f:=getfloat();
            return True or else i = 0;
        end
    return True;  //# return here
    f:=0/0.0;  // error
end
"""
        expect = "Unreachable statement: AssignStmt(Id(f),BinaryOp(/,IntLiteral(0),FloatLiteral(0.0)))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_unreachable_stmt9(self):
        """test_unreachable_stmt9"""
        input = """
procedure MaIn();
begin
    foo();
    foo9();
end

procedure foo();
var i:integer;
    f:real;
begin
    for i:=0 downtO -100 do  //# no return
        return;

    if i=f then
        begin
            f:=i+1;
            return ;
        end
    else
        f:=i+12;
end

procedure foo9();
var i:integer;
    f:real;
begin
    for i:=0 downtO -100 do
        return;
    return;  //# return here

    if I=F then  // error
        begin
            f:=i+1;
            return;
        end
    else
        f:=i+12;
end
"""
        expect = "Unreachable statement: If(BinaryOp(=,Id(I),Id(F)),[AssignStmt(Id(f),BinaryOp(+,Id(i),IntLiteral(1))),Return(None)],[AssignStmt(Id(f),BinaryOp(+,Id(i),IntLiteral(12)))])"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_unreachable_stmt10(self):
        """test_unreachable_stmt10"""
        input = """
procedure MaIn();
begin
    foo();
    foo10();
end

procedure foo();  // error
var a:integer;
begin
    if True then  //# no return
        begin
            a:=a;
            putintln(a);
            while True do
                return;

            for a:=0 downto a do
                begin
                    return;
                end
        end
    else
        begin
            a:=0;
            putintln(69);
            return;
        end

    main();
end

procedure foo10();
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            while True do
                break;
                
            return;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return;  //# return here
        end
        
    MAIN();  // error
end
"""
        expect = "Unreachable statement: CallStmt(Id(MAIN),[])"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_unreachable_stmt11(self):
        """test_unreachable_stmt11"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo11();
end

function foo():boolean;
var a:real;
begin
    while a = 1 do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end

    a:=a+1.0;
    return foo();  //# return here
end

function foo11():boolean;
var a:real;
begin
    while a = 1 do
        begin
            a:=0;
            if not (a=0) THEn
                begin
                    return falSE;
                    a:=1447;  // error
                end
            else
                return false or false;
        end

    a:=a+1.0;
    return foo();  //# return here
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1447))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_unreachable_stmt12(self):
        """test_unreachable_stmt12"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo12();
end

function foo():boolean;
var a:integer;
    b:real;
begin
    for a:=a to a do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end

    b:=a+1.0;
    return foo();  //# return here
end

function foo12():boolean;
var a:integer;
    b:real;
begin
    for a:=a to a do
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                begin
                    return false or false;
                    a:=1998;  // error
                end
        end

    b:=a+1.0;
    return foo();  //# return here
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1998))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_unreachable_stmt13(self):
        """test_unreachable_stmt13"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo13();
end

function foo():boolean;
var a:integer;
    b:real;
begin
    for a:=a to a do  //# no return
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                break;
                        end
                end
            return trUE;
        end
    
    b:=a+1.0;
    return FALsE;  //# return here
end

function foo13():boolean;
var a:integer;
    b:real;

begin
    for a:=a to a do
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                break;
                            return fALSE or false;  // error
                        end
                end
            return trUE;
        end

    b:=a+1.0;
    return FALsE;  //# return here
end
"""
        expect = "Unreachable statement: Return(Some(BinaryOp(or,BooleanLiteral(False),BooleanLiteral(False))))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_unreachable_stmt14(self):
        """test_unreachable_stmt14"""
        input = """
procedure main();
var i:real;
begin
    i:=foo();
    i:=foo14();
end

function foo():integer;
begin
    if true then
        return - 0;
    return - 0 - 1;  //# return here
end

function foo14():integer;
var bool:real;
begin
    if true then
        return - 0;
    return - 0 - 0;  //# return here
    bool  :=   foo();  // error
end
"""
        expect = "Unreachable statement: AssignStmt(Id(bool),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_unreachable_stmt15(self):
        """test_unreachable_stmt15"""
        input = """
procedure MaIn();
begin
    foo();
    foo15();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                end
            putfloatln(0.000) ;
        end

    a := 1;
end

procedure foo15();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                    return;
                end
            putintln(0) ;  // error
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putintln),[IntLiteral(0)])"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_unreachable_stmt16(self):
        """test_unreachable_stmt16"""
        input = """
procedure MaIn();
begin
    foo();
    foo16();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        putfloatLN(1.3);
                end
        end

    a := 1;
end

procedure foo16();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        return;
                end
            putfloatLN(1.9) ;  // error
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putfloatLN),[FloatLiteral(1.9)])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_unreachable_stmt17(self):
        """test_unreachable_stmt17"""
        input = """
procedure MaIn();
begin
    foo();
    foo17();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        putfloatLN(1.3);
                end
        end

    a := 1;
end

procedure foo17();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:real;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                    else
                        continue;
                    putfloatLN(1.998) ;  // error
                end
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putfloatLN),[FloatLiteral(1.998)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_undeclared_identifier3(self):
        """test_undeclared_identifier3"""
        input = """
procedure main();
var x:integer;
begin
    with
        x,y: real;
    do
        X:= 1998;
    X:= y;  // error
end
"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_unreachable_function1(self):
        """test_unreachable_function1"""
        input = """
var a:integer;
    b:boolean;

procedure main();
begin
end

function poor():integer;
begin
    b := fair();
    return -1;
end

function fair():boolean;
begin
    a := poor();
    return false;
end

function rich():string;
begin
    return "falSE";
end
"""
        expect = "Unreachable Function: rich"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_unreachable_function2(self):
        """test_unreachable_function2"""
        input = """
procedure main();
begin
end

function rich(b:boolean):boolean;
begin
    b:=rich(False);
    return false;
end
"""
        expect = "Unreachable Function: rich"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_unreachable_procedure1(self):
        """test_unreachable_procedure1"""
        input = """
procedure main();
begin
end

procedure poor();
begin
    fair();
end

procedure fair();
begin
    poor();
end

procedure rich();
begin
    return;
end
"""
        expect = "Unreachable Procedure: rich"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_unreachable_procedure2(self):
        """test_unreachable_procedure2"""
        input = """
procedure main();
begin
end

procedure poor();
begin
    poor();
end
"""
        expect = "Unreachable Procedure: poor"
        self.assertTrue(TestChecker.test(input,expect,499))

 