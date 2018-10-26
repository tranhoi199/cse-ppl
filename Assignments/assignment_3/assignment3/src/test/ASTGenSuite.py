import sys
sys.path.append('../main/mp/utils')
sys.path.append('../utils')


import unittest
from TestUtils import TestAST
from AST import *
# from AntiAST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_1_var_1list_1var(self):
        input = r"""
var a: integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2_var_1list_nvar(self):
        input = r"""
var a,b: string;
"""
        expect =str(Program([VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())]))                     
        self.assertTrue(        TestAST.test(         input,       expect,         302))

    def test_3_var_nlist(self):
        input = r"""
var x,y,z:integer; 
    g: string; 
    h,t: real;
"""
        expect=str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4_n_var(self):
        input = r"""
var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'f'),FloatType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r't'),StringType()),VarDecl(Id(r'h'),StringType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r'q'),BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5_proc(self):
        input = r"""
procedure foo();
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6_proc_param_1list_1var(self):
        input = r"""
procedure foo(a: string);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7_proc_param_nlist(self):
        input = r"""
procedure foo(a: string; b: Real);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8_proc_param_1list_nvar(self):
        input = r"""
procedure foo(a,b,c: string);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9_proc_param_nlist(self):
        input = r"""
procedure foo(a,b,c: string; f,k,o: integer; g,h,t: Real);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'f'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'o'),IntType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10_func(self):
        input = r"""
function foo(): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11_func_param_1list_1var(self):
        input = r"""
function foo(a: string): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12_func_param_nlist_1var(self):
        input = r"""
function foo(a: string; b: Real): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),FloatType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13_func_param_nlist_nvar(self):
        input = r"""
function foo(a,b,c: string; 
    f,k,o: integer; g,h,t: Real): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'f'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'o'),IntType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14_continue(self):
        input = r"""
function foo(): String;
begin
continue;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Continue()],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15_break(self):
        input = r"""
function foo(): String;
begin
break;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Break()],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16_ret_none(self):
        input = r"""
function foo(): String;
begin
return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(None)],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17_ret_call(self):
        input = r"""
function foo(): String;
begin
return ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18_call_param_1var(self):
        input = r"""
function foo(): String;
begin
return ok(1);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1)]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19_call_param_nvar(self):
        input = r"""
function foo(): String;
begin
return ok(1,2);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1),IntLiteral(2)]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20_call_param_nvar(self):
        input = r"""
function foo(): String;
begin
return ok(1,a);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1),Id(r'a')]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21_call_no_param(self):
        input = r"""
function foo(): String;
begin
ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22_call_param_1var(self):
        input = r"""
function foo(): String;
begin
ok(a);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a')])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23_call_param_nvar(self):
        input = r"""
function foo(): String;
begin
ok(a,1);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a'),IntLiteral(1)])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24_call_param_literal(self):
        input = r"""
function foo(): String;
begin
ok(a,"1",True,falSe);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a'),StringLiteral(r'1'),BooleanLiteral(True),BooleanLiteral(False)])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25_call_param_call(self):
        input = r"""
function foo(): String;
begin
ok("hi", foo());
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[StringLiteral(r'hi'),CallExpr(Id(r'foo'),[])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26_call_param_call(self):
        input = r"""
function foo(): String;
begin
ok("hi", foo(bar(), 1));
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[StringLiteral(r'hi'),CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),IntLiteral(1)])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27_call_param_arr(self):
        input = r"""
function foo(): String;
begin
ok(a[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28_call_param_arr(self):
        input = r"""
