import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

# Redeclared Variable: 5
    def test_redeclared_variable_1(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi1, conbocuoi2:integer;

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_redeclared_variable_2(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi1, conbocuoi2:integer;

function conbocuoi4(conbocuoi5:integer):integer;
var conbocuoi1:integer;
    conbocuoi1:real;
begin
    return 0;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_3(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi3, conbocuoi2:integer;
    conbocuoi3:array [1 .. 10] of real;
procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_variable_4(self):
        input = """
var conbocuoi1, conbocuoi2:integer;

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    with conbocuoi4:integer;
         conbocuoi4:array [1 .. 2] of real;
    do
        conbocuoi4 := 10;

    return;
end
"""
        expect = "Redeclared Variable: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_redeclared_variable_5(self):
        input = """
        
var conbocuoi5, conbocuoi2, conbocuoi3, conbocuoi5:integer;

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,404))
        
    
# Redeclared Function: 5
    def test_redeclared_function_1(self):
        input = """
        
var conbocuoi1, conbocuoi2:integer;

function conbocuoi1(hihi:integer):integer;
begin
    return 10;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin 
    conbocuoi1();
end
"""
        expect = "Redeclared Function: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_redeclared_function_2(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi2():integer;
begin
    return 10;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Function: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_function_3(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

function conbocuoi3():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Function: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_redeclared_function_4(self):
        input = """
        
var conbocuoi4:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

function conbocuoi4():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin
    return;
end

procedure conbocuoi4();
begin
    return;
end
"""
        expect = "Redeclared Function: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_redeclared_function_5(self):
        input = """
        
var conbocuoi4:integer;

function conbocuoi3():integer;
begin
    return conbocuoi4();
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure conbocuoi5();
begin
    return;
end

function conbocuoi5():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin
    return;
end
"""
        expect = "Redeclared Function: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,409))
        
# Redeclared Procedure: 5
    def test_redeclared_procedure_1(self):
        input = """
        
var conbocuoi1, conbocuoi2:integer;

procedure conbocuoi1(hihi:integer);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin 
    conbocuoi1();
end
"""
        expect = "Redeclared Procedure: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_redeclared_procedure_2(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

procedure conbocuoi2();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin 
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_procedure_3(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

procedure conbocuoi3();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin 
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_redeclared_procedure_4(self):
        input = """
        
var conbocuoi4:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

procedure conbocuoi4();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end

function conbocuoi4():integer;
begin
    return 100;
end
"""
        expect = "Redeclared Procedure: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_redeclared_procedure_5(self):
        input = """
        
var conbocuoi4:integer;

function conbocuoi3():integer;
begin
    return conbocuoi4();
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure conbocuoi5();
begin
    return;
end

procedure conbocuoi5();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,414))
        

# Redeclared Parameter: 5
    def test_redeclared_parameter_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi1:integer):integer;
begin
    return conbocuoi4;
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_redeclared_parameter_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi6(1, "conbocuoi");
end

function conbocuoi6(conbocuoi2:integer; conbocuoi2:string):integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_redeclared_parameter_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi3:integer; conbocuoi3:real):integer;
begin
    return conbocuoi4;
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_redeclared_parameter_4(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi4:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi4:array [1 .. 100] of real; conbocuoi4:string);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_redeclared_parameter_5(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi5:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,419))
        

# Undeclared Identifier: 5
    def test_undeclared_identifier_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var
    conbocuoi2:real;
begin
    conbocuoi1 := 1;
    return;
end
"""
        expect = "Undeclared Identifier: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_undeclared_identifier_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi1:real;
begin
    conbocuoi2 := 1;
    return;
end
"""
        expect = "Undeclared Identifier: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_undeclared_identifier_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi7(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    if (conbocuoi3) then conbocuoi3 := True;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin
    conbocuoi1 := 1;
    return;
end
"""
        expect = "Undeclared Identifier: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_undeclared_identifier_4(self):
        input = """
var conbocuoi5:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var
    conbocuoi2:real;
begin
    for conbocuoi4 := 1 to conbocuoi5 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
    end
    return;
end
"""
        expect = "Undeclared Identifier: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_undeclared_identifier_5(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin
    conbocuoi3(conbocuoi5, conbocuoi1);
    return;
end
"""
        expect = "Undeclared Identifier: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,424))


