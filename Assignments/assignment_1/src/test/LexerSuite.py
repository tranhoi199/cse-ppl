import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):


    def test_valid_lowercase_keywords(self):
        self.assertTrue(TestLexer.test(
            """
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

            "function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and then,or else,div,mod,not,and,or,<EOF>",
            101
        ))



    def test_valid_keywords(self):
        self.assertTrue(TestLexer.test(
            """
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
dIV mOd NOT and OR
            """,

            "FuNctiOn,prOceDure,Begin,END,True,FalSE,IF,thEn,ELSE,fOR,While,with,DO,To,downTo,RETURN,break,COntiNue,integer,string,REAL,BOOLean,ARRAY,VAR,Of,anD Then,or eLse,dIV,mOd,NOT,and,OR,<EOF>",
            102
        ))



    def test_specific_characters(self):
        self.assertTrue(TestLexer.test(
            """
+ - * / := <= >= <> = < >
( ) { } [ ] ; , : , ..
            """,

            "+,-,*,/,:=,<=,>=,<>,=,<,>,(,),[,],;,,,:,,,..,<EOF>",
            103
        ))



    def test_comments(self):
        self.assertTrue(TestLexer.test(
            """
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
            104
        ))




    def test_integer_literal(self):
        self.assertTrue(TestLexer.test(
            """
0 1 2 3 4 123 123456789
            """,

            "0,1,2,3,4,123,123456789,<EOF>",
            105
        ))



    def test_real_literal(self):
        self.assertTrue(TestLexer.test(
            """
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            106
        ))



    def test_string_literal(self):
        self.assertTrue(TestLexer.test(
            """
""      "A"     
"Mulitiple Characters"
""",

            "",
            107
        ))





    def test_identifiers(self):
        self.assertTrue(TestLexer.test(
            """
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc

h98f394__VWT_b5_VT_YGU87udhf__T_
            """,

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>",
            108
        ))




    def test_invalid_identifier(self):
        self.assertTrue(TestLexer.test(
            """123abc 123_abc 00000123_123abc""",

            "123,abc,123,_abc,0,0,0,0,0,123,_123abc,<EOF>",
            109
        ))




    def test_invalid_comments(self):
        """Test Invalid Comment"""
        self.assertTrue(TestLexer.test(
            """
// inline comment but
    is multiple lines
( block comment missing *
{ comment without close
(* comment not correct close )
            """,

            "is,multiple,lines,(,block,comment,missing,*,{,comment,without,close,(,*,comment,not,correct,close,),<EOF>",
            110
        ))




    def test_invalid_real(self):
        self.assertTrue(TestLexer.test(
            """e-12 e12 . 1e 12e 12.05e .05e ee e01""",

            "e,-,12,e12,.,1,e,12,e,12.05,e,.05,e,ee,e01,<EOF>",
            111
        ))



    def test_array(self):
        self.assertTrue(TestLexer.test(
            "array [1 .. 3] of integer",

            "array,[,1,..,3,],of,integer,<EOF>",
            112
        ))



    def test_unclose_string_no_endline(self):
        self.assertTrue(TestLexer.test(
            """  " hello lexer """,

            "Unclosed String:  hello lexer ",
            113
        ))



    def test_unclose_string_with_endline(self):
        self.assertTrue(TestLexer.test(
            """  " hello lexer 
            """,

            "Unclosed String:  hello lexer ",
            114
        ))


    
    def test_escape_string(self):
        self.assertTrue(TestLexer.test(
            """ 
" abc \n xyz "
" abc \\n xyz "
""
            """,
            "",
            115
        ))



    def test_illegal_escape(self):
        self.assertTrue(TestLexer.test(
            """ " hello lexer \t "     asdf  """,

            "Illegal Escape In String:  hello lexer 	 ",
            116
        ))



    def test_escape_string_literal(self):
        self.assertTrue(TestLexer.test(
            """
"Backspace  \b"
            """,
            "Illegal Escape In String: Backspace  ",
            117
        ))
        self.assertTrue(TestLexer.test(
            """
"Formfeed   \f"
            """,
            "Illegal Escape In String: Formfeed   ",
            118
        ))
        self.assertTrue(TestLexer.test(
            """
"Return     \r"
            """,
            """Illegal Escape In String: Return     
""",
            119
        ))
        self.assertTrue(TestLexer.test(
            """
"Newline    \n"
            """,
            """Illegal Escape In String: Newline    
""",
            120
        ))
        self.assertTrue(TestLexer.test(
            """
"Newline
    multiple lines
"           """,
            """Illegal Escape In String: Newline
    multiple lines
""",
            121
        ))
        self.assertTrue(TestLexer.test(
            """
"Tab        \t"
            """,
            "Illegal Escape In String: Tab        	",
            122
        ))
        self.assertTrue(TestLexer.test(
            """
"Backslash  \\ "
            """,
            "Illegal Escape In String: Backslash  \ ",
            123
        ))




