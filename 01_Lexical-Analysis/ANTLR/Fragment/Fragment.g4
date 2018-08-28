lexer grammar Fragment;

fragment LOWERCASE_LETTER   :  [a-z] ;
fragment DIGIT              :  [0-9] ;

ID                 :  LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)* ;
WS                 :  [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines