grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (variables_declaration | function_declaration)* EOF ;

// Variable declaration
variables_declaration: variables SM ;

// Function declaration
function_declaration: mc_type ID LP (variables (SM variables)*)? RP LB body RB ;

body: ( variables_declaration | stmt_assign | stmt_call | stmt_return )* ;

variables: mc_type ID (CM ID)* ;

stmt_assign: ID EQ exp SM ;

stmt_call: func_call SM ;

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


FLOATLIT  : INTLIT ([.][0-9]+)? ([eE][+-]? [0-9]+)? ;

INTLIT    : [1-9] [0-9]* | '0';

ID        : [_a-zA-Z] [_a-zA-Z0-9]* ;


WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;