import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """proceDure main() ;beGin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """proceDure main () ;BEGIN
            putIntLn(4);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss ) int main;( {}"""
        input = """proceDure main( beGin end"""
        expect = "Error on line 1 col 16: beGin"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_variable_declaration(self):
        input = """PROCEDURE main() ;
                    var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
                    BEGIN
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_function_declaration(self):
        input = """FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_procedure_declaration(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_assign_statement1(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := 1;
                    b := a[12] ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_assign_statement2(self):
        input = """proCeduRe foo() ;
                  var x,y: real ;
                  BEGIN
                    a := "conga";
                    b := func(1,a+1) ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_assign_statement3(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    1 := 1;
                    c := a[12] ;
                   END"""
        expect = "Error on line 4 col 22: :="
        self.assertTrue(TestParser.test(input,expect,209))
    def test_assign_statement4(self):
        input = """function foo(c: real): real ;
                   var x,y: array[m .. n] of real;
                   BEGIN
                    a[m+n] := a[m+1] ;
                    foo()[m*1] := a[a div 3] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_assign_statement5(self):
        input = """function foo(c: real): real ;
                   var x: integer ;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_assign_statement6(self):
        input = """function foo(c: real): real ; x:=a[1]"""
        expect = "Error on line 1 col 30: x"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_if_statement1(self):
        input = """function foo(c: real): real ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if a > b  c := d;
                    else d:= c;
                   END"""
        expect = "Error on line 5 col 35: c"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else foo();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_if_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_if_statement5(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_while_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_while_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_while_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_while_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                        if(a=1) then begin end
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_with_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_with_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_with_statement4(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; do
                        foo2(a,b,"anc");
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_for_statement1(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do s := s + 1;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_for_statement2(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) then s:=s-1;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_for_statement4(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_break_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_continue_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do continuE ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_return_statement1(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do reTuRn ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_return_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1) do reTuRn foo(a+1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_compound_statement(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1=1) do begin eND
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_call_statement1(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_call_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo1();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_call_statement4(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_call_statement5(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    textbackground(brown); {background colour}
                	ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    return func(a(1,2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_multi4(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_multi8(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 return ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_multi9(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_multi10(self):
        input = """
                procedure main() ;
                var a: array[0 .. m-1] of integer;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_multi11(self):
        input = """
                function sum_real_array(a: array[0 .. m-1] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. m-1] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_multi20(self):
        input = """
                Function KtraMangCapSoCong (A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                 for i:=1 to N do
                 if(A[i] <> A[i-1] + k) then
                  flag:=false;     // Cham dut, ket qua: khong phai
                 return flag; {Ket qua kiem tra la mang cap so cong}
                End
                """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,260))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_multi29(self):
        input = """
                Var a,b,c,s,p: real;
                pROCEDURE main() ;
                Begin
                if a then b := c;
                else if a then b:= c;
                else if a then b:= c;
                else if a b:=c;
                End
                """
        expect = "Error on line 8 col 26: b"
        self.assertTrue(TestParser.test(input,expect,269))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_multi31(self):
        input="""
              (
              var i: integer;
              )()
              """
        expect = "Error on line 2 col 14: ("
        self.assertTrue(TestParser.test(input,expect,271))
    def test_multi32(self):
        input= """
               var i: integer;
               )()
               """
        expect = "Error on line 3 col 15: )"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_multi33(self):
        input= """
                Procedure InSoLanXHcuaPTu( A:array[x+1 .. x+15] of REAL; N: Integer);
                Var i :Integer;
                Begin
                 For i:=0 to N do
                  Writeln( A[i],"  ===>  ", DemPtuX( A, N, A[i]));
                End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_multi34(self):
        input= """
                Procedure SxepDuongTangAmGiam ( A:array[1 .. 10] of integer; N:Integer );
                Var i ,j ,k:Integer;
                Begin
                 For i:=1 to N do
                  For j:=1 to N  do
                   If (((i<j)and (A[i] > A[j]) and (A[i]>0) and (A[j]>0)) or
                ((i<j) and ( 1[i][2]] < A[j] ) and ( A[i]<0) and ( A[j]<0))) then
                    Begin
                     k := A[i];      { Tien hanh hoan doi gia tri A[i], A[j]}
                     A[i] := A[j];             { thong qua bien tam k }
                     A[j] := k;
                    End
                End
                """
        expect = "Error on line 8 col 36: ]"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_multi35(self):
        input= """
                Procedure XoaPhanTu( A:array[1+m .. m+n] of sTRIng; N:Integer; k:sTRIng);
                Var i :Integer;
                Begin
                 For  i:=k to N-1 do
                  A[i] := A[i+1];
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_multi36(self):
        input= """
                pROCEDURE main();
                Var A:array[1 .. 100] of integer;
                 N,i,S:Integer;
                Begin
                {nhap mang}
                 
                  End
                {tinh tong}
                
                End
                """
        expect = "Error on line 11 col 16: End"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_multi37(self):
        input= """
                procedure UCLN_BCNN();
                Var a, b :integer; // Khai bao bien su dung
                Begin
                 Write("ab" ;
                End
                """
        expect = "Error on line 5 col 28: ;"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_multi38(self):
        input= """
                procedure MaxOfThreeNumber();
                var  a, b, c, max: real;
                begin
                 write("Nhap a = "); readln();
                 if a then b:= c;
                 if a then else begin end
                end
                """
        expect = "Error on line 7 col 27: else"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_multi39(self):
        input= """
                procedure ptb2() ;
                VAR a,b,c,x1,x2,d:REAL;
                BEGIN
                 for c=d downto e do begin end
                END
               """
        expect = "Error on line 5 col 22: ="
        self.assertTrue(TestParser.test(input,expect,279))
    def test_multi40(self):
        input= """
                procedure main();
                var i: integer;
                 S: integer;
                begin
                 with c,d do if ;
                end
               """
        expect = "Error on line 6 col 26: do"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_multi41(self):
        input= """
                procedure SquareRoot();
                 VAR Value, SqRoot:REAL;
                 Finished:String;
                BEGIN
                begin
                begin
                end
                END
               """
        expect = "Error on line 10 col 15: <EOF>"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_multi42(self):
        input= """
                Function LuyThua(a, k: Integer): integer;
                
               """
        expect = "Error on line 4 col 15: <EOF>"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_multi43(self):
        input= """
                Var
                So: I nteger;
                LT, STP: integer;
                CNP: String;
                
                """
        expect = "Error on line 3 col 20: I"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_multi44(self):
        input= """
            foo(3);
            """
        expect = "Error on line 2 col 12: foo"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_multi45(self):
        input= """
            var a : array [1 ... 5] of integer;
            """
        expect = "."
        self.assertTrue(TestParser.test(input,expect,285))
    def test_multi46(self):
         input= """
            procedure nested_ifelseChecking(k:integer);
            var
             { local variable definition }
             a, b : integer;
            begin
             a := a[[1]2]
            end"""
         expect = "Error on line 7 col 20: ["
         self.assertTrue(TestParser.test(input,expect,286))
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
         expect = "successful"
         self.assertTrue(TestParser.test(input,expect,287))
    def test_multi48(self):
         input= """
            procedure example_String();
            var
             str1, str2, str3 : string;
             str4: string;
             len: integer;
            begin
            if a then b:=c;
            else if a then b:= c;
                else if a then b:= c;
                    else if a then b;
            end
            """
         expect = "Error on line 11 col 36: ;"
         self.assertTrue(TestParser.test(input,expect,288))
    def test_multi49(self):
         input= """
            procedure swap(x, y: integer);
            var
             temp: integer;
            begin
             x := b and then c if a > b;
            end;
            """
         expect = "Error on line 6 col 31: if"
         self.assertTrue(TestParser.test(input,expect,289))
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
              Else If k mod 16 = 1 CTLP:="1"+CTLP;
              Else If k mod 16 = 2 then CTLP:="2"+CTLP;
              Else If k mod 16 = 3 then CTLP:="3"+CTLP;
             end
            end
            """
         expect = "Error on line 12 col 35: CTLP"
         self.assertTrue(TestParser.test(input,expect,290))
    def test_multi51(self):
         input= """
            procedurE foo (b : real) ;
            var
             a : array [2 .. 3] of integer;
             b: ;
             e: real;
             f: boolean;
            begin
             while(a=4) and (b=6+8-9-5 or 2) do
             e:=4;
            End
            """
         expect = "Error on line 5 col 16: ;"
         self.assertTrue(TestParser.test(input,expect,291))
    def test_multi52(self):
         input= """
            procedurE foo (b : real) ;
            var
            a : array [2 .. 3] of integer;
            b: string;
            e: real;
            f: boolean;
            begin
            while(a=4) and c=4) do
            for i:=4 downto 3+3 do
                for i:=5 to 9+9 do
                    if(a=3) and (a=True) then
                    e:=5;
            End
            """
         expect = "Error on line 9 col 30: )"
         self.assertTrue(TestParser.test(input,expect,292))
    def test_multi53(self):
         input= """
            procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4
            End
            """
            
         expect = "Error on line 8 col 12: End"
         self.assertTrue(TestParser.test(input,expect,293))
    
    def test_multi54(self):
         input= """
            procedurE foo (b : real) ;
            begin
             (1[2][3])[4] := 5;
            End
            """
            
         expect = "successful"
         self.assertTrue(TestParser.test(input,expect,294))

    def test_multi55(self):
         input= """
            procedurE foo (b : real) ;
            begin
             (1[2][3])[4] = 5;
            End
            """
            
         expect = "Error on line 4 col 26: ="
         self.assertTrue(TestParser.test(input,expect,295))
    def test_multi56(self):
         input= """
            procedurE foo b : real) ;
            begin
             (1[2][3])[4] = 5;
            End
            """
            
         expect = "Error on line 2 col 26: b"
         self.assertTrue(TestParser.test(input,expect,296))
    
    def test_multi57(self):
         input= """
            procedurE foo (b : float) ;
            begin
             (1[2][3])[4] = 5;
            End
            """
            
         expect = "Error on line 2 col 31: float"
         self.assertTrue(TestParser.test(input,expect,297))
    
    def test_multi58(self):
         input= """
            procedurE foo (b ; integer) ;
            begin
             (1[2][3])[4] = 5;
            End
            """
            
         expect = "Error on line 2 col 29: ;"
         self.assertTrue(TestParser.test(input,expect,298))

    def test_multi59(self):
         input= """
            procedurE foo (b : integer) ;
            begin
             (1[2][3])[4] := 5[1] := d +e := f;
            End
            """
            
         expect = "Error on line 4 col 42: :="
         self.assertTrue(TestParser.test(input,expect,299))

    def test_multi60(self):
         input= """
            procedurE foo (b : integer) ;
            begin
             for a : = b do begin end
            End
            """
            
         expect = "Error on line 4 col 19: :"
         self.assertTrue(TestParser.test(input,expect,300))