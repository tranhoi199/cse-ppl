import unittest
from TestUtils import TestAST
# from AST import *
from AntiAST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_301(self):
        input = """
function A(a:integer):integer;
var a:array[1 .. 2] of real;
begin

end
        """
        expect = r"Program([FuncDecl(Id(A),[VarDecl(Id(a),IntType)],IntType,[VarDecl(Id(a),ArrayType(1,2,FloatType))],[])])"
        self.assertTrue(TestAST.test(input,expect,301))
        

    def test_var_302(self):
        input = """
Var       
    Num1, Num2, Sum : Integer;
Procedure main();
Begin {no semicolon}
	Write("Input number 1:"); 
	Readln(Num1);
	Writeln("Input number 2:");
	Readln(Num2);
	Sum := Num1 + Num2; {addition} 
	Writeln(Sum);
	Readln();
End
        """
        expect = r"Program([VarDecl(Id(Num1),IntType),VarDecl(Id(Num2),IntType),VarDecl(Id(Sum),IntType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Input number 1:)]),CallStmt(Id(Readln),[Id(Num1)]),CallStmt(Id(Writeln),[StringLiteral(Input number 2:)]),CallStmt(Id(Readln),[Id(Num2)]),AssignStmt(Id(Sum),BinaryOp(+,Id(Num1),Id(Num2))),CallStmt(Id(Writeln),[Id(Sum)]),CallStmt(Id(Readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,302))
        

    def test_var_303(self):
        input = """
Var name, surname: String;
Procedure main();
Begin
	write("Enter your name:");
	readln(name);
	write("Enter your surname:");
	readln(surname);
	writeln();{new line}
	writeln();{new line}
	writeln("Your full name is: ",name," ",surname);
	readln();
End
        """
        expect = r"Program([VarDecl(Id(name),StringType),VarDecl(Id(surname),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(write),[StringLiteral(Enter your name:)]),CallStmt(Id(readln),[Id(name)]),CallStmt(Id(write),[StringLiteral(Enter your surname:)]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[StringLiteral(Your full name is: ),Id(name),StringLiteral( ),Id(surname)]),CallStmt(Id(readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,303))


    def test_var_304(self):
        input = """
Var 
	surname: String;
procedure main();
Begin
	Write("Enter your surname:");
	readln(surname);
	writeln();
	writeln();
	Writeln("Your full name is: ",name," ",surname);
	readln();
End
        """
        expect = r"Program([VarDecl(Id(surname),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Enter your surname:)]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[]),CallStmt(Id(Writeln),[StringLiteral(Your full name is: ),Id(name),StringLiteral( ),Id(surname)]),CallStmt(Id(readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,304))
        

    def test_var_305(self):
        input = """
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
        expect = r"Program([VarDecl(Id(Sel),StringType),VarDecl(Id(N1),FloatType),VarDecl(Id(N2),FloatType),VarDecl(Id(Total),FloatType),VarDecl(Id(YN),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(Total),IntLiteral(0)),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(3)]),CallStmt(Id(Writeln),[StringLiteral(1.Addition)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(4)]),CallStmt(Id(Writeln),[StringLiteral(2.Subtraction)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(3.Exit)]),CallStmt(Id(GotoXy),[IntLiteral(6),IntLiteral(8)]),CallStmt(Id(Write),[StringLiteral(Select: )]),AssignStmt(Id(Sel),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(Sel),StringLiteral(1)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(+,Id(N1),Id(N2))),CallStmt(Id(Writeln),[StringLiteral(Addition: ),Id(N1),StringLiteral( + ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[]),If(BinaryOp(=,Id(Sel),StringLiteral(2)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(-,Id(N1),Id(N2))),CallStmt(Id(Write),[StringLiteral(Subtraction: )]),CallStmt(Id(Write),[Id(N1),StringLiteral( - ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[]),If(BinaryOp(=,Id(Sel),StringLiteral(3)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Are you sure?(Y/N))]),AssignStmt(Id(YN),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(YN),StringLiteral(y)),[CallStmt(Id(Halt),[])],[]),If(BinaryOp(=,Id(YN),StringLiteral(n)),[CallStmt(Id(Goto1),[])],[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,305))
        

    def test_if_306(self):
        input = """
Var
	SEL : Integer;
	YN : String;
procedure main();
Begin
	Writeln("[1]. PLAY GAME");
	WRITELN("[2]. LOAD GAME");
	WRITELN("[3]. MULTIPLAYER");
	WRITELN("[4]. EXIT GAME");
	Writeln("note: Do not press anything except");
	Writeln("numbers; otherwise an error occurs!");
	Readln(SEL);
	
	If SEL = 1 Then
	Begin
		Writeln("You will soon be able to create");
		Writeln("games using Pascal Programming :-)");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 2 Then
	Begin
		Writeln("Ahhh... no saved games");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 3 Then
	Begin
		Writeln("networking or 2 players?");
		Delay(3000);
		Goto(Ret);
	end

	If SEL = 4 Then
	Begin
		Writeln("Are you sure you want to Exit?");
		YN := Readkey;
		If YN = "y" Then
		Begin
			Writeln("Good Bye...");
			Delay(1000);
			Halt(); {EXIT PROGRAM}
		end

		If YN = "n" Then
			Goto(Ret);
	end
end
        """
        expect = r"Program([VarDecl(Id(SEL),IntType),VarDecl(Id(YN),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral([1]. PLAY GAME)]),CallStmt(Id(WRITELN),[StringLiteral([2]. LOAD GAME)]),CallStmt(Id(WRITELN),[StringLiteral([3]. MULTIPLAYER)]),CallStmt(Id(WRITELN),[StringLiteral([4]. EXIT GAME)]),CallStmt(Id(Writeln),[StringLiteral(note: Do not press anything except)]),CallStmt(Id(Writeln),[StringLiteral(numbers; otherwise an error occurs!)]),CallStmt(Id(Readln),[Id(SEL)]),If(BinaryOp(=,Id(SEL),IntLiteral(1)),[CallStmt(Id(Writeln),[StringLiteral(You will soon be able to create)]),CallStmt(Id(Writeln),[StringLiteral(games using Pascal Programming :-))]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(2)),[CallStmt(Id(Writeln),[StringLiteral(Ahhh... no saved games)]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(3)),[CallStmt(Id(Writeln),[StringLiteral(networking or 2 players?)]),CallStmt(Id(Delay),[IntLiteral(3000)]),CallStmt(Id(Goto),[Id(Ret)])],[]),If(BinaryOp(=,Id(SEL),IntLiteral(4)),[CallStmt(Id(Writeln),[StringLiteral(Are you sure you want to Exit?)]),AssignStmt(Id(YN),Id(Readkey)),If(BinaryOp(=,Id(YN),StringLiteral(y)),[CallStmt(Id(Writeln),[StringLiteral(Good Bye...)]),CallStmt(Id(Delay),[IntLiteral(1000)]),CallStmt(Id(Halt),[])],[]),If(BinaryOp(=,Id(YN),StringLiteral(n)),[CallStmt(Id(Goto),[Id(Ret)])],[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,306))
        

    def test_while_307(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") AND (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") AND (n2 = "0") Then Halt(0);
    End
End
        """
        expect = r"Program([VarDecl(Id(n1),StringType),VarDecl(Id(n2),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter two numbers: (\"\"0\"\" & \"\"0\"\" to exit))]),While(UnaryOp(not,BinaryOp(AND,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0)))),[CallStmt(Id(Write),[StringLiteral(No.1: )]),CallStmt(Id(Readln),[Id(n1)]),CallStmt(Id(Write),[StringLiteral(No.2: )]),CallStmt(Id(Readln),[Id(n2)]),If(BinaryOp(AND,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0))),[CallStmt(Id(Halt),[IntLiteral(0)])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,307))
        

    def test_or_308(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") OR (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") OR (n2 = "0") Then Halt(0);
    End
End
        """
        expect = r"Program([VarDecl(Id(n1),StringType),VarDecl(Id(n2),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter two numbers: (\"\"0\"\" & \"\"0\"\" to exit))]),While(UnaryOp(not,BinaryOp(OR,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0)))),[CallStmt(Id(Write),[StringLiteral(No.1: )]),CallStmt(Id(Readln),[Id(n1)]),CallStmt(Id(Write),[StringLiteral(No.2: )]),CallStmt(Id(Readln),[Id(n2)]),If(BinaryOp(OR,BinaryOp(=,Id(n1),StringLiteral(0)),BinaryOp(=,Id(n2),StringLiteral(0))),[CallStmt(Id(Halt),[IntLiteral(0)])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,308))
        

    def test_not_309(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not (NOT (n1 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If NOT (n1 = "0") Then Halt(0);
    End
End
        """
        expect = r"Program([VarDecl(Id(n1),StringType),VarDecl(Id(n2),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter two numbers: (\"\"0\"\" & \"\"0\"\" to exit))]),While(UnaryOp(not,UnaryOp(NOT,BinaryOp(=,Id(n1),StringLiteral(0)))),[CallStmt(Id(Write),[StringLiteral(No.1: )]),CallStmt(Id(Readln),[Id(n1)]),CallStmt(Id(Write),[StringLiteral(No.2: )]),CallStmt(Id(Readln),[Id(n2)]),If(UnaryOp(NOT,BinaryOp(=,Id(n1),StringLiteral(0))),[CallStmt(Id(Halt),[IntLiteral(0)])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,309))
        

    def test_and_310(self):
        input = """
Var age : Integer;
procedure main();
Begin
	While (age > 0) AND (age <= 100) Do
    Begin
		Write("Enter age (1 - 100): ");
		Readln(age);
		If (age < 1) Then
			Writeln("Age cannot be less than 1...");
		Else If (age > 100) Then
			Writeln("Age cannot be greater than 100...");
    End
End
        """
        expect = r"Program([VarDecl(Id(age),IntType),FuncDecl(Id(main),[],VoidType(),[],[While(BinaryOp(AND,BinaryOp(>,Id(age),IntLiteral(0)),BinaryOp(<=,Id(age),IntLiteral(100))),[CallStmt(Id(Write),[StringLiteral(Enter age (1 - 100): )]),CallStmt(Id(Readln),[Id(age)]),If(BinaryOp(<,Id(age),IntLiteral(1)),[CallStmt(Id(Writeln),[StringLiteral(Age cannot be less than 1...)])],[If(BinaryOp(>,Id(age),IntLiteral(100)),[CallStmt(Id(Writeln),[StringLiteral(Age cannot be greater than 100...)])],[])])])])])"
        self.assertTrue(TestAST.test(input,expect,310))
        

    def test_bool_311(self):
        input = """
Var 
	bool : Boolean;
	A, B : Integer;
Procedure main();
Begin
	A := 10;
	B := 30;
	bool := False;
	bool := (A = 10) OR (B = 10);
	Writeln(bool); { outputs TRUE }
	bool := (A = 10) AND (B = 10);
	Writeln(bool); { outputs FALSE }
End
        """
        expect = r"Program([VarDecl(Id(bool),BoolType),VarDecl(Id(A),IntType),VarDecl(Id(B),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(A),IntLiteral(10)),AssignStmt(Id(B),IntLiteral(30)),AssignStmt(Id(bool),BooleanLiteral(False)),AssignStmt(Id(bool),BinaryOp(OR,BinaryOp(=,Id(A),IntLiteral(10)),BinaryOp(=,Id(B),IntLiteral(10)))),CallStmt(Id(Writeln),[Id(bool)]),AssignStmt(Id(bool),BinaryOp(AND,BinaryOp(=,Id(A),IntLiteral(10)),BinaryOp(=,Id(B),IntLiteral(10)))),CallStmt(Id(Writeln),[Id(bool)])])])"
        self.assertTrue(TestAST.test(input,expect,311))
        

    def test_bool_312(self):
        input = """
Var quit : Boolean;
    a    : String;
Procedure main();
Begin
	While NOT (quit = True) Do
    Begin
		Writeln("Type \\\"\\\"exit\\\"\\\" to quit:");
		Readln(a);
		If a = "exit" Then 
			quit := True;
    End
End
        """
        expect = r"Program([VarDecl(Id(quit),BoolType),VarDecl(Id(a),StringType),FuncDecl(Id(main),[],VoidType(),[],[While(UnaryOp(NOT,BinaryOp(=,Id(quit),BooleanLiteral(True))),[CallStmt(Id(Writeln),[StringLiteral(Type \"\"exit\"\" to quit:)]),CallStmt(Id(Readln),[Id(a)]),If(BinaryOp(=,Id(a),StringLiteral(exit)),[AssignStmt(Id(quit),BooleanLiteral(True))],[])])])])"
        self.assertTrue(TestAST.test(input,expect,312))
        

    def test_for_313(self):
        input = """
Procedure DrawLine(); 
{This procedure helps me to avoid the rewriting the for loops}
Var Counter : Integer;
Begin
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End
End

Procedure Main();
Begin
	GotoXy(10,5);
	DrawLine();
	GotoXy(10,6);
	DrawLine();
	GotoXy(10,7);
	DrawLine();
	GotoXy(10,10);
	DrawLine();
	Readkey();
End
        """
        expect = r"Program([FuncDecl(Id(DrawLine),[],VoidType(),[VarDecl(Id(Counter),IntType)],[CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])]),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(Readkey),[])])])"
        self.assertTrue(TestAST.test(input,expect,313))
        

    def test_for_314(self):
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

