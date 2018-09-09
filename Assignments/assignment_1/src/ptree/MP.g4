// My ID: 1610852

grammar MP;

options{
	language=Java;
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

ret_stmt: RETURN SEMI;

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

exp_int: ;

exp_real: ;

exp_str: ;

exp
	: operands
	| <assoc=right> OP_NOT exp
	| exp ( OP_DIV | OP_MUL | OP_MOD | OP_DIV_INT | OP_AND ) exp
	| exp ( OP_ADD | OP_SUB | OP_OR ) exp
	| operands ( OP_EQ | OP_NEQ | OP_GT | OP_LT | OP_GTE | OP_LTE ) operands
	| exp ( OP_AND_THEN | OP_OR_ELSE ) exp
	;

operands
	: LP exp RP
	| LIT_STR | LIT_REAL | LIT_INT | LIT_BOOL
	;

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
INT : I N T E G E R ;
STR : S T R I N G ;
REAL: R E A L ;
BOOL: B O O L E A N ;

// Compound Types
ARRAY: A R R A Y ;

// Others
VAR: V A R ;
OF: O F ;


/**
 * Operators
 * Please use name with prefix OP_
 */
OP_AND_THEN: A N D ' ' T H E N;
OP_OR_ELSE : O R ' ' E L S E ;

OP_DIV_INT: D I V ;
OP_MOD: M O D;
OP_NOT: N O T;
OP_AND: A N D;
OP_OR : O R  ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';

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
DOTDOT: '..'; // Dot Dot should be before Dot
DOT: '.';





// Domain Values
LIT_BOOL: TRUE | FALSE ;

LIT_STR: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"'] )* '"';

LIT_REAL
	: DIGIT+ DOT DIGIT* // 12.(05)
	| DIGIT* DOT DIGIT+ EXPONENT? // (12).05(e-4)
	| DIGIT+ EXPONENT // 12e-5
	;

// Integer should be after Real
LIT_INT : [1-9][0-9]* | '0';

fragment EXPONENT: [eE] [+-]? DIGIT+ ;
fragment DIGIT: [0-9] ;



ID: [_a-zA-Z][_a-zA-Z0-9]* ;



// Skip comments
BLOCK_COMMENT: ('(*' .*? '*)' | LCB .*? RCB) -> skip ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f]+ -> skip ; 


UNCLOSE_STRING: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"'] )*
	{
	}
	;

ILLEGAL_ESCAPE: '"' ('\\' ~[btnfr"'\\] | ~'\\')* '"'
	{
	}
	;


ERROR_CHAR: .
	{
	}
	;



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