function foo(): String;
begin
ok(1[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(IntLiteral(1),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29_call_param_arr_call(self):
        input = r"""
function foo(): String;
begin
ok(foo()[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30_call_param_arr_exp(self):
        input = r"""
function foo(): String;
begin
ok((foo())[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31_call_param_arr_id(self):
        input = r"""
function foo(): String;
begin
ok(a[b]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),Id(r'b'))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32_call_param_arr_idx_exp(self):
        input = r"""
function foo(): String;
begin
ok(a[foo()]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),CallExpr(Id(r'foo'),[]))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33_andthen(self):
        input = r"""
function foo(): String;
begin
ok(4 and then 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'andthen',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34_orelse(self):
        input = r"""
function foo(): String;
begin
ok(4 or else 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'orelse',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35_eq(self):
        input = r"""
function foo(): String;
begin
ok(4=5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'=',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36_lte(self):
        input = r"""
function foo(): String;
begin
ok(4>=5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'>=',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37_plus(self):
        input = r"""
function foo(): String;
begin
ok(4+5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'+',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38_div(self):
        input = r"""
function foo(): String;
begin
ok(4 div 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'div',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39_negative(self):
        input = r"""
function foo(): String;
begin
ok(-4);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[UnaryOp(r'-',IntLiteral(4))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40_exp_complex(self):
        input = r"""
function foo(): String;
begin
ok(5 and then (-6 + "nt" * 3 or 5) div 7 >= a+b-(-f * not(-5*"abc")));
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'andthen',IntLiteral(5),BinaryOp(r'>=',BinaryOp(r'div',BinaryOp(r'or',BinaryOp(r'+',UnaryOp(r'-',IntLiteral(6)),BinaryOp(r'*',StringLiteral(r'nt'),IntLiteral(3))),IntLiteral(5)),IntLiteral(7)),BinaryOp(r'-',BinaryOp(r'+',Id(r'a'),Id(r'b')),BinaryOp(r'*',UnaryOp(r'-',Id(r'f')),UnaryOp(r'not',BinaryOp(r'*',UnaryOp(r'-',IntLiteral(5)),StringLiteral(r'abc')))))))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41_var_local_1list_1var(self):
        input = r"""
procedure foo();
var a: integer;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42_var_local_nlist(self):
        input = r"""
procedure foo();
var a, b: integer; c: string;
    e, f, g: Boolean;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'g'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43_if(self):
        input = r"""
procedure foo();
begin
    if True then hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44_ifelse(self):
        input = r"""
procedure foo();
begin
    if True then hic(); else huc();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[CallStmt(Id(r'huc'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45_if_comp_1stmt(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46_if_comp_nstmt(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47_ifelse_comp(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else return oh();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[Return(CallExpr(Id(r'oh'),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48_ifelse_comp_1stmt(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else begin
        return; 
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49_ifelse_comp_nstmt(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else begin
        oh();
        return;
        break;
        huc();
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[CallStmt(Id(r'oh'),[]),Return(None),Break(),CallStmt(Id(r'huc'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50_ifelse_none(self):
        input = r"""
procedure foo();
begin
    if True then begin
    end else ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[],[CallStmt(Id(r'ok'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51_ifelse_none(self):
        input = r"""
procedure foo();
begin
    if True then begin
    end else begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52_assign_1lhs(self):
        input = r"""
procedure foo();
begin
    a := 1;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(1))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53_nassign_1lhs(self):
        input = r"""
procedure foo();
begin
    a := 1;
    b := True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),BooleanLiteral(True))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54_assign_nlhs(self):
        input = r"""
procedure foo();
begin
    a := b := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),StringLiteral(r'ahihi! hic hic')),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55_assign_lsh_arr(self):
        input = r"""
procedure foo();
begin
    a[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),IntLiteral(5)),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56_assign_lhs_arr_call(self):
        input = r"""
procedure foo();
begin
    foo()[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(5)),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57_assign_complex(self):
        input = r"""
procedure foo();
begin
    a := b[4] := foo()[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(5)),StringLiteral(r'ahihi! hic hic')),Assign(ArrayCell(Id(r'b'),IntLiteral(4)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(5))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58_assign_complex(self):
        input = r"""
procedure foo();
begin
    a[1+2] := foo(bar(), "hi", 3.4, -6.5)[4 And then trUE + FalsE];
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2))),ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hi'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59_assign_complex(self):
        input = r"""
procedure foo();
begin
    a[1+2] := foo(bar(), "hi", 3.4, -6.5)[4 And then trUE + FalsE] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hi'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))),StringLiteral(r'ahihi! hic hic')),Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2))),ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hi'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60_assign_complex(self):
        input = r"""
procedure foo();
begin
    a := -1.2+4.6*6 mod 7+m-f*k>4+2*5-6 div abc - - - 4 or 3 and then nhyil or else True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'>',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp(r'mod',BinaryOp(r'*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(7))),Id(r'm')),BinaryOp(r'*',Id(r'f'),Id(r'k'))),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(4),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),BinaryOp(r'div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(4)))),IntLiteral(3))),Id(r'nhyil')),BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61_assign_complex(self):
        input = r"""
procedure foo();
begin
    a := b := c := d := e := f := g := faLSE;
    g := -1.2+4.6*6 mod 7+m-f*k>4+2*5-6 div abc - - - 4 or 3 and then nhyil or else True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'g'),BooleanLiteral(False)),Assign(Id(r'f'),Id(r'g')),Assign(Id(r'e'),Id(r'f')),Assign(Id(r'd'),Id(r'e')),Assign(Id(r'c'),Id(r'd')),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'g'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'>',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp(r'mod',BinaryOp(r'*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(7))),Id(r'm')),BinaryOp(r'*',Id(r'f'),Id(r'k'))),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(4),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),BinaryOp(r'div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(4)))),IntLiteral(3))),Id(r'nhyil')),BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62_forto(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63_fordownto(self):
        input = r"""
procedure foo();
begin
    for i := 1 doWntO 10 do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),False,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64_for_exp(self):
        input = r"""
procedure foo();
begin
    for i := a+2*c doWntO h(f+r*2) do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),BinaryOp(r'+',Id(r'a'),BinaryOp(r'*',IntLiteral(2),Id(r'c'))),CallExpr(Id(r'h'),[BinaryOp(r'+',Id(r'f'),BinaryOp(r'*',Id(r'r'),IntLiteral(2)))]),False,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65_for_ret(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66_for_none(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67_for_comp(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68_while_call(self):
        input = r"""
procedure foo();
begin
    while True do gogo();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[CallStmt(Id(r'gogo'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69_while_ret(self):
        input = r"""
procedure foo();
begin
    while True do return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70_while_none(self):
        input = r"""
procedure foo();
begin
    while True do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71_while_call_none(self):
        input = r"""
procedure foo();
begin
    while Foo() do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(CallExpr(Id(r'Foo'),[]),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72_while_comp(self):
        input = r"""
procedure foo();
begin
    while false do begin 
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(False),[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73_with_1list1var(self):
        input = r"""
procedure foo();
begin
    with i: integer; do ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'ok'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74_with_1list1var_none(self):
        input = r"""
procedure foo();
begin
    with i: integer; do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75_with_1listnvar(self):
        input = r"""
procedure foo();
begin
    with i,j,k: integer; do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76_with_nlist(self):
        input = r"""
procedure foo();
begin
    with i,j,k: integer; 
        g: String;
        h,p,t: BooLean;
    do begin
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),BoolType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r't'),BoolType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77_with_comp(self):
        input = r"""
procedure foo();
begin
    with i: real;
    do begin
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),FloatType())],[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78_var_arr(self):
        input = r"""
var a: array[1 .. 2] of integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79_var_arr_n(self):
        input = r"""
var a, b, c: array[1 .. 2] of integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType())),VarDecl(Id(r'b'),ArrayType(1,2,IntType())),VarDecl(Id(r'c'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80_var_arr_nlist(self):
        input = r"""
var a: array[1 .. 2] of integer;
    u, v: array[1 .. 2] of string;
"""
        expect =str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType())),VarDecl(Id(r'u'),ArrayType(1,2,StringType())),VarDecl(Id(r'v'),ArrayType(1,2,StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81_var_complex(self):
        input = r"""
procedure foo(
    x: integer;
    y, z: real;
    g, h: string;
    arr_nodes: Array[0 .. 1000] of real
);

var 
    a, b, c: real;
    p: boolean;
    q: string;
    i, j: integer;
    dd: array[0 .. 1000005] of boolean;

begin

end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),StringType()),VarDecl(Id(r'arr_nodes'),ArrayType(0,1000,FloatType()))],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r'q'),StringType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'dd'),ArrayType(0,1000005,BoolType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82_random(self):
        input = r"""
procedure foo();
var a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]]] + 3;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),BinaryOp(r'+',Id(r'f'),ArrayCell(Id(r'y'),IntLiteral(2))))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83_random(self):
        input = r"""
procedure foo();
var a: real;

begin
    foo(2)[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),BinaryOp(r'-',BinaryOp(r'+',Id(r'f'),ArrayCell(Id(r'y'),IntLiteral(2))),BinaryOp(r'*',ArrayCell(Id(r'h'),ArrayCell(Id(r't'),BinaryOp(r'+',IntLiteral(5),Id(r'j')))),IntLiteral(4))))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84_random(self):
        input = r"""
procedure foo();
var a: real;

begin
    a := not - F * G div 5 + (I or L and N + Y or Q * not -P) and 6 * 5 + O div not (5 mod T) ;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'div',BinaryOp(r'*',UnaryOp(r'not',UnaryOp(r'-',Id(r'F'))),Id(r'G')),IntLiteral(5)),BinaryOp(r'*',BinaryOp(r'and',BinaryOp(r'or',BinaryOp(r'+',BinaryOp(r'or',Id(r'I'),BinaryOp(r'and',Id(r'L'),Id(r'N'))),Id(r'Y')),BinaryOp(r'*',Id(r'Q'),UnaryOp(r'not',UnaryOp(r'-',Id(r'P'))))),IntLiteral(6)),IntLiteral(5))),BinaryOp(r'div',Id(r'O'),UnaryOp(r'not',BinaryOp(r'mod',IntLiteral(5),Id(r'T'))))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85_random(self):
        input = r"""
procedure foo();
var a: real;

begin
    a := (((5 <> 6) < (6 = 5)) >= (4 + 5 > 1)) <= 1 ;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<=',BinaryOp(r'>=',BinaryOp(r'<',BinaryOp(r'<>',IntLiteral(5),IntLiteral(6)),BinaryOp(r'=',IntLiteral(6),IntLiteral(5))),BinaryOp(r'>',BinaryOp(r'+',IntLiteral(4),IntLiteral(5)),IntLiteral(1))),IntLiteral(1)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86_random(self):
        input = r"""
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
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[If(BinaryOp(r'>',Id(r'b'),IntLiteral(3)),[Assign(Id(r'c'),IntLiteral(5))],[Assign(Id(r'd'),IntLiteral(1))]),If(BinaryOp(r'<',Id(r'e'),IntLiteral(4)),[CallStmt(Id(r'ok'),[])],[])],[If(BinaryOp(r'>',Id(r'h'),IntLiteral(5)),[CallStmt(Id(r'nty'),[])],[CallStmt(Id(r'lyo'),[])]),Assign(Id(r'g'),IntLiteral(5))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87_random(self):
        input = r"""
procedure foo();
var a: real;
begin
    While i < 1 do begin
        i := i+1;
        if i = 1 then i := i - 1;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[While(BinaryOp(r'<',Id(r'i'),IntLiteral(1)),[Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),IntLiteral(1))),If(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[Assign(Id(r'i'),BinaryOp(r'-',Id(r'i'),IntLiteral(1)))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88_random(self):
        input = r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then break;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[For(Id(r'j'),Id(r'i'),IntLiteral(1),False,[If(BinaryOp(r'=',BinaryOp(r'mod',BinaryOp(r'+',Id(r'i'),Id(r'j')),IntLiteral(2)),IntLiteral(1)),[Break()],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89_random(self):
        input = r"""
procedure foo();
var a: real;
begin
    with 
        a: integer;
        b, c: array [0 .. 15] of Boolean;
        x, y, z: real;
    do begin
        a := x := y := 3;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),ArrayType(0,15,BoolType())),VarDecl(Id(r'c'),ArrayType(0,15,BoolType())),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'y'),IntLiteral(3)),Assign(Id(r'x'),Id(r'y')),Assign(Id(r'a'),Id(r'x'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90_random(self):
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect =str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[])]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91_random(self):
        input = r"""
procedure foo();
var a: real;
begin
    with 
        a: integer;
        b, c: array [0 .. 15] of Boolean;
        x, y, z: real;
    do begin
        a := x := y := 3;
    end
end

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

function foo(): String;
begin
    ok(a);
end

var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;

procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else return oh();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),ArrayType(0,15,BoolType())),VarDecl(Id(r'c'),ArrayType(0,15,BoolType())),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'y'),IntLiteral(3)),Assign(Id(r'x'),Id(r'y')),Assign(Id(r'a'),Id(r'x'))])],VoidType()),FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[If(BinaryOp(r'>',Id(r'b'),IntLiteral(3)),[Assign(Id(r'c'),IntLiteral(5))],[Assign(Id(r'd'),IntLiteral(1))]),If(BinaryOp(r'<',Id(r'e'),IntLiteral(4)),[CallStmt(Id(r'ok'),[])],[])],[If(BinaryOp(r'>',Id(r'h'),IntLiteral(5)),[CallStmt(Id(r'nty'),[])],[CallStmt(Id(r'lyo'),[])]),Assign(Id(r'g'),IntLiteral(5))])],VoidType()),FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a')])],StringType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'f'),FloatType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r't'),StringType()),VarDecl(Id(r'h'),StringType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r'q'),BoolType()),FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[Return(CallExpr(Id(r'oh'),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92_random(self):
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end

procedure foo();
begin
    if True then begin
    end else begin end
end

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect =str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[])]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType()),FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[],[])],VoidType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93_random(self):
        input = r"""
Var Sel: String;
    N1,N2, Total : Real;
    YN : String;  { this is a character variable type, which holds single characters ONLY }
procedure main();
Begin
	Total := 0;  { always initialise integer/real variables }
	GotoXy(4,3);
	Writeln("1.Addition");
	GotoXy(4,4);
	Writeln("2.Subtraction");
	GotoXy(4,5);
	Writeln("3.Exit");
	GotoXy(6,8);
	Write("Select: ");
	Sel := Readkey();

	If Sel = "1" {condition} Then 
	Begin  {more than one statement}
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 + N2;
		Writeln("Addition: ",N1," + ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end { Closing the if statement }

	If Sel = "2" Then { note that here we do not use an assignment statement } 
	Begin 
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 - N2;
		Write("Subtraction: ");
		Write(N1," - ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end  { Closing the if statement }

	If Sel = "3" Then 
	Begin
		ClrScr();
		Write("Are you sure?(Y/N)");
		YN := Readkey();
		If YN = "y" Then Halt(); { 1 instruction, so no need of Begin..End }
		If YN = "n" Then Goto1(); { the goto statement is not recommended for frequent use }
	End
End
"""
        expect =str(Program([VarDecl(Id(r'Sel'),StringType()),VarDecl(Id(r'N1'),FloatType()),VarDecl(Id(r'N2'),FloatType()),VarDecl(Id(r'Total'),FloatType()),VarDecl(Id(r'YN'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Total'),IntLiteral(0)),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(3)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'1.Addition')]),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(4)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'2.Subtraction')]),CallStmt(Id(r'GotoXy'),[IntLiteral(4),IntLiteral(5)]),CallStmt(Id(r'Writeln'),[StringLiteral(r'3.Exit')]),CallStmt(Id(r'GotoXy'),[IntLiteral(6),IntLiteral(8)]),CallStmt(Id(r'Write'),[StringLiteral(r'Select: ')]),Assign(Id(r'Sel'),CallExpr(Id(r'Readkey'),[])),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'1')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.1:')]),CallStmt(Id(r'Readln'),[Id(r'N1')]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.2:')]),CallStmt(Id(r'Readln'),[Id(r'N2')]),Assign(Id(r'Total'),BinaryOp(r'+',Id(r'N1'),Id(r'N2'))),CallStmt(Id(r'Writeln'),[StringLiteral(r'Addition: '),Id(r'N1'),StringLiteral(r' + '),Id(r'N2'),StringLiteral(r' = '),Id(r'Total')]),CallStmt(Id(r'Write'),[StringLiteral(r'Press any key to continue...')]),CallStmt(Id(r'Readkey'),[])],[]),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'2')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.1:')]),CallStmt(Id(r'Readln'),[Id(r'N1')]),CallStmt(Id(r'Write'),[StringLiteral(r'Input No.2:')]),CallStmt(Id(r'Readln'),[Id(r'N2')]),Assign(Id(r'Total'),BinaryOp(r'-',Id(r'N1'),Id(r'N2'))),CallStmt(Id(r'Write'),[StringLiteral(r'Subtraction: ')]),CallStmt(Id(r'Write'),[Id(r'N1'),StringLiteral(r' - '),Id(r'N2'),StringLiteral(r' = '),Id(r'Total')]),CallStmt(Id(r'Write'),[StringLiteral(r'Press any key to continue...')]),CallStmt(Id(r'Readkey'),[])],[]),If(BinaryOp(r'=',Id(r'Sel'),StringLiteral(r'3')),[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'Write'),[StringLiteral(r'Are you sure?(Y/N)')]),Assign(Id(r'YN'),CallExpr(Id(r'Readkey'),[])),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'y')),[CallStmt(Id(r'Halt'),[])],[]),If(BinaryOp(r'=',Id(r'YN'),StringLiteral(r'n')),[CallStmt(Id(r'Goto1'),[])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94_random(self):
        input = r"""
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if( a < 20 ) then
      (* if condition is true then print the following *)
      writeln("a is less than 20" );
   
   else
      (* if condition is false then print the following *) 
      writeln("a is not less than 20" );
      writeln("value of a is : ", a);
end
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(100)),If(BinaryOp(r'<',Id(r'a'),IntLiteral(20)),[CallStmt(Id(r'writeln'),[StringLiteral(r'a is less than 20')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'a is not less than 20')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'value of a is : '),Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95_random(self):
        input = r"""
var
exit: boolean;

choice: integer;

procedure main();
begin
   writeln("Do you want to continue? ");
   writeln("Enter Y/y for yes, and N/n for no");
   readln(choice);

if(choice = "n") then
   exit := true;
else
   exit := false;

if (exit) then
   writeln(" Good Bye!");
else
   writeln("Please Continue");

readln();
end
"""
        expect =str(Program([VarDecl(Id(r'exit'),BoolType()),VarDecl(Id(r'choice'),IntType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Do you want to continue? ')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Enter Y/y for yes, and N/n for no')]),CallStmt(Id(r'readln'),[Id(r'choice')]),If(BinaryOp(r'=',Id(r'choice'),StringLiteral(r'n')),[Assign(Id(r'exit'),BooleanLiteral(True))],[Assign(Id(r'exit'),BooleanLiteral(False))]),If(Id(r'exit'),[CallStmt(Id(r'writeln'),[StringLiteral(r' Good Bye!')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'Please Continue')])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96_random(self):
        input = r"""
  VAR X, Y1, Y2,  First, Last, Incr, Factor: REAL;
  Q1, Q2, Step:  INTEGER;
  PROCEDURE main();
  BEGIN
  { Input plot  parameters }
  Write("Enter  first value: ");
  Read(First);
  Write("Enter  last value: ");
  Read(Last);
  Write("Enter  scale factor: ");
  Read(Factor);
  Write("Enter an  increment: ");
  Read(Incr);
  WriteLn();
  { Draw  horizontal Y axis }
  FOR Step := 0 TO  MaxY DO
  IF (Step MOD 5 =  0) THEN
  Write("+");
  ELSE
  Write("-");
  Write(" Y ");
  WriteLn();
  { Do the Plot on  its side }
  X := First;
  WHILE X <=  Last DO BEGIN
  Y1 :=  SIN(3.14159 * X / 180.0);
  Y1 := Factor *  Y1;
  Q1 := ROUND(Y1);
  Y2 := 0.005 * X;
  Y2 := Factor *  Y2;
  Q2 := ROUND(Y2);
  FOR Step := 0 TO  MaxY DO
  IF Step = 0 THEN
  Write( "|");
  ELSE
  IF Step = Q1  THEN
  Write( "*");
  ELSE
  IF Step = Q2  THEN
  Write( "+");
  ELSE
  Write( " ");
  WriteLn();
  X := X + Incr;
  END { WHILE }
  Write("X");
  END { SidePlotXY  }
"""
        expect =str(Program([VarDecl(Id(r'X'),FloatType()),VarDecl(Id(r'Y1'),FloatType()),VarDecl(Id(r'Y2'),FloatType()),VarDecl(Id(r'First'),FloatType()),VarDecl(Id(r'Last'),FloatType()),VarDecl(Id(r'Incr'),FloatType()),VarDecl(Id(r'Factor'),FloatType()),VarDecl(Id(r'Q1'),IntType()),VarDecl(Id(r'Q2'),IntType()),VarDecl(Id(r'Step'),IntType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Write'),[StringLiteral(r'Enter  first value: ')]),CallStmt(Id(r'Read'),[Id(r'First')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter  last value: ')]),CallStmt(Id(r'Read'),[Id(r'Last')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter  scale factor: ')]),CallStmt(Id(r'Read'),[Id(r'Factor')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter an  increment: ')]),CallStmt(Id(r'Read'),[Id(r'Incr')]),CallStmt(Id(r'WriteLn'),[]),For(Id(r'Step'),IntLiteral(0),Id(r'MaxY'),True,[If(BinaryOp(r'=',BinaryOp(r'MOD',Id(r'Step'),IntLiteral(5)),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'+')])],[CallStmt(Id(r'Write'),[StringLiteral(r'-')])])]),CallStmt(Id(r'Write'),[StringLiteral(r' Y ')]),CallStmt(Id(r'WriteLn'),[]),Assign(Id(r'X'),Id(r'First')),While(BinaryOp(r'<=',Id(r'X'),Id(r'Last')),[Assign(Id(r'Y1'),CallExpr(Id(r'SIN'),[BinaryOp(r'/',BinaryOp(r'*',FloatLiteral(3.14159),Id(r'X')),FloatLiteral(180.0))])),Assign(Id(r'Y1'),BinaryOp(r'*',Id(r'Factor'),Id(r'Y1'))),Assign(Id(r'Q1'),CallExpr(Id(r'ROUND'),[Id(r'Y1')])),Assign(Id(r'Y2'),BinaryOp(r'*',FloatLiteral(0.005),Id(r'X'))),Assign(Id(r'Y2'),BinaryOp(r'*',Id(r'Factor'),Id(r'Y2'))),Assign(Id(r'Q2'),CallExpr(Id(r'ROUND'),[Id(r'Y2')])),For(Id(r'Step'),IntLiteral(0),Id(r'MaxY'),True,[If(BinaryOp(r'=',Id(r'Step'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'|')])],[If(BinaryOp(r'=',Id(r'Step'),Id(r'Q1')),[CallStmt(Id(r'Write'),[StringLiteral(r'*')])],[If(BinaryOp(r'=',Id(r'Step'),Id(r'Q2')),[CallStmt(Id(r'Write'),[StringLiteral(r'+')])],[CallStmt(Id(r'Write'),[StringLiteral(r' ')])])])])]),CallStmt(Id(r'WriteLn'),[]),Assign(Id(r'X'),BinaryOp(r'+',Id(r'X'),Id(r'Incr')))]),CallStmt(Id(r'Write'),[StringLiteral(r'X')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97_random(self):
        input = r"""
  VAR Pennies:  INTEGER;
  Tendered, Cost,  Remainder: REAL;
  PROCEDURE Main();
  BEGIN
  (* Input  necessary information *)
  Write("Enter cost  of item: ");
  Read(Cost);
  Write("Enter  amount tendered: ");
  Read(Tendered);
  (* Compute the  change in pennies *)
  Remainder :=  Tendered - Cost;
  Pennies := 0;
  WHILE Remainder  > 0 DO BEGIN
  Remainder :=  Remainder - 0.01;
  Pennies :=  Pennies + 1;
  END (* WHILE *)
  (* Output all  required Results *)
  Write("Cost is:  ");
  Write(Cost);
  Write(" Amount  tendered is: ");
  Write(Tendered);
  Write(" Change  is: ");
  WriteLn(Pennies);
  END (*  BadChanger *)
"""
        expect =str(Program([VarDecl(Id(r'Pennies'),IntType()),VarDecl(Id(r'Tendered'),FloatType()),VarDecl(Id(r'Cost'),FloatType()),VarDecl(Id(r'Remainder'),FloatType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Write'),[StringLiteral(r'Enter cost  of item: ')]),CallStmt(Id(r'Read'),[Id(r'Cost')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter  amount tendered: ')]),CallStmt(Id(r'Read'),[Id(r'Tendered')]),Assign(Id(r'Remainder'),BinaryOp(r'-',Id(r'Tendered'),Id(r'Cost'))),Assign(Id(r'Pennies'),IntLiteral(0)),While(BinaryOp(r'>',Id(r'Remainder'),IntLiteral(0)),[Assign(Id(r'Remainder'),BinaryOp(r'-',Id(r'Remainder'),FloatLiteral(0.01))),Assign(Id(r'Pennies'),BinaryOp(r'+',Id(r'Pennies'),IntLiteral(1)))]),CallStmt(Id(r'Write'),[StringLiteral(r'Cost is:  ')]),CallStmt(Id(r'Write'),[Id(r'Cost')]),CallStmt(Id(r'Write'),[StringLiteral(r' Amount  tendered is: ')]),CallStmt(Id(r'Write'),[Id(r'Tendered')]),CallStmt(Id(r'Write'),[StringLiteral(r' Change  is: ')]),CallStmt(Id(r'WriteLn'),[Id(r'Pennies')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98_random(self):
        input = r"""
  (* Demonstrates  some String actions *)
  (* that involve  names of people *)
  VAR FirstName,  LastName, FullName: STRING;
  Count,  NameCount, Gap: INTEGER;
  PROCEDURE main();
  BEGIN
  Space := "  ";
  Hyphen := "-";
  Greeting :=  "Hello there ";
  Write("Enter the  number of names: ");
  ReadLn(NameCount);
  WriteLn();
  WHILE NameCount  >0 DO BEGIN
  Write("Enter a  name, last name first: ");
  Read(FullName);
  Gap :=  POS(Space, FullName); { NOTE }
  IF Gap > 0  THEN BEGIN
  LastName :=  Copy(FullName, 1, Gap);
  Delete(FullName,  1, Gap); { NOTE }
  FirstName :=  FullName;
  IF Length(LastName) <= 4 THEN
  WriteLn("That is  a short last name");
  IF Pos(Hyphen,  LastName) <> 0 THEN
  WriteLn("That is  a hyphenated name");
  IF FirstName =  "Bill" THEN { etc., etc. }
  WriteLn("Bill is  a good name ");
  FullName :=  FirstName + Space + LastName;
  WriteLn(Greeting,  FullName);
  WriteLn();
  END { IF }
  NameCount :=  NameCount - 1;
  END { WHILE }
  END { NameParse  }
"""
        expect =str(Program([VarDecl(Id(r'FirstName'),StringType()),VarDecl(Id(r'LastName'),StringType()),VarDecl(Id(r'FullName'),StringType()),VarDecl(Id(r'Count'),IntType()),VarDecl(Id(r'NameCount'),IntType()),VarDecl(Id(r'Gap'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Space'),StringLiteral(r'  ')),Assign(Id(r'Hyphen'),StringLiteral(r'-')),Assign(Id(r'Greeting'),StringLiteral(r'Hello there ')),CallStmt(Id(r'Write'),[StringLiteral(r'Enter the  number of names: ')]),CallStmt(Id(r'ReadLn'),[Id(r'NameCount')]),CallStmt(Id(r'WriteLn'),[]),While(BinaryOp(r'>',Id(r'NameCount'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'Enter a  name, last name first: ')]),CallStmt(Id(r'Read'),[Id(r'FullName')]),Assign(Id(r'Gap'),CallExpr(Id(r'POS'),[Id(r'Space'),Id(r'FullName')])),If(BinaryOp(r'>',Id(r'Gap'),IntLiteral(0)),[Assign(Id(r'LastName'),CallExpr(Id(r'Copy'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')])),CallStmt(Id(r'Delete'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')]),Assign(Id(r'FirstName'),Id(r'FullName')),If(BinaryOp(r'<=',CallExpr(Id(r'Length'),[Id(r'LastName')]),IntLiteral(4)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a short last name')])],[]),If(BinaryOp(r'<>',CallExpr(Id(r'Pos'),[Id(r'Hyphen'),Id(r'LastName')]),IntLiteral(0)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a hyphenated name')])],[]),If(BinaryOp(r'=',Id(r'FirstName'),StringLiteral(r'Bill')),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Bill is  a good name ')])],[]),Assign(Id(r'FullName'),BinaryOp(r'+',BinaryOp(r'+',Id(r'FirstName'),Id(r'Space')),Id(r'LastName'))),CallStmt(Id(r'WriteLn'),[Id(r'Greeting'),Id(r'FullName')]),CallStmt(Id(r'WriteLn'),[])],[]),Assign(Id(r'NameCount'),BinaryOp(r'-',Id(r'NameCount'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99_random(self):
        input = r"""
Var
	f : String; { file var of type byte }
	sz : Integer;  { var for the size }

Procedure Main();
Begin
	Assign(f,"C:\\\\anyfile.txt");
	{$I-} Reset(f); {$I+}
	If (IOResult <> 0) Then
 	Begin     { file found? }
  		Writeln("File not found.. exiting");
  		Readln();
 	End Else
 	Begin
			{ Return the file size in Kilobytes }
  		sz := Round(FileSize(f)/1024);
  		Writeln("Size of the file in Kilobytes: ",sz," Kb");
  		Readln();
  		Close(f); 
 	End
End
"""
        expect =str(Program([VarDecl(Id(r'f'),StringType()),VarDecl(Id(r'sz'),IntType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'f'),StringLiteral(r'C:\\\\anyfile.txt')]),CallStmt(Id(r'Reset'),[Id(r'f')]),If(BinaryOp(r'<>',Id(r'IOResult'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'File not found.. exiting')]),CallStmt(Id(r'Readln'),[])],[Assign(Id(r'sz'),CallExpr(Id(r'Round'),[BinaryOp(r'/',CallExpr(Id(r'FileSize'),[Id(r'f')]),IntLiteral(1024))])),CallStmt(Id(r'Writeln'),[StringLiteral(r'Size of the file in Kilobytes: '),Id(r'sz'),StringLiteral(r' Kb')]),CallStmt(Id(r'Readln'),[]),CallStmt(Id(r'Close'),[Id(r'f')])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100_random(self):
        input = r"""
Var
	NewDir : String; { for searching the dir and create a new one, if it does not exist }
	F : String;

Procedure Main();
Begin
	{ search for the dir }
	NewDir := FSearch("C:\\\\Pascal Programming", GetEnv("")); 
	{ create a new one, if it does not exist }
	If NewDir = "" Then
		CreateDir("C:\\\\Pascal Programming"); 
	Assign(F,"C:\\\\Pascal Programming\\\\pascal-programming.txt");
	{$I-} ReWrite(F); {$I+} { disable and enable back again I/O error checking } 
	{ write to text file } 
	Writeln(F,"http://pascal-programming.info/"); 
	{$I-} Close(F); {$I+}
End
"""
        expect =str(Program([VarDecl(Id(r'NewDir'),StringType()),VarDecl(Id(r'F'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'NewDir'),CallExpr(Id(r'FSearch'),[StringLiteral(r'C:\\\\Pascal Programming'),CallExpr(Id(r'GetEnv'),[StringLiteral(r'')])])),If(BinaryOp(r'=',Id(r'NewDir'),StringLiteral(r'')),[CallStmt(Id(r'CreateDir'),[StringLiteral(r'C:\\\\Pascal Programming')])],[]),CallStmt(Id(r'Assign'),[Id(r'F'),StringLiteral(r'C:\\\\Pascal Programming\\\\pascal-programming.txt')]),CallStmt(Id(r'ReWrite'),[Id(r'F')]),CallStmt(Id(r'Writeln'),[Id(r'F'),StringLiteral(r'http://pascal-programming.info/')]),CallStmt(Id(r'Close'),[Id(r'F')])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 400))



    def test_101_leading0(self):
        input = r"""
procedure foo();
begin
    a := 00000012345;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(12345))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_102_bignum(self):
        input = r"""
procedure foo();
begin
    a := 123456789123456789;
    a := 123456789123456789123456789;
    a := 123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789123456789;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789123456789123456789))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 402))

    def test_103_floatingpoint(self):
        input = r"""
procedure foo();
begin
    a := 1.2 + 1. + .1 + 1e2 + 1.2E-2;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',FloatLiteral(1.2),FloatLiteral(1.0)),FloatLiteral(0.1)),FloatLiteral(100.0)),FloatLiteral(0.012)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 403))

    def test_104_floatingpoint(self):
        input = r"""
procedure foo();
begin
    a := 1.2e-2 + .1E2 + 9.0 + 12e8;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',FloatLiteral(0.012),FloatLiteral(10.0)),FloatLiteral(9.0)),FloatLiteral(1200000000.0)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 404))

    def test_105_floatingpoint(self):
        input = r"""
procedure foo();
begin
    a := 0.33E-3 + 128e-42 + 12.  +   .05; 
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',FloatLiteral(0.00033),FloatLiteral(1.28e-40)),FloatLiteral(12.0)),FloatLiteral(0.05)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 405))

    def test_106_floatingpoint(self):
        input = r"""
procedure foo();
begin
    a := 12.05  + 1e-5  +    1.5e-6 +  0.0005e3 +  2e21;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',FloatLiteral(12.05),FloatLiteral(1e-05)),FloatLiteral(1.5e-06)),FloatLiteral(0.5)),FloatLiteral(2e+21)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 406))

    def test_107_nolimit(self):
        input = r"""
procedure foo();
begin{
    a := 2e10;
    a := 3e100;
    a := 4e1000;
    a := 5e10000;
    a := 6e100000;}
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 407))

    def test_108_nolimit(self):
        input = r"""
procedure foo();
begin
    a := 2e-10000000;
    a := 3e-1000000;
    a := 4e-100000;
    a := 5e-10000;
    a := 6e-1000;
    a := 7e-100;
    a := 8e-10;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(7e-100)),Assign(Id(r'a'),FloatLiteral(8e-10))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 408))

    def test_109_nolimit(self):
        input = r"""
procedure foo();
begin
    a := 10000000000e-10000000000;
    a := 20000000000e-1000000000;
    a := 30000000000e-100000000;
    a := 40000000000e-10000000;
    a := 50000000000e-1000000;
    a := 60000000000e-100000;
    a := 70000000000e-10000;
    a := 80000000000e-1000;
    a := 90000000000e-100;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(9e-90))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 409))

    def test_110_nolimit(self):
        input = r"""
