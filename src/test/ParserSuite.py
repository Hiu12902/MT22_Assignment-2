import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
     
    def test_200(self):
        self.assertTrue(TestParser.test(""" //a string \n b :string = 1;""", "successful", 200))
        
    def test_201(self):
        self.assertTrue(TestParser.test(""" //"string\n" b " """, "Error on line 2 col 0:  b ", 201))
        
    def test_202(self):
        self.assertTrue(TestParser.test(""" //string\n """, "Error on line 2 col 1: <EOF>", 202))
        
    def test_203(self):
        self.assertTrue(TestParser.test(""" /* //string\n */ """, "Error on line 2 col 4: <EOF>", 203))
        
    def test_204(self):
        self.assertTrue(TestParser.test(""" /* /* //\n\\t string **/ """, "Error on line 2 col 14: <EOF>", 204))
        
    def test_205(self):
        self.assertTrue(TestParser.test(""" delta: string = "//this is a \n comment"; """, "//this is a ", 205))

    def test_206(self):
        self.assertTrue(TestParser.test(""" //12__34:/aa/*\n*/ """, "Error on line 2 col 0: *", 206))
        
    def test_207(self):
        self.assertTrue(TestParser.test(""" //delta: integer = 1; """, "Error on line 1 col 23: <EOF>", 207))
        
    def test_208(self):
        self.assertTrue(TestParser.test(""" /*delta: float = function () {} */ """, "Error on line 1 col 36: <EOF>", 208))
        
    def test_209(self):
        self.assertTrue(TestParser.test(""" /////////////abs/////////***/ """, "Error on line 1 col 31: <EOF>", 209))
        
    def test_210(self):
        self.assertTrue(TestParser.test(""" abc*/""", "Error on line 1 col 4: *", 210))

    def test_211(self):
        self.assertTrue(TestParser.test(""" /*/*/*/*// """, "Error on line 1 col 6: *", 211))
        
    def test_212(self):
        self.assertTrue(TestParser.test(""" abc // xyz """, "Error on line 1 col 12: <EOF>", 212))
        
    def test_213(self):
        self.assertTrue(TestParser.test(""" 12345//e-134.412//abcdef """, "Error on line 1 col 1: 12345", 213))
        
    def test_214(self):
        self.assertTrue(TestParser.test(""" abc /* string\n*/ """, "Error on line 2 col 3: <EOF>", 214))
        
    def test_215(self):
        self.assertTrue(TestParser.test(""" xyz //*****// """, "Error on line 1 col 15: <EOF>", 215))

    def test_216(self):
        self.assertTrue(TestParser.test(""" ///*abc*/ """, "Error on line 1 col 11: <EOF>", 216))
        
    def test_217(self):
        self.assertTrue(TestParser.test(""" //abc\txyz\abc"zya"\ndyx """, "Error on line 2 col 4: <EOF>", 217))
        
    def test_218(self):
        self.assertTrue(TestParser.test(""" delta: string /*abcdef*/ = 2 // 3456 // \n xyz: string = "a\\n" """, "Error on line 2 col 1: xyz", 218))
        
    def test_219(self):
        self.assertTrue(TestParser.test(""" /* u--eE//\n "string\\n"//*/ """, "Error on line 2 col 16: <EOF>", 219))
        
    def test_220(self):
        input = """ //a
        b, T: string = "chau", str::str; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            """, "Error on line 2 col 12: <EOF>", 221))
        
    def test_222(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
            
            main: function void() {
                delta: integer = fact(3);
                inc(x, delta);
                for (i = 0, i < 10, i+1) {
                    writeLn(i);
            }
            printInteger(x);
        }""", "Error on line 8 col 18: function", 222))
        
    def test_223(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            if (n != 0) return aBB3;
            else return n * fact(n - 1);
        }""", "successful", 223))
        
    def test_224(self):
        self.assertTrue(TestParser.test("""fact: /*xyz*/function integer (n: integer, x: integer, y: float) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        }""", "Error on line 5 col 8: }", 224))
        
    def test_225(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            if (n == 0) return 1;
            // else return 1.3e-4 * fact(n - 1);
            else return;
        }""", "successful", 225))

    def test_226(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            for (x != 3, x + a + 1_2.3-e4, x == y) { 
                boobby: float = cleopatra("a", e34);
            }
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }""", "Error on line 2 col 19: !=", 226))
        
    def test_227(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                for (i = 0, i < 10, i+1) {
                    if ()
                    {
                        while()
                        {
                            do {
                                delta + x - y == 0;
                            }
                            while(true);
                        }
                    }
            }
            printInteger(x);
        }""", "Error on line 3 col 24: )", 227))
        
    def test_228(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
        }""", "successful", 228))
        
    def test_229(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }""", "successful", 229))
        
    def test_230(self):
            """Function declarations"""
            input = """fact: function integer (n: integer) {
            while ((n || 4) && (n == 3)) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do {printHello();}
                    while (1 + 4 == 2);
                }
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test_232(self):
        """Expressions"""
        input = """fact: function float(x: array[] of string) {
                if (2<3) return a[x[y]];
                }"""
        expect = "Error on line 1 col 30: ]"
        self.assertTrue(TestParser.test(input, expect, 232))
        
    def test_233(self):
        input = """
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1 + foo(5)] = a[b[3][4]]+5;
                }
            } 
        }
        """
        expect = """Error on line 6 col 42: ["""
        self.assertTrue(TestParser.test(input,expect,233))
        
    def test_234(self):
        input = """
        main: function void (x: integer, a_123: string) {
            if (1 < (2 < 3)) 
            {
                return 1;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_235(self):
        input = """
        main: function void (x: integer, a_123: string) {
            if (1 < 2 < 3) 
            {
                return 1;
            }
        }
        """
        expect = """Error on line 3 col 22: <"""
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_236(self):
        input = """
        main: function void (x: integer, a_123: string) {
            if (1 < 2[3[4[5, array [1,2] of integer]]]) 
            {
                return 1;
            }
        }
        """
        expect = """Error on line 3 col 21: ["""
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_237(self):
        input = """x: array[3_6,0] of integer = {1,2,4};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,237))
    
    def test_238(self):
        input="""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                     while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i + 1_0.1_0923) {
                            writeln();
                        }
                    }
                }
            }
        }
        """
        expect = """Error on line 11 col 54: _0923"""
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_239(self):
        """Variable declarations"""
        input = """ a, b, c: auto = 4., 1+2, x; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_240(self):
        """Variable declarations"""
        input = """a, b, c: auto = 4., 1+2, __12"""
        expect = "Error on line 1 col 29: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_241(self):
        """Variable declarations"""
        input = """ array [array[0,1], 2] of integer """
        expect = "Error on line 1 col 1: array"
        self.assertTrue(TestParser.test(input, expect, 241))
    
    def test_242(self):
        """Variable declarations"""
        input = """a, b, c: integer = 3, 4, 5, 6;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_243(self):
        """Variable declarations"""
        input = """count,_12_5 = count(),true&&false;"""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test_244(self):
        """Variable declarations"""
        input = """count,_12_5 : void = count(),true&&false;"""
        expect = "Error on line 1 col 14: void"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_245(self):
        """Variable declarations"""
        input = """count,_12_5 : boolean = count(),true&&false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_246(self):
        """Variable declarations"""
        input = """inherit, T5_d[1_0] : array[2] of float;"""
        expect = "Error on line 1 col 0: inherit"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_247(self):
        """Variable declarations"""
        input = """bool, T5_d[1_0] : true<false>5, a[2];"""
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def test_248(self):
        """Variable declarations"""
        input = """name, _5_d :array[2]of float = true<(false>5), 5_6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    
    def test_249(self):
        """Variable declarations"""
        input = """x:array[3_6,0] of auto = {1,2,4};"""
        expect = "Error on line 1 col 18: auto"
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test_250(self):
        """Variable declarations"""
        input = """x:array[3_6,0] of integer = {1,2,4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_251(self):
        """Variable declarations"""
        input = """hkt:array[3_6,d12] of float = {1,{5.6e-34},4};"""
        expect = "Error on line 1 col 14: d12"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_252(self):
        """Variable declarations"""
        input = """_12:array[3_6,12] of float = {};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    
    def test_253(self):
        """Variable declarations"""
        input = """a12_d7 : array[3_6.e-4,10_2] of string = {};"""
        expect = "Error on line 1 col 15: 36.e-4"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test_254(self):
        """Variable declarations"""
        input = """dope : array[3,10_2] of string = {1,{5.6e-34},4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    
    def test_255(self):
        """Variable declarations"""
        input = """dope: float = 1.2e-4+6*7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def test_256(self):
        """Variable declarations"""
        input = """name: string = "duc"::chau[5,1_7];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_257(self):
        """Variable declarations"""
        input = """avg: float = (a + b + c2)/3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_258(self):
        """Variable declarations"""
        input = """random_num: integer = ();"""
        expect = "Error on line 1 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 258))
        
    def test_259(self):
        input = """getName: function string (inherit out x:array[2_1,8] of float) {
                return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    
    def test_260(self):
        input = """arr[4_5,0]: function void () inherit getName {
                return {};
                }"""
        expect = "Error on line 1 col 3: ["
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_261(self):
        input = """ array [1,2] of array void """
        expect = "Error on line 1 col 1: array"
        self.assertTrue(TestParser.test(input, expect, 261))
    
    def test_262(self):
        input = """ array [, 12] of integer """
        expect = "Error on line 1 col 1: array"
        self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_263(self):
        input = """_45_0: function auto () {
                return arr[5_6,1.];
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_264(self):
        input = """d5: function void();
                }"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 264))
    
        
    def test_265(self):
        input = """fact: function integer (n: integer) {
            while (n == 10 || n == 20 && n == 30) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do printHello();
                    while (1 + 4 == 2);
                }
            }"""
        expect = "Error on line 2 col 32: =="
        self.assertTrue(TestParser.test(input, expect, 265))
    
    def test_266(self):
        input = """Tdk__9:auto = __6H[2,3_09] + foo() / 3.4e-9+7__0;"""
        expect = "Error on line 1 col 45: __0"
        self.assertTrue(TestParser.test(input, expect, 266))
 
    def test_267(self):
        self.assertTrue(TestParser.test(""" x: array [0, ] of float = 2;""", "Error on line 1 col 14: ]", 267))
        
    def test_268(self):
        self.assertTrue(TestParser.test(""" x: array [9., 2.e-4/*kol*/ of string = 1; """, "Error on line 1 col 11: 9.", 268))
        
    def test_269(self):
        self.assertTrue(TestParser.test(""" x: array [1.0E-24, 2] of float = 2; """, "Error on line 1 col 11: 1.0E-24", 269))
        
    def test_270(self):
        self.assertTrue(TestParser.test(""" x: array [a, b, +, {] of integer == 3; """, "Error on line 1 col 11: a", 270))

    def test_271(self):
        self.assertTrue(TestParser.test(""" x_t: array [1,2,3,4,5] of integer = 4.eE7 """, "Error on line 1 col 39: eE7", 271))
        
    def test_272(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            do { } while ((n == 10)  && (n == 30)); {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do {printHello();}
                    while (1 + 4 == 2);
                    for () {
                        while() {
                            if () {
                                x: integer = "E";
                            }
                            else
                            {
                                foo([2,3, (3,2), (e, x), ("+", "==")]);
                            }
                        }
                    }
                }
            """, "Error on line 7 col 25: )", 272))
        
    def test_273(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                    for (i = 1, i + arr(boon(7)), i == 2) {
                        while(true) {
                            if () {
                                x: integer = "E";
                            }
                            else
                            {
                                foo([2,3, (3,2), (e, x), ("+", "==")]);
                            }
                        }
                    }
                }
            """, "Error on line 4 col 32: )", 273))
        
    def test_274(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                    for (i = 1, i + arr(boon(7)), i == 2) {
                        while(true) {
                            break;
                            else
                            {
                                foo([2,3, (3,2), (e, x), ("+", "==")]);
                            }
                        }
                    }
                }
            """, "Error on line 5 col 28: else", 274))
        
    def test_275(self):
        self.assertTrue(TestParser.test("""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2 + (abs(9_1) && abs(10.2));
                     while (x > 1) {
                        if (x == 1)
                        i = i + 1;
                        break;
                        for (i = 0, i <= 10, i + 1.0_1_2) {
                            writeln();
                        }
                    }
                }
            }
        }
        """, "Error on line 11 col 52: _1_2", 275))

    def test_276(self):
        self.assertTrue(TestParser.test("""
        main: function void (x: integer, a_123: string) {
            {
                {
                    a[1+foo(2)] = 5 + 3 + 2 * 2 + (abs(9_1) && abs(10.2, array[572, boo(199)]));
                    }
                }
            }
        }
        """, "Error on line 5 col 73: array", 276))
        
    def test_277(self):
        self.assertTrue(TestParser.test("""
        main: function void (x: integer, a_123: string) {
            i: integer =0;
            {
                {
                    a[1+foo(2)] = a[b[3][4]]+5;
                }
            } 
        }
        """, "Error on line 6 col 40: [", 277))
        
    def test_278(self):
        self.assertTrue(TestParser.test("""_45_0: function auto () {
                return arr[5_6,1.];
                do {
                    helloworld(2);
                }
                while (n * 2 == 1) if (n == 0) return 1 else return (n - 1) + fact(n + 2);
                }""", "Error on line 6 col 35: if", 278))
        
    def test_279(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            while (n == 10 || n == 20 && n == 30) {
                    delta: integer = fact(3);
                    inc(x, delta, alpha);
                    do printHello();
                    while (1 + 4 == 2);
                }
            }""", "Error on line 2 col 32: ==", 279))
        
    def test_280(self):
        self.assertTrue(TestParser.test("""a: function void () {
                return arr[1];
                }""", "successful", 280))

    def test_281(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            continue;
            return;
            break;
            foo(return;);
            }""", "Error on line 5 col 16: return", 281))
        
    def test_282(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            {
                r,s: integer = 1,2,3,4,5,foo("y");
                r = 2.0;
                a,b: array [5] of integer;
                s = r * r * a;
                a[0] = s;
            }
            }""", "Error on line 3 col 34: ,", 282))
        
    def test_283(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            {
                s = r * r * a + array [5] of integer
                1,2,3,4,5,foo("y");
                a[0, foo(7.E)] = s;
            }""", "Error on line 3 col 32: array", 283))
        
    def test_284(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            {
                // string
            }""", "Error on line 4 col 13: <EOF>", 284))
        
    def test_285(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
            {
                /* x: string; */
                func: integer = /*0*/123;
            }
            }""", "successful", 285))

    def test_286(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                x: integer;
                y: float;
                y: string;
            }""", "successful", 286))
        
    def test_287(self):
        self.assertTrue(TestParser.test("""x: integer;
                y: float;
                y: string = "123";
            """, "successful", 287))
        
    def test_288(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                fact: function float(i[abc, 1]) {
                    return;
                }
            }""", "Error on line 2 col 22: function", 288))
        
    def test_289(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                x: integer = "abc"::123::3456
            }""", "Error on line 2 col 39: ::", 289))
        
    def test_290(self):
        self.assertTrue(TestParser.test("""fact: function integer (n: integer) {
                x: integer = "abc"::(a+c*array[1,3] of float)
            }""", "Error on line 2 col 41: array", 290))

    def test_291(self):
        self.assertTrue(TestParser.test("""
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
        }
        """, "successful", 291))
        
    def test_292(self):
        self.assertTrue(TestParser.test("""main: function void (x: integer, a_123: string) {""", "Error on line 1 col 49: <EOF>", 292))
        
    def test_293(self):
        self.assertTrue(TestParser.test("""main: function void (x: integer, a_123: string) {return;if(false){if(true){x:boolean = .; else return;}}""", "Error on line 1 col 87: .", 293))
        
    def test_294(self):
        self.assertTrue(TestParser.test("""x: float == "\\n" """, "Error on line 1 col 9: ==", 294))
        
    def test_295(self):
        self.assertTrue(TestParser.test("""x: string = (x+Y(3::4));""", "successful", 295))

    def test_296(self):
        self.assertTrue(TestParser.test("""x: integer = "e=="+(9.6&&4.3203)""", "Error on line 1 col 32: <EOF>", 296))
        
    def test_297(self):
        self.assertTrue(TestParser.test("""lp: function void (auto/**/x: integer);""", "Error on line 1 col 19: auto", 297))
        
    def test_298(self):
        self.assertTrue(TestParser.test(""" x: float = ""::" "+"\b?vn"*"a\\"\\\\" """, "Error on line 1 col 35: <EOF>", 298))
        
    def test_299(self):
        self.assertTrue(TestParser.test(""" a :auto = 1.+"\\n"::(x*y) """, "Error on line 1 col 26: <EOF>", 299))