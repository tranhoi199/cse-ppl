grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;
body: funcall SEMI;
exp: funcall | INTLIT ;
funcall: ID LB exp? RB ;

fragment LETTER     : [a-z] ;
fragment DIGIT      : [0-9] ;
fragment SIGN       : [+-] ;

INTTYPE: 'int' ;
VOIDTYPE: 'void'  ;

ID     : LETTER ( LETTER | DIGIT )* ;
REAL   : SIGN? DIGIT+ ([.]DIGIT+)? ([e]SIGN? DIGIT+)? ;
INTLIT : [0-9]+;
STRING : ['] ((~[']) | (['][']))* ['];

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;