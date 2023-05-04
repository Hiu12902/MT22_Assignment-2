from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    # program: decllist EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.decllist():
            return self.visit(ctx.decl()) + self.visit(ctx.decllist())
        return self.visit(ctx.decl())
    # decl: vardcl | funcdcl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.vardcl() if ctx.vardcl() else ctx.funcdcl())
    # atomic_typ: BOOLEAN | INTEGER | FLOAT | STRING ;
    def visitAtomic_typ(self, ctx: MT22Parser.Atomic_typContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
    # typ: atomic_typ | AUTO | arr_typ;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.atomic_typ():
            return self.visit(ctx.atomic_typ())
        elif ctx.AUTO():
            return AutoType()
        elif ctx.arr_typ():
            return self.visit(ctx.arr_typ())
    # vardcl: ((idlist COLON typ) | varinit) SEMI;
    def visitVardcl(self, ctx: MT22Parser.VardclContext):
        if ctx.COLON():
            idlist = self.visit(ctx.idlist())
            count = len(idlist)
            result = []
            for i in range(count):
                vardecl = VarDecl(idlist[i], self.visit(ctx.typ()), None)
                result += [vardecl]
        elif ctx.varinit():
            vardeclist = self.visit(ctx.varinit())
            count = len(vardeclist)
            result = []
            for i in range(count):
                vardecl = VarDecl(vardeclist[i][0], vardeclist[i][1], vardeclist[(count - 1) - i][2])
                result += [vardecl]
        return result
    # varinit: ID COMMA varinit COMMA expr | ID COLON typ EQ expr;
    def visitVarinit(self, ctx: MT22Parser.VarinitContext):
        if ctx.EQ():
            return [(ctx.ID().getText(), 
                            self.visit(ctx.typ()), 
                            self.visit(ctx.expr()))]
        vardeclist = self.visit(ctx.varinit())
        typ = vardeclist[-1][1]
        return [(ctx.ID().getText(), 
                        typ, 
                        self.visit(ctx.expr()))] + vardeclist
    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.COMMA():
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]
    # funcdcl: ID COLON FUNCTION (typ | VOID) LB paramlist RB (inheritsub)? funcbody;
    def visitFuncdcl(self, ctx: MT22Parser.FuncdclContext):
        return [FuncDecl(ctx.ID().getText(), 
                        self.visit(ctx.typ()) if ctx.typ() else VoidType(), 
                        self.visit(ctx.paramlist()), 
                        self.visit(ctx.inheritsub()) if ctx.inheritsub() else None,
                        self.visit(ctx.funcbody()))]
    # inheritsub: INHERIT ID;
    def visitInheritsub(self, ctx: MT22Parser.InheritsubContext):
        return ctx.ID().getText()
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.paramprime():
            return self.visit(ctx.paramprime())
        return []
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        return [self.visit(ctx.param())]
    # param: INHERIT? OUT? ID COLON typ;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        return ParamDecl(ctx.ID().getText(), 
                     self.visit(ctx.typ()), 
                     True if ctx.OUT() else False, 
                     True if ctx.INHERIT() else False)
    # funcbody: blockstate | emptyblock;
    def visitFuncbody(self, ctx: MT22Parser.FuncbodyContext):
        return self.visit(ctx.blockstate()) if ctx.blockstate() else self.visit(ctx.emptyblock())
    # emptyblock: CUR_LB CUR_RB;
    def visitEmptyblock(self, ctx: MT22Parser.EmptyblockContext):
        return Block([])
    # callindex: ID SQU_LB exprprime SQU_RB;
    def visitCallindex(self, ctx: MT22Parser.CallindexContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprprime()))
    # callfunc: ID LB exprlist RB;
    def visitCallfunc(self, ctx: MT22Parser.CallfuncContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.exprlist()))
    # expr: expr1 DBL_COLON expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.DBL_COLON():
            return BinExpr(ctx.DBL_COLON().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))
    # expr1: expr2 (DBL_EQ | UEQ | MOR | LESS | MOR_EQ | LESS_EQ) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.DBL_EQ():
            return BinExpr(ctx.DBL_EQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.UEQ():
            return BinExpr(ctx.UEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.MOR():
            return BinExpr(ctx.MOR().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LESS():
            return BinExpr(ctx.LESS().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.MOR_EQ():
            return BinExpr(ctx.MOR_EQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LESS_EQ():
            return BinExpr(ctx.LESS_EQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.OR():
            return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.ADD():
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.SUB():
            return BinExpr(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.MOD():
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())
    # expr5: EXCLAM expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.EXCLAM():
            return UnExpr(ctx.EXCLAM().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())
    # expr7: LB expr RB | ID | INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | callfunc | callindex | indexarr;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.LB():
            return self.visit(ctx.expr())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            floatlit = ctx.FLOATLIT().getText()
            if floatlit[0] == '.':
                result = '0' + floatlit
                return FloatLit(float(result))
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.callfunc():
            return self.visit(ctx.callfunc())
        elif ctx.callindex():
            return self.visit(ctx.callindex())
        elif ctx.indexarr():
            return self.visit(ctx.indexarr())
    # stmt: (assignstate | ifstate | forstate | whilestate | dowhilestate | breakstate | continuestate | returnstate | blockstate | callstate);
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstate():
            return self.visit(ctx.assignstate())
        elif ctx.ifstate():
            return self.visit(ctx.ifstate())
        elif ctx.forstate():
            return self.visit(ctx.forstate())
        elif ctx.whilestate():
            return self.visit(ctx.whilestate())
        elif ctx.dowhilestate():
            return self.visit(ctx.dowhilestate())
        elif ctx.breakstate():
            return self.visit(ctx.breakstate())
        elif ctx.continuestate():
            return self.visit(ctx.continuestate())
        elif ctx.returnstate():
            return self.visit(ctx.returnstate())
        elif ctx.blockstate():
            return self.visit(ctx.blockstate())
        elif ctx.callstate():
            return self.visit(ctx.callstate())
    # statelist: stateprime | ;
    def visitStatelist(self, ctx: MT22Parser.StatelistContext):
        if ctx.stateprime():
            return self.visit(ctx.stateprime())
        return []
    # stateprime: (stmt|vardcl) stateprime | ;
    def visitStateprime(self, ctx: MT22Parser.StateprimeContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.vardcl(): 
            return self.visit(ctx.vardcl()) + self.visit(ctx.stateprime())
        elif ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stateprime())
    # scalarvar: ID | callindex;
    def visitScalarvar(self, ctx: MT22Parser.ScalarvarContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.callindex())
    # assignstate: scalarvar EQ expr SEMI;
    def visitAssignstate(self, ctx: MT22Parser.AssignstateContext):
        return AssignStmt(self.visit(ctx.scalarvar()), self.visit(ctx.expr()))
    # ifstate: IF LB expr RB stmt (ELSE stmt)?;
    def visitIfstate(self, ctx: MT22Parser.IfstateContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), None)
    # forstate: FOR LB (scalarvar EQ expr) COMMA expr COMMA expr RB statelist;
    # forstate: FOR LB (scalarvar EQ expr) COMMA expr COMMA expr RB stmt;
    def visitForstate(self, ctx: MT22Parser.ForstateContext):
        return ForStmt(AssignStmt(self.visit(ctx.scalarvar()), self.visit(ctx.expr(0)))
                       , self.visit(ctx.expr(1))
                       , self.visit(ctx.expr(2))
                       , self.visit(ctx.stmt()))
    # whilestate: WHILE LB expr RB statelist; 
    # whilestate: WHILE LB expr RB stmt; 
    def visitWhilestate(self, ctx: MT22Parser.WhilestateContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))
    # dowhilestate: DO blockstate WHILE LB expr RB SEMI;
    def visitDowhilestate(self, ctx: MT22Parser.DowhilestateContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstate()))
    # breakstate: BREAK SEMI;
    def visitBreakstate(self, ctx: MT22Parser.BreakstateContext):
        return BreakStmt()
    # continuestate: CONTINUE SEMI;
    def visitContinuestate(self, ctx: MT22Parser.ContinuestateContext):
        return ContinueStmt()
    # returnstate: RETURN (expr)? SEMI;
    def visitReturnstate(self, ctx: MT22Parser.ReturnstateContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)
    # callstate: ID LB exprlist RB SEMI;
    def visitCallstate(self, ctx: MT22Parser.CallstateContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlist()))
    # blockstate: CUR_LB statelist CUR_RB;
    def visitBlockstate(self, ctx: MT22Parser.BlockstateContext):
        return BlockStmt(self.visit(ctx.statelist()))
    # indexarr: CUR_LB exprlist CUR_RB;
    def visitIndexarr(self, ctx: MT22Parser.IndexarrContext):
        return ArrayLit(self.visit(ctx.exprlist()))
    # exprlist: exprprime | ;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprprime():
            return self.visit(ctx.exprprime())
        return []
    # exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        return [self.visit(ctx.expr())]
    # arr_typ: ARRAY SQU_LB intlist SQU_RB OF atomic_typ;
    def visitArr_typ(self, ctx: MT22Parser.Arr_typContext):
        return ArrayType(self.visit(ctx.intlist()), self.visit(ctx.atomic_typ()))
    # intlist: INTLIT COMMA intlist | INTLIT;
    def visitIntlist(self, ctx: MT22Parser.IntlistContext):
        if ctx.COMMA():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlist())
        return [int(ctx.INTLIT().getText())]