Procedure main();
Begin
	DrawLine(10,5);
	DrawLine(10,6);
	DrawLine(10,7);
	DrawLine(10,10);
	Readkey();
End
        """
        expect = r"Program([FuncDecl(Id(DrawLine),[VarDecl(Id(X),IntType),VarDecl(Id(Y),IntType)],VoidType(),[VarDecl(Id(Counter),IntType)],[CallStmt(Id(GotoXy),[Id(X),Id(Y)]),CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(DrawLine),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(Readkey),[])])])"
        self.assertTrue(TestAST.test(input,expect,314))
        

    def test_procedure_315(self):
        input = """
Procedure Square(Index : Integer; Result : Integer);
Begin
	Result := Index * Index;
End

Var
	Res : Integer;

Procedure Main();
Begin
	Writeln("The square of 5 is: ");
	Square(5, Res);
	Writeln(Res);
End
        """
        expect = r"Program([FuncDecl(Id(Square),[VarDecl(Id(Index),IntType),VarDecl(Id(Result),IntType)],VoidType(),[],[AssignStmt(Id(Result),BinaryOp(*,Id(Index),Id(Index)))]),VarDecl(Id(Res),IntType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(The square of 5 is: )]),CallStmt(Id(Square),[IntLiteral(5),Id(Res)]),CallStmt(Id(Writeln),[Id(Res)])])])"
        self.assertTrue(TestAST.test(input,expect,315))
        

    def test_string_316(self):
        input = """
Var
	UserFile : String;
	FileName, TFile : String;

Procedure Main();
Begin
	Writeln("Enter the file name (including its full path) of the text file (without the extension):");
	Readln(FileName); { A .txt file will be assigned to a text variable }
	Assign(UserFile, FileName + ".txt");
	Reset(UserFile); { "Reset(x)" - means open the file x and reset cursor to the beginning of file }
	While NOT Eof(UserFile) Do
    Begin
		Readln(UserFile,TFile);
		Writeln(TFile);
	End
	Close(UserFile);
	Readln();
End
        """
        expect = r"Program([VarDecl(Id(UserFile),StringType),VarDecl(Id(FileName),StringType),VarDecl(Id(TFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Enter the file name (including its full path) of the text file (without the extension):)]),CallStmt(Id(Readln),[Id(FileName)]),CallStmt(Id(Assign),[Id(UserFile),BinaryOp(+,Id(FileName),StringLiteral(.txt))]),CallStmt(Id(Reset),[Id(UserFile)]),While(UnaryOp(NOT,CallExpr(Id(Eof),[Id(UserFile)])),[CallStmt(Id(Readln),[Id(UserFile),Id(TFile)]),CallStmt(Id(Writeln),[Id(TFile)])]),CallStmt(Id(Close),[Id(UserFile)]),CallStmt(Id(Readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,316))
        

    def test_string_317(self):
        input = """
Var
	FName, Txt : String;
	UserFile   : String; 

Procedure Main();
Begin
	FName := "Textfile";
	Assign(UserFile, "C:\\\\" + FName + ".txt"); {assign a text file}
	Rewrite(UserFile); {open the file "fname" for writing}
	Writeln(UserFile, "PASCAL PROGRAMMING");
	Writeln(UserFile, "if you did not understand something,");
	Writeln(UserFile, "please send me an email to:");
	Writeln(UserFile, "victorsaliba@hotmail.com");
	Writeln("Write some text to the file:");
	Readln(Txt);
	Writeln(UserFile, "");
	Writeln(UserFile, "The user entered this text:");
	Writeln(UserFile, Txt);
	Close(UserFile);
End
        """
        expect = r"Program([VarDecl(Id(FName),StringType),VarDecl(Id(Txt),StringType),VarDecl(Id(UserFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(Id(FName),StringLiteral(Textfile)),CallStmt(Id(Assign),[Id(UserFile),BinaryOp(+,BinaryOp(+,StringLiteral(C:\\),Id(FName)),StringLiteral(.txt))]),CallStmt(Id(Rewrite),[Id(UserFile)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(PASCAL PROGRAMMING)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(if you did not understand something,)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(please send me an email to:)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(victorsaliba@hotmail.com)]),CallStmt(Id(Writeln),[StringLiteral(Write some text to the file:)]),CallStmt(Id(Readln),[Id(Txt)]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral()]),CallStmt(Id(Writeln),[Id(UserFile),StringLiteral(The user entered this text:)]),CallStmt(Id(Writeln),[Id(UserFile),Id(Txt)]),CallStmt(Id(Close),[Id(UserFile)])])])"
        self.assertTrue(TestAST.test(input,expect,317))
        

    def test_string_318(self):
        input = """
Var
	UFile : String;

Procedure main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	ReWrite(UFile); 
	Writeln(UFile, "How many sentences " + "are present in this file?");
	Close(UFile);
End
        """
        expect = r"Program([VarDecl(Id(UFile),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(UFile),StringLiteral(C:\\ADDTEXT.TXT)]),CallStmt(Id(ReWrite),[Id(UFile)]),CallStmt(Id(Writeln),[Id(UFile),BinaryOp(+,StringLiteral(How many sentences ),StringLiteral(are present in this file?))]),CallStmt(Id(Close),[Id(UFile)])])])"
        self.assertTrue(TestAST.test(input,expect,318))
        

    def test_string_319(self):
        input = """
Var
	UFile : String;

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Append(UFile); 
	Writeln(UFile, "How many sentences, "+"are present in this file?");
	Close(UFile);
End
        """
        expect = r"Program([VarDecl(Id(UFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(UFile),StringLiteral(C:\\ADDTEXT.TXT)]),CallStmt(Id(Append),[Id(UFile)]),CallStmt(Id(Writeln),[Id(UFile),BinaryOp(+,StringLiteral(How many sentences, ),StringLiteral(are present in this file?))]),CallStmt(Id(Close),[Id(UFile)])])])"
        self.assertTrue(TestAST.test(input,expect,319))
        

    def test_string_320(self):
        input = """
Var
	UFile : String; { or it could be of "file" type}

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Erase(UFile); 
End
        """
        expect = r"Program([VarDecl(Id(UFile),StringType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(UFile),StringLiteral(C:\\ADDTEXT.TXT)]),CallStmt(Id(Erase),[Id(UFile)])])])"
        self.assertTrue(TestAST.test(input,expect,320))
        

    def test_string_321(self):
        input = """
Var
	t : String;
	s : String;

Procedure main();
Begin
	Assign(t, "C:\\\\ABC.DEF");
	{$I-}   { disable i/o error checking }
	Reset(t);
	{$I+}   { enable again i/o error checking - important }
	If (IOResult <> 0) Then
	Begin
		Writeln("The file required to be opened is not found!");
		Readln();
	End Else 
	Begin
		Readln(t,s);
		Writeln("The first line of the file reads: ",s);
		Close(t);
	End
End
        """
        expect = r"Program([VarDecl(Id(t),StringType),VarDecl(Id(s),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(t),StringLiteral(C:\\ABC.DEF)]),CallStmt(Id(Reset),[Id(t)]),If(BinaryOp(<>,Id(IOResult),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(The file required to be opened is not found!)]),CallStmt(Id(Readln),[])],[CallStmt(Id(Readln),[Id(t),Id(s)]),CallStmt(Id(Writeln),[StringLiteral(The first line of the file reads: ),Id(s)]),CallStmt(Id(Close),[Id(t)])])])])"
        self.assertTrue(TestAST.test(input,expect,321))
        

    def test_string_322(self):
        input = """
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
        expect = r"Program([VarDecl(Id(NewDir),StringType),VarDecl(Id(F),StringType),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(Id(NewDir),CallExpr(Id(FSearch),[StringLiteral(C:\\Pascal Programming),CallExpr(Id(GetEnv),[StringLiteral()])])),If(BinaryOp(=,Id(NewDir),StringLiteral()),[CallStmt(Id(CreateDir),[StringLiteral(C:\\Pascal Programming)])],[]),CallStmt(Id(Assign),[Id(F),StringLiteral(C:\\Pascal Programming\\pascal-programming.txt)]),CallStmt(Id(ReWrite),[Id(F)]),CallStmt(Id(Writeln),[Id(F),StringLiteral(http://pascal-programming.info/)]),CallStmt(Id(Close),[Id(F)])])])"
        self.assertTrue(TestAST.test(input,expect,322))
        

    def test_string_323(self):
        input = """
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
        expect = r"Program([VarDecl(Id(f),StringType),VarDecl(Id(sz),IntType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(f),StringLiteral(C:\\anyfile.txt)]),CallStmt(Id(Reset),[Id(f)]),If(BinaryOp(<>,Id(IOResult),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(File not found.. exiting)]),CallStmt(Id(Readln),[])],[AssignStmt(Id(sz),CallExpr(Id(Round),[BinaryOp(/,CallExpr(Id(FileSize),[Id(f)]),IntLiteral(1024))])),CallStmt(Id(Writeln),[StringLiteral(Size of the file in Kilobytes: ),Id(sz),StringLiteral( Kb)]),CallStmt(Id(Readln),[]),CallStmt(Id(Close),[Id(f)])])])])"
        self.assertTrue(TestAST.test(input,expect,323))
        

    def test_array_324(self):
        input = """
Var
	myVar : Integer;
	myArray : Array[1 .. 5] of Integer;

Procedure Main();
Begin
	myArray[2] := 25;
	myVar := myArray[2];
