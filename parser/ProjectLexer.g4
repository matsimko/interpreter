lexer grammar ProjectLexer;

// Keywords
BOOL: 'bool';
ELSE: 'else';
FLOAT: 'float';
IF: 'if';
INT: 'int';
READ: 'read';
STRING: 'string';
WHILE: 'while';
WRITE: 'write';

// Literals
INT_LITERAL: [0-9]+; //(multiple) zeros at the beginning are allowed according to the specification
FLOAT_LITERAL: ([0-9]+ '.' [0-9]* | [0-9]* '.' [0-9]+);
BOOL_LITERAL: 'true' | 'false';
STRING_LITERAL: '"' (~["\\\r\n])* '"';

// Separators

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';

// Operators
ASSIGN: '=';
OR: '||';
AND: '&&';
EQUAL: '==';
NOT: '!';
NOTEQUAL: '!=';
LT: '<';
GT: '>';
ADD: '+';
SUB: '-';
CONCAT: '.';
MUL: '*';
DIV: '/';
MOD: '%';

// Whitespace and comments
WS: [ \t\r\n\u000C]+ -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);

// Identifiers
IDENTIFIER: Letter LetterOrDigit*;

// Fragment rules (these are just for convenience, they don't play a role in the actual lexer and parser)
fragment LetterOrDigit: Letter | [0-9];
fragment Letter: [a-zA-Z];