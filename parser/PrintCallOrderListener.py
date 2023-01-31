import inspect
from ProjectParser import ProjectParser
from ProjectParserListener import ProjectParserListener


class PrintCallOrderListener(ProjectParserListener):
    def __init__(self) -> None:
        super().__init__()

    def enterProgram(self, ctx: ProjectParser.ProgramContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#program.
    def exitProgram(self, ctx:ProjectParser.ProgramContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#literal.
    def enterLiteral(self, ctx:ProjectParser.LiteralContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#literal.
    def exitLiteral(self, ctx:ProjectParser.LiteralContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ProjectParser.EmptyStatementContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ProjectParser.EmptyStatementContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#declareVariables.
    def enterDeclareVariables(self, ctx:ProjectParser.DeclareVariablesContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#declareVariables.
    def exitDeclareVariables(self, ctx:ProjectParser.DeclareVariablesContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#exprStatement.
    def enterExprStatement(self, ctx:ProjectParser.ExprStatementContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#exprStatement.
    def exitExprStatement(self, ctx:ProjectParser.ExprStatementContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#readVariables.
    def enterReadVariables(self, ctx:ProjectParser.ReadVariablesContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#readVariables.
    def exitReadVariables(self, ctx:ProjectParser.ReadVariablesContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#writeExprs.
    def enterWriteExprs(self, ctx:ProjectParser.WriteExprsContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#writeExprs.
    def exitWriteExprs(self, ctx:ProjectParser.WriteExprsContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#blockStatement.
    def enterBlockStatement(self, ctx:ProjectParser.BlockStatementContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#blockStatement.
    def exitBlockStatement(self, ctx:ProjectParser.BlockStatementContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#ifStatement.
    def enterIfStatement(self, ctx:ProjectParser.IfStatementContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#ifStatement.
    def exitIfStatement(self, ctx:ProjectParser.IfStatementContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectParser.WhileStatementContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#whileStatement.
    def exitWhileStatement(self, ctx:ProjectParser.WhileStatementContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#block.
    def enterBlock(self, ctx:ProjectParser.BlockContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#block.
    def exitBlock(self, ctx:ProjectParser.BlockContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#identifierList.
    def enterIdentifierList(self, ctx:ProjectParser.IdentifierListContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#identifierList.
    def exitIdentifierList(self, ctx:ProjectParser.IdentifierListContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#exprList.
    def enterExprList(self, ctx:ProjectParser.ExprListContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#exprList.
    def exitExprList(self, ctx:ProjectParser.ExprListContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#variableType.
    def enterVariableType(self, ctx:ProjectParser.VariableTypeContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#variableType.
    def exitVariableType(self, ctx:ProjectParser.VariableTypeContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#variableExpr.
    def enterVariableExpr(self, ctx:ProjectParser.VariableExprContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#variableExpr.
    def exitVariableExpr(self, ctx:ProjectParser.VariableExprContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#parExpr.
    def enterParExpr(self, ctx:ProjectParser.ParExprContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#parExpr.
    def exitParExpr(self, ctx:ProjectParser.ParExprContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#logicalNot.
    def enterLogicalNot(self, ctx:ProjectParser.LogicalNotContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#logicalNot.
    def exitLogicalNot(self, ctx:ProjectParser.LogicalNotContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#equalNotEqual.
    def enterEqualNotEqual(self, ctx:ProjectParser.EqualNotEqualContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#equalNotEqual.
    def exitEqualNotEqual(self, ctx:ProjectParser.EqualNotEqualContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#addSubConcat.
    def enterAddSubConcat(self, ctx:ProjectParser.AddSubConcatContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#addSubConcat.
    def exitAddSubConcat(self, ctx:ProjectParser.AddSubConcatContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#assignment.
    def enterAssignment(self, ctx:ProjectParser.AssignmentContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#assignment.
    def exitAssignment(self, ctx:ProjectParser.AssignmentContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#literalExpr.
    def enterLiteralExpr(self, ctx:ProjectParser.LiteralExprContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#literalExpr.
    def exitLiteralExpr(self, ctx:ProjectParser.LiteralExprContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#ltGt.
    def enterLtGt(self, ctx:ProjectParser.LtGtContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#ltGt.
    def exitLtGt(self, ctx:ProjectParser.LtGtContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#logicalAnd.
    def enterLogicalAnd(self, ctx:ProjectParser.LogicalAndContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#logicalAnd.
    def exitLogicalAnd(self, ctx:ProjectParser.LogicalAndContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#unarySub.
    def enterUnarySub(self, ctx:ProjectParser.UnarySubContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#unarySub.
    def exitUnarySub(self, ctx:ProjectParser.UnarySubContext):
        print(inspect.stack()[0][3])


    # Enter a parse tree produced by ProjectParser#logicalOr.
    def enterLogicalOr(self, ctx:ProjectParser.LogicalOrContext):
        print(inspect.stack()[0][3])

    # Exit a parse tree produced by ProjectParser#logicalOr.
    def exitLogicalOr(self, ctx:ProjectParser.LogicalOrContext):
        print(inspect.stack()[0][3])