# Undeclared Function: 5
    def test_undeclared_function_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := conbocuoi1(10);
    return;
end
"""
        expect = "Undeclared Function: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_function_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi5:integer):integer;
begin
    for conbocuoi4 := 1 to 10 do
    begin
        conbocuoi5 := conbocuoi5 + 100;
        conbocuoi5 := conbocuoi5 - conbocuoi2(conbocuoi1);
    end
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Function: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_undeclared_function_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi5(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 - conbocuoi3("hihi");
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Function: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_undeclared_function_4(self):
        input = """
var conbocuoi5:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4(100);
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Function: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_undeclared_function_5(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi1 := conbocuoi5();
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Function: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,429))
        
# Undeclared Procedure: 5
    def test_undeclared_procedure_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    conbocuoi1();
    return;
end
"""
        expect = "Undeclared Procedure: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_undeclared_procedure_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    conbocuoi2("hehe");
    return;
end
"""
        expect = "Undeclared Procedure: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_undeclared_procedure_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        conbocuoi3();
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Procedure: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_undeclared_procedure_4(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi7(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        conbocuoi7(123, True);
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    if conbocuoi2 = 10 then
    begin
        conbocuoi3 := 10;
    end
    else conbocuoi4();
    return;
end
"""
        expect = "Undeclared Procedure: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_undeclared_procedure_5(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    conbocuoi5();
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    conbocuoi2 := 10;
    return;
end
"""
        expect = "Undeclared Procedure: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,434))

# TMIS If: 5
    def test_TMIS_IF_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    if (1) then
    begin
        conbocuoi2 := 1;
        conbocuoi3 := 2;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: If(IntLiteral(1),[AssignStmt(Id(conbocuoi2),IntLiteral(1)),AssignStmt(Id(conbocuoi3),IntLiteral(2))],[])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TMIS_IF_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    if (1.5) then
    begin
        conbocuoi2 := 1;
        conbocuoi3 := 2;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: If(FloatLiteral(1.5),[AssignStmt(Id(conbocuoi2),IntLiteral(1)),AssignStmt(Id(conbocuoi3),IntLiteral(2))],[])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_TMIS_IF_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    if ("conbocuoi") then
    begin
        conbocuoi2 := 1;
        conbocuoi3 := 2;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: If(StringLiteral(conbocuoi),[AssignStmt(Id(conbocuoi2),IntLiteral(1)),AssignStmt(Id(conbocuoi3),IntLiteral(2))],[])"
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_TMIS_IF_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    conbocuoi2 := 123;
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    if (True and True or not conbocuoi5 and then False) then
    begin
        conbocuoi2 := 1;
        conbocuoi3 := 2;
    end
    
    if (5 + 5) then
    begin
        conbocuoi2 := conbocuoi3;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLiteral(5),IntLiteral(5)),[AssignStmt(Id(conbocuoi2),Id(conbocuoi3))],[])"
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_TMIS_IF_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5:integer;
begin
    if conbocuoi4 then
        conbocuoi2 := 1;
    if not conbocuoi4 then
        return conbocuoi2;
    if conbocuoi4 or not conbocuoi4 and conbocuoi4 or conbocuoi4 then
        return conbocuoi5;
    conbocuoi2 := 123;
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    
    if (5 + 5) then
    begin
        conbocuoi2 := conbocuoi3;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLiteral(5),IntLiteral(5)),[AssignStmt(Id(conbocuoi2),Id(conbocuoi3))],[])"
        self.assertTrue(TestChecker.test(input,expect,439))
        
# TMIS For: 5
    def test_TMIS_FOR_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5:integer;