End
        """
        expect = r"Program([VarDecl(Id(myVar),IntType),VarDecl(Id(myArray),ArrayType(1,5,IntType)),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(ArrayCell(Id(myArray),IntLiteral(2)),IntLiteral(25)),AssignStmt(Id(myVar),ArrayCell(Id(myArray),IntLiteral(2)))])])"
        self.assertTrue(TestAST.test(input,expect,324))
        

    def test_array_325(self):
        input = """
Var
	i : Integer;
	myIntArray : Array[1 .. 20] of Integer;
	myBoolArray : Array[1 .. 20] of Boolean;

Procedure Main();
Begin
	For i := 1 to Length(myIntArray) do
	Begin
		myIntArray[i] := 1;
		myBoolArray[i] := True;
	End
End
        """
        expect = r"Program([VarDecl(Id(i),IntType),VarDecl(Id(myIntArray),ArrayType(1,20,IntType)),VarDecl(Id(myBoolArray),ArrayType(1,20,BoolType)),FuncDecl(Id(Main),[],VoidType(),[],[For(Id(i)IntLiteral(1),CallExpr(Id(Length),[Id(myIntArray)]),True,[AssignStmt(ArrayCell(Id(myIntArray),Id(i)),IntLiteral(1)),AssignStmt(ArrayCell(Id(myBoolArray),Id(i)),BooleanLiteral(True))])])])"
        self.assertTrue(TestAST.test(input,expect,325))
        

    def test_string_326(self):
        input = """
Var
    myString : String;

Procedure Main();
Begin
	myString := "Hey! How are you?";
	Writeln("The length of the string is ", byte(myString[0]));
	Write(myString[byte(myString[0])]);
	Write(" is the last character.");
End
        """
        expect = r"Program([VarDecl(Id(myString),StringType),FuncDecl(Id(Main),[],VoidType(),[],[AssignStmt(Id(myString),StringLiteral(Hey! How are you?)),CallStmt(Id(Writeln),[StringLiteral(The length of the string is ),CallExpr(Id(byte),[ArrayCell(Id(myString),IntLiteral(0))])]),CallStmt(Id(Write),[ArrayCell(Id(myString),CallExpr(Id(byte),[ArrayCell(Id(myString),IntLiteral(0))]))]),CallStmt(Id(Write),[StringLiteral( is the last character.)])])])"
        self.assertTrue(TestAST.test(input,expect,326))
        

    def test_string_327(self):
        input = """
Var
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	Write("The word \\"How\\" is found at char index ");
	Writeln(Pos("How", S));
	If Pos("Why", S) <= 0 Then
		Writeln("\\"Why\\" is not found.");
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey there! How are you?)),CallStmt(Id(Write),[StringLiteral(The word \"How\" is found at char index )]),CallStmt(Id(Writeln),[CallExpr(Id(Pos),[StringLiteral(How),Id(S)])]),If(BinaryOp(<=,CallExpr(Id(Pos),[StringLiteral(Why),Id(S)]),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(\"Why\" is not found.)])],[])])])"
        self.assertTrue(TestAST.test(input,expect,327))
        

    def test_string_328(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	S := Copy(S, 5, 6); { "there!" }
	Write(S);
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey there! How are you?)),AssignStmt(Id(S),CallExpr(Id(Copy),[Id(S),IntLiteral(5),IntLiteral(6)])),CallStmt(Id(Write),[Id(S)])])])"
        self.assertTrue(TestAST.test(input,expect,328))
        

    def test_string_329(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey Max! How are you?";
	Delete(S, 4, 4); { "Hey! How are you?" }
	Write(S);
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey Max! How are you?)),CallStmt(Id(Delete),[Id(S),IntLiteral(4),IntLiteral(4)]),CallStmt(Id(Write),[Id(S)])])])"
        self.assertTrue(TestAST.test(input,expect,329))
        

    def test_string_330(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey! How are you?";
	Insert(" Max", S, 4);
	Write(S);
  { "Hey Max! How are you?" }
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey! How are you?)),CallStmt(Id(Insert),[StringLiteral( Max),Id(S),IntLiteral(4)]),CallStmt(Id(Write),[Id(S)])])])"
        self.assertTrue(TestAST.test(input,expect,330))
        

    def test_string_331(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(Concat(S1, S2)); { "Hey! How are you?" }
End
        """
        expect = r"Program([VarDecl(Id(S1),StringType),VarDecl(Id(S2),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S1),StringLiteral(Hey!)),AssignStmt(Id(S2),StringLiteral( How are you?)),CallStmt(Id(Write),[CallExpr(Id(Concat),[Id(S1),Id(S2)])])])])"
        self.assertTrue(TestAST.test(input,expect,331))
        

    def test_string_332(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(S1 + S2); { "Hey! How are you?" }
End
        """
        expect = r"Program([VarDecl(Id(S1),StringType),VarDecl(Id(S2),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S1),StringLiteral(Hey!)),AssignStmt(Id(S2),StringLiteral( How are you?)),CallStmt(Id(Write),[BinaryOp(+,Id(S1),Id(S2))])])])"
        self.assertTrue(TestAST.test(input,expect,332))
        

    def test_string_333(self):
        input = """
Var 
   S : String;
   i : Integer;

Procedure main();
Begin
	S := "Hey! How are you?";
	For i := 1 to length(S) do
		S[i] := UpCase(S[i]);
	Write(S); { "HEY! HOW ARE YOU?" }
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),VarDecl(Id(i),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey! How are you?)),For(Id(i)IntLiteral(1),CallExpr(Id(length),[Id(S)]),True,[AssignStmt(ArrayCell(Id(S),Id(i)),CallExpr(Id(UpCase),[ArrayCell(Id(S),Id(i))]))]),CallStmt(Id(Write),[Id(S)])])])"
        self.assertTrue(TestAST.test(input,expect,333))
        

    def test_string_334(self):
        input = """
Var 
   S : String;

Procedure main();
Begin
	S := "Hey! How are you?";
	Write(UpCase(S)); { "HEY! HOW ARE YOU?" }
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(Hey! How are you?)),CallStmt(Id(Write),[CallExpr(Id(UpCase),[Id(S)])])])])"
        self.assertTrue(TestAST.test(input,expect,334))
        

    def test_string_335(self):
        input = """
Var 
	S : String;
	i : Real;

Procedure main();
Begin
	i := -0.563; 
	Str(i, S);
	Write(S); 
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),VarDecl(Id(i),FloatType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(i),UnaryOp(-,FloatLiteral(0.563))),CallStmt(Id(Str),[Id(i),Id(S)]),CallStmt(Id(Write),[Id(S)])])])"
        self.assertTrue(TestAST.test(input,expect,335))
        

    def test_string_336(self):
        input = """
Var 
	S     : String;
	error : Integer;
	R     : Real;

Procedure main();
Begin
	S := "-0.563"; 
	Val(S, R, error);
	If error > 0 Then
  	Write("Error in conversion.");
	Else
		Write(R); 
End
        """
        expect = r"Program([VarDecl(Id(S),StringType),VarDecl(Id(error),IntType),VarDecl(Id(R),FloatType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(S),StringLiteral(-0.563)),CallStmt(Id(Val),[Id(S),Id(R),Id(error)]),If(BinaryOp(>,Id(error),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(Error in conversion.)])],[CallStmt(Id(Write),[Id(R)])])])])"
        self.assertTrue(TestAST.test(input,expect,336))
        

    def test_complex_337(self):
        input = """
Procedure BubbleSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, temp : Integer;

Begin
	For i := size-1 DownTo 1 do
		For j := 2 to i do
			If (numbers[j-1] > numbers[j]) Then
			Begin
				temp := numbers[j-1];
				numbers[j-1] := numbers[j];
				numbers[j] := temp;
			End

End
        """
        expect = r"Program([FuncDecl(Id(BubbleSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(temp),IntType)],[For(Id(i)BinaryOp(-,Id(size),IntLiteral(1)),IntLiteral(1),False,[For(Id(j)IntLiteral(2),Id(i),True,[If(BinaryOp(>,ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),ArrayCell(Id(numbers),Id(j))),[AssignStmt(Id(temp),ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1)))),AssignStmt(ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),ArrayCell(Id(numbers),Id(j))),AssignStmt(ArrayCell(Id(numbers),Id(j)),Id(temp))],[])])])])])"
        self.assertTrue(TestAST.test(input,expect,337))
        

    def test_complex_338(self):
        input = """
Procedure InsertionSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, index : Integer;


Begin
	For i := 2 to size-1 do
	Begin
		index := numbers[i];
		j := i;
		While ((j > 1) AND (numbers[j-1] > index)) do
		Begin
			numbers[j] := numbers[j-1];
			j := j - 1;
		End
		numbers[j] := index;
	End
End
        """
        expect = r"Program([FuncDecl(Id(InsertionSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(index),IntType)],[For(Id(i)IntLiteral(2),BinaryOp(-,Id(size),IntLiteral(1)),True,[AssignStmt(Id(index),ArrayCell(Id(numbers),Id(i))),AssignStmt(Id(j),Id(i)),While(BinaryOp(AND,BinaryOp(>,Id(j),IntLiteral(1)),BinaryOp(>,ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),Id(index))),[AssignStmt(ArrayCell(Id(numbers),Id(j)),ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1)))),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))]),AssignStmt(ArrayCell(Id(numbers),Id(j)),Id(index))])])])"
        self.assertTrue(TestAST.test(input,expect,338))
        

    def test_complex_339(self):
        input = """
Procedure QSort(numbers : Array [1 .. 100] of Integer; left : Integer; right : Integer);
Var 
	pivot, l_ptr, r_ptr : Integer;

Begin
	l_ptr := left;
	r_ptr := right;
	pivot := numbers[left];

	While (left < right) do
	Begin
		While ((numbers[right] >= pivot) AND (left < right)) do
			right := right - 1;

		If (left <> right) Then
		Begin
			numbers[left] := numbers[right];
			left := left + 1;
		End

		While ((numbers[left] <= pivot) AND (left < right)) do
			left := left + 1;

		If (left <> right) Then
		Begin
			numbers[right] := numbers[left];
			right := right - 1;
		End
	End

	numbers[left] := pivot;
	pivot := left;
	left := l_ptr;
	right := r_ptr;

	If (left < pivot) Then
		QSort(numbers, left, pivot-1);

	If (right > pivot) Then
		QSort(numbers, pivot+1, right);
End

Procedure QuickSort(numbers : Array [1 .. 100] of Integer; size : Integer);
Begin
	QSort(numbers, 0, size-1);
End
        """
        expect = r"Program([FuncDecl(Id(QSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(left),IntType),VarDecl(Id(right),IntType)],VoidType(),[VarDecl(Id(pivot),IntType),VarDecl(Id(l_ptr),IntType),VarDecl(Id(r_ptr),IntType)],[AssignStmt(Id(l_ptr),Id(left)),AssignStmt(Id(r_ptr),Id(right)),AssignStmt(Id(pivot),ArrayCell(Id(numbers),Id(left))),While(BinaryOp(<,Id(left),Id(right)),[While(BinaryOp(AND,BinaryOp(>=,ArrayCell(Id(numbers),Id(right)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(left)),ArrayCell(Id(numbers),Id(right))),AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))],[]),While(BinaryOp(AND,BinaryOp(<=,ArrayCell(Id(numbers),Id(left)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(right)),ArrayCell(Id(numbers),Id(left))),AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))],[])]),AssignStmt(ArrayCell(Id(numbers),Id(left)),Id(pivot)),AssignStmt(Id(pivot),Id(left)),AssignStmt(Id(left),Id(l_ptr)),AssignStmt(Id(right),Id(r_ptr)),If(BinaryOp(<,Id(left),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),Id(left),BinaryOp(-,Id(pivot),IntLiteral(1))])],[]),If(BinaryOp(>,Id(right),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),BinaryOp(+,Id(pivot),IntLiteral(1)),Id(right)])],[])]),FuncDecl(Id(QuickSort),[VarDecl(Id(numbers),ArrayType(1,100,IntType)),VarDecl(Id(size),IntType)],VoidType(),[],[CallStmt(Id(QSort),[Id(numbers),IntLiteral(0),BinaryOp(-,Id(size),IntLiteral(1))])])])"
        self.assertTrue(TestAST.test(input,expect,339))
        

    def test_complex_340(self):
        input = """
