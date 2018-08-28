lexer grammar Final;

fragment LOWERCASE_LETTER   :  [a-z] ;
fragment DIGIT              :  [0-9] ;
fragment SIGN               :  [+-]? ;
fragment SCIENTIFIC         :  [e](SIGN)(DIGIT)+ ;
fragment DECIMAL_POINT      :  [.](DIGIT)+ ;

REAL               :  SIGN(DIGIT)+(DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC) ;
INT                :  SIGN(DIGIT)+ ;
ID                 :  LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)* ;
STRING             :  ['][^']+['] ;

WS                 :  [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines