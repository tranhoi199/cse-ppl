grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (variables_declaration | function_declaration)*;

// Variable declaration
variables_declaration: variables SM ;

variables: mc_type ID (CM ID)* ;

// Function declaration
function_declaration: mc_type ID LP (variables (SM variables)*)? RP LB body RP ;

body: (stmt_assign | stmt_call | stmt_return )* ;

stmt_assign: ID EQ exp SM;

stmt_call: ID LP (exp (CM exp)*)? RP SM ;

stmt_return: RETURN exp SM ;

/**
 * + is lowest precendence, right associative
 * - is higher +, non-associative
 * *, / is highest precendence, left associative
 */
exp : <assoc=right> exp ADD exp
	| operands SUB operands
	| exp (MUL | DIV) exp
	| operands
	;

operands: (LP exp RP) | stmt_call | ID | INTLIT | FLOATLIT ;

mc_type: INT | FLOAT;


// Lexer
fragment LETTER: [a-zA-Z];

ID: LETTER (LETTER | [0-9_])* ;

INTLIT: [0-9]+;
FLOATLIT: [0-9]+;

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

RETURN: 'return';
FLOAT: 'float';
INT: 'int';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;