Var
	myStack : Array[1 .. 100] of Integer;
	topPointer : Integer;


Procedure InitStack();
Begin
	topPointer := 0;
End
//We now implemement the IsEmpty() and IsFull() functions.

Function IsEmpty() : Boolean;
Begin
	IsEmpty := False;
	If (topPointer = 0) Then
		IsEmpty := true;
End

Function IsFull() : Boolean;
Begin
	IsFull := False;
	If ((topPointer + 1) = STACK_SIZE) Then
		IsFull := True;
End
//Here are the implementations of the Pop() and Push() functions and making use of the functions that we have just implemented.

Function Pop() : Integer;

Begin
	Pop := nil;

	If not IsEmpty Then
	Begin
		Pop := myStack[topPointer];
		topPointer := topPointer - 1; 
	End
End

Procedure Push(item : Integer);
Begin
	If not IsFull Then
	Begin
		myStack[topPointer+1] := item;
		topPointer := topPointer + 1;
	End
End

//Finally, we implement the utility function GetSize(). Although one can access the current size of the stack using the global variable topPointer, it is of good practice to make use of functions instead of global variables.

Function GetSize() : Integer;
Begin
	GetSize := topPointer;
End
        """
        expect = r"Program([VarDecl(Id(myStack),ArrayType(1,100,IntType)),VarDecl(Id(topPointer),IntType),FuncDecl(Id(InitStack),[],VoidType(),[],[AssignStmt(Id(topPointer),IntLiteral(0))]),FuncDecl(Id(IsEmpty),[],BoolType,[],[AssignStmt(Id(IsEmpty),BooleanLiteral(False)),If(BinaryOp(=,Id(topPointer),IntLiteral(0)),[AssignStmt(Id(IsEmpty),BooleanLiteral(True))],[])]),FuncDecl(Id(IsFull),[],BoolType,[],[AssignStmt(Id(IsFull),BooleanLiteral(False)),If(BinaryOp(=,BinaryOp(+,Id(topPointer),IntLiteral(1)),Id(STACK_SIZE)),[AssignStmt(Id(IsFull),BooleanLiteral(True))],[])]),FuncDecl(Id(Pop),[],IntType,[],[AssignStmt(Id(Pop),Id(nil)),If(UnaryOp(not,Id(IsEmpty)),[AssignStmt(Id(Pop),ArrayCell(Id(myStack),Id(topPointer))),AssignStmt(Id(topPointer),BinaryOp(-,Id(topPointer),IntLiteral(1)))],[])]),FuncDecl(Id(Push),[VarDecl(Id(item),IntType)],VoidType(),[],[If(UnaryOp(not,Id(IsFull)),[AssignStmt(ArrayCell(Id(myStack),BinaryOp(+,Id(topPointer),IntLiteral(1))),Id(item)),AssignStmt(Id(topPointer),BinaryOp(+,Id(topPointer),IntLiteral(1)))],[])]),FuncDecl(Id(GetSize),[],IntType,[],[AssignStmt(Id(GetSize),Id(topPointer))])])"
        self.assertTrue(TestAST.test(input,expect,340))
        

    def test_complex_341(self):
        input = """
Var Counter : Integer; { loop counter declared as integer }

Procedure main();
Begin
	For Counter := 1 to 7 do { it"s easy and fast! }
		Writeln("for loop");
	Readln();
End
        """
        expect = r"Program([VarDecl(Id(Counter),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(Counter)IntLiteral(1),IntLiteral(7),True,[CallStmt(Id(Writeln),[StringLiteral(for loop)])]),CallStmt(Id(Readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,341))
        

    def test_complex_342(self):
        input = """
Var 
	Counter : Integer;  { will be used as a loop counter }

Procedure main();
Begin

	For Counter := 1 to 5 do 
	Begin      
		gotoxy(25, 5 + Counter);
		Writeln("I");
	End

	For Counter := 5 Downto 1 do
	Begin  {an example of "downto" instead of "to", note the "gotoxy(_,_)"}
		gotoxy(32, 11 - Counter);
		Writeln("I");
	End

	For Counter := 1 to 6 do
	Begin
		gotoxy(25 + Counter, 11);
		Writeln("-");
	End

	For Counter := 6 Downto 1 do
	Begin
		gotoxy(32 - Counter, 5);
		Writeln("-");
	End

	{--------------The Corners(+)---------------}
	Gotoxy(25,5);
	Writeln("+");
	GotoXy(25,11);
	Writeln("+");
	GotoXy(32,5);
	Writeln("+");
	GotoXy(32,11);
	Writeln("+");
	GotoXy(45,7); 
	Write("Made with For Loops :)");
	Readln();
End
        """
        expect = r"Program([VarDecl(Id(Counter),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(Counter)IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(gotoxy),[IntLiteral(25),BinaryOp(+,IntLiteral(5),Id(Counter))]),CallStmt(Id(Writeln),[StringLiteral(I)])]),For(Id(Counter)IntLiteral(5),IntLiteral(1),False,[CallStmt(Id(gotoxy),[IntLiteral(32),BinaryOp(-,IntLiteral(11),Id(Counter))]),CallStmt(Id(Writeln),[StringLiteral(I)])]),For(Id(Counter)IntLiteral(1),IntLiteral(6),True,[CallStmt(Id(gotoxy),[BinaryOp(+,IntLiteral(25),Id(Counter)),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(-)])]),For(Id(Counter)IntLiteral(6),IntLiteral(1),False,[CallStmt(Id(gotoxy),[BinaryOp(-,IntLiteral(32),Id(Counter)),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(-)])]),CallStmt(Id(Gotoxy),[IntLiteral(25),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(25),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(32),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(32),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(+)]),CallStmt(Id(GotoXy),[IntLiteral(45),IntLiteral(7)]),CallStmt(Id(Write),[StringLiteral(Made with For Loops :))]),CallStmt(Id(Readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,342))
        

    def test_complex_343(self):
        input = """
Var Ch : String;

Procedure main();
Begin
	Writeln("Press \\"\\"q\\"\\" to exit...");
	Ch := Readkey();
	While Ch <> "q" do 
	Begin
		Writeln("Please press \\"\\"q\\"\\" to exit.");
		Ch := Readkey();
	End
End
        """
        expect = r"Program([VarDecl(Id(Ch),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Press \"\"q\"\" to exit...)]),AssignStmt(Id(Ch),CallExpr(Id(Readkey),[])),While(BinaryOp(<>,Id(Ch),StringLiteral(q)),[CallStmt(Id(Writeln),[StringLiteral(Please press \"\"q\"\" to exit.)]),AssignStmt(Id(Ch),CallExpr(Id(Readkey),[]))])])])"
        self.assertTrue(TestAST.test(input,expect,343))
        

    def test_complex_344(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;
	i : Integer;

Begin
	Result := n;
	If (n <= 1) Then
		Result := 1;
	Else
	For i := n-1 DownTo 1 do
		Result := Result * i; 
	Factorial := Result;
End
        """
        expect = r"Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType),VarDecl(Id(i),IntType)],[AssignStmt(Id(Result),Id(n)),If(BinaryOp(<=,Id(n),IntLiteral(1)),[AssignStmt(Id(Result),IntLiteral(1))],[For(Id(i)BinaryOp(-,Id(n),IntLiteral(1)),IntLiteral(1),False,[AssignStmt(Id(Result),BinaryOp(*,Id(Result),Id(i)))])]),AssignStmt(Id(Factorial),Id(Result))])])"
        self.assertTrue(TestAST.test(input,expect,344))
        

    def test_complex_345(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;

Begin
	If n = 1 Then 
		Factorial := 1;
	Else
		Factorial := n*Factorial(n-1);
End
        """
        expect = r"Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType)],[If(BinaryOp(=,Id(n),IntLiteral(1)),[AssignStmt(Id(Factorial),IntLiteral(1))],[AssignStmt(Id(Factorial),BinaryOp(*,Id(n),CallExpr(Id(Factorial),[BinaryOp(-,Id(n),IntLiteral(1))])))])])])"
        self.assertTrue(TestAST.test(input,expect,345))
        

    def test_complex_346(self):
        input = """
var
age, weekdays : integer;
taxrate, net_income: real;
choice, isready: boolean;
name, surname : string;
        """
        expect = r"Program([VarDecl(Id(age),IntType),VarDecl(Id(weekdays),IntType),VarDecl(Id(taxrate),FloatType),VarDecl(Id(net_income),FloatType),VarDecl(Id(choice),BoolType),VarDecl(Id(isready),BoolType),VarDecl(Id(name),StringType),VarDecl(Id(surname),StringType)])"
        self.assertTrue(TestAST.test(input,expect,346))
        

    def test_complex_347(self):
        input = """
var
firstname, surname: string;

procedure main();
begin
   writeln("Please enter your first name: ");
   readln(firstname);
   
   writeln("Please enter your surname: ");
   readln(surname);
   
   writeln();
   writeln(message, " ", firstname, " ", surname);
end
        """
        expect = r"Program([VarDecl(Id(firstname),StringType),VarDecl(Id(surname),StringType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(Please enter your first name: )]),CallStmt(Id(readln),[Id(firstname)]),CallStmt(Id(writeln),[StringLiteral(Please enter your surname: )]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[Id(message),StringLiteral( ),Id(firstname),StringLiteral( ),Id(surname)])])])"
        self.assertTrue(TestAST.test(input,expect,347))
        

    def test_complex_348(self):
        input = """
procedure main();
var a:integer;
begin
a := a = a and then b;
end
        """
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(a),IntType)],[AssignStmt(Id(a),BinaryOp(andthen,BinaryOp(=,Id(a),Id(a)),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,348))
        

    def test_complex_349(self):
        input = """
var
{ local variable declaration }
   a:integer;

procedure main();
begin
   a:= 10;
   (* check the boolean condition using if statement *)
   
   if( a < 20 ) then
      (* if condition is true then print the following *) 
      writeln("a is less than 20 " );
   writeln("value of a is : ", a);
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),If(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(a is less than 20 )])],[]),CallStmt(Id(writeln),[StringLiteral(value of a is : ),Id(a)])])])"
        self.assertTrue(TestAST.test(input,expect,349))
        

    def test_if_350(self):
        input = """
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
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),If(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(a is less than 20)])],[CallStmt(Id(writeln),[StringLiteral(a is not less than 20)])]),CallStmt(Id(writeln),[StringLiteral(value of a is : ),Id(a)])])])"
        self.assertTrue(TestAST.test(input,expect,350))
        

    def test_if_351(self):
        input = """
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if (a = 10)  then
      (* if condition is true then print the following *)
      writeln("Value of a is 10" );
   
   else if ( a = 20 ) then
      (* if else if condition is true *)
      writeln("Value of a is 20" );
   
   else if( a = 30 ) then 
      (* if else if condition is true  *)
      writeln("Value of a is 30" );
   
   else
      (* if none of the conditions is true *)
      writeln("None of the values is matching" );
      writeln("Exact value of a is: ", a );
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),If(BinaryOp(=,Id(a),IntLiteral(10)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 10)])],[If(BinaryOp(=,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 20)])],[If(BinaryOp(=,Id(a),IntLiteral(30)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 30)])],[CallStmt(Id(writeln),[StringLiteral(None of the values is matching)])])])]),CallStmt(Id(writeln),[StringLiteral(Exact value of a is: ),Id(a)])])])"
        self.assertTrue(TestAST.test(input,expect,351))
        

    def test_if_352(self):
        input = """
var
   { local variable definition }
   a, b : integer;

procedure main();
begin
   a := 100;
   b:= 200;
   
   (* check the boolean condition *)
   if (a = 100) then
      (* if condition is true then check the following *)
      if ( b = 200 ) then
         (* if nested if condition is true  then print the following *)
         writeln("Value of a is 100 and value of b is 200" );
   
   writeln("Exact value of a is: ", a );
   writeln("Exact value of b is: ", b );
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),If(BinaryOp(=,Id(a),IntLiteral(100)),[If(BinaryOp(=,Id(b),IntLiteral(200)),[CallStmt(Id(writeln),[StringLiteral(Value of a is 100 and value of b is 200)])],[])],[]),CallStmt(Id(writeln),[StringLiteral(Exact value of a is: ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(Exact value of b is: ),Id(b)])])])"
        self.assertTrue(TestAST.test(input,expect,352))
        

    def test_while_353(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   while  a < 20  do
   
   begin
      writeln("value of a: ", a);
      a := a + 1;
   end
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])"
        self.assertTrue(TestAST.test(input,expect,353))
        

    def test_for_354(self):
        input = """
