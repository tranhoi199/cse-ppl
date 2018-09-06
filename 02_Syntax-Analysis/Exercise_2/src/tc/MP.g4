grammar MP;


options{
	language=Java;
}


program: ( var_declare | func_declare )* EOF ;


var_declare: mc_type ids_list SM ;

func_declare: mc_type ID LP (mc_type ids_list (SM mc_type ids_list)*)? RP LB body RB ;

ids_list: ID (CM ID)* ;

body: ( var_declare | stmt_assign | stmt_call | stmt_return )* ;

stmt_assign: ID EQ exp SM ;

stmt_call: func_call SM ;

stmt_return: RETURN exp SM ;

/**
 * + is lowest precendence, right associative
 * - is higher +, non-associative
 * *, / is highest precendence, left associative
 */
exp
	: operands
	| exp (MUL | DIV) exp
	| operands SUB operands
	| <assoc=right> exp ADD exp
	;

operands: (LP exp RP) | func_call | ID | INTLIT | FLOATLIT ;

func_call: ID LP (exp (CM exp)*)? RP;


mc_type: INT | FLOAT ;




/** Lexer */

// Keywords
RETURN : 'return';
FLOAT  : 'float';
INT    : 'int';

// Specific characters
LB: '{';
RB: '}';
LP: '(';
RP: ')';

SM: ';';
CM: ',';

EQ: '=';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';


FLOATLIT: INTLIT ([.][0-9]+)? ([eE][+-]? [0-9]+)? ;

INTLIT: [1-9] [0-9]* | '0';


ID: [_a-zA-Z] [_a-zA-Z0-9]* ;


WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;