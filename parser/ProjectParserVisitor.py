# Generated from c:\Users\28D\Downloads\VSB material\3 - letni semestr\PJP\project\ProjectParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete generic visitor for a parse tree produced by ProjectParser.

class ProjectParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjectParser#program.
    def visitProgram(self, ctx:ProjectParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#literal.
    def visitLiteral(self, ctx:ProjectParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ProjectParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#declareVariables.
    def visitDeclareVariables(self, ctx:ProjectParser.DeclareVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#exprStatement.
    def visitExprStatement(self, ctx:ProjectParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#readVariables.
    def visitReadVariables(self, ctx:ProjectParser.ReadVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#writeExprs.
    def visitWriteExprs(self, ctx:ProjectParser.WriteExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#blockStatement.
    def visitBlockStatement(self, ctx:ProjectParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#ifStatement.
    def visitIfStatement(self, ctx:ProjectParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#whileStatement.
    def visitWhileStatement(self, ctx:ProjectParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#block.
    def visitBlock(self, ctx:ProjectParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#identifierList.
    def visitIdentifierList(self, ctx:ProjectParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#exprList.
    def visitExprList(self, ctx:ProjectParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#variableType.
    def visitVariableType(self, ctx:ProjectParser.VariableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#mulDivMod.
    def visitMulDivMod(self, ctx:ProjectParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#variableExpr.
    def visitVariableExpr(self, ctx:ProjectParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#parExpr.
    def visitParExpr(self, ctx:ProjectParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#logicalNot.
    def visitLogicalNot(self, ctx:ProjectParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#equalNotEqual.
    def visitEqualNotEqual(self, ctx:ProjectParser.EqualNotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#addSubConcat.
    def visitAddSubConcat(self, ctx:ProjectParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#assignment.
    def visitAssignment(self, ctx:ProjectParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#literalExpr.
    def visitLiteralExpr(self, ctx:ProjectParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#ltGt.
    def visitLtGt(self, ctx:ProjectParser.LtGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#logicalAnd.
    def visitLogicalAnd(self, ctx:ProjectParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#unarySub.
    def visitUnarySub(self, ctx:ProjectParser.UnarySubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#logicalOr.
    def visitLogicalOr(self, ctx:ProjectParser.LogicalOrContext):
        return self.visitChildren(ctx)



del ProjectParser