var
   a: integer;

procedure main();
begin
   for a := 10  to 20 do
   
   begin
      writeln("value of a: ", a);
   end
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(a)IntLiteral(10),IntLiteral(20),True,[CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)])])])])"
        self.assertTrue(TestAST.test(input,expect,354))
        

    def test_for_355(self):
        input = """
var
   i, j:integer;

procedure main();
begin
   for i := 2 to 50 do
   
   begin
      for j := 2 to i do
         if (i mod j)=0  then
            break; {* if factor found, not prime *}
      
      if(j = i) then
         writeln(i , " is prime" );
   end
end
        """
        expect = r"Program([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)IntLiteral(2),IntLiteral(50),True,[For(Id(j)IntLiteral(2),Id(i),True,[If(BinaryOp(=,BinaryOp(mod,Id(i),Id(j)),IntLiteral(0)),[Break],[])]),If(BinaryOp(=,Id(j),Id(i)),[CallStmt(Id(writeln),[Id(i),StringLiteral( is prime)])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,355))
        

    def test_break_356(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   (* while loop execution *)
   while  a < 20 do
   
   begin
      writeln("value of a: ", a);
      a:=a +1;
      
      if( a > 15) then
         (* terminate the loop using break statement *)
      break;
   end
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(BinaryOp(<,Id(a),IntLiteral(20)),[CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(>,Id(a),IntLiteral(15)),[Break],[])])])])"
        self.assertTrue(TestAST.test(input,expect,356))
        

    def test_continue_357(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   
   while not ( a = 20 ) do
   begin
      if( a = 15) then
      
      begin
         (* skip the iteration *)
         a := a + 1;
         continue;
      end
      
      writeln("value of a: ", a);
      a := a+1;
   end
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),While(UnaryOp(not,BinaryOp(=,Id(a),IntLiteral(20))),[If(BinaryOp(=,Id(a),IntLiteral(15)),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Continue],[]),CallStmt(Id(writeln),[StringLiteral(value of a: ),Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])"
        self.assertTrue(TestAST.test(input,expect,357))
        

    def test_function_358(self):
        input = """
function max(num1, num2: integer): integer;

var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end
        """
        expect = r"Program([FuncDecl(Id(max),[VarDecl(Id(num1),IntType),VarDecl(Id(num2),IntType)],IntType,[VarDecl(Id(result),IntType)],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result))])])"
        self.assertTrue(TestAST.test(input,expect,358))
        

    def test_function_359(self):
        input = """
var
   a, b, ret : integer;

(*function definition *)
function max(num1, num2: integer): integer;
var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end

procedure main();
begin
   a := 100;
   b := 200;
   (* calling a function to get max value *)
   ret := max(a, b);
   
   writeln( "Max value is : ", ret );
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(ret),IntType),FuncDecl(Id(max),[VarDecl(Id(num1),IntType),VarDecl(Id(num2),IntType)],IntType,[VarDecl(Id(result),IntType)],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result))]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(ret),CallExpr(Id(max),[Id(a),Id(b)])),CallStmt(Id(writeln),[StringLiteral(Max value is : ),Id(ret)])])])"
        self.assertTrue(TestAST.test(input,expect,359))
        

    def test_procedure_360(self):
        input = """
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m := x;
   else
      m := y;
   
   if z <m then
      m := z;
end { end of procedure findMin }  
        """
        expect = r"Program([FuncDecl(Id(findMin),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),VarDecl(Id(m),IntType)],VoidType(),[],[If(BinaryOp(<,Id(x),Id(y)),[AssignStmt(Id(m),Id(x))],[AssignStmt(Id(m),Id(y))]),If(BinaryOp(<,Id(z),Id(m)),[AssignStmt(Id(m),Id(z))],[])])])"
        self.assertTrue(TestAST.test(input,expect,360))
        

    def test_procedure_361(self):
        input = """
var
   a, b, c,  min: integer;
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m:= x;
   else
      m:= y;
   
   if z < m then
      m:= z;
end { end of procedure findMin }  

procedure main();
begin
   writeln(" Enter three numbers: ");
   readln( a, b, c);
   findMin(a, b, c, min); (* Procedure call *)
   
   writeln(" Minimum: ", min);
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(min),IntType),FuncDecl(Id(findMin),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),VarDecl(Id(m),IntType)],VoidType(),[],[If(BinaryOp(<,Id(x),Id(y)),[AssignStmt(Id(m),Id(x))],[AssignStmt(Id(m),Id(y))]),If(BinaryOp(<,Id(z),Id(m)),[AssignStmt(Id(m),Id(z))],[])]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral( Enter three numbers: )]),CallStmt(Id(readln),[Id(a),Id(b),Id(c)]),CallStmt(Id(findMin),[Id(a),Id(b),Id(c),Id(min)]),CallStmt(Id(writeln),[StringLiteral( Minimum: ),Id(min)])])])"
        self.assertTrue(TestAST.test(input,expect,361))
        

    def test_complex_362(self):
        input = """
var
   num, f: integer;
function fact(x: integer): integer; (* calculates factorial of x - x! *)

begin
   if x=0 then
      fact := 1;
   else
      fact := x * fact(x-1); (* recursive call *)
end { end of function fact}

procedure main();
begin
   writeln(" Enter a number: ");
   readln(num);
   f := fact(num);
   
   writeln(" Factorial ", num, " is: " , f);
end
        """
        expect = r"Program([VarDecl(Id(num),IntType),VarDecl(Id(f),IntType),FuncDecl(Id(fact),[VarDecl(Id(x),IntType)],IntType,[],[If(BinaryOp(=,Id(x),IntLiteral(0)),[AssignStmt(Id(fact),IntLiteral(1))],[AssignStmt(Id(fact),BinaryOp(*,Id(x),CallExpr(Id(fact),[BinaryOp(-,Id(x),IntLiteral(1))])))])]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral( Enter a number: )]),CallStmt(Id(readln),[Id(num)]),AssignStmt(Id(f),CallExpr(Id(fact),[Id(num)])),CallStmt(Id(writeln),[StringLiteral( Factorial ),Id(num),StringLiteral( is: ),Id(f)])])])"
        self.assertTrue(TestAST.test(input,expect,362))
        

    def test_complex_363(self):
        input = """
var
   i: integer;
function fibonacci(n: integer): integer;

begin
   if n=1 then
      fibonacci := 0;
   
   else if n=2 then
      fibonacci := 1;
   
   else
      fibonacci := fibonacci(n-1) + fibonacci(n-2);
end

procedure main();
begin
   for i:= 1 to 10 do
   
   write(fibonacci (i), "  ");
end
        """
        expect = r"Program([VarDecl(Id(i),IntType),FuncDecl(Id(fibonacci),[VarDecl(Id(n),IntType)],IntType,[],[If(BinaryOp(=,Id(n),IntLiteral(1)),[AssignStmt(Id(fibonacci),IntLiteral(0))],[If(BinaryOp(=,Id(n),IntLiteral(2)),[AssignStmt(Id(fibonacci),IntLiteral(1))],[AssignStmt(Id(fibonacci),BinaryOp(+,CallExpr(Id(fibonacci),[BinaryOp(-,Id(n),IntLiteral(1))]),CallExpr(Id(fibonacci),[BinaryOp(-,Id(n),IntLiteral(2))])))])])]),FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(write),[CallExpr(Id(fibonacci),[Id(i)]),StringLiteral(  )])])])])"
        self.assertTrue(TestAST.test(input,expect,363))
        

    def test_complex_364(self):
        input = """
var
   a, b : integer;
(*procedure definition *)
procedure swap(x, y: integer); 

var
   temp: integer;

begin
   temp := x;
   x:= y;
   y := temp;
end

procedure main();
begin
   a := 100;
   b := 200;
   writeln("Before swap, value of a : ", a );
   writeln("Before swap, value of b : ", b );
   
   (* calling the procedure swap  by value   *)
   swap(a, b);
   writeln("After swap, value of a : ", a );
   writeln("After swap, value of b : ", b );
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),FuncDecl(Id(swap),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType)],VoidType(),[VarDecl(Id(temp),IntType)],[AssignStmt(Id(temp),Id(x)),AssignStmt(Id(x),Id(y)),AssignStmt(Id(y),Id(temp))]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),CallStmt(Id(writeln),[StringLiteral(Before swap, value of a : ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(Before swap, value of b : ),Id(b)]),CallStmt(Id(swap),[Id(a),Id(b)]),CallStmt(Id(writeln),[StringLiteral(After swap, value of a : ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(After swap, value of b : ),Id(b)])])])"
        self.assertTrue(TestAST.test(input,expect,364))
        

    def test_easy_365(self):
        input = """
var
   a, b, c: integer;

procedure main();
begin
   (* actual initialization *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(10)),AssignStmt(Id(b),IntLiteral(20)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)])])])"
        self.assertTrue(TestAST.test(input,expect,365))
        

    def test_easy_366(self):
        input = """
var
   a, b, c: integer;
procedure display();

var
   a, b, c: integer;
begin
   (* local variables *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("Winthin the procedure display");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= a + b;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   display();
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),FuncDecl(Id(display),[],VoidType(),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)],[AssignStmt(Id(a),IntLiteral(10)),AssignStmt(Id(b),IntLiteral(20)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),CallStmt(Id(writeln),[StringLiteral(Winthin the procedure display)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)])]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),CallStmt(Id(writeln),[StringLiteral(Winthin the program exlocal)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(display),[])])])"
        self.assertTrue(TestAST.test(input,expect,366))
        

    def test_complex_367(self):
        input = """
