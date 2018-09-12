import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        """ Test Valid Lowercase Keywords """
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
            "function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and,then,or,else,and,then,or,else,div,mod,not,and,or,<EOF>",
            101
        ))
        

    def test_2(self):
        """ Test Valid Keywords """
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
AND             THeN   OR   elSE
dIV mOd NOT and OR
""",

            "FuNctiOn,prOceDure,Begin,END,True,FalSE,IF,thEn,ELSE,fOR,While,with,DO,To,downTo,RETURN,break,COntiNue,integer,string,REAL,BOOLean,ARRAY,VAR,Of,anD,Then,or,eLse,AND,THeN,OR,elSE,dIV,mOd,NOT,and,OR,<EOF>",
            102
        ))
        

    def test_3(self):
        """ Test Specific Characters """
        self.assertTrue(TestLexer.test(
            """
+ - * / := <= >= <> = < >
( ) { } [ ] ; , : , ..
""",

            "+,-,*,/,:=,<=,>=,<>,=,<,>,(,),[,],;,,,:,,,..,<EOF>",
            103
        ))
        

    def test_4(self):
        """ Test Inline Comments """
        self.assertTrue(TestLexer.test(
            """
// This is a line comment
""",

            "<EOF>",
            104
        ))
        

    def test_5(self):
        """ Test Block Comments 1 """
        self.assertTrue(TestLexer.test(
            """
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
            """
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
            107
        ))
        

    def test_8(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.test(
            """
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            108
        ))
        

    def test_9(self):
        """ Test Real Literal """
        self.assertTrue(TestLexer.test(
            """
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            109
        ))
        

    def test_10(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.test(
            """
""      "A"     
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            110
        ))
        

    def test_11(self):
        """ Test Identifiers """
        self.assertTrue(TestLexer.test(
            """
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
            """
123abc 123_abc 00000123_123abc
""",

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            112
        ))
        

    def test_13(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
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
            """
e-12 e12 . 1e 12e 12.05e .05e ee e01
""",

            "e,-,12,e12,.,1,e,12,e,12.05,e,.05,e,ee,e01,<EOF>",
            114
        ))
        

    def test_15(self):
        """ Test Array Declare """
        self.assertTrue(TestLexer.test(
            """
array [1 .. 3] of integer
""",

            "array,[,1,..,3,],of,integer,<EOF>",
            115
        ))
        

    def test_16(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            """  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))
        

    def test_17(self):
        """ Test Unclose String with endline """
        self.assertTrue(TestLexer.test(
            """
" hello lexer 

""",

            """Unclosed String:  hello lexer 

""",
            117
        ))
        

    def test_18(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
" abc \n xyz "
" abc \\n xyz "
""",

            ''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))
        

    def test_19(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
" hello lexer \t "     asdf 
""",

            ' hello lexer \t ,asdf,<EOF>',
            119
        ))
        

    def test_20(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
"Backspace  \b"
""",

            'Backspace  \b,<EOF>',
            120
        ))
        

    def test_21(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Formfeed   \f"
""",

            'Formfeed   \f,<EOF>',
            121
        ))
        

    def test_22(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Return     \r"
""",

            '''Return     
,<EOF>''',
            122
        ))
        

    def test_23(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Newline    \n"
""",

            '''Newline    \n,<EOF>''',
            123
        ))
        

    def test_24(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Newline
    multiple lines
"           """,

            '''Newline
    multiple lines
,<EOF>''',
            124
        ))
        

    def test_25(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Tab        \t"
""",

            'Tab        \t,<EOF>',
            125
        ))
        

    def test_26(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"Backslash  \\ "
""",

            "Illegal Escape In String: Backslash  \\ ",
            126
        ))
        

    def test_27(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
Illegal: "\a"
""",

            '''Illegal,:,,<EOF>''',
            127
        ))
        

    def test_28(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))
        

    def test_29(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))
        

    def test_30(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))
        

    def test_31(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" abc ' xyz "
""",

            "Illegal Escape In String:  abc '",
            131
        ))
        

    def test_32(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" abc \' xyz "
""",

            " abc ' xyz ,<EOF>",
            132
        ))
        

    def test_33(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
" abc \" xyz " ghi
""",

            " abc ,xyz,Unclosed String:  ghi\n",
            133
        ))
        

    def test_34(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))
        

    def test_35(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
!== != & ^ % $ # ... \
""",

            "Error Token !",
            135
        ))
        

    def test_36(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
if a != b then
""",

            "if,a,Error Token !",
            136
        ))
        

    def test_37(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
a := a & 1
""",

            "a,:=,a,Error Token &",
            137
        ))
        

    def test_38(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))
        

    def test_39(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
#define for 1
""",

            "Error Token #",
            139
        ))
        

    def test_40(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.test(
            """
1234 0000001234 0000043123
""",

            "1234,0000001234,0000043123,<EOF>",
            140
        ))
        

    def test_41(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.test(
            """
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))
        

    def test_42(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))
        

    def test_43(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))
        

    def test_44(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"abc \\ xyz"
""",

            "Illegal Escape In String: abc \ ",
            144
        ))
        

    def test_45(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"\\"
""",

            '''Unclosed String: \"
''',
            145
        ))
        

    def test_46(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"\\ "
""",

            "Illegal Escape In String: \ ",
            146
        ))
        

    def test_47(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"\"
""",

            ",<EOF>",
            147
        ))
        

    def test_48(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
"\""
""",

            """,Unclosed String: 
""",
            148
        ))
        

    def test_49(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
s = "string           
"a = 4
g = 9
""",

            '''s,=,string           
,a,=,4,g,=,9,<EOF>''',
            149
        ))
        

    def test_50(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            150
        ))
        

    def test_51(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            151
        ))
        

    def test_52(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            152
        ))
        

    def test_53(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            153
        ))
        

    def test_54(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            154
        ))
        

    def test_55(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            155
        ))
        

    def test_56(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            156
        ))
        

    def test_57(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            157
        ))
        

    def test_58(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            158
        ))
        

    def test_59(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            159
        ))
        

    def test_60(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            160
        ))
        

    def test_61(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            161
        ))
        

    def test_62(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            162
        ))
        

    def test_63(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            163
        ))
        

    def test_64(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            164
        ))
        

    def test_65(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            165
        ))
        

    def test_66(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            166
        ))
        

    def test_67(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            167
        ))
        

    def test_68(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            168
        ))
        

    def test_69(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            169
        ))
        

    def test_70(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            170
        ))
        

    def test_71(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            171
        ))
        

    def test_72(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            172
        ))
        

    def test_73(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            173
        ))
        

    def test_74(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            174
        ))
        

    def test_75(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            175
        ))
        

    def test_76(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            176
        ))
        

    def test_77(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            177
        ))
        

    def test_78(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            178
        ))
        

    def test_79(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            179
        ))
        

    def test_80(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            180
        ))
        

    def test_81(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            181
        ))
        

    def test_82(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            182
        ))
        

    def test_83(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            183
        ))
        

    def test_84(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            184
        ))
        

    def test_85(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            185
        ))
        

    def test_86(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            186
        ))
        

    def test_87(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            187
        ))
        

    def test_88(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            188
        ))
        

    def test_89(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            189
        ))
        

    def test_90(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            190
        ))
        

    def test_91(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            191
        ))
        

    def test_92(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            192
        ))
        

    def test_93(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            193
        ))
        

    def test_94(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            194
        ))
        

    def test_95(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            195
        ))
        

    def test_96(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            196
        ))
        

    def test_97(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            197
        ))
        

    def test_98(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            198
        ))
        

    def test_99(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            199
        ))
        

    def test_100(self):
        """ Test  """
        self.assertTrue(TestLexer.test(
            """
""",

            "<EOF>",
            200
        ))
        