procedure foo();
begin
    a := 1.000000000000001;
    a := 2.00000000000001;
    a := 3.0000000000001;
    a := 4.000000000001;
    a := 5.00000000001;
    a := 6.0000000001;
    a := 7.000000001;
    a := 8.00000001;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),FloatLiteral(1.000000000000001)),Assign(Id(r'a'),FloatLiteral(2.00000000000001)),Assign(Id(r'a'),FloatLiteral(3.0000000000001)),Assign(Id(r'a'),FloatLiteral(4.000000000001)),Assign(Id(r'a'),FloatLiteral(5.00000000001)),Assign(Id(r'a'),FloatLiteral(6.0000000001)),Assign(Id(r'a'),FloatLiteral(7.000000001)),Assign(Id(r'a'),FloatLiteral(8.00000001))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 410))

    def test_111_nolimit(self):
        input = r"""
procedure foo();
begin
    a := 0000001.0000000001;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),FloatLiteral(1.0000000001))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 411))

    def test_112_nolimit(self):
        input = r"""
procedure foo();
begin
    a := 000000000000000000000000001.00000000001e-10000000000;
    a := 000000000000000000000000002.00000000001e-1000000000;
    a := 000000000000000000000000003.00000000001e-100000000;
    a := 000000000000000000000000004.00000000001e-10000000;
    a := 000000000000000000000000005.00000000001e-1000000;
    a := 000000000000000000000000006.00000000001e-100000;
    a := 000000000000000000000000007.00000000001e-10000;
    a := 000000000000000000000000008.00000000001e-1000;
    a := 000000000000000000000000009.00000000001e-100;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(0.0)),Assign(Id(r'a'),FloatLiteral(9.00000000001e-100))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 412))

    def test_113_nolimit(self):
        input = r"""
procedure foo();
begin{
    a := 000000000000000000000000004.00000000001e10000;
    a := 000000000000000000000000005.00000000001e1000;
    a := 000000000000000000000000006.00000000001e100;
    a := 000000000000000000000000007.00000000001e10;
    a := 000000000000000000000000008.00000000001e1;}
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 413))

    def test_114_nolimit(self):
        input = r"""
