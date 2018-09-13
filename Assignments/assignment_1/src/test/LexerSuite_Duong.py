import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_identifier2(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
    def test_identifier4(self):
        self.assertTrue(TestLexer.test("01ancmds _abc 12mckm","01,ancmds,_abc,12,mckm,<EOF>",104))
    def test_identifier5(self):
        self.assertTrue(TestLexer.test("mddsdsd _abc 12mckm","mddsdsd,_abc,12,mckm,<EOF>",105))
    def test_identifier6(self):
        self.assertTrue(TestLexer.test("mddAsBBs12dsd 1AAabc mc123km","mddAsBBs12dsd,1,AAabc,mc123km,<EOF>",106))
    def test_identifier7(self):
        self.assertTrue(TestLexer.test("eP 9yMbMU6 KaiQx82p SL12zI","eP,9,yMbMU6,KaiQx82p,SL12zI,<EOF>",107))
    def test_identifier8(self):
        self.assertTrue(TestLexer.test("rdad 40oBhenK292aWfTSFLt6","rdad,40,oBhenK292aWfTSFLt6,<EOF>",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.test("vJozdspl3p1iOcRiAI12 dUB 1.NM 2cY2","vJozdspl3p1iOcRiAI12,dUB,1.,NM,2,cY2,<EOF>",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.test("0gChhrlnd8xI1dsxd s dwdski6E","0,gChhrlnd8xI1dsxd,s,dwdski6E,<EOF>",110))


    def test_keyword1(self):
        self.assertTrue(TestLexer.test("01anc mds For c brEaK 21mc continuE km","01,anc,mds,For,c,brEaK,21,mc,continuE,km,<EOF>",111))
    def test_keyword2(self):
        self.assertTrue(TestLexer.test("tO doWnto Do if thEn elSE return1","tO,doWnto,Do,if,thEn,elSE,return1,<EOF>",112))
    def test_keyword3(self):
        self.assertTrue(TestLexer.test("reTuRn whILe beGin eND function o","reTuRn,whILe,beGin,eND,function,o,<EOF>",113))
    def test_keyword4(self):
        self.assertTrue(TestLexer.test("pROCEDURE TRUe 1.12VAR45 ARRay OF 12REAL","pROCEDURE,TRUe,1.12,VAR45,ARRay,OF,12,REAL,<EOF>",114))
    def test_keyword5(self):
        self.assertTrue(TestLexer.test("BOOLEAN int 1.12INTEGER sTRIng not 12and","BOOLEAN,int,1.12,INTEGER,sTRIng,not,12,and,<EOF>",115))
    def test_keyword6(self):
        self.assertTrue(TestLexer.test("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Mod,nottrEu,<EOF>",116))
    def test_keyword7(self):
        self.assertTrue(TestLexer.test("if then else diMod 12String true ds false","if,then,else,diMod,12,String,true,ds,false,<EOF>",117))
    def test_keyword8(self):
        self.assertTrue(TestLexer.test("anD then elsediMod doWnTO.1trueds false","anD,then,elsediMod,doWnTO,.1,trueds,false,<EOF>",118))
    def test_keyword9(self):
        self.assertTrue(TestLexer.test("anD thadenelsediMod doWnTO.1truedsfalse BOOLEAN float 1.12INTEGER sTRIng noT d15s0and",
        "anD,thadenelsediMod,doWnTO,.1,truedsfalse,BOOLEAN,float,1.12,INTEGER,sTRIng,noT,d15s0and,<EOF>",119))
    def test_keyword10(self):
        self.assertTrue(TestLexer.test("12while int 1.12 INTEGER oR 12function","12,while,int,1.12,INTEGER,oR,12,function,<EOF>",120))


    def test_string1(self):
        self.assertTrue(TestLexer.test("\"ahihi\\\"\"","ahihi\\\",<EOF>",121))
    def test_string2(self):
        self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",122))
    def test_string3(self):
        self.assertTrue(TestLexer.test("\"abc\\ta\\nbc\"","abc\\ta\\nbc,<EOF>",123))
    def test_string4(self):
        self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",124))
    def test_string5(self):
        self.assertTrue(TestLexer.test("\"0.1anc\\'cv\" 0.mne \"12\\\\3\"","0.1anc\\'cv,0.,mne,12\\\\3,<EOF>",125))
    def test_string6(self):
        self.assertTrue(TestLexer.test("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,abc1!!@#$$%^i\\n,12,yz,<EOF>",126))
    def test_string7(self):
        self.assertTrue(TestLexer.test("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","!h$5FBi6,_q,!SZR,H},sIfpw,<EOF>",127))
    def test_string8(self):
        self.assertTrue(TestLexer.test("4\"&J^1a_.\" QGn\"?67Sp\"{,}6Asz\"Yx](\"","4,&J^1a_.,QGn,?67Sp,6,Asz,Yx](,<EOF>",128))
    def test_string9(self):
        self.assertTrue(TestLexer.test("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,^VLR@\\\\OusM;,uGM,+,jE,<EOF>",129))
    def test_string10(self):
        self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","(IFq+lq(,IhK6we,GdvS,<EOF>",130))


    def test_operator1(self):
        self.assertTrue(TestLexer.test("ddsls<l>02>=d1s<=123","ddsls,<,l,>,02,>=,d1s,<=,123,<EOF>",131))
    def test_operator2(self):
        self.assertTrue(TestLexer.test("dlsd+1ds-*dmdsa/<>mdks","dlsd,+,1,ds,-,*,dmdsa,/,<>,mdks,<EOF>",132))
    def test_operator3(self):
        self.assertTrue(TestLexer.test("lsddl<>=1<>=112>=<=d1","lsddl,<>,=,1,<>,=,112,>=,<=,d1,<EOF>",133))
    def test_operator4(self):
        self.assertTrue(TestLexer.test("13ek3<9e=9eend<>=Edasdndm<=>erE","13,ek3,<,9,e,=,9,eend,<>,=,Edasdndm,<=,>,erE,<EOF>",134))
    def test_operator5(self):
        self.assertTrue(TestLexer.test("djeiwjd1A<=>12>=<=d","djeiwjd1A,<=,>,12,>=,<=,d,<EOF>",135))
    def test_operator6(self):
        self.assertTrue(TestLexer.test("<-mod>=not+mod+and+not","<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>",136))
    def test_operator7(self):
        self.assertTrue(TestLexer.test("*and<=>mod</<=","*,and,<=,>,mod,<,/,<=,<EOF>",137))
    def test_operator8(self):
        self.assertTrue(TestLexer.test("=or<=<><>=-<=>","=,or,<=,<>,<>,=,-,<=,>,<EOF>",138))
    def test_operator9(self):
        self.assertTrue(TestLexer.test("not<>=and>=mod<=-and","not,<>,=,and,>=,mod,<=,-,and,<EOF>",139))
    def test_operator10(self):
        self.assertTrue(TestLexer.test("mod<=<===mod/<=<","mod,<=,<=,=,=,mod,/,<=,<,<EOF>",140))


    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.test("\"bac\\ma\"","Illegal Escape In String: bac\\m",141))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.test("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",142))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.test("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",143))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.test("\"ado\\mado\"","Illegal Escape In String: ado\\m",144))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.test("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\k",145))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.test("\"aa\wb\"","Illegal Escape In String: aa\w",146))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.test("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l",147))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.test("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",148))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\f\"","+,1.1,Illegal Escape In String: ba\\q",149))
    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.test("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",150))


    def test_unclose_String1(self):
        self.assertTrue(TestLexer.test("\"bacxyc","Unclosed String: bacxyc",151))
    def test_unclose_String2(self):
        self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(","NmkobYn,+,I1,+,Unclosed String: `YS2h.J(",152))
    def test_unclose_String3(self):
        self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",153))
    def test_unclose_String4(self):
        self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,123,Unclosed String: abc",154))
    def test_unclose_String5(self):
        self.assertTrue(TestLexer.test("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",155))
    def test_unclose_String6(self):
        self.assertTrue(TestLexer.test("38n\"[#Ffs?0ED\"0.\"T`#!7n","38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n",156))
    def test_unclose_String7(self):
        self.assertTrue(TestLexer.test("\".Hub`22Y\"<{;}\"Y`=DxXhZKh",".Hub`22Y,<,Unclosed String: Y`=DxXhZKh",157))
    def test_unclose_String8(self):
        self.assertTrue(TestLexer.test("\"ULxM*`~.~+C_DISD2","Unclosed String: ULxM*`~.~+C_DISD2",158))
    def test_unclose_String9(self):
        self.assertTrue(TestLexer.test("{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1","Nk8U;,rA,@Y3*,oV,Unclosed String: bh1",159))
    def test_unclose_String10(self):
        self.assertTrue(TestLexer.test("\"o|F&)LqX\"+>X+\"#Fft","o|F&)LqX,+,>,X,+,Unclosed String: #Fft",160))


    def test_integer_real1(self):
        self.assertTrue(TestLexer.test("1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
        "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>",161))
    def test_integer_real2(self):
        self.assertTrue(TestLexer.test("9.0 12e8 0.33E-3 128e-42","9.0,12e8,0.33E-3,128e-42,<EOF>",162))
    def test_integer_real3(self):
        #TODO: fix -42
        self.assertTrue(TestLexer.test("11.0 12.e8 0.11+E-3 145Ee-42","11.0,12.e8,0.11,+,E,-,3,145,Ee,-,42,<EOF>",163))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.test(".11E2 1.11 .33 1.e12 1E-15",".11E2,1.11,.33,1.e12,1E-15,<EOF>",164))
    def test_integer_real5(self):
        #TODO:  fix -15
        self.assertTrue(TestLexer.test("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>",165))
    def test_integer_real6(self):
        self.assertTrue(TestLexer.test("e-12.1 11.e11 12..12 2. .2 11e11 .1e-3","e,-,12.1,11.e11,12.,.12,2.,.2,11e11,.1e-3,<EOF>",166))
    def test_integer_real7(self):
        self.assertTrue(TestLexer.test("12.e0 -101 11.E 11.1e2","12.e0,-,101,11.,E,11.1e2,<EOF>",167))


    def test_comment1(self):
        self.assertTrue(TestLexer.test("(*12.e0 -101*) 11.E //11.1e2","11.,E,<EOF>",168))
    def test_comment2(self):
        self.assertTrue(TestLexer.test("(*12.e0} -101*) {11.E} 11.1e2","11.1e2,<EOF>",169))
    def test_comment3(self):
        self.assertTrue(TestLexer.test("{abc} //1.abc","<EOF>",170))
    def test_comment4(self):
        self.assertTrue(TestLexer.test("(*1.e0 - 101* {11.E} //22.12\n","(,*,1.e0,-,101,*,<EOF>",171))
    def test_comment5(self):
        #TODO: Fix reallit , intlit
        self.assertTrue(TestLexer.test("(*12.e0\nabc*) -101*) 11.1e2","-,101,*,),11.1e2,<EOF>",172))
    def test_comment6(self):
        self.assertTrue(TestLexer.test("13ek3<9e=9eendE//dasd1.ndm<>d1.02erE","13,ek3,<,9,e,=,9,eendE,<EOF>",173))
    def test_comment7(self):
        self.assertTrue(TestLexer.test("//dasd1.ndm\n<>d1.02erE","<>,d1,.02,erE,<EOF>",174))
    def test_comment8(self):
        self.assertTrue(TestLexer.test("{abc<>xyzb>cv} (*12mds<>dsd=(*dsd*)*)*","*,),*,<EOF>",175))
    def test_comment9(self):
        self.assertTrue(TestLexer.test("//abc{abc<>xyzb>cv}","<EOF>",176))
    def test_comment10(self):
        self.assertTrue(TestLexer.test("abc{abc<>x//yzb>cv}","abc,<EOF>",177))
    def test_comment11(self):
        self.assertTrue(TestLexer.test("(*abc{abc<>x//yzb>cv}*)","<EOF>",178))


    def test_error_char1(self):
        self.assertTrue(TestLexer.test("(*-101*) 11.+12*#$","11.,+,12,*,Error Token #",179))
    def test_error_char2(self):
        self.assertTrue(TestLexer.test("Arj4AORqwExkrCxZPi`:","Arj4AORqwExkrCxZPi,Error Token `",180))
    def test_error_char3(self):
        self.assertTrue(TestLexer.test("o%jvhs'Ty{*(0Ay0s&n|","o,Error Token %",181))
    def test_error_char4(self):
        self.assertTrue(TestLexer.test("(C*.=22Pta!0=&o","(,C,*,Error Token .",182))
    def test_error_char5(self):
        self.assertTrue(TestLexer.test(";J~%IbnQL!x-OBd",";,J,Error Token ~",183))
    def test_error_char6(self):
        self.assertTrue(TestLexer.test("b(9KZ!YBraRCF","b,(,9,KZ,Error Token !",184))
    def test_error_char7(self):
        self.assertTrue(TestLexer.test("kz-70S9+0s)f<)?0gg","kz,-,70,S9,+,0,s,),f,<,),Error Token ?",185))
    def test_error_char8(self):
        self.assertTrue(TestLexer.test("C+9and+EG9{?r2v}hFAX|>","C,+,9,and,+,EG9,hFAX,Error Token |",186))
    def test_error_char9(self):
        self.assertTrue(TestLexer.test("pQ*6'q0+Y@}f(^9Xn","pQ,*,6,Error Token '",187))
    def test_error_char10(self):
        self.assertTrue(TestLexer.test("aFG[@WQS{QBW7Y6]le$5","aFG,[,Error Token @",188))
    def test_random1(self):
        self.assertTrue(TestLexer.test(""" "hel\\\"l\\\'o\\\\hehe" ""","hel\\\"l\\\'o\\\\hehe,<EOF>",189))
    def test_random2(self):
        self.assertTrue(TestLexer.test(""" 2+3 andthen 6 ""","2,+,3,andthen,6,<EOF>",190))
    def test_random3(self):
        self.assertTrue(TestLexer.test(""" 
        "abcd  
        efg
        ""","Unclosed String: abcd  ",191))
    def test_random4(self):
        self.assertTrue(TestLexer.test(""" 
        "abcd \b 
        efg
        ""","Unclosed String: abcd ",192))
    def test_random5(self):
        self.assertTrue(TestLexer.test(""" 
        "t \f
        efg
        ""","Unclosed String: t ",193))
    def test_random6(self):
        self.assertTrue(TestLexer.test(""" 
        "t \f efg"
        ""","Unclosed String: t ",194))
    def test_random7(self):
        self.assertTrue(TestLexer.test(""" 
        "t \\\\x efg"
        ""","t \\\\x efg,<EOF>",195))
    def test_random8(self):
        self.assertTrue(TestLexer.test(""" 
        "t \ {abcd}\\x efg"
        ""","Illegal Escape In String: t \ ",196))
    def test_random9(self):
        self.assertTrue(TestLexer.test(""" 
        "t \{abcd}\\x efg"
        ""","Illegal Escape In String: t \{",197))
    def test_random10(self):
        self.assertTrue(TestLexer.test(""" 
        (*(*abcd*)*)
        ""","*,),<EOF>",198))
    def test_random11(self):
        self.assertTrue(TestLexer.test(""" 
        (* {abcd (*abcd*)}eftg *)
        ""","Error Token }",199))