var
   a, b, c: integer;
procedure display();
var
   x, y, z: integer;

begin
   (* local variables *)
   x := 10;
   y := 20;
   z := x + y;
   
   (*global variables *)
   a := 30;
   b:= 40;
   c:= a + b;
   
   writeln("Winthin the procedure display");
   writeln(" Displaying the global variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   writeln("Displaying the local variables x, y, and z");
   
   writeln("value of x = ", x , " y =  ",  y, " and z = ", z);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= 300;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   
   display();
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),FuncDecl(Id(display),[],VoidType(),[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType)],[AssignStmt(Id(x),IntLiteral(10)),AssignStmt(Id(y),IntLiteral(20)),AssignStmt(Id(z),BinaryOp(+,Id(x),Id(y))),AssignStmt(Id(a),IntLiteral(30)),AssignStmt(Id(b),IntLiteral(40)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),CallStmt(Id(writeln),[StringLiteral(Winthin the procedure display)]),CallStmt(Id(writeln),[StringLiteral( Displaying the global variables a, b, and c)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(writeln),[StringLiteral(Displaying the local variables x, y, and z)]),CallStmt(Id(writeln),[StringLiteral(value of x = ),Id(x),StringLiteral( y =  ),Id(y),StringLiteral( and z = ),Id(z)])]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(c),IntLiteral(300)),CallStmt(Id(writeln),[StringLiteral(Winthin the program exlocal)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(display),[])])])"
        self.assertTrue(TestAST.test(input,expect,367))
        

    def test_complex_368(self):
        input = """
var
   a, b, c: integer;
procedure display();

var
   a, b, c: integer;

begin
   (* local variables *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("Winthin the procedure display");
   writeln(" Displaying the global variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   writeln("Displaying the local variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= 300;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);   
   
   display();
end
        """
        expect = r"Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),FuncDecl(Id(display),[],VoidType(),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)],[AssignStmt(Id(a),IntLiteral(10)),AssignStmt(Id(b),IntLiteral(20)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),CallStmt(Id(writeln),[StringLiteral(Winthin the procedure display)]),CallStmt(Id(writeln),[StringLiteral( Displaying the global variables a, b, and c)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(writeln),[StringLiteral(Displaying the local variables a, b, and c)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)])]),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(c),IntLiteral(300)),CallStmt(Id(writeln),[StringLiteral(Winthin the program exlocal)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(display),[])])])"
        self.assertTrue(TestAST.test(input,expect,368))
        

    def test_string_369(self):
        input = """
var
   greetings: string;
   name: array [1 .. 10] of integer;
   organisation: string;

procedure main();
begin
   greetings := "Hello ";
   message := "Good Day!";
   
   writeln("Please Enter your Name");
   readln(name);
   
   writeln("Please Enter the name of your Organisation");
   readln(organisation);
   
   writeln(greetings, name, " from ", organisation);
   writeln(message); 
end
        """
        expect = r"Program([VarDecl(Id(greetings),StringType),VarDecl(Id(name),ArrayType(1,10,IntType)),VarDecl(Id(organisation),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(greetings),StringLiteral(Hello )),AssignStmt(Id(message),StringLiteral(Good Day!)),CallStmt(Id(writeln),[StringLiteral(Please Enter your Name)]),CallStmt(Id(readln),[Id(name)]),CallStmt(Id(writeln),[StringLiteral(Please Enter the name of your Organisation)]),CallStmt(Id(readln),[Id(organisation)]),CallStmt(Id(writeln),[Id(greetings),Id(name),StringLiteral( from ),Id(organisation)]),CallStmt(Id(writeln),[Id(message)])])])"
        self.assertTrue(TestAST.test(input,expect,369))
        

    def test_string_370(self):
        input = """
var
   str1, str2, str3 : string;
   str4: string;
   len: integer;

procedure main();
begin
   str1 := "Hello ";
   str2 := "There!";
   
   (* copy str1 into str3 *)
   str3 := str1;
   writeln("appendstr( str3, str1) :  ", str3 );
   
   (* concatenates str1 and str2 *)
   appendstr( str1, str2);
   writeln( "appendstr( str1, str2) " , str1 );
   str4 := str1 + str2;
   writeln("Now str4 is: ", str4);
   
   (* total lenghth of str4 after concatenation  *)
   len := byte(str4[0]);
   writeln("Length of the final string str4: ", len); 
end
        """
        expect = r"Program([VarDecl(Id(str1),StringType),VarDecl(Id(str2),StringType),VarDecl(Id(str3),StringType),VarDecl(Id(str4),StringType),VarDecl(Id(len),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(str1),StringLiteral(Hello )),AssignStmt(Id(str2),StringLiteral(There!)),AssignStmt(Id(str3),Id(str1)),CallStmt(Id(writeln),[StringLiteral(appendstr( str3, str1) :  ),Id(str3)]),CallStmt(Id(appendstr),[Id(str1),Id(str2)]),CallStmt(Id(writeln),[StringLiteral(appendstr( str1, str2) ),Id(str1)]),AssignStmt(Id(str4),BinaryOp(+,Id(str1),Id(str2))),CallStmt(Id(writeln),[StringLiteral(Now str4 is: ),Id(str4)]),AssignStmt(Id(len),CallExpr(Id(byte),[ArrayCell(Id(str4),IntLiteral(0))])),CallStmt(Id(writeln),[StringLiteral(Length of the final string str4: ),Id(len)])])])"
        self.assertTrue(TestAST.test(input,expect,370))
        

    def test_bool_371(self):
        input = """
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
        expect = r"Program([VarDecl(Id(exit),BoolType),VarDecl(Id(choice),IntType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(Do you want to continue? )]),CallStmt(Id(writeln),[StringLiteral(Enter Y/y for yes, and N/n for no)]),CallStmt(Id(readln),[Id(choice)]),If(BinaryOp(=,Id(choice),StringLiteral(n)),[AssignStmt(Id(exit),BooleanLiteral(True))],[AssignStmt(Id(exit),BooleanLiteral(False))]),If(Id(exit),[CallStmt(Id(writeln),[StringLiteral( Good Bye!)])],[CallStmt(Id(writeln),[StringLiteral(Please Continue)])]),CallStmt(Id(readln),[])])])"
        self.assertTrue(TestAST.test(input,expect,371))
        

    def test_array_372(self):
        input = """
var
   n: array [1 .. 10] of integer;   (* n is an array of 10 integers *)
   i, j: integer;

