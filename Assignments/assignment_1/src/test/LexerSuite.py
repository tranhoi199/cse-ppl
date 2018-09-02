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

                (* nestest comments { 
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