// My ID: 1610852

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: PROCEDURE 'main' LP RP LCB body? RCB EOF ;

method_types: PROCEDURE | FUNCTION ;

data_types: INT | REAL | STR | BOOL;

body: SEMI;


/**
 * Built-in Functions
 */




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

// Data Types
INT : 'integer';
STR : 'string' ;
REAL: 'real'   ;
BOOL: 'boolean';

// Data Structures
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
LIT_INT : [0-9]+;
LIT_BOOL: TRUE | FALSE ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;