# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_typ.
    def visitAtomic_typ(self, ctx:MT22Parser.Atomic_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardcl.
    def visitVardcl(self, ctx:MT22Parser.VardclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varinit.
    def visitVarinit(self, ctx:MT22Parser.VarinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdcl.
    def visitFuncdcl(self, ctx:MT22Parser.FuncdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritsub.
    def visitInheritsub(self, ctx:MT22Parser.InheritsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#emptyblock.
    def visitEmptyblock(self, ctx:MT22Parser.EmptyblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callindex.
    def visitCallindex(self, ctx:MT22Parser.CallindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callfunc.
    def visitCallfunc(self, ctx:MT22Parser.CallfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statelist.
    def visitStatelist(self, ctx:MT22Parser.StatelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stateprime.
    def visitStateprime(self, ctx:MT22Parser.StateprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstate.
    def visitAssignstate(self, ctx:MT22Parser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalarvar.
    def visitScalarvar(self, ctx:MT22Parser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstate.
    def visitIfstate(self, ctx:MT22Parser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstate.
    def visitForstate(self, ctx:MT22Parser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestate.
    def visitWhilestate(self, ctx:MT22Parser.WhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestate.
    def visitDowhilestate(self, ctx:MT22Parser.DowhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstate.
    def visitBreakstate(self, ctx:MT22Parser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestate.
    def visitContinuestate(self, ctx:MT22Parser.ContinuestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstate.
    def visitReturnstate(self, ctx:MT22Parser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstate.
    def visitCallstate(self, ctx:MT22Parser.CallstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstate.
    def visitBlockstate(self, ctx:MT22Parser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#comments.
    def visitComments(self, ctx:MT22Parser.CommentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexarr.
    def visitIndexarr(self, ctx:MT22Parser.IndexarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr_typ.
    def visitArr_typ(self, ctx:MT22Parser.Arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)



del MT22Parser