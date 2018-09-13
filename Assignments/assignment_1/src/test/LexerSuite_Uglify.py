import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_49a6bba6f1e0c173fb9cad1e3855c9(self):
        """ Test ... """
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
            r"function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and,then,or,else,and,then,or,else,div,mod,not,and,or,<EOF>",
            101
        ))
        

    def test_c553d49d933ead4e71a79b92773316(self):
        """ Test ... """
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
        

    def test_b4dba1517d6c4f0143608bede5f2fb(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
+ - * / := <= >= <> = < >
( ) [ ] ; , : , ..
""",

            "+,-,*,/,:=,<=,>=,<>,=,<,>,(,),[,],;,,,:,,,..,<EOF>",
            103
        ))
        

    def test_7dea43c6c0b227003292919cc734be(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// This is a line comment
""",

            "<EOF>",
            104
        ))
        

    def test_b9db27504a9e420d1496f06fbdee65(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
(* Comment with multiple lines
    Hello comments
*)
""",

            "<EOF>",
            105
        ))
        

    def test_ea172537796ea8cb0b7becf390c567(self):
        """ Test ... """
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
        

    def test_461f8b5da3700a7ff22f4c76f6091f(self):
        """ Test ... """
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
        

    def test_bc679ad5078e83f28f919abf7ec878(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            108
        ))
        

    def test_8d6721602cf24db31081463d7cdfe9(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            109
        ))
        

    def test_1d764260bc0090324e2f6a530e1713(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
""      "A"     
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            110
        ))
        

    def test_e77df159d160929155992e00e3845e(self):
        """ Test ... """
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
        

    def test_bc2395beaee02745fcf191e2c21a41(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
123abc 123_abc 00000123_123abc
""",

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            112
        ))
        

    def test_37c654ef25cd342d2dba31f0057fae(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// inline comment but
    is multiple lines
( block comment missing *
{ comment without close
(* comment not correct close )
""",

            "is,multiple,lines,(,block,comment,missing,*,Error Token {",
            113
        ))
        

    def test_527c1ebb86e3bf802050ed3e612974(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
e-12 e12 . 1e 12e 12.05e .05e ee e01
""",

            "e,-,12,e12,Error Token .",
            114
        ))
        

    def test_3230057206b6fcae766b44c4d1df4a(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
array [1 .. 3] of integer
""",

            "array,[,1,..,3,],of,integer,<EOF>",
            115
        ))
        

    def test_d48dc96c19f58ec8a449ec0055cf03(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))
        

    def test_6b0f20776c6d30afa47828939e521f(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" abcxyz
""",

            r"""Unclosed String:  abcxyz
""",
            117
        ))
        

    def test_613d13c1924eb65ea8034ef248c504(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))
        

    def test_527bf1519dcefd20822b831595a42d(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" hello lexer \t "     asdf 
""",

            r' hello lexer \t ,asdf,<EOF>',
            119
        ))
        

    def test_1767e450bb89d2ad52af6a45518752(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Backspace  \b"
""",

            r'Backspace  \b,<EOF>',
            120
        ))
        

    def test_32f79fbb0aac0ac7a7d1bf715deeba(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Formfeed   \f"
""",

            r'Formfeed   \f,<EOF>',
            121
        ))
        

    def test_41005177ada9555838cde1fcac23f4(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Return     \r"
""",

            r'''Return     \r,<EOF>''',
            122
        ))
        

    def test_6b134dc48e0f63b5b13ab9bf5fafd1(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            123
        ))
        

    def test_da139ef4f3f969acf236907809fad3(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Newline
    multiple lines
"           """,

            r'''Unclosed String: Newline
''',
            124
        ))
        

    def test_3ea2f970c7e5b2326fd7a8847d178c(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            125
        ))
        

    def test_0a124dae7214a711f30595d629a800(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            126
        ))
        

    def test_897910ae1d00a840bfa357cc2384e0(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
Illegal: "\a"
""",

            r'''Illegal,:,Illegal Escape In String: \a''',
            127
        ))
        

    def test_78789cf0b3d0e391d981431ba53cbe(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))
        

    def test_92a7c87a7983f239fdf0a1c2afcdc3(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))
        

    def test_9a29b34df71b9f709103d86ee3f96e(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))
        

    def test_3677618709e840b09c0620556f3228(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" abc ' xyz "
""",

            "Illegal Escape In String:  abc '",
            131
        ))
        

    def test_9293bb68e3657a12a3cf39539dcac4(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" abc \' xyz "
""",

            r" abc \' xyz ,<EOF>",
            132
        ))
        

    def test_cd3d71d7929936786e3362dbf22d7d(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
" abc \" xyz " ghi
""",

            r" abc \" xyz ,ghi,<EOF>",
            133
        ))
        

    def test_b0fd40c93ad7ba2df005d579f80da4(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))
        

    def test_42d8493155a5c5ceafaff35b454e70(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
!== != & ^ % $ # ... \
""",

            "Error Token !",
            135
        ))
        

    def test_19fbd05785c67ec0c64892e59779aa(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
if a != b then
""",

            "if,a,Error Token !",
            136
        ))
        

    def test_af12c14d100e441728cb7ca160102d(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
a := a & 1
""",

            "a,:=,a,Error Token &",
            137
        ))
        

    def test_28122acc7e4ae203a3ecee5f4bb6a7(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))
        

    def test_03f51bf8b3c7713100a6d090d86478(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
#define for 1
""",

            "Error Token #",
            139
        ))
        

    def test_403414d8b72cf5bb1459914e71d68e(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
1234 0000001234 0000043123
""",

            "1234,0000001234,0000043123,<EOF>",
            140
        ))
        

    def test_3a1d1d16915a4d99fbcddcbbe60395(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))
        

    def test_9f269a8587fa9b65ee10b1e1ce3ece(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))
        

    def test_a79241d66bde35be9e7128d9af5e43(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))
        

    def test_d7df5589344b504e5b90d815fa1f30(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            144
        ))
        

    def test_f349013e5803c638801a333373c3b8(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            145
        ))
        

    def test_107831a65cf7df72195c5717e391d3(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            146
        ))
        

    def test_278a55d3bcfc3d719eea0fe06d822c(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\"
""",

            r"""Unclosed String: \"
""",
            147
        ))
        

    def test_baf9a6d2ec1a654a1bd5b8cb8f2dda(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\""
""",

            r"""\",<EOF>""",
            148
        ))
        

    def test_d29dce00b2e0d7209765bd840e5b4c(self):
        """ Test ... """
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
        

    def test_cf44cb23ccb4ff5837f1beb4140be0(self):
        """ Test ... """
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
        

    def test_a672e3851f51fe92a7dc507ef5fb2d(self):
        """ Test ... """
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
        

    def test_0b52555fca9ad7731252ffe7f70c35(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc""",

            r"s,=,Unclosed String: abc",
            152
        ))
        

    def test_1dbf836f49fd388786aaef56955425(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc                   ;
a = "xyz"
""",

            r"""s,=,Unclosed String: abc                   ;
""",
            153
        ))
        

    def test_36ca319e7609ce8b217d573ab8d160(self):
        """ Test ... """
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
        

    def test_702ce91ba98fbdf0c8a7ad55c803ad(self):
        """ Test ... """
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
        

    def test_56262386013f5a7bd668e351f42d55(self):
        """ Test ... """
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
        

    def test_d0a78ea8dac294ffd4a8d4f689710b(self):
        """ Test ... """
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
        

    def test_34d5ae2e890484deed0f973fe78462(self):
        """ Test ... """
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
        

    def test_8d5f439a5d7f6ecc8e0d39dd9cc969(self):
        """ Test ... """
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
        

    def test_824f7de04f5c38932d29911416f411(self):
        """ Test ... """
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
        

    def test_75321f87b8a45b3d14f6752218a3b7(self):
        """ Test ... """
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
        

    def test_38b3c0971c8603b2937f0d8b930ab4(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
/*123*/
""",

            "/,*,123,*,/,<EOF>",
            162
        ))
        

    def test_8ffc160277a2a96638e8b4b65fe7ab(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
\\ // / \
""",

            "Error Token \\",
            163
        ))
        

    def test_309a186bfe08dd395983b7352fd633(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
@1
""",

            r"Error Token @",
            164
        ))
        

    def test_5ff12e78c9c77bda08f5e0287b5601(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"@1"
""",

            "@1,<EOF>",
            165
        ))
        

    def test_b4ac58c6400768a840078908ae9927(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\"\"\" \' \' "
""",

            r"\"\"\" \' \' ,<EOF>",
            166
        ))
        

    def test_a9badd3ae391a22f275d6b869c7f29(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
%%%%%%
""",

            r"Error Token %",
            167
        ))
        

    def test_951354b5debc465c010d2507d0959b(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\t\t\t\t\t\t\t\t"
""",

            r"\t\t\t\t\t\t\t\t,<EOF>",
            168
        ))
        

    def test_82bdf7fc5c8811c418be7669e76c20(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
"\n\n\n\n\n\n\n\n\n"
""",

            r"\n\n\n\n\n\n\n\n\n,<EOF>",
            169
        ))
        

    def test_d247113fef6d1646385d9591c84b77(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
\r\r\r\r\r\r\r\r\r\
""",

            """Error Token \\""",
            170
        ))
        

    def test_4e06e7209f2174fddfda086441ce3c(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
\.\x\\
""",

            """Error Token \\""",
            171
        ))


    def test_7ee59003d6534ad716b9d03a07e706(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// [,<>,( k6301 with begin,],true
+ - integer N0699 + > then L09e7 >= real > >= , ] <> * eb142 > integer / while boolean procedure false
(* false procedure Z2262,do,G9a7c end e46e2,+,break*)
""",

            r"+,-,integer,N0699,+,>,then,L09e7,>=,real,>,>=,,,],<>,*,eb142,>,integer,/,while,boolean,procedure,false,<EOF>",
            172
        ))


    def test_2e271d9a962b5c896725dcc29e8dbb(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// :=,+,> Wcb78 ; false,else,>=
and real ] p5c22 ) array break w1ca2 array mod while , var div to + D989c := - function downto <= + ,
(* for false hb039,string,N6d32 not ua0fa,while,var*)
""",

            r"and,real,],p5c22,),array,break,w1ca2,array,mod,while,,,var,div,to,+,D989c,:=,-,function,downto,<=,+,,,<EOF>",
            173
        ))


    def test_e2bcac64b054fdd448df08a595d0bf(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// (,true,[ acb40 mod for,),with
= boolean .. p104c ] function do z71ae of < begin if break with of procedure b4169 break - of = = function div
(* <= : a41aa,while,m8bcd .. E8869,,,string*)
""",

            r"=,boolean,..,p104c,],function,do,z71ae,of,<,begin,if,break,with,of,procedure,b4169,break,-,of,=,=,function,div,<EOF>",
            174
        ))


    def test_6ba33a916d87390916e7a65da7f750(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// or,(,procedure d7bab true and,,,>=
do >= div nae0b ) else := W12e2 ( for / > if false <= <= pdb8e := + := <> .. to /
(* div > b8286,function,u0f83 .. Iaffa,,,**)
""",

            r"do,>=,div,nae0b,),else,:=,W12e2,(,for,/,>,if,false,<=,<=,pdb8e,:=,+,:=,<>,..,to,/,<EOF>",
            175
        ))


    def test_8702ca9870bd6d3c69fc97d79aa736(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// string,array,break Vbb79 break <>,(,<>
: .. do n1afd then - of Be562 ] end * > .. string * + W0977 var function else or mod if not
(* boolean real M89a9,do,yc501 , x38af,(,/*)
""",

            r":,..,do,n1afd,then,-,of,Be562,],end,*,>,..,string,*,+,W0977,var,function,else,or,mod,if,not,<EOF>",
            176
        ))


    def test_dfbcfd7af59a3a6bf11985be3fa057(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// /,<=,>= af9f4 , ,,and,mod
- [ string O902e boolean , and y680b string + > , else <> else = a5cbe := return end var boolean [ +
(* <= string Z1f1f,return,s847c with Xa8a2,continue,integer*)
""",

            r"-,[,string,O902e,boolean,,,and,y680b,string,+,>,,,else,<>,else,=,a5cbe,:=,return,end,var,boolean,[,+,<EOF>",
            177
        ))


    def test_4462c21284b2ebbd13e0e76cc88b34(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// and,:=,false C34d9 = else,<,..
do var [ oa6ec - - .. vc463 var <= , var end ) - [ nedb5 var * - <= * * then
(* / >= Q0dab,mod,qc5bc [ l4ebc,or,string*)
""",

            r"do,var,[,oa6ec,-,-,..,vc463,var,<=,,,var,end,),-,[,nedb5,var,*,-,<=,*,*,then,<EOF>",
            178
        ))


    def test_469abb4bea0ba4b3ab546873185ba4(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// ),-,return Rb4ac true >=,,,not
procedure , with Wd12f boolean >= [ b308a array ) ) or * for , >= n5d7e , , or <= , + <
(* := to Dd5f9,<>,l8df4 - ha663,>=,[*)
""",

            r"procedure,,,with,Wd12f,boolean,>=,[,b308a,array,),),or,*,for,,,>=,n5d7e,,,,,or,<=,,,+,<,<EOF>",
            179
        ))


    def test_9a60a91e62611b3cfeff9bf5799aa0(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// >=,<=,for of8ae * :=,then,>=
- + false P4366 ; * , l84bc , > : array procedure [ / while Va93a boolean and integer function - , false
(* function , Wbffd,),y6349 else w7e53,(,)*)
""",

            r"-,+,false,P4366,;,*,,,l84bc,,,>,:,array,procedure,[,/,while,Va93a,boolean,and,integer,function,-,,,false,<EOF>",
            180
        ))


    def test_1777c3138a229184c43ac4a5f38e5f(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// or,,,>= Y3137 := :,/,then
: * do b3084 function .. array X35a7 real <= .. continue < function continue := Zc3a0 if else <> of then function and
(* begin not Eea5a,then,D1682 and S7555,=,continue*)
""",

            r":,*,do,b3084,function,..,array,X35a7,real,<=,..,continue,<,function,continue,:=,Zc3a0,if,else,<>,of,then,function,and,<EOF>",
            181
        ))


    def test_177e9cfb7958b69dbe3473b47a685a(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// downto,-,= kf07d string :,real,string
, return not C4462 <> function true n69bd mod with var then < and continue and M615c <= > [ - ; - string
(* real < u5368,:,Z36b0 string dcbf1,;,<>*)
""",

            r",,return,not,C4462,<>,function,true,n69bd,mod,with,var,then,<,and,continue,and,M615c,<=,>,[,-,;,-,string,<EOF>",
            182
        ))


    def test_e6ed0cf657b6b0830b51c1a9181fe5(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// and,<=,return v415f ( div,and,or
+ , or b328b = <= ) G39be : then else break / * = [ Qd057 ] var break * >= do >
(* end , b60f1,>=,dd28e , dd3ab,string,of*)
""",

            r"+,,,or,b328b,=,<=,),G39be,:,then,else,break,/,*,=,[,Qd057,],var,break,*,>=,do,>,<EOF>",
            183
        ))


    def test_b94615faaf77d02abf04b09a030a58(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// then,return,< e0352 : ,,of,>=
return > array Qbfb5 , function var M274c if <= ; function or <= to = x4045 procedure to <> ] ( else *
(* false of Bcdfa,<=,J490b begin J6626,<=,break*)
""",

            r"return,>,array,Qbfb5,,,function,var,M274c,if,<=,;,function,or,<=,to,=,x4045,procedure,to,<>,],(,else,*,<EOF>",
            184
        ))


    def test_9fa99d7cb7babd94fb01f6d34f3731(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// ],],* ae0bc not mod,return,,
function < + Qefbe and ; of o366c false array else < > and downto for J4981 : <> return = for then ..
(* of break h80bb,or,bfa18 ) W6bd3,real,<*)
""",

            r"function,<,+,Qefbe,and,;,of,o366c,false,array,else,<,>,and,downto,for,J4981,:,<>,return,=,for,then,..,<EOF>",
            185
        ))


    def test_6a36c0eb158b3b7e359b114120cf7d(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// <>,while,] jb8be true for,,,<=
else and * x68ae .. continue end c1976 to boolean := or function , * , Y0db2 and <= of else ) mod :
(* else for j5904,true,weadc , e6f92,..,;*)
""",

            r"else,and,*,x68ae,..,continue,end,c1976,to,boolean,:=,or,function,,,*,,,Y0db2,and,<=,of,else,),mod,:,<EOF>",
            186
        ))


    def test_0eb6580b301febdeecf306ff7a350e(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// :,..,<= fef8b / div,=,continue
return ) then lb1e7 true mod , Ve4b7 , := true do begin or >= >= v8b5e := for <> >= or ) [
(* continue ) p0698,*,Oc0d5 .. c9970,,,downto*)
""",

            r"return,),then,lb1e7,true,mod,,,Ve4b7,,,:=,true,do,begin,or,>=,>=,v8b5e,:=,for,<>,>=,or,),[,<EOF>",
            187
        ))


    def test_2010ecd19c6138b6a0af9c9551a0b8(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// <=,var,> B2bb9 else real,boolean,return
and false then edaa6 integer , break P278e if <> [ * / function while div d74f0 > not <> , ] begin /
(* ; continue Feecf,false,Hc361 <> mf34e,else,or*)
""",

            r"and,false,then,edaa6,integer,,,break,P278e,if,<>,[,*,/,function,while,div,d74f0,>,not,<>,,,],begin,/,<EOF>",
            188
        ))


    def test_5669012f246cddad2cd4b7305e0d9f(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// begin,),] lc648 ; not,(,/
, + var Cd03e else to do xd695 ( string of ; end : ] .. f5179 >= + + [ = ; <=
(* or := d3d6a,begin,I6a5a not Cf2e7,/,<=*)
""",

            r",,+,var,Cd03e,else,to,do,xd695,(,string,of,;,end,:,],..,f5179,>=,+,+,[,=,;,<=,<EOF>",
            189
        ))


    def test_91e1e3786d21302313d0e9946e58ed(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// (,while,: H050f end return,+,[
, / or M3ff3 while / for y848d while downto - + , ] ) >= Hdcb8 false / for > not and (
(* ( [ bc9ca,],B1ebd ; w28cd,procedure,if*)
""",

            r",,/,or,M3ff3,while,/,for,y848d,while,downto,-,+,,,],),>=,Hdcb8,false,/,for,>,not,and,(,<EOF>",
            190
        ))


    def test_e74e6aebb6d40f15f24f7511d914eb(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// var,+,, M6af4 , with,=,-
to >= ( Q51ca : ] to Ie94f for , integer ; , for return if Bbfd7 + real <> if do downto :
(* * ) e4686,end,rf588 > R8121,-,,*)
""",

            r"to,>=,(,Q51ca,:,],to,Ie94f,for,,,integer,;,,,for,return,if,Bbfd7,+,real,<>,if,do,downto,:,<EOF>",
            191
        ))


    def test_df14106034e79a2238a11d1cc65afd(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// <>,>,:= z77c3 ] else,with,or
begin real for s229b else ; continue lf8f5 not := <= end <= , mod continue Df28f * := - mod , of ;
(* , for zd0ec,end,T9167 = He16f,-,(*)
""",

            r"begin,real,for,s229b,else,;,continue,lf8f5,not,:=,<=,end,<=,,,mod,continue,Df28f,*,:=,-,mod,,,of,;,<EOF>",
            192
        ))


    def test_a112ba5d134ec3505996f1cf460f9d(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// real,),: E75c5 / if,and,array
<> : ; Oadae ( < >= R76a7 [ procedure procedure false while else .. + T3117 while * <> / if <> mod
(* ; do z8fe1,continue,F7d93 .. F69d9,,,<>*)
""",

            r"<>,:,;,Oadae,(,<,>=,R76a7,[,procedure,procedure,false,while,else,..,+,T3117,while,*,<>,/,if,<>,mod,<EOF>",
            193
        ))


    def test_4e1b5f7d197d7051dbd8a208b9c685(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// for,[,( t59e3 := function,real,while
( false end ebd2c / real <= n9afc begin <> for < to * if array Icd8e := ] ; + return = [
(* , - N3453,+,caa7a <> Zf62a,+,]*)
""",

            r"(,false,end,ebd2c,/,real,<=,n9afc,begin,<>,for,<,to,*,if,array,Icd8e,:=,],;,+,return,=,[,<EOF>",
            194
        ))


    def test_a58b5508a0b3da82bb93c2df56d682(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// break,+,] e8fe2 of ..,:=,if
:= boolean then M7be9 function end > k3932 / := .. >= to while true downto Wcaa7 = := begin else else ( return
(* ( function Nc1f8,*,T9f7a := Z1d53,<>,..*)
""",

            r":=,boolean,then,M7be9,function,end,>,k3932,/,:=,..,>=,to,while,true,downto,Wcaa7,=,:=,begin,else,else,(,return,<EOF>",
            195
        ))


    def test_2d9d3f1ef05b4622fc4f470bdab8e6(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// or,not,- Zbe2a ; <=,of,)
or * of fa09c ) ; < Ha69c <= mod real mod ) end else >= fa290 <> array end continue var not <
(* of <= g6834,then,k6652 ) h3b64,=,do*)
""",

            r"or,*,of,fa09c,),;,<,Ha69c,<=,mod,real,mod,),end,else,>=,fa290,<>,array,end,continue,var,not,<,<EOF>",
            196
        ))


    def test_c6ddd0af0bb887c53a602bc723fb37(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// div,:,/ R0b5a end <>,,,>
or array ] l2cb2 and >= - ie67b ] or break then string ] and [ Y4895 false , continue not real ) div
(* procedure div ya03a,*,Gdc83 / B4f31,,,>=*)
""",

            r"or,array,],l2cb2,and,>=,-,ie67b,],or,break,then,string,],and,[,Y4895,false,,,continue,not,real,),div,<EOF>",
            197
        ))


    def test_67e09dcf1f9e80fdb02c6c5670ce1e(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// or,*,; i8959 or *,<,downto
* break do wa59d : do .. xabf4 boolean = and > else ; do .. Xcc01 do + .. - break function or
(* or / pb4f1,<>,D7985 if Z564d,,,**)
""",

            r"*,break,do,wa59d,:,do,..,xabf4,boolean,=,and,>,else,;,do,..,Xcc01,do,+,..,-,break,function,or,<EOF>",
            198
        ))


    def test_e5c8fd2c0cf4c6d9e8a6dea381f1db(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// of,string,.. A7535 break >=,div,for
mod false then M46f3 = / , e934f + := boolean := < real + var d94de : ; with break or + =
(* procedure < w9efc,:,Y62a0 , wd3d0,/,<>*)
""",

            r"mod,false,then,M46f3,=,/,,,e934f,+,:=,boolean,:=,<,real,+,var,d94de,:,;,with,break,or,+,=,<EOF>",
            199
        ))


    def test_fff5127d8fec7c6f493ce4a0abed68(self):
        """ Test ... """
        self.assertTrue(TestLexer.test(
            r"""
// :=,while,var U1c82 and for,>,)
, string of wdb12 - false procedure C7cbd and * boolean >= .. / div and O328e := and return , ; , :=
(* procedure .. Pbe60,..,S9332 not F30d6,boolean,begin*)
""",

            r",,string,of,wdb12,-,false,procedure,C7cbd,and,*,boolean,>=,..,/,div,and,O328e,:=,and,return,,,;,,,:=,<EOF>",
            200
        ))

