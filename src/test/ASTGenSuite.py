import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """x, y, z: integer = 1, a, .e34;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, Id(a))
	VarDecl(z, IntegerType, FloatLit(0.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
    printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
            
    def test_305(self):
        input = """aizza: function boolean(bool: boolean) {
                do {
                    getGirlFr("jenny"::firstName+" \\n");
                } while (false % true);
            }"""
        expect = """Program([
\tFuncDecl(aizza, BooleanType, [Param(bool, BooleanType)], None, BlockStmt([DoWhileStmt(BinExpr(%, BooleanLit(False), BooleanLit(True)), BlockStmt([CallStmt(getGirlFr, BinExpr(::, StringLit(jenny), BinExpr(+, Id(firstName), StringLit( \\n))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
            
    def test_306(self):
        input = """
    x: integer = 65;
    fact: function integer (n: integer) {
        if (n == 0) return 1;
        else return n * fact(n - 1);
    }
    inc: function void(out n: integer, delta: integer) {
        n = n + delta;
    }
    main: function void() {
        delta: integer = fact(3);
        x: integer;
        y: integer = 43;
        inc(x, delta);
        printInteger(x);
    }
    """
        expect = """Program([
\tVarDecl(x, IntegerType, IntegerLit(65))
\tFuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
\tFuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), VarDecl(x, IntegerType), VarDecl(y, IntegerType, IntegerLit(43)), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
            
    def test_307(self):
        input = """a: float = .12E+3;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(120.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
            
    def test_308(self):
        input = """ //a string \n b :string = 1;"""
        expect = """Program([
\tVarDecl(b, StringType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
            
    def test_309(self):
        input = """ //a
    b, T: string = "chau", str::str; """
        expect = """Program([
\tVarDecl(b, StringType, StringLit(chau))
\tVarDecl(T, StringType, BinExpr(::, Id(str), Id(str)))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
            
    def test_310(self):
        input = """fact: function integer (n: integer) {
        if (n != 0) return aBB3;
        else return n * fact(n - 1);
    }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(n), IntegerLit(0)), ReturnStmt(Id(aBB3)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
            
    def test_311(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            // else return 1.3e-4 * fact(n - 1);
            else return;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """fact: function integer (n: integer) {
            while (true) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do {printHello();}
                    while (1 + 4 == 2);
                }
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta), Id(alpha)), DoWhileStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(4)), IntegerLit(2)), BlockStmt([CallStmt(printHello, )]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_315(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = """Program([
	FuncDecl(_45_0, AutoType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(56), FloatLit(1.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_316(self):
        input = """main: function void (x: integer, a_123: string) {
            if (1 < (2 < 3)) 
            {
                return 1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(1), BinExpr(<, IntegerLit(2), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_317(self):
        input = """x: array[3_6,0] of integer = {1,2,4};"""
        expect = """Program([
	VarDecl(x, ArrayType([36, 0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_318(self):
        input = """a, b, c: auto = 4., 1+2, x; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(4.0))
	VarDecl(b, AutoType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, AutoType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test_319(self):
        input = """count,_12_5 : boolean = count(),true&&false;"""
        expect = """Program([
	VarDecl(count, BooleanType, FuncCall(count, []))
	VarDecl(_12_5, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
            
    def test_320(self):
        input = """name, _5_d :array[2]of float = true<(false>5), 5_6;"""
        expect = """Program([
	VarDecl(name, ArrayType([2], FloatType), BinExpr(<, BooleanLit(True), BinExpr(>, BooleanLit(False), IntegerLit(5))))
	VarDecl(_5_d, ArrayType([2], FloatType), IntegerLit(56))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
            
    def test_321(self):
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = """Program([
	VarDecl(x, ArrayType([36, 0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """_12:array[3_6,12] of float = {};"""
        expect = """Program([
	VarDecl(_12, ArrayType([36, 12], FloatType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """dope : array[3,10_2] of string = {1,{5.6e-34},4};"""
        expect = """Program([
	VarDecl(dope, ArrayType([3, 102], StringType), ArrayLit([IntegerLit(1), ArrayLit([FloatLit(5.6e-34)]), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """dope: float = 1.2e-4+6*7;"""
        expect = """Program([
	VarDecl(dope, FloatType, BinExpr(+, FloatLit(0.00012), BinExpr(*, IntegerLit(6), IntegerLit(7))))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_325(self):
        input = """name: string = "duc"::chau[5,1_7];"""
        expect = """Program([
	VarDecl(name, StringType, BinExpr(::, StringLit(duc), ArrayCell(chau, [IntegerLit(5), IntegerLit(17)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_326(self):
        input = """avg: float = (a + b + c2)/3;"""
        expect = """Program([
	VarDecl(avg, FloatType, BinExpr(/, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c2)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_327(self):
        input = """getName: function string (inherit out x:array[2_1,8] of float) {
                return;
                }"""
        expect = """Program([
	FuncDecl(getName, StringType, [InheritOutParam(x, ArrayType([21, 8], FloatType))], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test_328(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = """Program([
	FuncDecl(_45_0, AutoType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(56), FloatLit(1.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_329(self):
        input = """a: function void () {
                return arr[1];
                }"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
            
    def test_330(self):
        input = """fact: function integer (n: integer) {
            {
                /* x: string; */
                func: integer = /*0*/123;
            }
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([BlockStmt([VarDecl(func, IntegerType, IntegerLit(123))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
            
    def test_331(self):
        input = """fact: function integer (n: integer) {
                x: integer;
                y: float;
                y: string;
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType), VarDecl(y, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.0, i >= 10 + 1 + 2, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.0)), BinExpr(>=, Id(i), BinExpr(+, BinExpr(+, IntegerLit(10), IntegerLit(1)), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """x: string = (x+Y(3::4));"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(+, Id(x), FuncCall(Y, [BinExpr(::, IntegerLit(3), IntegerLit(4))])))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """a, b, c: auto = 4., 1+2, x; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(4.0))
	VarDecl(b, AutoType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, AutoType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_335(self):
        input = """count,_12_5 : boolean = count(),true&&false;"""
        expect = """Program([
	VarDecl(count, BooleanType, FuncCall(count, []))
	VarDecl(_12_5, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test_336(self):
        input = """name, _5_d :array[2]of float = true<(false>5), 5_6;"""
        expect = """Program([
	VarDecl(name, ArrayType([2], FloatType), BinExpr(<, BooleanLit(True), BinExpr(>, BooleanLit(False), IntegerLit(5))))
	VarDecl(_5_d, ArrayType([2], FloatType), IntegerLit(56))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_337(self):
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = """Program([
	VarDecl(x, ArrayType([36, 0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_338(self):
        input = """_12:array[3_6,12] of float = {};"""
        expect = """Program([
	VarDecl(_12, ArrayType([36, 12], FloatType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_339(self):
        input = """dope : array[3,10_2] of string = {1,{5.6e-34},4};"""
        expect = """Program([
	VarDecl(dope, ArrayType([3, 102], StringType), ArrayLit([IntegerLit(1), ArrayLit([FloatLit(5.6e-34)]), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
            
    def test_340(self):
        input = """x: integer;
                y: float;
                y: string = "123";"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(y, StringType, StringLit(123))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
            
    def test_341(self):
        input = """fact: function integer (n: integer) {
                x: integer;
                y: float;
                y: string;
            }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType), VarDecl(y, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """x: integer;
                y: float;
                y: string = {"11", "a", "array"::"string"};"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(y, StringType, ArrayLit([StringLit(11), StringLit(a), BinExpr(::, StringLit(array), StringLit(string))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.0, i >= 10 + 1 + 2, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.0)), BinExpr(>=, Id(i), BinExpr(+, BinExpr(+, IntegerLit(10), IntegerLit(1)), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """x: string = (x+Y(3::4));"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(+, Id(x), FuncCall(Y, [BinExpr(::, IntegerLit(3), IntegerLit(4))])))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_345(self):
        input = """a, b, c: auto = 4., 1+2, x; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(4.0))
	VarDecl(b, AutoType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, AutoType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_346(self):
        input = """count,_12_5 : boolean = count(),true&&false;"""
        expect = """Program([
	VarDecl(count, BooleanType, FuncCall(count, []))
	VarDecl(_12_5, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_347(self):
        input = """name, _5_d :array[2]of float = true<(false>5), 5_6;"""
        expect = """Program([
	VarDecl(name, ArrayType([2], FloatType), BinExpr(<, BooleanLit(True), BinExpr(>, BooleanLit(False), IntegerLit(5))))
	VarDecl(_5_d, ArrayType([2], FloatType), IntegerLit(56))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_348(self):
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = """Program([
	VarDecl(x, ArrayType([36, 0], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_349(self):
        input = """_12:array[3_6,12] of float = {};"""
        expect = """Program([
	VarDecl(_12, ArrayType([36, 12], FloatType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
            
    def test_350(self):
        input = """dope : array[3,10_2] of string = {1,{5.6e-34},4};"""
        expect = """Program([
	VarDecl(dope, ArrayType([3, 102], StringType), ArrayLit([IntegerLit(1), ArrayLit([FloatLit(5.6e-34)]), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
            
    def test_351(self):
        input = """dope: float = 1.2e-4+6*7;"""
        expect = """Program([
	VarDecl(dope, FloatType, BinExpr(+, FloatLit(0.00012), BinExpr(*, IntegerLit(6), IntegerLit(7))))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """name: string = "duc"::chau[5,1_7];"""
        expect = """Program([
	VarDecl(name, StringType, BinExpr(::, StringLit(duc), ArrayCell(chau, [IntegerLit(5), IntegerLit(17)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """avg: float = (a + b + c2)/3;"""
        expect = """Program([
	VarDecl(avg, FloatType, BinExpr(/, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c2)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """lexer: function void() {
                parser, x: integer = getAge(), getName();
                age = getAge();
                return age;
                }"""
        expect = """Program([
	FuncDecl(lexer, VoidType, [], None, BlockStmt([VarDecl(parser, IntegerType, FuncCall(getAge, [])), VarDecl(x, IntegerType, FuncCall(getName, [])), AssignStmt(Id(age), FuncCall(getAge, [])), ReturnStmt(Id(age))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_355(self):
        input = """main: function void(arr: array[1,2] of string) {
                if (str::str) if (7 - 4 ==-3) return; else break;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(arr, ArrayType([1, 2], StringType))], None, BlockStmt([IfStmt(BinExpr(::, Id(str), Id(str)), IfStmt(BinExpr(==, BinExpr(-, IntegerLit(7), IntegerLit(4)), UnExpr(-, IntegerLit(3))), ReturnStmt(), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_356(self):
        input = """main: function void(x: boolean) {
                if (true || " "::{" " + str}) continue;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, BooleanType)], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(||, BooleanLit(True), StringLit( )), ArrayLit([BinExpr(+, StringLit( ), Id(str))])), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test_357(self):
        input = """nestedIf: function boolean(bool: boolean) {
                if (true) 
                    if (10 == 4 + 5) UwU = U::U;
                    else print(UwU);
                else {}
                }"""
        expect = """Program([
	FuncDecl(nestedIf, BooleanType, [Param(bool, BooleanType)], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, IntegerLit(10), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(Id(UwU), BinExpr(::, Id(U), Id(U))), CallStmt(print, Id(UwU))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test_358(self):
        input = """main: function void() {
                while(x+1) {}
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_359(self):
        input = """nestedLoop: function array[2,3] of string(n: integer) {
                while(y%3 == 0) {
                    for (i = 3, i < 1_2, i) {
                        while(true) n = false;
                    }
                }
                }"""
        expect = """Program([
	FuncDecl(nestedLoop, ArrayType([2, 3], StringType), [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(3)), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<, Id(i), IntegerLit(12)), Id(i), BlockStmt([WhileStmt(BooleanLit(True), AssignStmt(Id(n), BooleanLit(False)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
            
    def test_360(self):
        input = """germany: function string(out str: string){
                while(heyo::str)
                    do {}
                    while(heyo-.e45);
                }"""
        expect = """Program([
	FuncDecl(germany, StringType, [OutParam(str, StringType)], None, BlockStmt([WhileStmt(BinExpr(::, Id(heyo), Id(str)), DoWhileStmt(BinExpr(-, Id(heyo), FloatLit(0.0)), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
            
    def test_361(self):
        input = """UwU: function string(s: float) {
                i: integer = 0;
                do {
                    i = i + 1;
                    print(i);
                } while(--i < s);
                }"""
        expect = """Program([
	FuncDecl(UwU, StringType, [Param(s, FloatType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, UnExpr(-, UnExpr(-, Id(i))), Id(s)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """fact: function void() {}"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                     while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i + (1_000_1.03)) {
                            writeln();
                        }
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), BreakStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(10001.03)), BlockStmt([CallStmt(writeln, )]))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                    while (x > 1) {
                        do {
                            while (n < 1) {
                                for (i = 3.0, i >= 10 + 1 + 2, i+2) {
                                    return;
                                }
                            }
                        }
                        while (x > 1);
                        i = i + 1;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.0)), BinExpr(>=, Id(i), BinExpr(+, BinExpr(+, IntegerLit(10), IntegerLit(1)), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test_365(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                    res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1){}  
                         if (arr[i] > res)
                            res = arr[i];
                    }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), BlockStmt([])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test_366(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1)
                        if (arr[i] > res)
                            res = arr[i];
                    return res;
                }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test_367(self):
        input = """main: function array [10,10] of integer (a: array [10,10] of integer, out b: array [10,10] of integer, r: integer, c: integer ) {
                    for (i = 0, i < r, 1) 
                        for (j = 0, j < c, 1)
                            b[j,i] = a[i,j];
                    return b;
                }"""
        expect = """Program([
	FuncDecl(main, ArrayType([10, 10], IntegerType), [Param(a, ArrayType([10, 10], IntegerType)), OutParam(b, ArrayType([10, 10], IntegerType)), Param(r, IntegerType), Param(c, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), IntegerLit(1), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), IntegerLit(1), AssignStmt(ArrayCell(b, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)])))), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test_368(self):
        input = """fact: function float(x: array[7] of string) {
                if (2<3) return a[x[y]];
                }"""
        expect = """Program([
	FuncDecl(fact, FloatType, [Param(x, ArrayType([7], StringType))], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(2), IntegerLit(3)), ReturnStmt(ArrayCell(a, [ArrayCell(x, [Id(y)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test_369(self):
        input = """main: function string (x: float,y: integer) {
                x=1;
                y= x + x * y;
                }"""
        expect = """Program([
	FuncDecl(main, StringType, [Param(x, FloatType), Param(y, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), BinExpr(+, Id(x), BinExpr(*, Id(x), Id(y))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
            
    def test_370(self):
        input = """main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = a[b[3,4]]+5;
                }
            } 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(3), IntegerLit(4)])]), IntegerLit(5)))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
            
    def test_371(self):
        input = """a: array [3] of string = {{}};"""
        expect = """Program([
	VarDecl(a, ArrayType([3], StringType), ArrayLit([ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """main: function void(fact: integer) {
                fact[0] = 1;
                fact = n * fact(n-!-1);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(fact, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(fact, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(Id(fact), BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), UnExpr(!, UnExpr(-, IntegerLit(1))))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """nestedIf: function boolean(bool: boolean) {
                if (true) 
                    if (10 == 4 + 5) UwU = U::U;
                    else print(UwU);
                else {}
                }"""
        expect = """Program([
	FuncDecl(nestedIf, BooleanType, [Param(bool, BooleanType)], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BinExpr(==, IntegerLit(10), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(Id(UwU), BinExpr(::, Id(U), Id(U))), CallStmt(print, Id(UwU))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """main: function void(x: boolean) {
                if (true || ""::{"" + str}) continue;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, BooleanType)], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(||, BooleanLit(True), StringLit()), ArrayLit([BinExpr(+, StringLit(), Id(str))])), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test_375(self):
        input = """main: function void(arr: array[1,2] of string) {
                if (str::str) if (7 - 4 ==-3) return; else break;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(arr, ArrayType([1, 2], StringType))], None, BlockStmt([IfStmt(BinExpr(::, Id(str), Id(str)), IfStmt(BinExpr(==, BinExpr(-, IntegerLit(7), IntegerLit(4)), UnExpr(-, IntegerLit(3))), ReturnStmt(), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test_376(self):
        input = """fact: function void() {
                if (true || false && "tom")
                    x = arr[10,1];
                else
                    {}
                }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), StringLit(tom)), AssignStmt(Id(x), ArrayCell(arr, [IntegerLit(10), IntegerLit(1)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_377(self):
        input = """F: function auto() {
                dict[pair[1]+pair[0]] = 7.e-9/3;
                return dict[2.];
                }"""
        expect = """Program([
	FuncDecl(F, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(dict, [BinExpr(+, ArrayCell(pair, [IntegerLit(1)]), ArrayCell(pair, [IntegerLit(0)]))]), BinExpr(/, FloatLit(7e-09), IntegerLit(3))), ReturnStmt(ArrayCell(dict, [FloatLit(2.0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test_378(self):
        input = """func: function void() {
                for (idx[1]=2_1,7==(4>5),--i)
                    arr[idx[i]] = arr[idx[i]]::"jdk";
                }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(idx, [IntegerLit(1)]), IntegerLit(21)), BinExpr(==, IntegerLit(7), BinExpr(>, IntegerLit(4), IntegerLit(5))), UnExpr(-, UnExpr(-, Id(i))), AssignStmt(ArrayCell(arr, [ArrayCell(idx, [Id(i)])]), BinExpr(::, ArrayCell(arr, [ArrayCell(idx, [Id(i)])]), StringLit(jdk))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_379(self):
        input = """__C__: array[7] of float = germanyTOM(jK[""::{""}]);"""
        expect = """Program([
	VarDecl(__C__, ArrayType([7], FloatType), FuncCall(germanyTOM, [ArrayCell(jK, [BinExpr(::, StringLit(), ArrayLit([StringLit()]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
            
    def test_380(self):
        input = """fact: function integer(n: auto) {
                fact = n * fact(n-!-1);
                return fact;
                }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([AssignStmt(Id(fact), BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), UnExpr(!, UnExpr(-, IntegerLit(1))))]))), ReturnStmt(Id(fact))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
            
    def test_381(self):
        input = """non_Assoc1st: function string(inherit out x:array[2] of string) {
                x[1,2] = (" "::concat)::foo("haizz"); 
                }"""
        expect = """Program([
	FuncDecl(non_Assoc1st, StringType, [InheritOutParam(x, ArrayType([2], StringType))], None, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), BinExpr(::, BinExpr(::, StringLit( ), Id(concat)), FuncCall(foo, [StringLit(haizz)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """main: function float(out _x: auto) inherit tom {
                // blebolmmfowf :D
                res: string = "";
                res[3.e1+fact(7)] = x[y[8%floor]]+4;
                res[1_2_3] = {1,2,{1,2}};
                main();
                return;
                }"""
        expect = """Program([
	FuncDecl(main, FloatType, [OutParam(_x, AutoType)], tom, BlockStmt([VarDecl(res, StringType, StringLit()), AssignStmt(ArrayCell(res, [BinExpr(+, FloatLit(30.0), FuncCall(fact, [IntegerLit(7)]))]), BinExpr(+, ArrayCell(x, [ArrayCell(y, [BinExpr(%, IntegerLit(8), Id(floor))])]), IntegerLit(4))), AssignStmt(ArrayCell(res, [IntegerLit(123)]), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(1), IntegerLit(2)])])), CallStmt(main, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """main: function void() inherit tom {
                print(true + false == false&&"0_7" + !true);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], tom, BlockStmt([CallStmt(print, BinExpr(==, BinExpr(+, BooleanLit(True), BooleanLit(False)), BinExpr(&&, BooleanLit(False), BinExpr(+, StringLit(0_7), UnExpr(!, BooleanLit(True))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """x:float = -foo(a%b + c) - 7_89.e-5+7;"""
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, BinExpr(-, UnExpr(-, FuncCall(foo, [BinExpr(+, BinExpr(%, Id(a), Id(b)), Id(c))])), FloatLit(0.00789)), IntegerLit(7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test_385(self):
        input = """fact: function float(x: array[7] of string) {
                if (2<3) return a[x[y]];
                }"""
        expect = """Program([
	FuncDecl(fact, FloatType, [Param(x, ArrayType([7], StringType))], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(2), IntegerLit(3)), ReturnStmt(ArrayCell(a, [ArrayCell(x, [Id(y)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_386(self):
        input = """fact: function float(x: array[7] of string) {
                for(i = 0, i < 1, i+i[1,2,3]){}
                }"""
        expect = """Program([
	FuncDecl(fact, FloatType, [Param(x, ArrayType([7], StringType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), ArrayCell(i, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_387(self):
        input = """fact: function float(x: array[7] of string) {
                if (2<3) return a[x[y]];
                }"""
        expect = """Program([
	FuncDecl(fact, FloatType, [Param(x, ArrayType([7], StringType))], None, BlockStmt([IfStmt(BinExpr(<, IntegerLit(2), IntegerLit(3)), ReturnStmt(ArrayCell(a, [ArrayCell(x, [Id(y)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_388(self):
        input = """main: function integer (a: array [2] of integer, b: integer)
        {
            i: integer =0;
            while (a[i] > b)
            {
                writeln(a[i]);
                i = i + 1;
            }
                    
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, ArrayType([2], IntegerType)), Param(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(>, ArrayCell(a, [Id(i)]), Id(b)), BlockStmt([CallStmt(writeln, ArrayCell(a, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_389(self):
        input = """x: integer;
        fact: function integer (n: integer)
        {
            if(n==0)
                return 1;
            else
                return n* fact(n-1);
        }
        /*
        comment
        */
        main: function integer (x: integer)
        {
            x = 10;
            fact(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, IntegerType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(10)), CallStmt(fact, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
            
    def test_390(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                    res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1){}  
                         if (arr[i] > res)
                            res = arr[i];
                    }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), BlockStmt([])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
            
    def test_391(self):
        input = """main: function integer (arr: array [100] of integer, n: integer){
                res: integer;
                    res = arr[0];
                    for (i = 1, i < n, 1)
                        if (arr[i] > res)
                            res = arr[i];
                    return res;
                }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType), AssignStmt(Id(res), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), IntegerLit(1), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(res)), AssignStmt(Id(res), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """main: function array [10,10] of integer (a: array [10,10] of integer, out b: array [10,10] of integer, r: integer, c: integer ) {
                    for (i = 0, i < r, 1) 
                        for (j = 0, j < c, 1)
                            b[j,i] = a[i,j];
                    return b;
                }"""
        expect = """Program([
	FuncDecl(main, ArrayType([10, 10], IntegerType), [Param(a, ArrayType([10, 10], IntegerType)), OutParam(b, ArrayType([10, 10], IntegerType)), Param(r, IntegerType), Param(c, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), IntegerLit(1), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), IntegerLit(1), AssignStmt(ArrayCell(b, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)])))), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """main: function string (start: array [10] of integer, end: integer) {
                    size, i, j,p : integer;
                    size = end - start;
                    i = 1;
                    j = size - 1;
                    p = start[0];
                    while (true)
                    {
                        while (start[i] < p)
                            if (i == size - 1)
                                break;
                        while (start[j] > p)
                            if (j == 0)
                                break;
                        if (i >= j) 
                            break;
                        swap(start[i], start[j]);
                    }
                    swap(start[0], start[j]);
                    return start[j];
                }"""
        expect = """Program([
	FuncDecl(main, StringType, [Param(start, ArrayType([10], IntegerType)), Param(end, IntegerType)], None, BlockStmt([VarDecl(size, IntegerType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(p, IntegerType), AssignStmt(Id(size), BinExpr(-, Id(end), Id(start))), AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(j), BinExpr(-, Id(size), IntegerLit(1))), AssignStmt(Id(p), ArrayCell(start, [IntegerLit(0)])), WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BinExpr(<, ArrayCell(start, [Id(i)]), Id(p)), IfStmt(BinExpr(==, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BreakStmt())), WhileStmt(BinExpr(>, ArrayCell(start, [Id(j)]), Id(p)), IfStmt(BinExpr(==, Id(j), IntegerLit(0)), BreakStmt())), IfStmt(BinExpr(>=, Id(i), Id(j)), BreakStmt()), CallStmt(swap, ArrayCell(start, [Id(i)]), ArrayCell(start, [Id(j)]))])), CallStmt(swap, ArrayCell(start, [IntegerLit(0)]), ArrayCell(start, [Id(j)])), ReturnStmt(ArrayCell(start, [Id(j)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """main: function string (x: array [100] of integer,n: integer, exp: float) {
                    output: array [100] of integer;
                    count: array [10] of integer = {0};
                    i: integer;
                    for (i = 0, i < n, i+1)
                        count[(arr[i] / exp) % 10] = count[(arr[i] / exp) % 10] + 1;
                    for (i = 1, i < 10, i+1)
                        count[i] = count[i] + count[i-1];
                    for (i = n-1, i >= 0, i-1)
                    {
                        output[count[(arr[i] / exp)%10] - 1] = arr[i];
                        count[(arr[i] / exp) % 10] = count[(arr[i] / exp) % 10] - 1;
                    }
                }"""
        expect = """Program([
	FuncDecl(main, StringType, [Param(x, ArrayType([100], IntegerType)), Param(n, IntegerType), Param(exp, FloatType)], None, BlockStmt([VarDecl(output, ArrayType([100], IntegerType)), VarDecl(count, ArrayType([10], IntegerType), ArrayLit([IntegerLit(0)])), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), BinExpr(+, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(count, [Id(i)]), BinExpr(+, ArrayCell(count, [Id(i)]), ArrayCell(count, [BinExpr(-, Id(i), IntegerLit(1))])))), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(output, [BinExpr(-, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1))]), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), BinExpr(-, ArrayCell(count, [BinExpr(%, BinExpr(/, ArrayCell(arr, [Id(i)]), Id(exp)), IntegerLit(10))]), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test_395(self):
        input = """main: function string (x: float,y: integer) {
                x=1;
                y= x + x * y;
                y = foo (x[2] * y[1,2] + 9);
                }"""
        expect = """Program([
	FuncDecl(main, StringType, [Param(x, FloatType), Param(y, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), BinExpr(+, Id(x), BinExpr(*, Id(x), Id(y)))), AssignStmt(Id(y), FuncCall(foo, [BinExpr(+, BinExpr(*, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(1), IntegerLit(2)])), IntegerLit(9))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_396(self):
        input = """foo: /*comment*/function void (a: integer, b: float) {
                    i: float = .0E2;
                    do {
                        a[i] = b + 1.0;
                        i=i+1;
                    }
                    while (false);
                }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), DoWhileStmt(BooleanLit(False), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), FloatLit(1.0))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_397(self):
        input = """foo: /*comment*/function void (a: integer, b: float) {
                    i: float = .0E1;
                    while (i<=5)
                    {
                        a[i] = b + 1.0;
                        i=i+1;
                    }
                }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), WhileStmt(BinExpr(<=, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, Id(b), FloatLit(1.0))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_398(self):
        input = """main: function void (a: string, b: string) {
            printString(a::b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([CallStmt(printString, BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test_399(self):
        input = """main: function void (x: integer, a_123: string) {
            i: integer =0;
            x[1+2*3] = {1,2,{1,2}};
            y= z[foo(1)*foo[2]%foo(2)];

        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(x, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3)))]), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(1), IntegerLit(2)])])), AssignStmt(Id(y), ArrayCell(z, [BinExpr(%, BinExpr(*, FuncCall(foo, [IntegerLit(1)]), ArrayCell(foo, [IntegerLit(2)])), FuncCall(foo, [IntegerLit(2)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))