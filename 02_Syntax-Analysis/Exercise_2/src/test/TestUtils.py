import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/mp/parser/' in sys.path:
    sys.path.append('./main/mp/parser/')
if os.path.isdir('../target/main/mp/parser') and not '../target/main/mp/parser/' in sys.path:
    sys.path.append('../target/main/mp/parser/')
from MPLexer import MPLexer
from MPParser import MPParser
from lexererr import *

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = MPLexer
Parser = MPParser

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestLexer.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
    
    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(soldir + "/" + str(num) + ".txt","w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            # dest.write(tok.text+",")
            dest.write(tok.text + ": " + str(tok.type) + "\n")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestParser.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(soldir + "/" + str(num) + ".txt","w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()