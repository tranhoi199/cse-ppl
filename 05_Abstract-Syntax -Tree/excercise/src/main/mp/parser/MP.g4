grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}





INTLIT: [0-9]+ ;

COMMA: ',';

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COLON: ':' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

PROCEDURE: P R O C E D U R E;

FUNCTION: F U N C T I O N;

BEGIN: B E G I N;

END: E N D;

INTTYPE: I N T E G E R;

FLOATTYPE: F L O A T;

ID: [a-zA-Z]+ ;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

ERROR_CHAR: .;
