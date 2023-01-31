# Generated from c:\Users\28D\Downloads\VSB material\3 - letni semestr\PJP\project\ProjectParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete listener for a parse tree produced by ProjectParser.
class ProjectParserListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectParser#program.
    def enterProgram(self, ctx:ProjectParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProjectParser#program.
    def exitProgram(self, ctx:ProjectParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProjectParser#literal.
    def enterLiteral(self, ctx:ProjectParser.LiteralContext):
        pass

    # Exit a parse tree produced by ProjectParser#literal.
    def exitLiteral(self, ctx:ProjectParser.LiteralContext):
        pass


    # Enter a parse tree produced by ProjectParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ProjectParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ProjectParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#declareVariables.
    def enterDeclareVariables(self, ctx:ProjectParser.DeclareVariablesContext):
        pass

    # Exit a parse tree produced by ProjectParser#declareVariables.
    def exitDeclareVariables(self, ctx:ProjectParser.DeclareVariablesContext):
        pass


    # Enter a parse tree produced by ProjectParser#exprStatement.
    def enterExprStatement(self, ctx:ProjectParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#exprStatement.
    def exitExprStatement(self, ctx:ProjectParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#readVariables.
    def enterReadVariables(self, ctx:ProjectParser.ReadVariablesContext):
        pass

    # Exit a parse tree produced by ProjectParser#readVariables.
    def exitReadVariables(self, ctx:ProjectParser.ReadVariablesContext):
        pass


    # Enter a parse tree produced by ProjectParser#writeExprs.
    def enterWriteExprs(self, ctx:ProjectParser.WriteExprsContext):
        pass

    # Exit a parse tree produced by ProjectParser#writeExprs.
    def exitWriteExprs(self, ctx:ProjectParser.WriteExprsContext):
        pass


    # Enter a parse tree produced by ProjectParser#blockStatement.
    def enterBlockStatement(self, ctx:ProjectParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#blockStatement.
    def exitBlockStatement(self, ctx:ProjectParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#ifStatement.
    def enterIfStatement(self, ctx:ProjectParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#ifStatement.
    def exitIfStatement(self, ctx:ProjectParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#whileStatement.
    def exitWhileStatement(self, ctx:ProjectParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#block.
    def enterBlock(self, ctx:ProjectParser.BlockContext):
        pass

    # Exit a parse tree produced by ProjectParser#block.
    def exitBlock(self, ctx:ProjectParser.BlockContext):
        pass


    # Enter a parse tree produced by ProjectParser#identifierList.
    def enterIdentifierList(self, ctx:ProjectParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by ProjectParser#identifierList.
    def exitIdentifierList(self, ctx:ProjectParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by ProjectParser#exprList.
    def enterExprList(self, ctx:ProjectParser.ExprListContext):
        pass

    # Exit a parse tree produced by ProjectParser#exprList.
    def exitExprList(self, ctx:ProjectParser.ExprListContext):
        pass


    # Enter a parse tree produced by ProjectParser#variableType.
    def enterVariableType(self, ctx:ProjectParser.VariableTypeContext):
        pass

    # Exit a parse tree produced by ProjectParser#variableType.
    def exitVariableType(self, ctx:ProjectParser.VariableTypeContext):
        pass


    # Enter a parse tree produced by ProjectParser#mulDivMod.
    def enterMulDivMod(self, ctx:ProjectParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ProjectParser#mulDivMod.
    def exitMulDivMod(self, ctx:ProjectParser.MulDivModContext):
        pass


    # Enter a parse tree produced by ProjectParser#variableExpr.
    def enterVariableExpr(self, ctx:ProjectParser.VariableExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#variableExpr.
    def exitVariableExpr(self, ctx:ProjectParser.VariableExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#parExpr.
    def enterParExpr(self, ctx:ProjectParser.ParExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#parExpr.
    def exitParExpr(self, ctx:ProjectParser.ParExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#logicalNot.
    def enterLogicalNot(self, ctx:ProjectParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by ProjectParser#logicalNot.
    def exitLogicalNot(self, ctx:ProjectParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by ProjectParser#equalNotEqual.
    def enterEqualNotEqual(self, ctx:ProjectParser.EqualNotEqualContext):
        pass

    # Exit a parse tree produced by ProjectParser#equalNotEqual.
    def exitEqualNotEqual(self, ctx:ProjectParser.EqualNotEqualContext):
        pass


    # Enter a parse tree produced by ProjectParser#addSubConcat.
    def enterAddSubConcat(self, ctx:ProjectParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by ProjectParser#addSubConcat.
    def exitAddSubConcat(self, ctx:ProjectParser.AddSubConcatContext):
        pass


    # Enter a parse tree produced by ProjectParser#assignment.
    def enterAssignment(self, ctx:ProjectParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#assignment.
    def exitAssignment(self, ctx:ProjectParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#literalExpr.
    def enterLiteralExpr(self, ctx:ProjectParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#literalExpr.
    def exitLiteralExpr(self, ctx:ProjectParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#ltGt.
    def enterLtGt(self, ctx:ProjectParser.LtGtContext):
        pass

    # Exit a parse tree produced by ProjectParser#ltGt.
    def exitLtGt(self, ctx:ProjectParser.LtGtContext):
        pass


    # Enter a parse tree produced by ProjectParser#logicalAnd.
    def enterLogicalAnd(self, ctx:ProjectParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by ProjectParser#logicalAnd.
    def exitLogicalAnd(self, ctx:ProjectParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by ProjectParser#unarySub.
    def enterUnarySub(self, ctx:ProjectParser.UnarySubContext):
        pass

    # Exit a parse tree produced by ProjectParser#unarySub.
    def exitUnarySub(self, ctx:ProjectParser.UnarySubContext):
        pass


    # Enter a parse tree produced by ProjectParser#logicalOr.
    def enterLogicalOr(self, ctx:ProjectParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by ProjectParser#logicalOr.
    def exitLogicalOr(self, ctx:ProjectParser.LogicalOrContext):
        pass



del ProjectParser