procedure foo();
begin
    a := - - - - - - - - - - - - - "";
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',StringLiteral(r'')))))))))))))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 414))

    def test_115_nolimit(self):
        input = r"""
procedure foo();
begin
    a := "      abc         \n \t \b \\         ;;   cltq ";
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),StringLiteral(r'      abc         \n \t \b \\         ;;   cltq '))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 415))

    def test_116_and_then_or_else(self):
        input = r"""
procedure foo();
begin
    a := true or trUE Or falSE oR TRUE OR FalSE;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'OR',BinaryOp(r'oR',BinaryOp(r'Or',BinaryOp(r'or',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 416))

    def test_117_and_then_or_else(self):
        input = r"""
procedure foo();
begin
    a := true And Then trUE or else falSE oR ELse TRUE AND THEN FalSE;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'orelse',BinaryOp(r'orelse',BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 417))

    def test_118_curry_stmt(self):
        input = r"""
procedure foo();
begin
    a := b := 1;
    begin
        foo();
        return;
        break;
            begin
                return OK();
                return OK;
            end
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'b'),IntLiteral(1)),Assign(Id(r'a'),Id(r'b')),CallStmt(Id(r'foo'),[]),Return(None),Break(),Return(CallExpr(Id(r'OK'),[])),Return(Id(r'OK'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 418))

    def test_119_n_dimen_array(self):
        input = r"""
procedure foo();
begin
    a[1][2][3][4] := 1;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(ArrayCell(ArrayCell(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(1))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 419))

    def test_120(self):
        input = r"""
