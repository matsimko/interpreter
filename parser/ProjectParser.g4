parser grammar ProjectParser;

options {
	tokenVocab = ProjectLexer;
}

//There needs to be EOF if the whole file should be always read (otherwise it will take the longest error-free prefix)
program: statement+ EOF;

literal:
	INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL;

statement:
	';'												# emptyStatement
	| variableType identifierList ';'				# declareVariables
	| expr ';'										# exprStatement
	| READ identifierList ';'						# readVariables
	| WRITE exprList ';'							# writeExprs
	| block											# blockStatement
	| IF '(' expr ')' statement (ELSE statement)?	# ifStatement
	| WHILE '(' expr ')' statement					# whileStatement;

block: '{' statement* '}';

identifierList: IDENTIFIER ( ',' IDENTIFIER)*;
exprList: expr ( ',' expr)*;

variableType: BOOL | INT | FLOAT | STRING;

expr:
	op = SUB expr								# unarySub
	| op = NOT expr								# logicalNot
	| expr op = (MUL | DIV | MOD) expr			# mulDivMod
	| expr op = (ADD | SUB | CONCAT) expr		# addSubConcat
	| expr op = (LT | GT) expr					# ltGt
	| expr op = (EQUAL | NOTEQUAL) expr			# equalNotEqual
	| expr op = AND expr						# logicalAnd
	| expr op = OR expr							# logicalOr
	| <assoc = right> IDENTIFIER ASSIGN expr	# assignment
	| literal									# literalExpr
	| IDENTIFIER								# variableExpr
	| '(' expr ')'								# parExpr;