procedure main();
begin
   (* initialize elements of array n to 0 *)        
   for i := 1 to 10 do
       n[ i ] := i + 100;   (* set element at location i to i + 100 *)
    (* output each array element"s value *)
   
   for j:= 1 to 10 do
      writeln("Element[", j, "] = ", n[j] );
end
        """
        expect = r"Program([VarDecl(Id(n),ArrayType(1,10,IntType)),VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)IntLiteral(1),IntLiteral(10),True,[AssignStmt(ArrayCell(Id(n),Id(i)),BinaryOp(+,Id(i),IntLiteral(100)))]),For(Id(j)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(writeln),[StringLiteral(Element[),Id(j),StringLiteral(] = ),ArrayCell(Id(n),Id(j))])])])])"
        self.assertTrue(TestAST.test(input,expect,372))
        

    def test_complex_373(self):
        input = """
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
        expect = r"Program([VarDecl(Id(X),FloatType),VarDecl(Id(Y1),FloatType),VarDecl(Id(Y2),FloatType),VarDecl(Id(First),FloatType),VarDecl(Id(Last),FloatType),VarDecl(Id(Incr),FloatType),VarDecl(Id(Factor),FloatType),VarDecl(Id(Q1),IntType),VarDecl(Id(Q2),IntType),VarDecl(Id(Step),IntType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Enter  first value: )]),CallStmt(Id(Read),[Id(First)]),CallStmt(Id(Write),[StringLiteral(Enter  last value: )]),CallStmt(Id(Read),[Id(Last)]),CallStmt(Id(Write),[StringLiteral(Enter  scale factor: )]),CallStmt(Id(Read),[Id(Factor)]),CallStmt(Id(Write),[StringLiteral(Enter an  increment: )]),CallStmt(Id(Read),[Id(Incr)]),CallStmt(Id(WriteLn),[]),For(Id(Step)IntLiteral(0),Id(MaxY),True,[If(BinaryOp(=,BinaryOp(MOD,Id(Step),IntLiteral(5)),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(+)])],[CallStmt(Id(Write),[StringLiteral(-)])])]),CallStmt(Id(Write),[StringLiteral( Y )]),CallStmt(Id(WriteLn),[]),AssignStmt(Id(X),Id(First)),While(BinaryOp(<=,Id(X),Id(Last)),[AssignStmt(Id(Y1),CallExpr(Id(SIN),[BinaryOp(/,BinaryOp(*,FloatLiteral(3.14159),Id(X)),FloatLiteral(180.0))])),AssignStmt(Id(Y1),BinaryOp(*,Id(Factor),Id(Y1))),AssignStmt(Id(Q1),CallExpr(Id(ROUND),[Id(Y1)])),AssignStmt(Id(Y2),BinaryOp(*,FloatLiteral(0.005),Id(X))),AssignStmt(Id(Y2),BinaryOp(*,Id(Factor),Id(Y2))),AssignStmt(Id(Q2),CallExpr(Id(ROUND),[Id(Y2)])),For(Id(Step)IntLiteral(0),Id(MaxY),True,[If(BinaryOp(=,Id(Step),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(|)])],[If(BinaryOp(=,Id(Step),Id(Q1)),[CallStmt(Id(Write),[StringLiteral(*)])],[If(BinaryOp(=,Id(Step),Id(Q2)),[CallStmt(Id(Write),[StringLiteral(+)])],[CallStmt(Id(Write),[StringLiteral( )])])])])]),CallStmt(Id(WriteLn),[]),AssignStmt(Id(X),BinaryOp(+,Id(X),Id(Incr)))]),CallStmt(Id(Write),[StringLiteral(X)])])])"
        self.assertTrue(TestAST.test(input,expect,373))
        

    def test_complex_374(self):
        input = """
  VAR First,  Second, Left, Right: BOOLEAN;
  PROCEDURE  WriteBool(Val: BOOLEAN);
  BEGIN
  IF Val THEN
  Write("TRUE ");
  ELSE
  Write("FALSE ");
  END { WriteBool  }
  PROCEDURE Main();
  BEGIN
  { Write Header }
  WriteLn("Proof  of DeMorgan theorem ");
  WriteLn();
  WriteLn("First  Second Left Right ");
  WriteLn("-----  ------ ----- ----- ");
  { Loop through  all truth value combinations }
  FOR First :=  FALSE TO TRUE DO
  FOR Second :=  FALSE TO TRUE DO BEGIN
  { Write out  Input values of First, Second }
  WriteBool(First);
  WriteBool(Second);
  { Separate Input  values from the output }
  Write(" ");
  Left := (NOT  First) AND (NOT Second);
  Right := NOT(First OR Second);
  { Write out the  new values of Left, Right }
  WriteBool(Left);
  WriteBool(Right);
  WriteLn();
  END { Inner FOR  }
  END { TruthTable  }
        """
        expect = r"Program([VarDecl(Id(First),BoolType),VarDecl(Id(Second),BoolType),VarDecl(Id(Left),BoolType),VarDecl(Id(Right),BoolType),FuncDecl(Id(WriteBool),[VarDecl(Id(Val),BoolType)],VoidType(),[],[If(Id(Val),[CallStmt(Id(Write),[StringLiteral(TRUE )])],[CallStmt(Id(Write),[StringLiteral(FALSE )])])]),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(WriteLn),[StringLiteral(Proof  of DeMorgan theorem )]),CallStmt(Id(WriteLn),[]),CallStmt(Id(WriteLn),[StringLiteral(First  Second Left Right )]),CallStmt(Id(WriteLn),[StringLiteral(-----  ------ ----- ----- )]),For(Id(First)BooleanLiteral(False),BooleanLiteral(True),True,[For(Id(Second)BooleanLiteral(False),BooleanLiteral(True),True,[CallStmt(Id(WriteBool),[Id(First)]),CallStmt(Id(WriteBool),[Id(Second)]),CallStmt(Id(Write),[StringLiteral( )]),AssignStmt(Id(Left),BinaryOp(AND,UnaryOp(NOT,Id(First)),UnaryOp(NOT,Id(Second)))),AssignStmt(Id(Right),UnaryOp(NOT,BinaryOp(OR,Id(First),Id(Second)))),CallStmt(Id(WriteBool),[Id(Left)]),CallStmt(Id(WriteBool),[Id(Right)]),CallStmt(Id(WriteLn),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,374))
        

    def test_string_375(self):
        input = """
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
        expect = r"Program([VarDecl(Id(FirstName),StringType),VarDecl(Id(LastName),StringType),VarDecl(Id(FullName),StringType),VarDecl(Id(Count),IntType),VarDecl(Id(NameCount),IntType),VarDecl(Id(Gap),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(Space),StringLiteral(  )),AssignStmt(Id(Hyphen),StringLiteral(-)),AssignStmt(Id(Greeting),StringLiteral(Hello there )),CallStmt(Id(Write),[StringLiteral(Enter the  number of names: )]),CallStmt(Id(ReadLn),[Id(NameCount)]),CallStmt(Id(WriteLn),[]),While(BinaryOp(>,Id(NameCount),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(Enter a  name, last name first: )]),CallStmt(Id(Read),[Id(FullName)]),AssignStmt(Id(Gap),CallExpr(Id(POS),[Id(Space),Id(FullName)])),If(BinaryOp(>,Id(Gap),IntLiteral(0)),[AssignStmt(Id(LastName),CallExpr(Id(Copy),[Id(FullName),IntLiteral(1),Id(Gap)])),CallStmt(Id(Delete),[Id(FullName),IntLiteral(1),Id(Gap)]),AssignStmt(Id(FirstName),Id(FullName)),If(BinaryOp(<=,CallExpr(Id(Length),[Id(LastName)]),IntLiteral(4)),[CallStmt(Id(WriteLn),[StringLiteral(That is  a short last name)])],[]),If(BinaryOp(<>,CallExpr(Id(Pos),[Id(Hyphen),Id(LastName)]),IntLiteral(0)),[CallStmt(Id(WriteLn),[StringLiteral(That is  a hyphenated name)])],[]),If(BinaryOp(=,Id(FirstName),StringLiteral(Bill)),[CallStmt(Id(WriteLn),[StringLiteral(Bill is  a good name )])],[]),AssignStmt(Id(FullName),BinaryOp(+,BinaryOp(+,Id(FirstName),Id(Space)),Id(LastName))),CallStmt(Id(WriteLn),[Id(Greeting),Id(FullName)]),CallStmt(Id(WriteLn),[])],[]),AssignStmt(Id(NameCount),BinaryOp(-,Id(NameCount),IntLiteral(1)))])])])"
        self.assertTrue(TestAST.test(input,expect,375))
        

    def test_easy_376(self):
        input = """
PROCEDURE main(); 
  BEGIN (* To De-Militarize Time *)
  Read(MilTime);
  Hours := MilTime  DIV 100;
  Minutes :=  MilTime MOD 100;
  Write(Hours,  Minutes);
  END (* of  De-Militarizing Time *)
        """
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Read),[Id(MilTime)]),AssignStmt(Id(Hours),BinaryOp(DIV,Id(MilTime),IntLiteral(100))),AssignStmt(Id(Minutes),BinaryOp(MOD,Id(MilTime),IntLiteral(100))),CallStmt(Id(Write),[Id(Hours),Id(Minutes)])])])"
        self.assertTrue(TestAST.test(input,expect,376))
        

    def test_complex_377(self):
        input = """
  (* Problem of  Interest on a loan *)
  (* Computes: the  Balloon Payment total interest *)
  VAR
  Amount,  Duration, Payment, Interest,
  Balance, Time,  IntSum: INTEGER;
  Rate: REAL;
  PROCEDURE main();
  BEGIN
  (* Input  necessary information *)
  Write("Enter  amount of loan: ");
  Read(Amount);
  Write("Enter  payment amount: ");
  Read(Payment);
  Write("Enter the  duration in months: ");
  Read(Duration);
  WriteLn("Enter  annual interest rate ");
  Write("as a  decimal percent: ");
  Read(Rate);
  Rate :=  Rate/1200; (* Convert to monthly *)
  (* Compute the  Ballon Payment *)
  Balance :=  Amount;
  IntSum := 0;
  Time := 1;
  WHILE Time <  Duration DO BEGIN
  Interest :=  TRUNC(Balance * Rate);
  Balance :=  Balance + Interest;
  Balance :=  Balance - Payment;
  IntSum := IntSum  + Interest;
  Time := Time +  1;
  (* Begin trace  ************************)
  Write(Time);
  Write(" Balance  = ");
  WriteLn(Balance);
  (* End trace  **************************)
  END (* WHILE *)
  (* Output all  required Results *)
  Write("Balloon  Balance is: ");
  WriteLn(Balance);
  Write("Total  interest is : ");
  WriteLn(IntSum);
  END (* Loan *)
        """
        expect = r"Program([VarDecl(Id(Amount),IntType),VarDecl(Id(Duration),IntType),VarDecl(Id(Payment),IntType),VarDecl(Id(Interest),IntType),VarDecl(Id(Balance),IntType),VarDecl(Id(Time),IntType),VarDecl(Id(IntSum),IntType),VarDecl(Id(Rate),FloatType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Enter  amount of loan: )]),CallStmt(Id(Read),[Id(Amount)]),CallStmt(Id(Write),[StringLiteral(Enter  payment amount: )]),CallStmt(Id(Read),[Id(Payment)]),CallStmt(Id(Write),[StringLiteral(Enter the  duration in months: )]),CallStmt(Id(Read),[Id(Duration)]),CallStmt(Id(WriteLn),[StringLiteral(Enter  annual interest rate )]),CallStmt(Id(Write),[StringLiteral(as a  decimal percent: )]),CallStmt(Id(Read),[Id(Rate)]),AssignStmt(Id(Rate),BinaryOp(/,Id(Rate),IntLiteral(1200))),AssignStmt(Id(Balance),Id(Amount)),AssignStmt(Id(IntSum),IntLiteral(0)),AssignStmt(Id(Time),IntLiteral(1)),While(BinaryOp(<,Id(Time),Id(Duration)),[AssignStmt(Id(Interest),CallExpr(Id(TRUNC),[BinaryOp(*,Id(Balance),Id(Rate))])),AssignStmt(Id(Balance),BinaryOp(+,Id(Balance),Id(Interest))),AssignStmt(Id(Balance),BinaryOp(-,Id(Balance),Id(Payment))),AssignStmt(Id(IntSum),BinaryOp(+,Id(IntSum),Id(Interest))),AssignStmt(Id(Time),BinaryOp(+,Id(Time),IntLiteral(1))),CallStmt(Id(Write),[Id(Time)]),CallStmt(Id(Write),[StringLiteral( Balance  = )]),CallStmt(Id(WriteLn),[Id(Balance)])]),CallStmt(Id(Write),[StringLiteral(Balloon  Balance is: )]),CallStmt(Id(WriteLn),[Id(Balance)]),CallStmt(Id(Write),[StringLiteral(Total  interest is : )]),CallStmt(Id(WriteLn),[Id(IntSum)])])])"
        self.assertTrue(TestAST.test(input,expect,377))
        

    def test_complex_378(self):
        input = """
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
        expect = r"Program([VarDecl(Id(Pennies),IntType),VarDecl(Id(Tendered),FloatType),VarDecl(Id(Cost),FloatType),VarDecl(Id(Remainder),FloatType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Enter cost  of item: )]),CallStmt(Id(Read),[Id(Cost)]),CallStmt(Id(Write),[StringLiteral(Enter  amount tendered: )]),CallStmt(Id(Read),[Id(Tendered)]),AssignStmt(Id(Remainder),BinaryOp(-,Id(Tendered),Id(Cost))),AssignStmt(Id(Pennies),IntLiteral(0)),While(BinaryOp(>,Id(Remainder),IntLiteral(0)),[AssignStmt(Id(Remainder),BinaryOp(-,Id(Remainder),FloatLiteral(0.01))),AssignStmt(Id(Pennies),BinaryOp(+,Id(Pennies),IntLiteral(1)))]),CallStmt(Id(Write),[StringLiteral(Cost is:  )]),CallStmt(Id(Write),[Id(Cost)]),CallStmt(Id(Write),[StringLiteral( Amount  tendered is: )]),CallStmt(Id(Write),[Id(Tendered)]),CallStmt(Id(Write),[StringLiteral( Change  is: )]),CallStmt(Id(WriteLn),[Id(Pennies)])])])"
        self.assertTrue(TestAST.test(input,expect,378))
        

    def test_complex_379(self):
        input = """
  { An Extended  Payroll program
  }
  { Selection  nested in Else branch of outer
  Selection }

  VAR Hours, Pay: INTEGER;
  PROCEDURE main();
  BEGIN
  RegularRate := 10;
  ExtraRate := 15;
  DoubleRate := 20;
  BaseHours := 40;
  ExtraHours := 20;
  DoubleTimeStart  := BaseHours + ExtraHours;
  BasePay :=  RegularRate * BaseHours;
  ExtraPay :=  ExtraRate * ExtraHours;
  Write("Enter  hours");
  Read(Hours);
  WriteLn();
  IF Hours >  DoubleTimeStart THEN
  Pay := BasePay +  ExtraPay +
  DoubleRate *  (Hours -
  DoubleTimeStart);
  ELSE
  IF Hours <=  BaseHours THEN
  Pay :=  RegularRate * Hours;
  ELSE
  Pay := BasePay +
  ExtraRate *  (Hours -
  BaseHours);
  Write("The gross  pay is ");
  Write(Pay);
  WriteLn();
  END {  ExtendedPay }
        """
        expect = r"Program([VarDecl(Id(Hours),IntType),VarDecl(Id(Pay),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(RegularRate),IntLiteral(10)),AssignStmt(Id(ExtraRate),IntLiteral(15)),AssignStmt(Id(DoubleRate),IntLiteral(20)),AssignStmt(Id(BaseHours),IntLiteral(40)),AssignStmt(Id(ExtraHours),IntLiteral(20)),AssignStmt(Id(DoubleTimeStart),BinaryOp(+,Id(BaseHours),Id(ExtraHours))),AssignStmt(Id(BasePay),BinaryOp(*,Id(RegularRate),Id(BaseHours))),AssignStmt(Id(ExtraPay),BinaryOp(*,Id(ExtraRate),Id(ExtraHours))),CallStmt(Id(Write),[StringLiteral(Enter  hours)]),CallStmt(Id(Read),[Id(Hours)]),CallStmt(Id(WriteLn),[]),If(BinaryOp(>,Id(Hours),Id(DoubleTimeStart)),[AssignStmt(Id(Pay),BinaryOp(+,BinaryOp(+,Id(BasePay),Id(ExtraPay)),BinaryOp(*,Id(DoubleRate),BinaryOp(-,Id(Hours),Id(DoubleTimeStart)))))],[If(BinaryOp(<=,Id(Hours),Id(BaseHours)),[AssignStmt(Id(Pay),BinaryOp(*,Id(RegularRate),Id(Hours)))],[AssignStmt(Id(Pay),BinaryOp(+,Id(BasePay),BinaryOp(*,Id(ExtraRate),BinaryOp(-,Id(Hours),Id(BaseHours)))))])]),CallStmt(Id(Write),[StringLiteral(The gross  pay is )]),CallStmt(Id(Write),[Id(Pay)]),CallStmt(Id(WriteLn),[])])])"
        self.assertTrue(TestAST.test(input,expect,379))
        

    def test_complex_380(self):
        input = """
  { An Extended  Payroll program }
  { Decision  nested in Else branch of outer Decision }
  { Normal  indentation }
  VAR Hours, Pay: INTEGER;
  PROCEDURE main();
  BEGIN
  RegularRate := 10;
  ExtraIncrease :=  5;
  DoubleIncrease :=  5;
  BaseHours := 40;
  ExtraHours := 20;
  HoursInWeek := 7 * 24;
  DoubleTimeStart  := BaseHours + ExtraHours;
  Write("Enter  hours: ");
  Read(Hours);
  WriteLn();
  IF Hours >= 0  THEN { regular pay}
  Pay :=  RegularRate * Hours;
  IF Hours >  BaseHours THEN { add extra pay }
  Pay := Pay +  ExtraIncrease * (Hours - BaseHours);
  IF Hours >  DoubleTimeStart THEN { add double pay }
  Pay := Pay +  DoubleIncrease *
  (Hours - DoubleTimeStart);
  IF (Hours <  0) OR (Hours > HoursInWeek) THEN
  Pay := 0;
  WriteLn("The  gross pay is ", Pay);
  END {  NewExtendedPay }

        """
        expect = r"Program([VarDecl(Id(Hours),IntType),VarDecl(Id(Pay),IntType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(RegularRate),IntLiteral(10)),AssignStmt(Id(ExtraIncrease),IntLiteral(5)),AssignStmt(Id(DoubleIncrease),IntLiteral(5)),AssignStmt(Id(BaseHours),IntLiteral(40)),AssignStmt(Id(ExtraHours),IntLiteral(20)),AssignStmt(Id(HoursInWeek),BinaryOp(*,IntLiteral(7),IntLiteral(24))),AssignStmt(Id(DoubleTimeStart),BinaryOp(+,Id(BaseHours),Id(ExtraHours))),CallStmt(Id(Write),[StringLiteral(Enter  hours: )]),CallStmt(Id(Read),[Id(Hours)]),CallStmt(Id(WriteLn),[]),If(BinaryOp(>=,Id(Hours),IntLiteral(0)),[AssignStmt(Id(Pay),BinaryOp(*,Id(RegularRate),Id(Hours)))],[]),If(BinaryOp(>,Id(Hours),Id(BaseHours)),[AssignStmt(Id(Pay),BinaryOp(+,Id(Pay),BinaryOp(*,Id(ExtraIncrease),BinaryOp(-,Id(Hours),Id(BaseHours)))))],[]),If(BinaryOp(>,Id(Hours),Id(DoubleTimeStart)),[AssignStmt(Id(Pay),BinaryOp(+,Id(Pay),BinaryOp(*,Id(DoubleIncrease),BinaryOp(-,Id(Hours),Id(DoubleTimeStart)))))],[]),If(BinaryOp(OR,BinaryOp(<,Id(Hours),IntLiteral(0)),BinaryOp(>,Id(Hours),Id(HoursInWeek))),[AssignStmt(Id(Pay),IntLiteral(0))],[]),CallStmt(Id(WriteLn),[StringLiteral(The  gross pay is ),Id(Pay)])])])"
        self.assertTrue(TestAST.test(input,expect,380))
        

    def test_random_381(self):
        input = """
procedure main();
begin
    writeln("71a1c003a2b855d85582c8f6c7648c49d3fe836408a7e1b5d9b222448acb3c1b");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(71a1c003a2b855d85582c8f6c7648c49d3fe836408a7e1b5d9b222448acb3c1b)])])])"
        self.assertTrue(TestAST.test(input, expect, 381))


    def test_random_382(self):
        input = """
procedure main();
begin
    writeln("27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd)])])])"
        self.assertTrue(TestAST.test(input, expect, 382))


    def test_random_383(self):
        input = """
procedure main();
begin
    writeln("e0850a775c17a87060c0cf6efad1020e0cbef5a44ba942bef6add5776598de53");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(e0850a775c17a87060c0cf6efad1020e0cbef5a44ba942bef6add5776598de53)])])])"
        self.assertTrue(TestAST.test(input, expect, 383))


    def test_random_384(self):
        input = """
procedure main();
begin
    writeln("1e68ed4e3d58a51096a7feea3947f40debf1fd9246ec977eb62ab93c81823ad9");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(1e68ed4e3d58a51096a7feea3947f40debf1fd9246ec977eb62ab93c81823ad9)])])])"
        self.assertTrue(TestAST.test(input, expect, 384))


    def test_random_385(self):
        input = """
procedure main();
begin
    writeln("a0d177b4967a6d99f4ff117defe1c0d23d4e78ca4630febcb948ee9e4520eff3");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(a0d177b4967a6d99f4ff117defe1c0d23d4e78ca4630febcb948ee9e4520eff3)])])])"
        self.assertTrue(TestAST.test(input, expect, 385))


    def test_random_386(self):
        input = """