function foo(
    a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL
):
    array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of BoOLeAn;

var a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
    d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;

begin
    with
        a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
        d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
    do begin
        with
            a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
            d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
        do begin
            with
                a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
            do begin
                with
                    a: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    b: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    c: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of sTriNG; 
                    d,e,f,g,h,i,j,k: array [-999999999999999999999999999999999999999 .. 999999999999999999999999999999999999999] of REAL;
                do begin
                    return ok();
                end
            end
        end
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[With([VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[With([VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[With([VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[With([VarDecl(Id(r'a'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'b'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'c'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,StringType())),VarDecl(Id(r'd'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'e'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'f'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'g'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'h'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'i'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'j'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType())),VarDecl(Id(r'k'),ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,FloatType()))],[Return(CallExpr(Id(r'ok'),[]))])])])])],ArrayType(-999999999999999999999999999999999999999,999999999999999999999999999999999999999,BoolType()))]))
        self.assertTrue(TestAST.test(input, expect, 420))

    def test_121(self):
        input = r"""
procedure foo();
begin
    a := a+5*f - not ( -True OR (a <> b*"String"+"False"*False) or else fgh mOD TYR ------ 666666 *
    ("abc" <= "xyz") ) DIV FalSE MOD QUE + ---- False * "{{}}1e5" + 2e5 {  ....  };
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'+',Id(r'a'),BinaryOp(r'*',IntLiteral(5),Id(r'f'))),BinaryOp(r'MOD',BinaryOp(r'DIV',UnaryOp(r'not',BinaryOp(r'orelse',BinaryOp(r'OR',UnaryOp(r'-',BooleanLiteral(True)),BinaryOp(r'<>',Id(r'a'),BinaryOp(r'+',BinaryOp(r'*',Id(r'b'),StringLiteral(r'String')),BinaryOp(r'*',StringLiteral(r'False'),BooleanLiteral(False))))),BinaryOp(r'-',BinaryOp(r'mOD',Id(r'fgh'),Id(r'TYR')),BinaryOp(r'*',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',IntLiteral(666666)))))),BinaryOp(r'<=',StringLiteral(r'abc'),StringLiteral(r'xyz')))))),BooleanLiteral(False)),Id(r'QUE'))),BinaryOp(r'*',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',BooleanLiteral(False))))),StringLiteral(r'{{}}1e5'))),FloatLiteral(200000.0)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 421))

    def test_122(self):
        input = r"""
procedure foo();
begin
    a := b[1][2][3][4] := foo()[b][3][bar()] := true;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(ArrayCell(ArrayCell(CallExpr(Id(r'foo'),[]),Id(r'b')),IntLiteral(3)),CallExpr(Id(r'bar'),[])),BooleanLiteral(True)),Assign(ArrayCell(ArrayCell(ArrayCell(ArrayCell(Id(r'b'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),ArrayCell(ArrayCell(ArrayCell(CallExpr(Id(r'foo'),[]),Id(r'b')),IntLiteral(3)),CallExpr(Id(r'bar'),[]))),Assign(Id(r'a'),ArrayCell(ArrayCell(ArrayCell(ArrayCell(Id(r'b'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 422))

    def test_123(self):
        input = r"""
procedure foo();
begin
    a := (((((((((((((((((((((((((((((((((((((((((u)))))))))))))))))))))))))))))))))))))))));
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),Id(r'u'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 423))