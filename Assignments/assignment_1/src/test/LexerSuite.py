import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        """ Test Valid Lowercase Keywords """
        self.assertTrue(TestLexer.test(
            r"""
function procedure
begin end
true false
if then else
for while with do to downto
return break continue
integer string real boolean
array
var of
and then
or else
and         then
or          else
div mod not and or
""",
            "function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and,then,or,else,and,then,or,else,div,mod,not,and,or,<EOF>",
            101
        ))
        

    def test_2(self):
        """ Test Valid Keywords """
        self.assertTrue(TestLexer.test(
            r"""
FuNctiOn prOceDure
Begin END
True FalSE
IF thEn ELSE
fOR While with DO To downTo
RETURN break COntiNue
integer string REAL BOOLean
ARRAY
VAR Of
anD Then
or eLse
AND             THeN   OR   elSE
dIV mOd NOT and OR
""",

            "FuNctiOn,prOceDure,Begin,END,True,FalSE,IF,thEn,ELSE,fOR,While,with,DO,To,downTo,RETURN,break,COntiNue,integer,string,REAL,BOOLean,ARRAY,VAR,Of,anD,Then,or,eLse,AND,THeN,OR,elSE,dIV,mOd,NOT,and,OR,<EOF>",
            102
        ))
        

    def test_3(self):
        """ Test Specific Characters """
        self.assertTrue(TestLexer.test(
            r"""
+ - * / := <= >= <> = < >
( ) { } [ ] ; , : , ..
""",

            "+,-,*,/,:=,<=,>=,<>,=,<,>,(,),[,],;,,,:,,,..,<EOF>",
            103
        ))
        

    def test_4(self):
        """ Test Inline Comments """
        self.assertTrue(TestLexer.test(
            r"""
// This is a line comment
""",

            "<EOF>",
            104
        ))
        

    def test_5(self):
        """ Test Block Comments 1 """
        self.assertTrue(TestLexer.test(
            r"""
(* Comment with multiple lines
    Hello comments
*)
""",

            "<EOF>",
            105
        ))
        

    def test_6(self):
        """ Test Block Comments 2 """
        self.assertTrue(TestLexer.test(
            r"""
{ This is a block comment }

{
    Comment multiple lines
}
""",

            "<EOF>",
            106
        ))
        

    def test_7(self):
        """ Test Mix Comments """
        self.assertTrue(TestLexer.test(
            r"""
(* This is a block comment *)

{ This is a block comment }

// This is a line comment

(* Comment with multiple lines
    Hello comments
*)

{
    Comment multiple lines
}

(* nest comments { 
block 
comment
    // inline comment
} 

// inline comment { block 

comment }
*)
""",

            "<EOF>",
            107
        ))
        

    def test_8(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.test(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            108
        ))
        

    def test_9(self):
        """ Test Real Literal """
        self.assertTrue(TestLexer.test(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            109
        ))
        

    def test_10(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.test(
            r"""
""      "A"     
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            110
        ))
        

    def test_11(self):
        """ Test Identifiers """
        self.assertTrue(TestLexer.test(
            r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc

h98f394__VWT_b5_VT_YGU87udhf__T_
""",

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>",
            111
        ))
        

    def test_12(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.test(
            r"""
123abc 123_abc 00000123_123abc
""",

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            112
        ))
        

    def test_13(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            r"""
// inline comment but
    is multiple lines
( block comment missing *
{ comment without close
(* comment not correct close )
""",

            "is,multiple,lines,(,block,comment,missing,*,{,comment,without,close,(,*,comment,not,correct,close,),<EOF>",
            113
        ))
        

    def test_14(self):
        """ Test Invalid Real Literal """
        self.assertTrue(TestLexer.test(
            r"""
e-12 e12 . 1e 12e 12.05e .05e ee e01
""",

            "e,-,12,e12,.,1,e,12,e,12.05,e,.05,e,ee,e01,<EOF>",
            114
        ))
        

    def test_15(self):
        """ Test Array Declare """
        self.assertTrue(TestLexer.test(
            r"""
array [1 .. 3] of integer
""",

            "array,[,1,..,3,],of,integer,<EOF>",
            115
        ))
        

    def test_16(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            r"""  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))
        

    def test_17(self):
        """ Test Unclose String with endline """
        self.assertTrue(TestLexer.test(
            r"""
" abcxyz
""",

            r"""Unclosed String:  abcxyz
""",
            117
        ))
        

    def test_18(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))
        

    def test_19(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
" hello lexer \t "     asdf 
""",

            r' hello lexer \t ,asdf,<EOF>',
            119
        ))
        

    def test_20(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Backspace  \b"
""",

            r'Backspace  \b,<EOF>',
            120
        ))
        

    def test_21(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            r"""
"Formfeed   \f"
""",

            r'Formfeed   \f,<EOF>',
            121
        ))
        

    def test_22(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            r"""
"Return     \r"
""",

            r'''Return     \r,<EOF>''',
            122
        ))
        

    def test_23(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            123
        ))
        

    def test_24(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"Newline
    multiple lines
"           """,

            r'''Unclosed String: Newline
''',
            124
        ))
        

    def test_25(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            125
        ))
        

    def test_26(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            126
        ))
        

    def test_27(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
Illegal: "\a"
""",

            r'''Illegal,:,Illegal Escape In String: \a''',
            127
        ))
        

    def test_28(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))
        

    def test_29(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))
        

    def test_30(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))
        

    def test_31(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
" abc ' xyz "
""",

            "Illegal Escape In String:  abc '",
            131
        ))
        

    def test_32(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \' xyz "
""",

            r" abc \' xyz ,<EOF>",
            132
        ))
        

    def test_33(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \" xyz " ghi
""",

            r" abc \" xyz ,ghi,<EOF>",
            133
        ))
        

    def test_34(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))
        

    def test_35(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
!== != & ^ % $ # ... \
""",

            "Error Token !",
            135
        ))
        

    def test_36(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
if a != b then
""",

            "if,a,Error Token !",
            136
        ))
        

    def test_37(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
a := a & 1
""",

            "a,:=,a,Error Token &",
            137
        ))
        

    def test_38(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))
        

    def test_39(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
#define for 1
""",

            "Error Token #",
            139
        ))
        

    def test_40(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
1234 0000001234 0000043123
""",

            "1234,0000001234,0000043123,<EOF>",
            140
        ))
        

    def test_41(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))
        

    def test_42(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))
        

    def test_43(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))
        

    def test_44(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            144
        ))
        

    def test_45(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            145
        ))
        

    def test_46(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            146
        ))
        

    def test_47(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"\"
""",

            r"""Unclosed String: \"
""",
            147
        ))
        

    def test_48(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"\""
""",

            r"""\",<EOF>""",
            148
        ))
        

    def test_49(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
s = "string           
"a = 4
g = 9
""",

            r'''s,=,Unclosed String: string           
''',
            149
        ))
        

    def test_50(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
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

var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
""",

            r"var,a,,,b,,,c,:,real,;,var,x,,,y,,,z,:,Boolean,;,g,,,h,,,y,:,Integer,;,function,nty,(,),:,Real,;,var,x,,,y,,,z,:,Integer,;,begin,readLine,(,),;,fs,:=,readStdin,(,),;,with,i,:,integer,;,do,begin,for,i,:=,4,downto,-,5,do,h,:=,6,;,if,i,>,6,then,return,0,;,end,return,1,;,end,var,q,,,w,:,integer,;,var,a,:,string,;,begin,end,<EOF>",
            150
        ))
        

    def test_51(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    while i do begin
        ok()
    end
end
""",

            r"procedure,foo,(,),;,begin,while,i,do,begin,ok,(,),end,end,<EOF>",
            151
        ))
        

    def test_52(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc""",

            r"s,=,Unclosed String: abc",
            152
        ))
        

    def test_53(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc                   ;
a = "xyz"
""",

            r"""s,=,Unclosed String: abc                   ;
""",
            153
        ))
        

    def test_54(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
""",

            r"procedure,foo,(,),;,begin,while,1,<,2,<,3,<,4,<,5,do,ok,(,),;,end,<EOF>",
            154
        ))
        

    def test_55(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a: string do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,:,string,do,ok,(,),;,end,<EOF>",
            155
        ))
        

    def test_56(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,,,b,,,c,,,d,:,string,;,f,:,integer,do,ok,(,),;,end,<EOF>",
            156
        ))
        

    def test_57(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
""",

            r"procedure,foo,(,),;,var,a,:,real,;,begin,for,i,:=,1,to,10,do,begin,for,j,:=,i,downto,1,do,if,(,i,+,j,),mod,2,=,1,then,continue,break,;,end,end,<EOF>",
            157
        ))
        

    def test_58(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
""",

            r"procedure,foo,(,),;,begin,a,:=,a,[,d,<,y,(,5,>,3,),+,3,*,n,(,12,),],:=,5,[,3,],:=,3,[,2,],:=,b,;,end,<EOF>",
            158
        ))
        

    def test_59(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    s = "asdfghjklwertyuio  xcvbnm,dfghjkl;567"
    t = " dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    "
    y = "dfghjkl 
    
    
    ";
end
""",

            r"""procedure,foo,(,),;,begin,s,=,asdfghjklwertyuio  xcvbnm,dfghjkl;567,t,=, dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    ,y,=,Unclosed String: dfghjkl 
""",
            159
        ))
        

    def test_60(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    s = "asdfghjklwertyuio  xcvbnm,dfghjkl;567"
    t = " dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    "
    y = "dfghjkl 
    
    
    ";

    begin end
    ok();
    break;
end
""",

            r"""procedure,foo,(,),;,begin,s,=,asdfghjklwertyuio  xcvbnm,dfghjkl;567,t,=, dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    ,y,=,Unclosed String: dfghjkl 
""",
            160
        ))
        

    def test_61(self):
        """ Test Real Number """
        self.assertTrue(TestLexer.test(
            r"""
12.
12.e05
12.e-05
12.05e05
12.05e-05
12.05
.05
.05e05
.05e-05
""",

            r"12.,12.e05,12.e-05,12.05e05,12.05e-05,12.05,.05,.05e05,.05e-05,<EOF>",
            161
        ))
        

    def test_62(self):
        """ Test /* """
        self.assertTrue(TestLexer.test(
            r"""
/*123*/
""",

            "/,*,123,*,/,<EOF>",
            162
        ))
        

    def test_63(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
\\ // / \
""",

            "Error Token \\",
            163
        ))
        

    def test_64(self):
        """ Test Error Token @ """
        self.assertTrue(TestLexer.test(
            r"""
@1
""",

            r"Error Token @",
            164
        ))
        

    def test_65(self):
        """ Test String @ """
        self.assertTrue(TestLexer.test(
            r"""
"@1"
""",

            "@1,<EOF>",
            165
        ))
        

    def test_66(self):
        """ Test ' " """
        self.assertTrue(TestLexer.test(
            r"""
"\"\"\" \' \' "
""",

            r"\"\"\" \' \' ,<EOF>",
            166
        ))
        

    def test_67(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
%%%%%%
""",

            r"Error Token %",
            167
        ))
        

    def test_68(self):
        """ Test \t """
        self.assertTrue(TestLexer.test(
            r"""
"\t\t\t\t\t\t\t\t"
""",

            r"\t\t\t\t\t\t\t\t,<EOF>",
            168
        ))
        

    def test_69(self):
        """ Test \n  """
        self.assertTrue(TestLexer.test(
            r"""
"\n\n\n\n\n\n\n\n\n"
""",

            r"\n\n\n\n\n\n\n\n\n,<EOF>",
            169
        ))
        

    def test_70(self):
        """ Test \r """
        self.assertTrue(TestLexer.test(
            r"""
\r\r\r\r\r\r\r\r\r\
""",

            """Error Token \\""",
            170
        ))
        

    def test_71(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
\.\x\\
""",

            """Error Token \\""",
            171
        ))


    def test_72(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dd79d686b57();
begin
    e5d4ddedf07(g947c466502, p14411c769e) ;
end
""",

            r"procedure,dd79d686b57,(,),;,begin,e5d4ddedf07,(,g947c466502,,,p14411c769e,),;,end,<EOF>",
            172
        ))


    def test_73(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d0fa903bcb4();
begin
    e991c3640ba(gb2b9be4aa1, p89a20f5ad6) ;
end
""",

            r"procedure,d0fa903bcb4,(,),;,begin,e991c3640ba,(,gb2b9be4aa1,,,p89a20f5ad6,),;,end,<EOF>",
            173
        ))


    def test_74(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d46b7fff30e();
begin
    e1c53bd38aa(g9c735324ad, p908f0c5cb6) ;
end
""",

            r"procedure,d46b7fff30e,(,),;,begin,e1c53bd38aa,(,g9c735324ad,,,p908f0c5cb6,),;,end,<EOF>",
            174
        ))


    def test_75(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d52b770fcdf();
begin
    eb7867138ec(gd1b75502ba, pda5cd57603) ;
end
""",

            r"procedure,d52b770fcdf,(,),;,begin,eb7867138ec,(,gd1b75502ba,,,pda5cd57603,),;,end,<EOF>",
            175
        ))


    def test_76(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure da8b1b16c2c();
begin
    e278b29aa93(g6785cef97d, p62244d82be) ;
end
""",

            r"procedure,da8b1b16c2c,(,),;,begin,e278b29aa93,(,g6785cef97d,,,p62244d82be,),;,end,<EOF>",
            176
        ))


    def test_77(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d58ef7c6457();
begin
    e5e5568e279(g5d23768f28, p5a52abb670) ;
end
""",

            r"procedure,d58ef7c6457,(,),;,begin,e5e5568e279,(,g5d23768f28,,,p5a52abb670,),;,end,<EOF>",
            177
        ))


    def test_78(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d03a41c5ca7();
begin
    eb26715e160(g03f30d9ba8, p3be34416f3) ;
end
""",

            r"procedure,d03a41c5ca7,(,),;,begin,eb26715e160,(,g03f30d9ba8,,,p3be34416f3,),;,end,<EOF>",
            178
        ))


    def test_79(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d9080f974be();
begin
    ed57a1483a3(g43162561cb, p6c37a9e235) ;
end
""",

            r"procedure,d9080f974be,(,),;,begin,ed57a1483a3,(,g43162561cb,,,p6c37a9e235,),;,end,<EOF>",
            179
        ))


    def test_80(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d95b0e69014();
begin
    eb6e0cbc69a(g0239ba1dc3, p0f3a0cb2aa) ;
end
""",

            r"procedure,d95b0e69014,(,),;,begin,eb6e0cbc69a,(,g0239ba1dc3,,,p0f3a0cb2aa,),;,end,<EOF>",
            180
        ))


    def test_81(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dddb4475bf7();
begin
    ed23c93eb77(gf3d9b09267, pe616d5655e) ;
end
""",

            r"procedure,dddb4475bf7,(,),;,begin,ed23c93eb77,(,gf3d9b09267,,,pe616d5655e,),;,end,<EOF>",
            181
        ))


    def test_82(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d3acd34ba94();
begin
    ed3e27f33c3(g9aa0c9b7cd, pab82ffd8d0) ;
end
""",

            r"procedure,d3acd34ba94,(,),;,begin,ed3e27f33c3,(,g9aa0c9b7cd,,,pab82ffd8d0,),;,end,<EOF>",
            182
        ))


    def test_83(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d5054612cf4();
begin
    e16d6c8dd71(gce748b87ad, p8ad5d0b988) ;
end
""",

            r"procedure,d5054612cf4,(,),;,begin,e16d6c8dd71,(,gce748b87ad,,,p8ad5d0b988,),;,end,<EOF>",
            183
        ))


    def test_84(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure db35ec8e359();
begin
    e33ef6fbcb2(gfe428d8128, p1e22269f9a) ;
end
""",

            r"procedure,db35ec8e359,(,),;,begin,e33ef6fbcb2,(,gfe428d8128,,,p1e22269f9a,),;,end,<EOF>",
            184
        ))


    def test_85(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d7db18e8753();
begin
    ecac48726c1(g85aad62e0f, pbbd6379653) ;
end
""",

            r"procedure,d7db18e8753,(,),;,begin,ecac48726c1,(,g85aad62e0f,,,pbbd6379653,),;,end,<EOF>",
            185
        ))


    def test_86(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dd04cbf48f8();
begin
    e3cb000e415(g7ccfa21695, p1cfbd6241a) ;
end
""",

            r"procedure,dd04cbf48f8,(,),;,begin,e3cb000e415,(,g7ccfa21695,,,p1cfbd6241a,),;,end,<EOF>",
            186
        ))


    def test_87(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d32b51c796f();
begin
    e0250d6d93a(gf91147025c, pa776cb4023) ;
end
""",

            r"procedure,d32b51c796f,(,),;,begin,e0250d6d93a,(,gf91147025c,,,pa776cb4023,),;,end,<EOF>",
            187
        ))


    def test_88(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d7d33a68224();
begin
    ea9715713e6(g06c28fab02, pafcfccb2f9) ;
end
""",

            r"procedure,d7d33a68224,(,),;,begin,ea9715713e6,(,g06c28fab02,,,pafcfccb2f9,),;,end,<EOF>",
            188
        ))


    def test_89(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d56e5b5d4bd();
begin
    e8df4b44a1e(g06e9e66b73, p3485082f7c) ;
end
""",

            r"procedure,d56e5b5d4bd,(,),;,begin,e8df4b44a1e,(,g06e9e66b73,,,p3485082f7c,),;,end,<EOF>",
            189
        ))


    def test_90(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure ddc109a622f();
begin
    ef3e0dc249a(gc5bf4feeee, p01018b9ae9) ;
end
""",

            r"procedure,ddc109a622f,(,),;,begin,ef3e0dc249a,(,gc5bf4feeee,,,p01018b9ae9,),;,end,<EOF>",
            190
        ))


    def test_91(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure db06b7e2825();
begin
    eb1be80b3d9(g4321850693, p63370d46c5) ;
end
""",

            r"procedure,db06b7e2825,(,),;,begin,eb1be80b3d9,(,g4321850693,,,p63370d46c5,),;,end,<EOF>",
            191
        ))


    def test_92(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure da4adc7a26e();
begin
    eb2fa72f865(g03f31b764d, p80d73d3d11) ;
end
""",

            r"procedure,da4adc7a26e,(,),;,begin,eb2fa72f865,(,g03f31b764d,,,p80d73d3d11,),;,end,<EOF>",
            192
        ))


    def test_93(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure de3186afb25();
begin
    e5c4014bf20(g9b9d23d42f, p3ac00e0d5f) ;
end
""",

            r"procedure,de3186afb25,(,),;,begin,e5c4014bf20,(,g9b9d23d42f,,,p3ac00e0d5f,),;,end,<EOF>",
            193
        ))


    def test_94(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure db5e3f9b3ca();
begin
    edf34758819(g1d0be9c647, p02a2c5f99e) ;
end
""",

            r"procedure,db5e3f9b3ca,(,),;,begin,edf34758819,(,g1d0be9c647,,,p02a2c5f99e,),;,end,<EOF>",
            194
        ))


    def test_95(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dca31627248();
begin
    e60e17597de(g73c68e0336, p6d6ef9ba7b) ;
end
""",

            r"procedure,dca31627248,(,),;,begin,e60e17597de,(,g73c68e0336,,,p6d6ef9ba7b,),;,end,<EOF>",
            195
        ))


    def test_96(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dde0ef9b5e7();
begin
    eb8ea58f418(gb082d9668c, p7a82750781) ;
end
""",

            r"procedure,dde0ef9b5e7,(,),;,begin,eb8ea58f418,(,gb082d9668c,,,p7a82750781,),;,end,<EOF>",
            196
        ))


    def test_97(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d73cf0b42bf();
begin
    ee87cf9f79b(g53f2d4bf50, paad9d53dab) ;
end
""",

            r"procedure,d73cf0b42bf,(,),;,begin,ee87cf9f79b,(,g53f2d4bf50,,,paad9d53dab,),;,end,<EOF>",
            197
        ))


    def test_98(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure d25dceb3fc7();
begin
    eb44e630ebc(g8dfa032272, pd9524994e4) ;
end
""",

            r"procedure,d25dceb3fc7,(,),;,begin,eb44e630ebc,(,g8dfa032272,,,pd9524994e4,),;,end,<EOF>",
            198
        ))


    def test_99(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dbe1cb2ae09();
begin
    e182152bc38(g610bbf4d35, p85b6b95ffe) ;
end
""",

            r"procedure,dbe1cb2ae09,(,),;,begin,e182152bc38,(,g610bbf4d35,,,p85b6b95ffe,),;,end,<EOF>",
            199
        ))


    def test_100(self):
        """ Test Automatic Generated Code """
        self.assertTrue(TestLexer.test(
            r"""
procedure dc6889cff4d();
begin
    e6d8e4b3f36(g0c0f9998c4, p6e709c2933) ;
end
""",

            r"procedure,dc6889cff4d,(,),;,begin,e6d8e4b3f36,(,g0c0f9998c4,,,p6e709c2933,),;,end,<EOF>",
            200
        ))

