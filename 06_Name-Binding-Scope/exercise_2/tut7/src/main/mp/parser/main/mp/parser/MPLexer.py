# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\u00c5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\3\2\6\2S\n\2\r\2\16\2T\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7`\n\7\r\7\16\7a\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\r")
        buf.write("\u008c\n\r\r\r\16\r\u008d\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\2\2)\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65")
        buf.write("\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\17\3\2\37\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\4\2C\\c|\4\2CCcc\4\2DDdd\4\2")
        buf.write("EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr")
        buf.write("r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2")
        buf.write("YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u00ad\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2O\3\2\2\2\3R\3\2\2\2\5V")
        buf.write("\3\2\2\2\7X\3\2\2\2\tZ\3\2\2\2\13\\\3\2\2\2\r_\3\2\2\2")
        buf.write("\17e\3\2\2\2\21o\3\2\2\2\23x\3\2\2\2\25~\3\2\2\2\27\u0082")
        buf.write("\3\2\2\2\31\u008b\3\2\2\2\33\u008f\3\2\2\2\35\u0091\3")
        buf.write("\2\2\2\37\u0093\3\2\2\2!\u0095\3\2\2\2#\u0097\3\2\2\2")
        buf.write("%\u0099\3\2\2\2\'\u009b\3\2\2\2)\u009d\3\2\2\2+\u009f")
        buf.write("\3\2\2\2-\u00a1\3\2\2\2/\u00a3\3\2\2\2\61\u00a5\3\2\2")
        buf.write("\2\63\u00a7\3\2\2\2\65\u00a9\3\2\2\2\67\u00ab\3\2\2\2")
        buf.write("9\u00ad\3\2\2\2;\u00af\3\2\2\2=\u00b1\3\2\2\2?\u00b3\3")
        buf.write("\2\2\2A\u00b5\3\2\2\2C\u00b7\3\2\2\2E\u00b9\3\2\2\2G\u00bb")
        buf.write("\3\2\2\2I\u00bd\3\2\2\2K\u00bf\3\2\2\2M\u00c1\3\2\2\2")
        buf.write("O\u00c3\3\2\2\2QS\t\2\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2")
        buf.write("\2TU\3\2\2\2U\4\3\2\2\2VW\7*\2\2W\6\3\2\2\2XY\7+\2\2Y")
        buf.write("\b\3\2\2\2Z[\7=\2\2[\n\3\2\2\2\\]\7<\2\2]\f\3\2\2\2^`")
        buf.write("\t\3\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2")
        buf.write("\2\2cd\b\7\2\2d\16\3\2\2\2ef\59\35\2fg\5=\37\2gh\5\67")
        buf.write("\34\2hi\5\37\20\2ij\5#\22\2jk\5!\21\2kl\5C\"\2lm\5=\37")
        buf.write("\2mn\5#\22\2n\20\3\2\2\2op\5%\23\2pq\5C\"\2qr\5\65\33")
        buf.write("\2rs\5\37\20\2st\5A!\2tu\5+\26\2uv\5\67\34\2vw\5\65\33")
        buf.write("\2w\22\3\2\2\2xy\5\35\17\2yz\5#\22\2z{\5\'\24\2{|\5+\26")
        buf.write("\2|}\5\65\33\2}\24\3\2\2\2~\177\5#\22\2\177\u0080\5\65")
        buf.write("\33\2\u0080\u0081\5!\21\2\u0081\26\3\2\2\2\u0082\u0083")
        buf.write("\5+\26\2\u0083\u0084\5\65\33\2\u0084\u0085\5A!\2\u0085")
        buf.write("\u0086\5#\22\2\u0086\u0087\5\'\24\2\u0087\u0088\5#\22")
        buf.write("\2\u0088\u0089\5=\37\2\u0089\30\3\2\2\2\u008a\u008c\t")
        buf.write("\4\2\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\32\3\2\2\2\u008f\u0090")
        buf.write("\t\5\2\2\u0090\34\3\2\2\2\u0091\u0092\t\6\2\2\u0092\36")
        buf.write("\3\2\2\2\u0093\u0094\t\7\2\2\u0094 \3\2\2\2\u0095\u0096")
        buf.write("\t\b\2\2\u0096\"\3\2\2\2\u0097\u0098\t\t\2\2\u0098$\3")
        buf.write("\2\2\2\u0099\u009a\t\n\2\2\u009a&\3\2\2\2\u009b\u009c")
        buf.write("\t\13\2\2\u009c(\3\2\2\2\u009d\u009e\t\f\2\2\u009e*\3")
        buf.write("\2\2\2\u009f\u00a0\t\r\2\2\u00a0,\3\2\2\2\u00a1\u00a2")
        buf.write("\t\16\2\2\u00a2.\3\2\2\2\u00a3\u00a4\t\17\2\2\u00a4\60")
        buf.write("\3\2\2\2\u00a5\u00a6\t\20\2\2\u00a6\62\3\2\2\2\u00a7\u00a8")
        buf.write("\t\21\2\2\u00a8\64\3\2\2\2\u00a9\u00aa\t\22\2\2\u00aa")
        buf.write("\66\3\2\2\2\u00ab\u00ac\t\23\2\2\u00ac8\3\2\2\2\u00ad")
        buf.write("\u00ae\t\24\2\2\u00ae:\3\2\2\2\u00af\u00b0\t\25\2\2\u00b0")
        buf.write("<\3\2\2\2\u00b1\u00b2\t\26\2\2\u00b2>\3\2\2\2\u00b3\u00b4")
        buf.write("\t\27\2\2\u00b4@\3\2\2\2\u00b5\u00b6\t\30\2\2\u00b6B\3")
        buf.write("\2\2\2\u00b7\u00b8\t\31\2\2\u00b8D\3\2\2\2\u00b9\u00ba")
        buf.write("\t\32\2\2\u00baF\3\2\2\2\u00bb\u00bc\t\33\2\2\u00bcH\3")
        buf.write("\2\2\2\u00bd\u00be\t\34\2\2\u00beJ\3\2\2\2\u00bf\u00c0")
        buf.write("\t\35\2\2\u00c0L\3\2\2\2\u00c1\u00c2\t\36\2\2\u00c2N\3")
        buf.write("\2\2\2\u00c3\u00c4\13\2\2\2\u00c4P\3\2\2\2\6\2Ta\u008d")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    LB = 2
    RB = 3
    SEMI = 4
    COLON = 5
    WS = 6
    PROCEDURE = 7
    FUNCTION = 8
    BEGIN = 9
    END = 10
    INTTYPE = 11
    ID = 12
    ERROR_CHAR = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "LB", "RB", "SEMI", "COLON", "WS", "PROCEDURE", "FUNCTION", 
            "BEGIN", "END", "INTTYPE", "ID", "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "LB", "RB", "SEMI", "COLON", "WS", "PROCEDURE", 
                  "FUNCTION", "BEGIN", "END", "INTTYPE", "ID", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