procedure main();
begin
    writeln("00338ce57bbc14b33bd6695bc8eb32cdf2fb5f3a7d89ec14a43825e15d39df60");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(00338ce57bbc14b33bd6695bc8eb32cdf2fb5f3a7d89ec14a43825e15d39df60)])])])"
        self.assertTrue(TestAST.test(input, expect, 386))


    def test_random_387(self):
        input = """
procedure main();
begin
    writeln("d7cdaa5ca0582076c8e772cce739e32c5077cfd24f2ea33f04bb754594989a56");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(d7cdaa5ca0582076c8e772cce739e32c5077cfd24f2ea33f04bb754594989a56)])])])"
        self.assertTrue(TestAST.test(input, expect, 387))


    def test_random_388(self):
        input = """
procedure main();
begin
    writeln("23c657f2efda7731a3c1990b25f318fa2eb1332208f97ab9cc2a7eac70ab5a76");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(23c657f2efda7731a3c1990b25f318fa2eb1332208f97ab9cc2a7eac70ab5a76)])])])"
        self.assertTrue(TestAST.test(input, expect, 388))


    def test_random_389(self):
        input = """
procedure main();
begin
    writeln("af180e4359fc6179dc953abdcbdcaf7c146b53e1bee2b335e50dead11ccefa07");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(af180e4359fc6179dc953abdcbdcaf7c146b53e1bee2b335e50dead11ccefa07)])])])"
        self.assertTrue(TestAST.test(input, expect, 389))


    def test_random_390(self):
        input = """
procedure main();
begin
    writeln("09895de0407bcb0386733daa14bdb5dfa544505530c634334a05a60f161b71fc");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(09895de0407bcb0386733daa14bdb5dfa544505530c634334a05a60f161b71fc)])])])"
        self.assertTrue(TestAST.test(input, expect, 390))


    def test_random_391(self):
        input = """
procedure main();
begin
    writeln("33512007840ced1bb0aab68f47cb5f702abd494a15f26bcbe26a1e47af03d841");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(33512007840ced1bb0aab68f47cb5f702abd494a15f26bcbe26a1e47af03d841)])])])"
        self.assertTrue(TestAST.test(input, expect, 391))


    def test_random_392(self):
        input = """
procedure main();
begin
    writeln("6db6eb4af1e18ab81d3878e44672185d60ca8c988c9e2f7783de220735534c33");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(6db6eb4af1e18ab81d3878e44672185d60ca8c988c9e2f7783de220735534c33)])])])"
        self.assertTrue(TestAST.test(input, expect, 392))


    def test_random_393(self):
        input = """
procedure main();
begin
    writeln("7cb676d57114874e00c536916e6dcad2a5d3cb8c9a5abc06335df359cd9a6ef9");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(7cb676d57114874e00c536916e6dcad2a5d3cb8c9a5abc06335df359cd9a6ef9)])])])"
        self.assertTrue(TestAST.test(input, expect, 393))


    def test_random_394(self):
        input = """
procedure main();
begin
    writeln("2cfc8ccbd7c0b17615323b41e815651ff2ae9ffae45a4599c0499b98ff940439");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(2cfc8ccbd7c0b17615323b41e815651ff2ae9ffae45a4599c0499b98ff940439)])])])"
        self.assertTrue(TestAST.test(input, expect, 394))


    def test_random_395(self):
        input = """
procedure main();
begin
    writeln("9cfd3c755be26b4e1645918e2a64a26e3d851ede421e0b257f783b443bc443d1");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(9cfd3c755be26b4e1645918e2a64a26e3d851ede421e0b257f783b443bc443d1)])])])"
        self.assertTrue(TestAST.test(input, expect, 395))


    def test_random_396(self):
        input = """
procedure main();
begin
    writeln("a0f8b2c4cb1ac82abdb37f0fe5203b97be556c4468c83bba18684d620fd8eaf9");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(a0f8b2c4cb1ac82abdb37f0fe5203b97be556c4468c83bba18684d620fd8eaf9)])])])"
        self.assertTrue(TestAST.test(input, expect, 396))


    def test_random_397(self):
        input = """
procedure main();
begin
    writeln("4c15f47afe7f817fd559e12ddbc276f4930c5822f2049088d6f6605bec7cea56");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(4c15f47afe7f817fd559e12ddbc276f4930c5822f2049088d6f6605bec7cea56)])])])"
        self.assertTrue(TestAST.test(input, expect, 397))


    def test_random_398(self):
        input = """
procedure main();
begin
    writeln("76ebdb6d45c61ca12e622118cc90939ade672adf7890aa2b246405d4884dd75a");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(76ebdb6d45c61ca12e622118cc90939ade672adf7890aa2b246405d4884dd75a)])])])"
        self.assertTrue(TestAST.test(input, expect, 398))


    def test_random_399(self):
        input = """
procedure main();
begin
    writeln("308831041ea4863c3f87d222c31f759411898c874a9006b4bd6c745858b8f3bd");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(308831041ea4863c3f87d222c31f759411898c874a9006b4bd6c745858b8f3bd)])])])"
        self.assertTrue(TestAST.test(input, expect, 399))


    def test_random_400(self):
        input = """
procedure main();
begin
    writeln("983bd614bb5afece5ab3b6023f71147cd7b6bc2314f9d27af7422541c6558389");
end
"""
        expect = r"Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(writeln),[StringLiteral(983bd614bb5afece5ab3b6023f71147cd7b6bc2314f9d27af7422541c6558389)])])])"
        self.assertTrue(TestAST.test(input, expect, 400))