begin
    conbocuoi2 := 123;
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    for conbocuoi3 := 1 to True do
    begin
        conbocuoi2 := conbocuoi2 + 1.0;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: For(Id(conbocuoi3)IntLiteral(1),BooleanLiteral(True),True,[AssignStmt(Id(conbocuoi2),BinaryOp(+,Id(conbocuoi2),FloatLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_TMIS_FOR_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    for conbocuoi := conbocuoi5 downto conbocuoi5 - 100 do
    begin
        conbocuoi6(conbocuoi5, True);
        break;
    end
    conbocuoi2 := 123;
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    for conbocuoi := 1 to conbocuoi5 do
        for conbocuoi7 := conbocuoi + 1 to conbocuoi5 + 100 do
            continue;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    for conbocuoi3 := "conbocuoi1" to conbocuoi2 do
    begin
        conbocuoi2 := conbocuoi2 + 1.0;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: For(Id(conbocuoi3)StringLiteral(conbocuoi1),Id(conbocuoi2),True,[AssignStmt(Id(conbocuoi2),BinaryOp(+,Id(conbocuoi2),FloatLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_TMIS_FOR_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    for conbocuoi := conbocuoi5 downto conbocuoi5 - 100 do
    begin
        conbocuoi6(conbocuoi5, True);
        break;
    end
    conbocuoi2 := 123;
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    for conbocuoi := 1 to conbocuoi5 do
        for conbocuoi7 := conbocuoi + 1 to conbocuoi5 + 100 do
            continue;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin

    for conbocuoi3 := 10 downto -10 do
        for conbocuoi3 := 1 to 1000 do
            for conbocuoi2 := 1 to 10 do
                break;
    return;
end
"""
        expect = "Type Mismatch In Statement: For(Id(conbocuoi2)IntLiteral(1),IntLiteral(10),True,[Break])"
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_TMIS_FOR_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    for conbocuoi := conbocuoi5 downto conbocuoi5 - 100 do
    begin
        conbocuoi6(conbocuoi5, True);
        break;
    end
    conbocuoi2 := 123;
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    for conbocuoi := 1 to conbocuoi5 do
        for conbocuoi7 := conbocuoi + 1 to conbocuoi5 + 100 do
            continue;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    for conbocuoi3 := 1 + 1 - 100 to 10 * 10 do
        break;
        
    for conbocuoi3 := 1/1 to conbocuoi2 do
    begin
        conbocuoi2 := conbocuoi2 + 1.0;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: For(Id(conbocuoi3)BinaryOp(/,IntLiteral(1),IntLiteral(1)),Id(conbocuoi2),True,[AssignStmt(Id(conbocuoi2),BinaryOp(+,Id(conbocuoi2),FloatLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_TMIS_FOR_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    for conbocuoi := conbocuoi5 downto conbocuoi5 - 100 do
    begin
        conbocuoi6(conbocuoi5, True);
        break;
    end
    conbocuoi2 := 123;
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
begin
    while conbocuoi6 do
    begin
        conbocuoi5 := conbocuoi5 + 10;
        if conbocuoi6 or else not conbocuoi6 then
            return;
        continue;
    end
    for conbocuoi := 1 to conbocuoi5 do
        for conbocuoi7 := conbocuoi + 1 to conbocuoi5 + 100 do
            continue;
    for conbocuoi5 := 1 to conbocuoi6 do
        break;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
begin
    for conbocuoi3 := "conbocuoi1" to conbocuoi2 do
    begin
        conbocuoi2 := conbocuoi2 + 1.0;
    end
    return;
end
"""
        expect = "Type Mismatch In Statement: For(Id(conbocuoi5)IntLiteral(1),Id(conbocuoi6),True,[Break])"
        self.assertTrue(TestChecker.test(input,expect,444))
        

# TMIS While: 5
    def test_TMIS_WHILE_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    while (conbocuoi1) do
        break;
        
    while conbocuoi2 + conbocuoi3 do
        conbocuoi1 := False;
        
    return;
end
"""
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(conbocuoi2),Id(conbocuoi3)),[AssignStmt(Id(conbocuoi1),BooleanLiteral(False))])"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_TMIS_WHILE_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    while (conbocuoi4 and True) do
        break;
    while (conbocuoi4 and not conbocuoi4 or conbocuoi4) do
        continue;
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    while (conbocuoi1) do
        break;
        
    while conbocuoi2 + conbocuoi3 do
        conbocuoi1 := False;
        
    return;
end
"""
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(conbocuoi2),Id(conbocuoi3)),[AssignStmt(Id(conbocuoi1),BooleanLiteral(False))])"
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_TMIS_WHILE_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    while (conbocuoi4 and True) do
        break;
    while (conbocuoi4 and not conbocuoi4 or conbocuoi4) do
        continue;
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    while (conbocuoi7 + conbocuoi) do
        break;
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    while (conbocuoi1) do
        break;
        
    return;
end
"""
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(conbocuoi7),Id(conbocuoi)),[Break])"
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_TMIS_WHILE_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    while (conbocuoi4 and True) do
        break;
    while (conbocuoi4 and not conbocuoi4 or conbocuoi4) do
        continue;
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    while (conbocuoi3) do
        break;
    while (True) do
        break;
    while (False) do
        break;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    while (conbocuoi1) do
        break;
        
    while conbocuoi2 + conbocuoi3 do
        conbocuoi1 := False;
        
    return;
end
"""
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(conbocuoi2),Id(conbocuoi3)),[AssignStmt(Id(conbocuoi1),BooleanLiteral(False))])"
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_TMIS_WHILE_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin
    while (conbocuoi4 and True) do
        break;
    while (conbocuoi4 and not conbocuoi4 or conbocuoi4) do
        continue;
    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    while (conbocuoi1) do
        break;
        
    while ("conbocuoi") do
        break;
        
    return;
end
"""
        expect = "Type Mismatch In Statement: While(StringLiteral(conbocuoi),[Break])"
        self.assertTrue(TestChecker.test(input,expect,449))
        
# TMIS Assign: 5
    def test_TMIS_ASSIGN_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi2 := conbocuoi3;
    conbocuoi3 := conbocuoi2;
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(conbocuoi3),Id(conbocuoi2))"
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_TMIS_ASSIGN_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi2 := conbocuoi3;
    conbocuoi3 := conbocuoi2 := conbocuoi4 := 10;
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(conbocuoi3),Id(conbocuoi2))"
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_TMIS_ASSIGN_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
    conbocuoi7:string;
begin
    conbocuoi1 := True;
    conbocuoi2 := 123.0;
    conbocuoi3 := 111;
    conbocuoi7 := "hello";
    conbocuoi2 := conbocuoi3;
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(conbocuoi7),StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_TMIS_ASSIGN_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
    conbocuoi7:array[1 .. 100] of integer;
begin
    conbocuoi2 := conbocuoi3;
    conbocuoi2 := conbocuoi7[1];
    conbocuoi3 := conbocuoi7[10];
    conbocuoi3 := conbocuoi2;
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(conbocuoi3),Id(conbocuoi2))"
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_TMIS_ASSIGN_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin
    conbocuoi3 := True;
    conbocuoi := conbocuoi7 + 100;
    return;
end

procedure main(); 
var conbocuoi3:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi2 := conbocuoi3;
    conbocuoi3 := conbocuoi2;
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(conbocuoi3),Id(conbocuoi2))"
        self.assertTrue(TestChecker.test(input,expect,454))
        
# TMIS Return: 5
    def test_TMIS_RETURN_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi := conbocuoi3("conbocuoi", conbocuoi);
    conbocuoi2 := conbocuoi3("conbocuoi", conbocuoi);
    return;
end
"""
        expect = "Type Mismatch In Statement: Return(Some(Id(conbocuoi4)))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TMIS_RETURN_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi2;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return conbocuoi3;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi := conbocuoi3("conbocuoi", conbocuoi);
    conbocuoi2 := conbocuoi3("conbocuoi", conbocuoi);
    return;
end
"""
        expect = "Type Mismatch In Statement: Return(Some(Id(conbocuoi3)))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TMIS_RETURN_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):array [1 .. 100] of string;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
    conbocuoi6:array [1 .. 100] of string;
    conbocuoi7:array [1 .. 200] of integer;
begin
    return conbocuoi6;
end

function conbocuoi8(conbocuoi1:string; conbocuoi2:integer):array [1 .. 100] of string;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
    conbocuoi6:array [1 .. 100] of string;
    conbocuoi7:array [1 .. 200] of integer;
begin
    return conbocuoi7;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi := conbocuoi3("conbocuoi", conbocuoi);
    conbocuoi2 := conbocuoi3("conbocuoi", conbocuoi);
    return;
end
"""
        expect = "Type Mismatch In Statement: Return(Some(Id(conbocuoi7)))"
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_TMIS_RETURN_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return 100 + 200;
end

function conbocuoi9(conbocuoi1:string; conbocuoi2:integer):boolean;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi5;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi := conbocuoi3("conbocuoi", conbocuoi);
    conbocuoi2 := conbocuoi3("conbocuoi", conbocuoi);
    return;
end
"""
        expect = "Type Mismatch In Statement: Return(Some(Id(conbocuoi5)))"
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_TMIS_RETURN_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):real;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return conbocuoi5;
end

function conbocuoi8(conbocuoi1:string; conbocuoi2:integer):real;
var conbocuoi4:boolean;
    conbocuoi5, conbocuoi:integer;
begin

    return "buon ngu qua di";
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi := conbocuoi3("conbocuoi", conbocuoi);
    conbocuoi2 := conbocuoi3("conbocuoi", conbocuoi);
    return;
end
"""
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(buon ngu qua di)))"
        self.assertTrue(TestChecker.test(input,expect,459))
        
# TMIS Procedure Call: 5
    def test_TMIS_PROCEDURE_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_TMIS_PROCEDURE_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi2, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi2),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_TMIS_PROCEDURE_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi1, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi1),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_TMIS_PROCEDURE_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi8:array [1 .. 100] of integer);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:array[1 .. 100] of integer;
    conbocuoi2:array[1 .. 100] of real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi);
    conbocuoi6(conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_TMIS_PROCEDURE_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:string);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6("123123123");
    conbocuoi6("buon ngu qua hu hu");
    conbocuoi6(conbocuoi, "hehe");
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi),StringLiteral(hehe)])"
        self.assertTrue(TestChecker.test(input,expect,464))

