from calendar import c
from cmath import exp
from msilib.schema import Error
from ProjectParser import ProjectParser
from ProjectParserListener import ProjectParserListener
from Type import Type
from Errors import errors


class TypeCheckingListener(ProjectParserListener):

    def __init__(self):
        self.ctx_types = {}  # contains types set by each context of the tree
        self.variable_types = {}  # contains types of declared variables

    def handle_if_already_error(self, parent_ctx, *child_contexts):
        for ctx in child_contexts:
            if self.ctx_types[ctx] == Type.ERROR:
                self.ctx_types[parent_ctx] = Type.ERROR
                return True
        return False

    def handle_float_int_ops(self, ctx):  # for binary operations only
        expr1_ctx = ctx.expr(0)
        expr2_ctx = ctx.expr(1)
        if self.handle_if_already_error(ctx, expr1_ctx, expr2_ctx):
            return

        type1 = self.ctx_types[expr1_ctx]
        type2 = self.ctx_types[expr2_ctx]
        if (type1 == Type.FLOAT and type2 == Type.INT or
                type1 == Type.INT and type2 == Type.FLOAT or
                type1 == Type.FLOAT and type2 == Type.FLOAT):
            self.ctx_types[ctx] = Type.FLOAT
        elif (type1 == Type.INT and type2 == Type.INT):
            self.ctx_types[ctx] = Type.INT
        else:
            self.ctx_types[ctx] = Type.ERROR
            allowed_types = '[float, float], [int, int], [float, int] or [int, float]'
            errors.add(
                ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: {allowed_types}, but got [{type1}, {type2}]')

    def handle_logical_ops(self, ctx):  # for binary operations only
        expr1_ctx = ctx.expr(0)
        expr2_ctx = ctx.expr(1)
        if self.handle_if_already_error(ctx, expr1_ctx, expr2_ctx):
            return

        type1 = self.ctx_types[expr1_ctx]
        type2 = self.ctx_types[expr2_ctx]
        if type1 == Type.BOOL and type2 == Type.BOOL:
            self.ctx_types[ctx] = Type.BOOL
        else:
            errors.add(
                ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: [bool, bool], but got: [{type1}, {type2}]')
            self.ctx_types[ctx] = Type.ERROR

    # def exitProgram(self, ctx: ProjectParser.ProgramContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#literal.

    def exitLiteral(self, ctx: ProjectParser.LiteralContext):
        if ctx.BOOL_LITERAL():
            self.ctx_types[ctx] = Type.BOOL
        elif ctx.INT_LITERAL():
            self.ctx_types[ctx] = Type.INT
        elif ctx.FLOAT_LITERAL():
            self.ctx_types[ctx] = Type.FLOAT
        elif ctx.STRING_LITERAL():
            self.ctx_types[ctx] = Type.STRING

        pass

    # def exitEmptyStatement(self, ctx: ProjectParser.EmptyStatementContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#declareVariables.
    def exitDeclareVariables(self, ctx: ProjectParser.DeclareVariablesContext):
        type = self.ctx_types[ctx.variableType()]
        for identifier in ctx.identifierList().IDENTIFIER():
            id = identifier.getText()
            if id in self.variable_types:
                errors.add(identifier, f'Variable {id} was already declared')
            self.variable_types[id] = type
        pass

    # def exitExprStatement(self, ctx: ProjectParser.ExprStatementContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#readVariables.
    def exitReadVariables(self, ctx: ProjectParser.ReadVariablesContext):
        for identifier in ctx.identifierList().IDENTIFIER():
            if identifier.getText() not in self.variable_types:
                errors.add(identifier,
                           f'Variable {identifier.getText()} was not declared before usage')
                # self.ctx_types[ctx] = Type.ERROR # I'm not checking errors of statements anyway, so no need to add it here
                return
        pass

    # def exitWriteExpr(self, ctx: ProjectParser.WriteExprsContext):
    #     pass

    # def exitBlockStatement(self, ctx: ProjectParser.BlockStatementContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#ifStatement.
    def exitIfStatement(self, ctx: ProjectParser.IfStatementContext):
        # I don't check for statements, because their errors don't not conflict with the expr
        if self.handle_if_already_error(ctx, ctx.expr()):
            return

        expr_type = self.ctx_types[ctx.expr()]
        if expr_type != Type.BOOL:
            errors.add(ctx.expr(
            ).start, f'Expression in if statement must be of type bool, but got: {expr_type}')
            # self.ctx_types[ctx] = Type.ERROR # I'm not checking errors of statements anyway, so no need to add it here

        pass

    # Exit a parse tree produced by ProjectParser#whileStatement.
    def exitWhileStatement(self, ctx: ProjectParser.WhileStatementContext):
        if self.handle_if_already_error(ctx, ctx.expr()):
            return

        expr_type = self.ctx_types[ctx.expr()]
        if expr_type != Type.BOOL:
            errors.add(ctx.expr(
            ).start, f'Expression in while statement must be of type bool, but got: {expr_type}')
            # self.ctx_types[ctx] = Type.ERROR # I'm not checking errors of statements anyway, so no need to add it here

    # Exit a parse tree produced by ProjectParser#block.
    # def exitBlock(self, ctx: ProjectParser.BlockContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#identifierList.
    # def exitIdentifierList(self, ctx: ProjectParser.IdentifierListContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#exprList.
    # def exitExprList(self, ctx: ProjectParser.ExprListContext):
    #     pass

    # Exit a parse tree produced by ProjectParser#variableType.
    def exitVariableType(self, ctx: ProjectParser.VariableTypeContext):
        if ctx.BOOL():
            self.ctx_types[ctx] = Type.BOOL
        elif ctx.INT():
            self.ctx_types[ctx] = Type.INT
        elif ctx.FLOAT():
            self.ctx_types[ctx] = Type.FLOAT
        elif ctx.STRING():
            self.ctx_types[ctx] = Type.STRING

    # Exit a parse tree produced by ProjectParser#mulDivMod.
    def exitMulDivMod(self, ctx: ProjectParser.MulDivModContext):
        if ctx.MOD():
            if self.handle_if_already_error(ctx, ctx.expr(0), ctx.expr(1)):
                return
            type1 = self.ctx_types[ctx.expr(0)]
            type2 = self.ctx_types[ctx.expr(1)]
            if type1 == Type.INT and type2 == Type.INT:
                self.ctx_types[ctx] = Type.INT
            else:
                errors.add(
                    ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: [int, int], but got [{type1}, {type2}]')
                self.ctx_types[ctx] = Type.ERROR
        else:
            self.handle_float_int_ops(ctx)

    # Exit a parse tree produced by ProjectParser#variableExpr.
    def exitVariableExpr(self, ctx: ProjectParser.VariableExprContext):
        var = ctx.IDENTIFIER().getText()
        if var not in self.variable_types:
            errors.add(ctx.IDENTIFIER(),
                       f'Variable {var} was not declared before usage')
            self.ctx_types[ctx] = Type.ERROR
        else:
            self.ctx_types[ctx] = self.variable_types[var]

    # Exit a parse tree produced by ProjectParser#parExpr.
    def exitParExpr(self, ctx: ProjectParser.ParExprContext):
        self.ctx_types[ctx] = self.ctx_types[ctx.expr()]

    # Exit a parse tree produced by ProjectParser#logicalNot.
    def exitLogicalNot(self, ctx: ProjectParser.LogicalNotContext):
        if self.handle_if_already_error(ctx, ctx.expr()):
            return
        expr_type = self.ctx_types[ctx.expr()]
        if expr_type != Type.BOOL:
            errors.add(ctx.expr(
            ).start, f'Operation "{ctx.NOT().getText()}" expected expression of type bool, but got: {expr_type}')
            self.ctx_types[ctx] = Type.ERROR
        else:
            self.ctx_types[ctx] = Type.BOOL

    # Exit a parse tree produced by ProjectParser#equalNotEqual.
    def exitEqualNotEqual(self, ctx: ProjectParser.EqualNotEqualContext):
        expr1_ctx = ctx.expr(0)
        expr2_ctx = ctx.expr(1)
        if self.handle_if_already_error(ctx, expr1_ctx, expr2_ctx):
            return

        type1 = self.ctx_types[expr1_ctx]
        type2 = self.ctx_types[expr2_ctx]

        if ((type1 == type2 and type1 in [Type.INT, Type.FLOAT, Type.STRING]) or
                type1 == Type.FLOAT and type2 == Type.INT or
                type1 == Type.INT and type2 == Type.FLOAT):
            self.ctx_types[ctx] = Type.BOOL

        else:
            allowed_types = '[int, int], [float, float], or [string, string]'
            errors.add(
                ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: {allowed_types}, but got: [{type1}, {type2}]')
            self.ctx_types[ctx] = Type.ERROR

    # Exit a parse tree produced by ProjectParser#addSubConcat.
    def exitAddSubConcat(self, ctx: ProjectParser.AddSubConcatContext):
        if ctx.CONCAT():
            if self.handle_if_already_error(ctx, ctx.expr(0), ctx.expr(1)):
                return
            type1 = self.ctx_types[ctx.expr(0)]
            type2 = self.ctx_types[ctx.expr(1)]
            if type1 == Type.STRING and type2 == Type.STRING:
                self.ctx_types[ctx] = Type.STRING
            else:
                errors.add(
                    ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: [string, string], but got [{type1}, {type2}]')
                self.ctx_types[ctx] = Type.ERROR
        else:
            self.handle_float_int_ops(ctx)

    # Exit a parse tree produced by ProjectParser#assignment.
    def exitAssignment(self, ctx: ProjectParser.AssignmentContext):
        if self.handle_if_already_error(ctx, ctx.expr()):
            return

        var = ctx.IDENTIFIER().getText()
        if var not in self.variable_types:
            errors.add(ctx.IDENTIFIER(),
                       f'Variable {var} was not declared before usage')
            self.ctx_types[ctx] = Type.ERROR
        else:
            var_type = self.variable_types[var]
            expr_type = self.ctx_types[ctx.expr()]
            if var_type == expr_type:
                self.ctx_types[ctx] = var_type
            elif var_type == Type.FLOAT and expr_type == Type.INT:  # assigning int expr into float variable
                self.ctx_types[ctx] = Type.FLOAT
            else:
                errors.add(
                    ctx.IDENTIFIER(), f'Assignment error: type of variable {var} is {var_type}, while type of {ctx.expr().getText()} is {expr_type}')
                self.ctx_types[ctx] = Type.ERROR

        pass

    # Exit a parse tree produced by ProjectParser#literalExpr.
    def exitLiteralExpr(self, ctx: ProjectParser.LiteralExprContext):
        self.ctx_types[ctx] = self.ctx_types[ctx.literal()]

    # Exit a parse tree produced by ProjectParser#ltGt.
    def exitLtGt(self, ctx: ProjectParser.LtGtContext):
        expr1_ctx = ctx.expr(0)
        expr2_ctx = ctx.expr(1)
        if self.handle_if_already_error(ctx, expr1_ctx, expr2_ctx):
            return

        type1 = self.ctx_types[expr1_ctx]
        type2 = self.ctx_types[expr2_ctx]
        if ((type1 == type2 and type1 in [Type.INT, Type.FLOAT]) or
                type1 == Type.FLOAT and type2 == Type.INT or
                type1 == Type.INT and type2 == Type.FLOAT):
            self.ctx_types[ctx] = Type.BOOL
        else:
            errors.add(
                ctx.op, f'Operation "{ctx.op.text}" expected expressions of types: [int, int], or [float, float] but got: [{type1}, {type2}]')
            self.ctx_types[ctx] = Type.ERROR

    # Exit a parse tree produced by ProjectParser#logicalAnd.
    def exitLogicalAnd(self, ctx: ProjectParser.LogicalAndContext):
        self.handle_logical_ops(ctx)

    # Exit a parse tree produced by ProjectParser#unarySub.
    def exitUnarySub(self, ctx: ProjectParser.UnarySubContext):
        if self.handle_if_already_error(ctx, ctx.expr()):
            return
        expr_type = self.ctx_types[ctx.expr()]
        if expr_type in [Type.INT, Type.FLOAT]:
            self.ctx_types[ctx] = expr_type
        else:
            errors.add(
                ctx.SUB(), f'Operation "{ctx.SUB().getText()}" expected expression of type float, or int, but got {expr_type}')
            self.ctx_types[ctx] = Type.ERROR

    # Exit a parse tree produced by ProjectParser#logicalOr.
    def exitLogicalOr(self, ctx: ProjectParser.LogicalOrContext):
        self.handle_logical_ops(ctx)
