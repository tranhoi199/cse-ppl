import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def testValidKeywords(self):
        "Test Valid Keywords"
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
            + - * / := <= >= <> = < >
            ( ) { } [ ] ; , : , ..
            """,

            "function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and then,or else,div,mod,not,and,or,+,-,*,/,:=,<=,>=,<>,=,<,>,(,),[,],;,,,:,,,..,<EOF>",
            101
        ))

    def testValidComment(self):
        "Test Valid Comment"
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
            102
        ))

    def testValidLiteralBoolean(self):
        """Test Valid Literal Boolean"""
        self.assertTrue(TestLexer.test(
            """true false""",
            "true,false,<EOF>",
            103
        ))

    def testValidLiteralInteger(self):
        """Test Valid Literal Integer"""
        self.assertTrue(TestLexer.test(
            """0 1 2 3 4 123 123456789""",
            "0,1,2,3,4,123,123456789,<EOF>",
            104
        ))

    def testValidLiteralReal(self):
        """Test Valid Literal Real"""
        self.assertTrue(TestLexer.test(
            """
            1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
            12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            105
        ))

    def testValidLiteralString(self):
        """Test Valid Literal String"""
        self.assertTrue(TestLexer.test(
            """
            ""      "A"     
            "Mulitiple Characters"
            """,

            '''"","A","Mulitiple Characters",<EOF>''',
            106
        ))

    def testEscapeLiteralString(self):
        """Test Escape Literal String"""
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
            
            '''",Backspace,,",",Formfeed,",",Return,",",Newline,",",Newline,multiple,lines,",",Tab,",",Quotes,',',',"","   ",",Backslash,\,",<EOF>''',
            107
        ))

    def testValidIdentifiers(self):
        """Test Valid Identifiers"""
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

    def testInvalidIdentifiers(self):
        """Test Invalid Identifiers"""
        self.assertTrue(TestLexer.test(
            """123abc 123_abc 00000123_123abc""",
            "123,abc,123,_abc,0,0,0,0,0,123,_123abc,<EOF>",
            109
        ))

    def testInvalidComment(self):
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

    def testInvalidLiteralReal(self):
        """Test Invalid Literal Real"""
        self.assertTrue(TestLexer.test(
            """e-12 e12 . 1e 12e 12.05e .05e ee e01""",
            "e,-,12,e12,.,1,e,12,e,12.05,e,.05,e,ee,e01,<EOF>",
            111
        ))

    def testInvalidLiteralBoolean(self):
        """Test Valid Literal Boolean"""
        self.assertTrue(TestLexer.test(
            """True False trUe faLSE trues falses Fals""",
            "True,False,trUe,faLSE,trues,falses,Fals,<EOF>",
            112
        ))

    def testArray(self):
        """Test Array"""
        self.assertTrue(TestLexer.test(
            "array [1 .. 3] of integer",
            "array,[,1,..,3,],of,integer,<EOF>",
            113
        ))
        self.assertTrue(TestLexer.test(
            "array [1..3] of integer",
            "array,[,1,..,3,],of,integer,<EOF>",
            114
        ))

    def testUncloseString(self):
        """Test Unclose String"""
        self.assertTrue(TestLexer.test(
            ''' "unclose string here    ''',
            "Unclosed String: ...",
            114
        ))
        self.assertTrue(TestLexer.test(
            ''' 
                "unclose string here    ''',
            "Unclosed String: ...",
            115
        ))
        self.assertTrue(TestLexer.test(
            ''' 
                "unclose string here   
                
            ''',
            "Unclosed String: ...",
            116
        ))

