# TMIE Array: 5
    def test_TMIE_ARRAY_1(self):
        input = """
procedure main(); 
var conbocuoi1:array [1 .. 100] of integer;
    conbocuoi2:array [1 .. 100] of real;
    conbocuoi3:array [1 .. 100] of boolean;
    conbocuoi4:array [1 .. 100] of string;
    c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := conbocuoi1[1];
    c2 := conbocuoi1[2];
    c3 := conbocuoi1[3];
    return;
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(c3),ArrayCell(Id(conbocuoi1),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_TMIE_ARRAY_2(self):
        input = """
procedure main(); 
var conbocuoi1:array [1 .. 100] of integer;
    conbocuoi2:array [1 .. 100] of real;
    conbocuoi3:array [1 .. 100] of boolean;
    c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := conbocuoi1[1 + 1];
    c2 := conbocuoi2[2 + 2];
    c3 := conbocuoi3[3 + 3];
    c3 := conbocuoi3["1"];
    return;
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(conbocuoi3),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_TMIE_ARRAY_3(self):
        input = """
procedure main(); 
var conbocuoi1:array [1 .. 100] of integer;
    conbocuoi2:array [1 .. 100] of real;
    conbocuoi3:array [1 .. 100] of boolean;
    c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := conbocuoi1[1];
    c2 := conbocuoi2[2];
    c3 := conbocuoi3[3/3];
    return;
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(conbocuoi3),BinaryOp(/,IntLiteral(3),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_TMIE_ARRAY_4(self):
        input = """
