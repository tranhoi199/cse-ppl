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
div mod not and or
            """,

            "",
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

            "",
            102
        ))



    def test_specific_characters(self):
        self.assertTrue(TestLexer.test(
            """
+ - * / := <= >= <> = < >
( ) { } [ ] ; , : , ..
            """,

            "",
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

            "",
            105
        ))



    def test_real_literal(self):
        self.assertTrue(TestLexer.test(
            """
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
            """,

            "",
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



    def test_escape_string_literal(self):
        self.assertTrue(TestLexer.test(
            """
"Backspace  \b"
"Formfeed   \f"
"Return     \r"
"Newline    \n"
"Newline
multiple lines
"
"Tab        \t"
"Quotes ''   '  ""  "   "
"Backslash  \\"
            """,

            "",
            108
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

            "",
            109
        ))




    def test_invalid_identifier(self):
        self.assertTrue(TestLexer.test(
            """123abc 123_abc 00000123_123abc""",

            "",
            110
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

            "",
            111
        ))




    def test_invalid_real(self):
        self.assertTrue(TestLexer.test(
            """e-12 e12 . 1e 12e 12.05e .05e ee e01""",

            "",
            112
        ))



    def test_array(self):
        self.assertTrue(TestLexer.test(
            "array [1..3] of integer",

            "",
            113
        ))



    def test_unclose_string_no_endline(self):
        self.assertTrue(TestLexer.test(
            """  " hello lexer """,

            "",
            114
        ))



    def test_unclose_string_with_endline(self):
        self.assertTrue(TestLexer.test(
            """  " hello lexer 
            """,

            "",
            115
        ))


    
    def test_illegal_escape_ok(self):
        self.assertTrue(TestLexer.test(
            """ 
" hello lexer \\b \\t \\n \\f \\r \\" \\'  "
" string    \\\\ \\ttt \\bbb \aaa "
            """,

            "",
            116
        ))



    def test_illegal_escape(self):
        self.assertTrue(TestLexer.test(
            """ " hello lexer \t "     asdf  """,

            "",
            117
        ))










