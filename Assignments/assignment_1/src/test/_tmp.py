def testCode161(self):
    '''Test Code file 161'''
    self.assertTrue(TestLexer.test(
        """
procedure foo(a:array [1..2] of real);
        """,
        "procedure,foo,(,a,:,array,[,1.,.2,],of,real,),;,<EOF>",
        161
    ))

def testCode162(self):
    '''Test Code file 162'''
    self.assertTrue(TestLexer.test(
        """
function foo(b:array [1..2] of integer):array [2 .. 3] of real;
var
a: array [2 .. 3] of real;
begin
if () then return a; //CORRECT 
else return b; // WRONG
end
        """,
        "",
        162
    ))

def testCode163(self):
    '''Test Code file 163'''
    self.assertTrue(TestLexer.test(
        """
procedure goo(x:array [1..2] of real );
var
y: array [2 .. 3] of real;
z: array [1 .. 2] of integer;
begin
foo(x); // CORRECT 
foo(y); // WRONG 
foo(z); // WRONG
end
        """,
        "",
        163
    ))

def testCode164(self):
    '''Test Code file 164'''
    self.assertTrue(TestLexer.test(
        """
function foo (): real; 
begin
if () then return 2.3; // CORRECT
else return 2; // CORRECT 
end
        """,
        "",
        164
    ))