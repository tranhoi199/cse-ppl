// My ID: 1610852

grammar MP;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


/** 
 * 2 Program Structure
 */
program: (var_declare | func_declare | proc_declare)* EOF ;

// 2.1 Variable declaration
var_declare: VAR (ids_list_with_type SEMI)+;

//2.2 Function declaration
func_declare: FUNCTION ID LP params_list? RP COLON data_types SEMI var_declare? compound_stmt ;

// 2.3 Procedure declaration
proc_declare: PROCEDURE ID LP params_list? RP SEMI var_declare? compound_stmt ;





/** 
 * 6 Statements and Control Flow
 */
stmt
	: compound_stmt
	| if_stmt 
	| while_stmt | for_stmt | with_stmt
	| brk_stmt | cont_stmt | ret_stmt
	| assign_stmt
	| call_stmt
	;

// Assignment
assign_stmt: assign_lhs SEMI;

assign_lhs: exp ASSIGN assign ;

assign: <assoc=right> assign ASSIGN assign | exp ;

// Flow
if_stmt: IF exp_bool THEN stmt (ELSE stmt)?;

// Loop
while_stmt: WHILE exp_bool DO stmt ;

for_stmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt ;

with_stmt: WITH (ids_list_with_type SEMI)+ DO stmt ;

// Stop
brk_stmt: BREAK SEMI ;

cont_stmt: CONTINUE SEMI ;

ret_stmt: ret_stmt_func | ret_stmt_proc ;

ret_stmt_proc: RETURN SEMI ;

ret_stmt_func: RETURN exp SEMI ;

// Call
call_stmt: call_exp SEMI;

// Complex
compound_stmt: BEGIN stmts_list? END ;






/**
 * 7 Built-in Functions 
 */




/** 
 * 5 Expressions
 */
exp_bool: exp;

exp_int: exp;

exp_real: exp;

exp_str: exp;

exp
	: operands
	| exp LSB exp RSB
	| <assoc=right> (NOT | SUB) exp
	| exp ( DIV | MUL | MOD | DIV_INT | AND ) exp
	| exp ( ADD | SUB | OR ) exp
	| exp ( EQ | NEQ | GT | LT | GTE | LTE ) exp
	| exp ( op_and_then | op_or_else ) exp
	;

operands
	: literal
	| ID
	| call_exp
	| LP exp RP
	;

call_exp: ID LP exps_list? RP;


/**
 * Utilities
 */
params_list: ids_list_with_type (SEMI ids_list_with_type)*;

ids_list_with_type: ids_list COLON data_types ;

ids_list: ID (COMMA ID)* ;

exps_list: exp (COMMA exp)* ;

stmts_list: stmt+ ;

method_types: PROCEDURE | FUNCTION ;

data_types: primitive_types | compound_types;

compound_types: ARRAY LSB INTEGER_LITERAL DOTDOT INTEGER_LITERAL RSB OF primitive_types ;

primitive_types: INTEGER | REAL | STRING | BOOLEAN;

op_and_then: AND THEN ;

op_or_else: OR ELSE ;

literal
	: INTEGER_LITERAL
	| REAL_LITERAL
	| STRING_LITERAL
	| boolean_literal
	;


/** Lexers Declaration */

/**
 * Keywords
 */

// Methods
FUNCTION : F U N C T I O N ;
PROCEDURE: P R O C E D U R E ;

// Scope
BEGIN: B E G I N ;
END  : E N D ;

// Value
TRUE : T R U E ;
FALSE: F A L S E ;

// Flow Statement
IF  : I F ;
THEN: T H E N ;
ELSE: E L S E ;

// Loop Statement
FOR   : F O R ;
WHILE : W H I L E ;
WITH  : W I T H ;
DO    : D O ;
TO    : T O ;
DOWNTO: D O W N T O ;

// Stop Statement
RETURN  : R E T U R N ;
BREAK   : B R E A K ;
CONTINUE: C O N T I N U E ;

// Primitive Types
INTEGER : I N T E G E R ;
STRING : S T R I N G ;
REAL: R E A L ;
BOOLEAN: B O O L E A N ;

// Compound Types
ARRAY: A R R A Y ;

// Others
VAR: V A R ;
OF: O F ;


/**
 * Operators
 */

DIV_INT: D I V ;
MOD: M O D;
NOT: N O T;
AND: A N D;
OR : O R  ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ASSIGN: ':=';
LTE: '<=';
GTE: '>=';
NEQ: '<>';
EQ : '=' ;
LT : '<' ;
GT : '>' ;



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
DOTDOT: '..'; // Dot Dot should be before Dot
DOT: '.';





// Domain Values
boolean_literal: TRUE | FALSE ;

STRING_LITERAL: '"' STR_CHAR* '"';


REAL_LITERAL
	: DIGIT+ DOT DIGIT* // 12.(05)
	| DIGIT* DOT DIGIT+ EXPONENT? // (12).05(e-4)
	| DIGIT+ EXPONENT // 12e-5
	;


// Integer should be after Real
INTEGER_LITERAL : [1-9][0-9]* | '0';


fragment EXPONENT: [eE] SIGN? DIGIT+ ;

fragment DIGIT: [0-9] ;

fragment SIGN: [+-] ;




ID: [_a-zA-Z][_a-zA-Z0-9]* ;



// Skip comments
BLOCK_COMMENT: ('(*' .*? '*)' | LCB .*? RCB) -> skip ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;



// Skip spaces, tabs, newlines
WS : [ \t\r\n\f]+ -> skip ; 




UNCLOSE_STRING: '"' STR_CHAR*
	{
		y = str(self.text)
		raise UncloseString(y[1:])
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;


fragment STR_CHAR: ESC_SEQ | ~["\\] ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;







fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];