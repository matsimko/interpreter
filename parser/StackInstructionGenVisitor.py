from ProjectParserVisitor import ProjectParserVisitor
from ProjectParser import ProjectParser
from Type import Type, StackTypeMap, TypeDefaultValueMap


class StackInstructionGenVisitor(ProjectParserVisitor):
    BINARY_OP_INSTRUCTIONS = {
        # these return the same type as the operands
        # (and there is potential float conversion)
        '*': 'mul',
        '/': 'div',
        '%': 'mod',
        '+': 'add',
        '-': 'sub',
        '.': 'concat',
        '&&': 'and',
        '||': 'or',
        # these return boolean
        '>': 'gt',
        '<': 'lt',
        '==': 'eq',
        '!=': 'eq', # not is added afterwards
        # assignment '=' is handled separately
    }

    BOOLEAN_BINARY_OPS = ['>', '<', '==']

    UNARY_OP_INSTRUCTIONS = {
        '-': 'uminus',
        '!': 'not',
    }

    def __init__(self) -> None:
        super().__init__()
        self.variable_types = {}
        self.instructions = []
        self.current_label = -1

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def insert_instruction(self, idx, instruction):
        self.instructions.insert(idx, instruction)

    def pop(self):
        self.add_instruction('pop')

    def itof(self):
        self.add_instruction('itof')

    def save(self, id):
        self.add_instruction(f'save {id}')

    def load(self, id):
        self.add_instruction(f'load {id}')

    def push(self, type, value):
        self.add_instruction(f'push {StackTypeMap[type]} {value}')

    def label(self, n):
        self.add_instruction(f'label {n}')

    def jmp(self, n):
        self.add_instruction(f'jmp {n}')

    def fjmp(self, n):
        self.add_instruction(f'fjmp {n}')

    def print(self, n):
        self.add_instruction(f'print {n}')

    def read(self, type):
        self.add_instruction(f'read {StackTypeMap[type]}')

    def next_label(self):
        self.current_label += 1
        return self.current_label

    def handle_binary_ops(self, ctx):
        type1 = self.visit(ctx.expr(0))
        type2 = self.visit(ctx.expr(1))
        # it doesn't what operation it is because types check has already been done
        if type1 == Type.INT and type2 == Type.FLOAT:
            type1 = Type.FLOAT
            self.insert_instruction(len(self.instructions) - 1, 'itof')
        elif type1 == Type.FLOAT and type2 == Type.INT:
            self.itof()

        instruction = self.BINARY_OP_INSTRUCTIONS[ctx.op.text]
        self.add_instruction(instruction)

        if ctx.op.text in self.BOOLEAN_BINARY_OPS:
            return Type.BOOL
        else:
            return type1

    def handle_unary_ops(self, ctx):
        type = self.visit(ctx.expr())
        instruction = self.UNARY_OP_INSTRUCTIONS[ctx.op.text]
        self.add_instruction(instruction)
        return type

    # Visit a parse tree produced by ProjectParser#program.
    def visitProgram(self, ctx: ProjectParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#literal.
    def visitLiteral(self, ctx: ProjectParser.LiteralContext):
        if ctx.BOOL_LITERAL():
            return Type.BOOL, ctx.BOOL_LITERAL().getText()
        elif ctx.INT_LITERAL():
            return Type.INT, ctx.INT_LITERAL().getText()
        elif ctx.FLOAT_LITERAL():
            return Type.FLOAT, ctx.FLOAT_LITERAL().getText()
        elif ctx.STRING_LITERAL():
            return Type.STRING, ctx.STRING_LITERAL().getText()

    # Visit a parse tree produced by ProjectParser#emptyStatement.
    def visitEmptyStatement(self, ctx: ProjectParser.EmptyStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#declareVariables.
    def visitDeclareVariables(self, ctx: ProjectParser.DeclareVariablesContext):
        type = self.visit(ctx.variableType())
        for identifier in ctx.identifierList().IDENTIFIER():
            self.variable_types[identifier.getText()] = type
            self.push(type, TypeDefaultValueMap[type])
            self.save(identifier.getText())

    # Visit a parse tree produced by ProjectParser#exprStatement.
    def visitExprStatement(self, ctx: ProjectParser.ExprStatementContext):
        self.visitChildren(ctx)
        self.pop()

    # Visit a parse tree produced by ProjectParser#readVariables.
    def visitReadVariables(self, ctx: ProjectParser.ReadVariablesContext):
        for identifier in ctx.identifierList().IDENTIFIER():
            self.read(self.variable_types[identifier.getText()])
            self.save(identifier.getText())

    # Visit a parse tree produced by ProjectParser#writeExprs.
    def visitWriteExprs(self, ctx: ProjectParser.WriteExprsContext):
        for expr in ctx.exprList().expr():
            self.visit(expr)
        self.print(len(ctx.exprList().expr()))

    # Visit a parse tree produced by ProjectParser#blockStatement.
    def visitBlockStatement(self, ctx: ProjectParser.BlockStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#ifStatement.
    def visitIfStatement(self, ctx: ProjectParser.IfStatementContext):
        self.visit(ctx.expr())
        label_else = self.next_label()
        label_end = self.next_label()
        self.fjmp(label_else)

        self.visit(ctx.statement(0))
        self.jmp(label_end)

        self.label(label_else)
        if (ctx.statement(1)):  # if there is "else"
            self.visit(ctx.statement(1))

        self.label(label_end)

    # Visit a parse tree produced by ProjectParser#whileStatement.
    def visitWhileStatement(self, ctx: ProjectParser.WhileStatementContext):
        label_start = self.next_label()
        label_end = self.next_label()
        self.label(label_start)
        self.visit(ctx.expr())
        self.fjmp(label_end)
        self.visit(ctx.statement())
        self.jmp(label_start)
        self.label(label_end)

    # Visit a parse tree produced by ProjectParser#block.
    def visitBlock(self, ctx: ProjectParser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#identifierList.
    def visitIdentifierList(self, ctx: ProjectParser.IdentifierListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#exprList.
    # def visitExprList(self, ctx:ProjectParser.ExprListContext):
    #     return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#variableType.
    def visitVariableType(self, ctx: ProjectParser.VariableTypeContext):
        if ctx.BOOL():
            return Type.BOOL
        elif ctx.INT():
            return Type.INT
        elif ctx.FLOAT():
            return Type.FLOAT
        elif ctx.STRING():
            return Type.STRING

    # Visit a parse tree produced by ProjectParser#mulDivMod.
    def visitMulDivMod(self, ctx: ProjectParser.MulDivModContext):
        return self.handle_binary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#variableExpr.
    def visitVariableExpr(self, ctx: ProjectParser.VariableExprContext):
        id = ctx.IDENTIFIER().getText()
        self.load(id)
        return self.variable_types[id]

    # Visit a parse tree produced by ProjectParser#parExpr.
    def visitParExpr(self, ctx: ProjectParser.ParExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#logicalNot.
    def visitLogicalNot(self, ctx: ProjectParser.LogicalNotContext):
        return self.handle_unary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#equalNotEqual.
    def visitEqualNotEqual(self, ctx: ProjectParser.EqualNotEqualContext):
        self.handle_binary_ops(ctx)
        if ctx.NOTEQUAL():
            self.add_instruction('not')
        return Type.BOOL

    # Visit a parse tree produced by ProjectParser#addSubConcat.
    def visitAddSubConcat(self, ctx: ProjectParser.AddSubConcatContext):
        return self.handle_binary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#assignment.
    def visitAssignment(self, ctx: ProjectParser.AssignmentContext):
        expr_type = self.visit(ctx.expr())
        id = ctx.IDENTIFIER().getText()
        var_type = self.variable_types[id]
        if var_type == Type.FLOAT and expr_type == Type.INT:
            self.itof()
        self.save(id)
        self.load(id)
        return var_type

    # Visit a parse tree produced by ProjectParser#literalExpr.
    def visitLiteralExpr(self, ctx: ProjectParser.LiteralExprContext):
        type, value = self.visit(ctx.literal())
        self.push(type, value)
        return type

    # Visit a parse tree produced by ProjectParser#ltGt.
    def visitLtGt(self, ctx: ProjectParser.LtGtContext):
        return self.handle_binary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#logicalAnd.
    def visitLogicalAnd(self, ctx: ProjectParser.LogicalAndContext):
        return self.handle_binary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#unarySub.
    def visitUnarySub(self, ctx: ProjectParser.UnarySubContext):
        return self.handle_unary_ops(ctx)

    # Visit a parse tree produced by ProjectParser#logicalOr.
    def visitLogicalOr(self, ctx: ProjectParser.LogicalOrContext):
        return self.handle_binary_ops(ctx)
