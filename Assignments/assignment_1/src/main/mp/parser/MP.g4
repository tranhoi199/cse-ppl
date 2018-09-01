// My ID: 1610852

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}




/** 
 * 2 Program Structure
 */
program: (var_def | func_def | proc_def)* EOF ;

// 2.1 Variable declaration
var_def: VAR (ids_list_with_type SEMI)+;

//2.2 Function declaration
func_def: FUNCTION ID LP params_list? RP COLON data_types SEMI var_def compound_stmt ;

// 2.3 Procedure declaration
proc_def: PROCEDURE ID LP params_list? RP SEMI var_def compound_stmt ;





/** 
 * 6 Statements and Control Flow 
 */
stmts
	: compound_stmt
	| if_stmt 
	| while_stmt | for_stmt | with_stmt
	| brk_stmt | cont_stmt | ret_stmt 
	| assign_stmt 
	| call_stmt
	;

// Assign
assign_stmt: <assoc=right> exp OP_ASS exp SEMI;

// Flow
if_stmt: IF exp_bool THEN stmts (ELSE stmts)?;

// Loop
while_stmt: WHILE exp_bool DO stmts ;

for_stmt: FOR ID OP_ASS exp (TO | DOWNTO) exp DO stmts ;

with_stmt: WITH (ids_list_with_type SEMI)+ DO stmts ;

// Stop
brk_stmt: BREAK SEMI ;

cont_stmt: CONTINUE SEMI ;

ret_stmt: SEMI;

// Call
call_stmt: ID LP exps_list? RP SEMI;

// Complex
compound_stmt: BEGIN stmts* END ;






/**
 * 7 Built-in Functions 
 */




/** 
 * 5 Expressions
 */
exp_bool: ;

exp: ;



/**
 * Utilities
 */
params_list: ids_list_with_type (SEMI ids_list_with_type)*;

ids_list_with_type: ids_list COLON data_types ;

ids_list: ID (COMMA ID)? ;

exps_list: exp (COMMA exp)? ;

method_types: PROCEDURE | FUNCTION ;

data_types: primitive_types | compound_types;

compound_types: ARRAY LSB LIT_INT DOTDOT LIT_INT RSB OF primitive_types ;

primitive_types: INT | REAL | STR | BOOL;






/** Lexers Declaration */

/**
 * Keywords
 */

// Methods
FUNCTION : 'function' ;
PROCEDURE: 'procedure';

// Scope
BEGIN: 'begin';
END  : 'end'  ;

// Value
TRUE : 'true' ;
FALSE: 'false';

// Flow Statement
IF  : 'if'  ;
THEN: 'then';
ELSE: 'else';

// Loop Statement
FOR   : 'for'   ;
WHILE : 'while' ;
WITH  : 'with'  ;
DO    : 'do'    ;
TO    : 'to'    ;
DOWNTO: 'downto';

// Stop Statement
RETURN  : 'return'  ;
BREAK   : 'break'   ;
CONTINUE: 'continue';

// Primitive Types
INT : 'integer';
STR : 'string' ;
REAL: 'real'   ;
BOOL: 'boolean';

// Compound Types
ARRAY: 'array';

// Others
VAR: 'var';
OF: 'of';


/**
 * Operators
 * Please use name with prefix OP_
 */
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';

OP_DIV_INT: 'div';
OP_MOD: 'mod';
OP_NOT: 'not';
OP_AND: 'and';
OP_OR : 'or' ;

OP_ASS: ':=';
OP_LTE: '<=';
OP_GTE: '>=';
OP_NEQ: '<>';
OP_EQ : '=' ;
OP_LT : '<' ;
OP_GT : '>' ;



/**
 * Specific characters
 * Please search name for characters here
 * https://www.compart.com
 */

LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

SEMI: ';'; // Semicolon
COMMA: ','; // Comma
COLON: ':'; // Colon
DOT: '.';
DOTDOT: '..';



ID: [a-zA-Z]+ ;


// Domain Values
LIT_INT : [+-]?[0-9]+;
LIT_BOOL: TRUE | FALSE ;


// Comments
BLOCK_COMMENT: '(*' .*? '*)' | LCB .*? RCB -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;



WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;