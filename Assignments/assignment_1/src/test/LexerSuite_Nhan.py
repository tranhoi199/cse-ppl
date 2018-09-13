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
        self.assertTrue(TestLexer.test("11.0 12.e8 0.11+E-3 145Ee-42","11.0,12.e8,0.11,+,E,-,3,145,Ee,-,42,<EOF>",163))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.test(".11E2 1.11 .33 1.e12 1E-15",".11E2,1.11,.33,1.e12,1E-15,<EOF>",164))
    def test_integer_real5(self):
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
        self.assertTrue(TestLexer.test("\"hel\\\"l\\\'o\\\\hehe\"","hel\\\"l\\\'o\\\\hehe,<EOF>",189))
    def test_random2(self):
        inp = "n = input()\ns = raw_input()\n\ni = 0\nt = [\"RU\", \"UR\"]\nwhile (i < len(s)):\n    if s[i:i+2] in t:\n        s = s[0:i] + \"D\" + s[i+2:len(s)]\n    i += 1\nprint len(s)"
        out = "n,=,input,(,),s,=,raw_input,(,),i,=,0,t,=,[,RU,,,UR,],while,(,i,<,len,(,s,),),:,if,s,[,i,:,i,+,2,],in,t,:,s,=,s,[,0,:,i,],+,D,+,s,[,i,+,2,:,len,(,s,),],i,+,=,1,print,len,(,s,),<EOF>"
        self.assertTrue(TestLexer.test(inp, out, 190))
    def test_random3(self):
        inp = "def f(k):\n    if len(k) == 1:\n        return 1\n    if len(k) % 2 == 1:\n        return 1 + f(k[0:len(k)-1])\n    if k[0:len(k)/2] == k[len(k)/2:len(k)]:\n        return 1 + f(k[0:len(k)/2])\n    return 1 + f(k[0:len(k)-1])\n\nn = input()\ns = raw_input()\n\nprint f(s)"
        out = "def,f,(,k,),:,if,len,(,k,),=,=,1,:,return,1,if,len,(,k,),Error Token %"
        self.assertTrue(TestLexer.test(inp, out, 191))
    def test_random4(self):
        inp = "n = input()\nl = list(map(int, raw_input().strip().split()))\ns = [abs(l[i+1] - l[i]) for i in range(len(l)-1)]\nq = sorted(list(set(s)))\nif len(q) == 2:\n    if q[0] != 1:\n        print \"NO\"\n    else:\n        y = q[1]\n        m = max(s)\n        x = m/y + 1\n        \n        kt = 1\n        for i in range(len(s)):\n            if (l[i+1] - l[i] == 1 and l[i] % y == 0) or (l[i] - l[i+1] == 1 and l[i+1] % y ==0):\n                kt = 0\n                break;\n        if (kt):\n            print \"YES\"\n            print x,y\n        else:\n            print \"NO\"\nelse:\n    if len(q) == 1 and q[0] != 0:\n        y = q[0]\n        m = max(s)\n        x = m/y + 1\n        print \"YES\"\n        print x,y\n    else:\n        print \"NO\""
        out = "n,=,input,(,),l,=,list,(,map,(,int,,,raw_input,(,),Error Token ."
        self.assertTrue(TestLexer.test(inp, out, 192))
    def test_random5(self):
        inp = "[n,m,s,t] = map(int, raw_input().strip().split())\n\nmatrix = [[0 for i in range(n)] for i in range(n)]\n\nfor i in range(m):\n    [a, b] = map(int, raw_input().strip().split())\n    matrix[a-1][b-1] = 1\n    matrix[b-1][a-1] = 1\n\nds = [0 for i in range(n)]\ndt = [0 for i in range(n)]\n\nlist = [(s - 1, 0)]\n\nwhile len(list) != 0:\n    el = list.pop(len(list) - 1)\n    for i in range(n):\n        if matrix[el[0]][i] == 1 and ds[i] == 0:\n            ds[i] = el[1] + 1\n   list.append((i, ds[i]))\nds[s-1] = 0\n\nlist = [(t - 1, 0)]\nwhile len(list) != 0:\n    el = list.pop(len(list) - 1)\n    for i in range(n):\n        if matrix[el[0]][i] == 1 and dt[i] == 0:\n            dt[i] = el[1] + 1\n            list.append((i, dt[i]))\ndt[t-1] = 0\n\nk = ds[t-1]\n\ncount = 0\nfor i in range(n - 1):\n    for j in range(i + 1, n):\n        if [i, j] == [s - 1, t - 1]:\n            continue\n        if matrix[i][j] == 0:\n            kz = ds[i] + 1 + dt[j]\nkx = ds[j] + 1 + dt[i]\n            if k <= kz and k <= kx:\n                count += 1\n\nprint count"
        out = "[,n,,,m,,,s,,,t,],=,map,(,int,,,raw_input,(,),Error Token ."
        self.assertTrue(TestLexer.test(inp, out, 193))
    def test_random6(self):
        inp = "def checkdiff(a, b):\n    s = 0\n    for i in range(len(a)):\n        for j in range(len(a[0])):\n            if a[i][j] != b[i][j]:\n                s += 1\n    return s\n\nn = input()\n\npieces = []\nfor i in range(4):\n    piece = []\n    for j in range(n):\n        st = raw_input()\n        if st == \"\":\n            st = raw_input()\n        ro = [i for i in st]\n        piece.append(ro)\n    \n    pieces.append(piece)\n    \nstr_0 = \"01\"*(n/2) + \"0\"\nstr_1 = \"10\"*(n/2) + \"1\"\nlist_0 = [i for i in str_0]\nlist_1 = [i for i in str_1]\n\npiece_0 = []\nfor i in range(n/2):\n    piece_0.append(list_0)\n    piece_0.append(list_1)\npiece_0.append(list_0)\n\npiece_1 = []\nfor i in range(n/2):\n    piece_1.append(list_1)\n    piece_1.append(list_0)\npiece_1.append(list_1)\n\n\ncheck_0 = []\nfor i in range(4):\n    check_0.append(checkdiff(pieces[i], piece_0))\n\ncheck_1 = []\nfor i in range(4):\n    check_1.append(checkdiff(pieces[i], piece_1))\n\nans = check_0[0] + check_0[1] + check_1[2] + check_1[3]\n\nfor i in range(3):\n    for j in range(i + 1, 4):\n        t = check_0[i] + check_0[j]\n        for k in range(4):\n            if k != i and k != j:\n                t += check_1[k]\n        ans = min(ans, t)\n\nprint ans"
        out = "def,checkdiff,(,a,,,b,),:,s,=,0,for,i,in,range,(,len,(,a,),),:,for,j,in,range,(,len,(,a,[,0,],),),:,if,a,[,i,],[,j,],Error Token !"
        self.assertTrue(TestLexer.test(inp, out, 194))
    def test_random7(self):
        inp = "[n, m] = map(int, raw_input().strip().split())\nl = map(int, raw_input().strip().split())\n\nc = [0 for i in range(n)]\nfor i in l:\n    c[i-1] += 1\nprint min(c)"
        out = "[,n,,,m,],=,map,(,int,,,raw_input,(,),Error Token ."
        self.assertTrue(TestLexer.test(inp, out, 195))
    def test_random8(self):
        inp = "int min(int a, int b)\n{\n    if (a > b)\n        return b;\n    return a;\n}\n\nint style(string s)\n{\n    if (s == \"M\")\n        return 1;\n    if (s == \"S\")\n        return 2;\n    if (s == \"L\")\n        return 3;\n    if (s == \"XS\")\n        return 4;\n    if (s == \"XL\")\n        return 5;\n    if (s == \"XXS\")\n        return 6;\n    if (s == \"XXL\")\n        return 7;\n    if (s == \"XXXS\")\n        return 8;\n    if (s == \"XXXL\")\n        return 9;\n    return 0;\n\n}\n\nint main()\n{\n    int n;\n    cin >> n;\n    \n    string s;\n    int ar[10];\n    for (int i = 0; i < 10; i ++)\n        ar[i] = 0;\n    for (int i = 0; i < n; i ++)\n    {\n        cin >> s;\n        ar[style(s)] ++;\n    }\n    \n    int br[10];\n    for (int i = 0; i < 10; i ++)\n        br[i] = 0;\n    for (int i = 0; i < n; i ++)\n    {\n        cin >> s;\n        br[style(s)] ++;\n    }\n    \n    int ans = 0;\n    \n    int t = 0;\n    int sum = 0;\n    for (int i = 1; i < 10; i ++)\n    {\n        t += min(ar[i], br[i]);\n        sum += ar[i];\n    }\n    ans = sum - t;\n    \n    cout << ans << endl;\n    \n    return 0;\n}"
        out = "int,min,(,int,a,,,int,b,),int,style,(,string,s,),int,main,(,),int,br,[,10,],;,for,(,int,i,=,0,;,i,<,10,;,i,+,+,),br,[,i,],=,0,;,for,(,int,i,=,0,;,i,<,n,;,i,+,+,),int,ans,=,0,;,int,t,=,0,;,int,sum,=,0,;,for,(,int,i,=,1,;,i,<,10,;,i,+,+,),ans,=,sum,-,t,;,cout,<,<,ans,<,<,endl,;,return,0,;,Error Token }"
        self.assertTrue(TestLexer.test(inp, out, 196))

    def test_random9(self):
        inp = "n = input()\nl = map(int, raw_input().strip().split())\nk = 0\ns = 0\nsu = sum(l)\nwhile (s < su/2):\n    s += l[k]\n    k += 1\nprint k"
        out = "n,=,input,(,),l,=,map,(,int,,,raw_input,(,),Error Token ."
        self.assertTrue(TestLexer.test(inp, out, 197))

    def test_random10(self):
        inp = "import math\ndef check(a, b):\n    i = 0\n    j = 0\n    while i < len(b) and j < len(a):\n        while j < len(a) and a[j] != b[i]:\n            j += 1\n        if j >= len(a):\n            break\n        i += 1\n        j += 1\n    if i >= len(b):\n        return 1\n    return 0\n        \nn = input()\nk = math.trunc(math.sqrt(n))\n\nans = -1\n\ni = k\nwhile ans == -1 and i >= 1:\n    x = i * i\n    if check(str(n), str(x)) == 1:\n        ans = len(str(n)) - len(str(x))\n    i -= 1\nprint ans\n"
        out = "import,math,def,check,(,a,,,b,),:,i,=,0,j,=,0,while,i,<,len,(,b,),and,j,<,len,(,a,),:,while,j,<,len,(,a,),and,a,[,j,],Error Token !"
        self.assertTrue(TestLexer.test(inp, out, 198))

    def test_random11(self):
        inp = "def f(tp):\n    nx = tp[0]\n    ax = tp[1]\n    bx = tp[2]\n    if nx == 0:\n        return [ax, bx]\n    ax = max(0, ax - nx / 2 - (nx % 2))\n    bx = max(0, bx - nx / 2)\n    return [ax, bx]\n\n[n, a, b] = map(int, raw_input().strip().split())\ns = raw_input().strip().split(\'*\')\n\nse = sorted([len(i) for i in s])\n\nc = max(a, b)\nd = min(a, b)\n\nfor i in range(len(se)):\n    k = f([se[len(se) - i - 1], c, d])\n    c = max(k[0], k[1])\n    d = min(k[0], k[1])\n    if k == (0, 0):\n        break\nprint a + b - c - d"
        out = "def,f,(,tp,),:,nx,=,tp,[,0,],ax,=,tp,[,1,],bx,=,tp,[,2,],if,nx,=,=,0,:,return,[,ax,,,bx,],ax,=,max,(,0,,,ax,-,nx,/,2,-,(,nx,Error Token %"
        self.assertTrue(TestLexer.test(inp, out, 199))
    def test_random12(self):
        inp = "int main()\n{\n    int n;\n    cin >> n;\n    pair<long long, int> s;\n    vector<pair<long long, int> > arr;\n    for (int i = 0; i < n; i ++)\n    {\n        cin >> s.first;\n        s.second = 1;\n        arr.push_back(s);\n        \n        cin >> s.first;\n        s.first ++;\n        s.second = -1;\n        arr.push_back(s);\n    }\n    \n    sort(arr.begin(), arr.end());\n    \n    long long ans[n + 1];\n    for (int i = 0; i < n + 1; i ++)\n        ans[i] = 0;\n    int t = 0;\n    for (int i = 0; i < 2 * n - 1; i ++)\n    {\n        t += arr[i].second;\n        ans[t] += arr[i + 1].first - arr[i].first;\n    }\n    \n    for (int i = 1; i < n + 1; i ++)\n    {\n        cout << ans[i] << \" \";\n    }\n    cout << endl;    \n    \n    return 0;\n}"
        out = "int,main,(,),sort,(,arr,Error Token ."
        self.assertTrue(TestLexer.test(inp, out, 200))
