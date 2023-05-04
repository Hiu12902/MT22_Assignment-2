// 2013153
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF;
decllist: decl decllist | decl;
decl: vardcl | funcdcl;

atomic_typ: BOOLEAN | INTEGER | FLOAT | STRING ;
typ: atomic_typ | AUTO | arr_typ;

//--------------------DECLARATION--------------------
vardcl: ((idlist COLON typ) | varinit) SEMI;
varinit: ID COMMA varinit COMMA expr |  ID COLON typ EQ expr;
// varele:;
idlist: ID COMMA idlist | ID;

funcdcl: ID COLON FUNCTION (typ | VOID) LB paramlist RB inheritsub? funcbody;
// funcproto: ;
inheritsub: INHERIT ID;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: INHERIT? OUT? ID COLON typ;
funcbody: blockstate | emptyblock;
emptyblock: CUR_LB CUR_RB;

//--------------------EXPRESSION--------------------
// callindex: ID SQU_LB exprlist SQU_RB;
callindex: ID SQU_LB exprprime SQU_RB;
callfunc: ID LB exprlist RB;

expr: expr1 DBL_COLON expr1 | expr1;
expr1: expr2 (DBL_EQ | UEQ | MOR | LESS | MOR_EQ | LESS_EQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: EXCLAM expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: LB expr RB | ID | INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | callfunc | callindex | indexarr;

// expr: strexpr | relexpr;

// strexpr: strexpr1 DBL_COLON strexpr1 | strexpr1;
// strexpr1: ID | callfunc | callindex | STRINGLIT;

// relexpr: relexpr1 | relexpr2;
// relexpr1: relexpr11 (DBL_EQ | UEQ) relexpr11 | relexpr11;
// relexpr11: ID | callfunc | callindex | intexpr | boolexpr;
// relexpr2: relexpr21 (MOR | LESS | MOR_EQ | LESS_EQ) relexpr21 | relexpr21;
// relexpr21: ID | callfunc | callindex | intexpr | floatexpr;

// boolexpr: boolexpr (AND | OR) boolexpr1 | boolexpr1;
// boolexpr1: EXCLAM boolexpr1 | boolexpr2;
// boolexpr2: BOOLEANLIT | ID | callfunc | callindex;

// intexpr: intexpr (ADD | SUB) intexpr1 | intexpr1;
// intexpr1: intexpr1 (MUL | DIV | MOD) intexpr2 | intexpr2;
// intexpr2: SUB intexpr2 | intexpr3;
// intexpr3: INTLIT | ID | callfunc | callindex;

// floatexpr: floatexpr (ADD | SUB) floatexpr1 | floatexpr1;
// floatexpr1: floatexpr1 (MUL | DIV) floatexpr2 | floatexpr2;
// floatexpr2: SUB floatexpr2 | floatexpr3;
// floatexpr3: FLOATLIT | ID | callfunc | callindex;

//--------------------STATEMENTS--------------------
stmt: (assignstate | ifstate | forstate | whilestate | dowhilestate | breakstate | continuestate | returnstate | blockstate | callstate);
statelist: stateprime | ;
// stateprime: stateunit stateprime | stateunit;
stateprime: (stmt|vardcl) stateprime |;

// assignstate: elelist SEMI;
// elelist : scalarvar COMMA elelist COMMA expr | scalarvar EQ expr;
// element: scalarvar EQ expr;

assignstate: scalarvar EQ expr SEMI;
scalarvar: ID | callindex;

ifstate: IF LB expr RB stmt (ELSE stmt)?;
// ifstate: IF LB relexpr RB stmt (ELSE stmt)?;

// forstate: FOR LB scalarvar EQ expr COMMA expr COMMA expr RB statelist;
forstate: FOR LB scalarvar EQ expr COMMA expr COMMA expr RB stmt;

// forbody: scalarvar EQ expr COMMA expr COMMA expr;
// forbody: scalarvar EQ intexpr COMMA relexpr intexpr;

// whilestate: WHILE LB expr RB statelist; 
whilestate: WHILE LB expr RB stmt; 
// whilestate: WHILE LB relexpr RB statelist; 

// dowhilestate: DO blockstate WHILE LB relexpr RB SEMI;
dowhilestate: DO blockstate WHILE LB expr RB SEMI;

breakstate: BREAK SEMI;

continuestate: CONTINUE SEMI;

returnstate: RETURN (expr)? SEMI;

callstate: ID LB exprlist RB SEMI;

blockstate: CUR_LB (statelist) CUR_RB;
// vardcllist: vardcl vardcllist | vardcl;

//--------------------COMMENT-------------------- 
comments: (SL_CMT | MUL_CMT)*;
SL_CMT: '//' ~[\n]* ('\n' | EOF) -> skip;
MUL_CMT: '/*' .*? '*/' -> skip;

//--------------------LITERAL--------------------
INTLIT: [0] | NON_ZERO DIGIT* (UNDERSCORE DIGIT+)* {self.text = self.text.replace("_", "")};
FLOATLIT: INTLIT (DOT DIGIT*)? ([eE] [-+]? DIGIT+)? {self.text = self.text.replace("_", "")}| (DOT DIGIT* [eE] [-+]? DIGIT+) ;
BOOLEANLIT: FALSE | TRUE;
STRINGLIT: '"' STRINGCHAR* '"' {self.text = self.text[1:-1]};
fragment STRINGCHAR: ESC | SAFECODEPOINT;
fragment ESC: '\\' (["\\/bfnrt]);
// fragment SAFECODEPOINT: ~ (["] | [\\] | [\n] | [\r] | [\u0000-\u001F]);
fragment SAFECODEPOINT: ~[\r\n\\"];

indexarr: CUR_LB exprlist CUR_RB;
// exprlist: expr COMMA exprlist | expr;
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;

//--------------------TYPE--------------------

arr_typ: ARRAY SQU_LB intlist SQU_RB OF atomic_typ;
// dimensions: SQU_LB intlist SQU_RB;
intlist: INTLIT COMMA intlist | INTLIT;

//--------------------/KEYWORD--------------------
AUTO: 'auto';
BREAK: 'break'; 
BOOLEAN: 'boolean'; 
DO: 'do'; 
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for'; 
FUNCTION: 'function'; 
IF: 'if';
INTEGER: 'integer'; 
RETURN: 'return'; 
STRING: 'string'; 
TRUE: 'true'; 
WHILE: 'while';
VOID: 'void'; 
OUT: 'out'; 
CONTINUE: 'continue'; 
OF: 'of'; 
INHERIT: 'inherit';
ARRAY: 'array';

//--------------------OPERATOR--------------------
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
AND: '&&';
OR: '||';
DBL_EQ: '==';
UEQ: '!=';
LESS: '<';
MOR: '>';
LESS_EQ: '<=';
MOR_EQ: '>=';
EXCLAM: '!';
DBL_COLON: '::';

//--------------------SEPERATOR--------------------
LB: '(';
RB: ')';
CUR_LB: '{';
CUR_RB: '}';
SQU_LB: '[';
SQU_RB: ']';
EQ: '=';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';

//--------------------WHITESPACE--------------------
WS: (' '| '\t' | '\b' | '\f' | '\r' | '\n' )+ -> skip ;

//--------------------IDENTIFIER--------------------
ID: (CHAR | UNDERSCORE) (CHAR | DIGIT | UNDERSCORE)*;
fragment CHAR: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: [_];
fragment NON_ZERO: [1-9];

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STRINGCHAR* (EOF | [\n\r]) 
{
	if (self.text[-1] in ['\n', '\r']): 
		raise UncloseString(self.text[1:-1]) 
	else: 
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' STRINGCHAR* ('\\' ~[bfnrt'\\"]) 
{
	raise IllegalEscape(self.text[1:])
};
// UNTERMINATED_COMMENT: '/*' .*? (EOF)
// {
// 	raise UnterminatedComment(self.text[2:])
// };