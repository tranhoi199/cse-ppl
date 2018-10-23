grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: mptype EOF;

// arraytype:  primtype dimens  ;
arraytype: arraytype dimen | primtype dimen;

mptype: primtype | arraytype;

primtype: INTTYPE | FLOATTYPE; 

// dimens: dimen+;

dimen: LSB num DOTDOT num RSB;

num: SIGN? INTLIT;

INTLIT: [0-9]+ ;

INTTYPE: 'integer';

FLOATTYPE: 'real';

LSB: '[' ;

RSB: ']' ;

SIGN: '-';

DOTDOT: '..' ;

COMMA: ',' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