procedure main(); 
var conbocuoi1:array [1 .. 100] of integer;
    conbocuoi2:array [1 .. 100] of real;
    conbocuoi3:array [1 .. 100] of boolean;
    c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := conbocuoi1[1];
    c2 := conbocuoi2[2];
    c3 := conbocuoi3[True and False];
    return;
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(conbocuoi3),BinaryOp(and,BooleanLiteral(True),BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,468))
        
    def test_TMIE_ARRAY_5(self):
        input = """
procedure main(); 
var conbocuoi1:array [1 .. 100] of integer;
    conbocuoi2:array [1 .. 100] of real;
    conbocuoi3:array [1 .. 100] of boolean;
    c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := conbocuoi1[1];
    c2 := conbocuoi2[2];
    c3 := c1[3];
    return;
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(c1),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,469))
        

# TMIE Bin Exp: 5
    def test_TMIE_BIN_1(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 + c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 - c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_TMIE_BIN_2(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 - c1;
    c2 := c1 * c2;
    c2 := c1 / c1;
    c2 := c2 + c2;
    c3 := c3 and c3;
    c3 := c1 / c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_TMIE_BIN_3(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 + c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 and then c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(andthen,Id(c1),Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_TMIE_BIN_4(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 div c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 > c2;
    c3 := c1 <= c2;
    c3 := c1 mod c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(mod,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_TMIE_BIN_5(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 mod c1;
    c2 := c1 + c2;
    c3 := c2 <> c1;
    c3 := c1 div c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(div,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,474))

# TMIE Un Exp: 5
    def test_TMIE_UN_1(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := -c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_TMIE_UN_2(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := -c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_TMIE_UN_3(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_TMIE_UN_4(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not c1;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(c1))"
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_TMIE_UN_5(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not - not False;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,UnaryOp(not,BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,479))

# TMIE Function Call: 5
    def test_TMIE_FUNC_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi1(c2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallExpr(Id(conbocuoi1),[Id(c2)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_TMIE_FUNC_2(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi2(c3);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallExpr(Id(conbocuoi2),[Id(c3)])"
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_TMIE_FUNC_3(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi3(c4);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallExpr(Id(conbocuoi3),[Id(c4)])"
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_TMIE_FUNC_4(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi4(c4)[10];
    c2 := conbocuoi3(c4);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallExpr(Id(conbocuoi3),[Id(c4)])"
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_TMIE_FUNC_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi1(c2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallExpr(Id(conbocuoi1),[Id(c2)])"
        self.assertTrue(TestChecker.test(input,expect,484))
        
# Func not return: 5
    def test_NOT_RETURN_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi4(c4)[10];
    return;
end
"""
        expect = "Function conbocuoi1 Not Return "
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_NOT_RETURN_2(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    if True then return 1.0;
    
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi4(c4)[10];
    return;
end
"""
        expect = "Function conbocuoi2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_NOT_RETURN_3(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    while True do
        return 1;
        
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi4(c4)[10];
    return;
end
"""
        expect = "Function conbocuoi1 Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_NOT_RETURN_4(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    if True then return 1; else return 2;
end

function conbocuoi2(conbocuoi:real):real;
begin
    
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi4(c4)[10];
    return;
end
"""
        expect = "Function conbocuoi2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_NOT_RETURN_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin

end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi4(c4)[10];
    return;
end
"""
        expect = "Function conbocuoi5 Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))
        
# Break/Continue: 5
    def test_NOT_RETURN_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    continue;
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end

procedure main();
begin
    
    return;
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_NOT_RETURN_2(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    break;
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end

procedure main();
begin
    
    return;
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_NOT_RETURN_3(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end

procedure main();
begin
    if True then break;
    return;
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_NOT_RETURN_4(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    for conbocuoi := 1 to 100 do
    begin
        conbocuoi := 10;
        if conbocuoi < 10 then
            break;
        if conbocuoi > 10 then
            continue;
        
        conbocuoi := 20;
        
    end
    return;
end

procedure main();
begin
    break;
    return;
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_NOT_RETURN_5(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end

procedure main();
begin
    continue;
    return;
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,494))

# No Entry Point: 1
    def test_NO_ENTRY(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,495))
        
# Unreachable Stmt: 2

    def test_UR_STMT_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
        break;
        conbocuoi := conbocuoi + 10;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    return;
end

procedure main();
begin
    return;
end
"""
        expect = "Unreachable statement: AssignStmt(Id(conbocuoi),BinaryOp(+,Id(conbocuoi),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,496))
        
    def test_UR_STMT_2(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    while True do
    begin
        conbocuoi := conbocuoi + 10;
        return;
        conbocuoi := 100;
    end
    return;
end

procedure main();
begin
    return;
end
"""
        expect = "Unreachable statement: AssignStmt(Id(conbocuoi),IntLiteral(100))"
        self.assertTrue(TestChecker.test(input,expect,497))
        
# Unreachable Function/Procedure: 2

    def test_UR_FP_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    while True do
    begin
        conbocuoi := conbocuoi + 10;
        return;
    end
    return;
end

procedure main();
begin
    conbocuoi2(100);
    return;
end
"""
        expect = "Unreachable Function: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_UR_FP_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    for conbocuoi := 1 to 10 do
    begin
        for conbocuoi := 1 to 10 do
            break;
        while conbocuoi < 10 do
            continue;
        if conbocuoi > 1 then break; else continue;
    end
    
    return 10;
end

procedure conbocuoi2(conbocuoi:integer);
begin
    while True do
    begin
        conbocuoi := conbocuoi + 10;
        return;
    end
    return;
end

procedure main();
var conbocuoi:integer;
begin
    conbocuoi := conbocuoi1(696969696969696969696969696969696969696969696969);
    return;
end
"""
        expect = "Unreachable Procedure: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,499))

    
    