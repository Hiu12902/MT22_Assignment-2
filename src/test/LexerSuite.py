import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_100(self):
        self.assertTrue(TestLexer.test(	"""hiu_______nguyn?eiodf""", "hiu_______nguyn,Error Token ?", 100))
        
    def test_101(self):
        self.assertTrue(TestLexer.test(	""" /* abcdef """, "/,*,abcdef,<EOF>", 101))
        
    def test_102(self):
        self.assertTrue(TestLexer.test(	"""0.34_342E-10
""", "0.34,_342E,-,10,<EOF>", 102))
        
    def test_103(self):
        self.assertTrue(TestLexer.test(""" 1.0e567 u7 """, "1.0e567,u7,<EOF>", 103))
        
    def test_104(self):
        self.assertTrue(TestLexer.test(	""" 12 """, "12,<EOF>", 104))
        
    def test_105(self):
        self.assertTrue(TestLexer.test(	"""0__12""", "0,__12,<EOF>", 105))

    def test_106(self):
        self.assertTrue(TestLexer.test("""1_2_0""", "120,<EOF>", 106))
        
    def test_107(self):
        self.assertTrue(TestLexer.test("""_0_1_""", "_0_1_,<EOF>", 107))
        
    def test_108(self):
        self.assertTrue(TestLexer.test("""00_0""", "0,0,_0,<EOF>", 108))
        
    def test_109(self):
        self.assertTrue(TestLexer.test("""_0_0""", "_0_0,<EOF>", 109))
        
    def test_110(self):
        self.assertTrue(TestLexer.test("""0.1_2""", "0.1,_2,<EOF>", 110))

    def test_111(self):
        self.assertTrue(TestLexer.test("""1._e23""", "1.,_e23,<EOF>", 111))
        
    def test_112(self):
        self.assertTrue(TestLexer.test("""2_3_4.31_3""", "234.31,_3,<EOF>", 112))
        
    def test_113(self):
        self.assertTrue(TestLexer.test("""2_3.""", "23.,<EOF>", 113))
        
    def test_114(self):
        self.assertTrue(TestLexer.test("""2.3_0__1""", "2.3,_0__1,<EOF>", 114))
        
    def test_115(self):
        self.assertTrue(TestLexer.test(""".45_2_0""", ".,4520,<EOF>", 115))

    def test_116(self):
        self.assertTrue(TestLexer.test("""10.-e4_3""", "10.,-,e4_3,<EOF>", 116))
        
    def test_117(self):
        self.assertTrue(TestLexer.test("""000_2.e-""", "0,0,0,_2,.,e,-,<EOF>", 117))
        
    def test_118(self):
        self.assertTrue(TestLexer.test("""1_2_3.E02_1""", "123.E02,_1,<EOF>", 118))
        
    def test_119(self):
        self.assertTrue(TestLexer.test(""""abc""", "Unclosed String: abc", 119))
        
    def test_120(self):
        self.assertTrue(TestLexer.test(""" "abc" """, "abc,<EOF>", 120))

    def test_121(self):
        self.assertTrue(TestLexer.test(""" "abc\ndef" """, "Unclosed String: abc", 121))
        
    def test_122(self):
        self.assertTrue(TestLexer.test(""" "abc\\ndef\\r" """, "abc\\ndef\\r,<EOF>", 122))
        
    def test_123(self):
        self.assertTrue(TestLexer.test(""" "abc123?" """, "abc123?,<EOF>", 123))
        
    def test_124(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\" """, "abc\\\,<EOF>", 124))
        
    def test_125(self):
        self.assertTrue(TestLexer.test(""" "\\n abc def" """, "\\n abc def,<EOF>", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test(""" " abc \\" def " """, " abc \\\" def ,<EOF>", 126))
        
    def test_127(self):
        self.assertTrue(TestLexer.test(""" "abc\pdef" """, "Illegal Escape In String: abc\p", 127))
        
    def test_128(self):
        self.assertTrue(TestLexer.test("""abc""", "abc,<EOF>", 128))
        
    def test_129(self):
        self.assertTrue(TestLexer.test("""ABC""", "ABC,<EOF>", 129))
        
    def test_130(self):
        self.assertTrue(TestLexer.test("""A_B_C """, "A_B_C,<EOF>", 130))

    def test_131(self):
        self.assertTrue(TestLexer.test(""" A_b_0 """, "A_b_0,<EOF>", 131))
        
    def test_132(self):
        self.assertTrue(TestLexer.test("""_1aB_0""", "_1aB_0,<EOF>", 132))
        
    def test_133(self):
        self.assertTrue(TestLexer.test("""0AbcC""", "0,AbcC,<EOF>", 133))
        
    def test_134(self):
        self.assertTrue(TestLexer.test("""oUt""", "oUt,<EOF>", 134))
        
    def test_135(self):
        self.assertTrue(TestLexer.test("""integer_abc""", "integer_abc,<EOF>", 135))

    def test_136(self):
        self.assertTrue(TestLexer.test("""a?#b_c""", "a,Error Token ?", 136))
        
    def test_137(self):
        self.assertTrue(TestLexer.test("""+""", "+,<EOF>", 137))
        
    def test_138(self):
        self.assertTrue(TestLexer.test("""%%""", "%,%,<EOF>", 138))
        
    def test_139(self):
        self.assertTrue(TestLexer.test("""?""", "Error Token ?", 139))
        
    def test_140(self):
        self.assertTrue(TestLexer.test(""" "abc+==def" """, "abc+==def,<EOF>", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test(""" "aBc%1_23.e45" """, "aBc%1_23.e45,<EOF>", 141))
        
    def test_142(self):
        self.assertTrue(TestLexer.test(""" ".0" """, ".0,<EOF>", 142))
        
    def test_143(self):
        self.assertTrue(TestLexer.test(""" "a*b" """, "a*b,<EOF>", 143))
        
    def test_144(self):
        self.assertTrue(TestLexer.test(""" "a*+=0_b1_4.E2" """, "a*+=0_b1_4.E2,<EOF>", 144))
        
    def test_145(self):
        self.assertTrue(TestLexer.test(""" "!+=" """, "!+=,<EOF>", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test(""" "\\w?vn" """, "Illegal Escape In String: \w", 146))
        
    def test_147(self):
        self.assertTrue(TestLexer.test(""" abc::def """, "abc,::,def,<EOF>", 147))
        
    def test_148(self):
        self.assertTrue(TestLexer.test(""" {} """, "{,},<EOF>", 148))
        
    def test_149(self):
        self.assertTrue(TestLexer.test("""{1,2,3}""", "{,1,,,2,,,3,},<EOF>", 149))
        
    def test_150(self):
        self.assertTrue(TestLexer.test(""" {"a", "b", "c"} """, "{,a,,,b,,,c,},<EOF>", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test(""" {+, _, +} """, "{,+,,,_,,,+,},<EOF>", 151))
        
    def test_152(self):
        self.assertTrue(TestLexer.test(""" {(),;} """, "{,(,),,,;,},<EOF>", 152))
        
    def test_153(self):
        self.assertTrue(TestLexer.test("""{a, 1, "b"}""", "{,a,,,1,,,b,},<EOF>", 153))
        
    def test_154(self):
        self.assertTrue(TestLexer.test(""" {(a1bv,} """, "{,(,a1bv,,,},<EOF>", 154))
        
    def test_155(self):
        self.assertTrue(TestLexer.test(""" {__1.0e7H} """, "{,__1,.0e7,H,},<EOF>", 155))

    def test_156(self):
        self.assertTrue(TestLexer.test("""aaaA_1223++DnN""", "aaaA_1223,+,+,DnN,<EOF>", 156))
        
    def test_157(self):
        self.assertTrue(TestLexer.test(""" _x_XX_2o0-.12_? """, "_x_XX_2o0,-,.,12,_,Error Token ?", 157))
        
    def test_158(self):
        self.assertTrue(TestLexer.test(""" "=f(b=na8" """, "=f(b=na8,<EOF>", 158))
        
    def test_159(self):
        self.assertTrue(TestLexer.test(""" L-t!2SQp """, "L,-,t,!,2,SQp,<EOF>", 159))
        
    def test_160(self):
        self.assertTrue(TestLexer.test(""" 23x2+23abcd_\"!@*32==23.34_23eEEEEe-10+123.123 """, "23,x2,+,23,abcd_,Unclosed String: !@*32==23.34_23eEEEEe-10+123.123 ", 160))

    def test_161(self):
        self.assertTrue(TestLexer.test("""fehG}tHU""", "fehG,},tHU,<EOF>", 161))
        
    def test_162(self):
        self.assertTrue(TestLexer.test("""P:2SWw)!""", "P,:,2,SWw,),!,<EOF>", 162))
        
    def test_163(self):
        self.assertTrue(TestLexer.test("""yQjk{/4___==uUUeE""", "yQjk,{,/,4,___,==,uUUeE,<EOF>", 163))
        
    def test_164(self):
        self.assertTrue(TestLexer.test(""" P$.e=+y*fe02=lwe'""", "P,Error Token $", 164))
        
    def test_165(self):
        self.assertTrue(TestLexer.test("""wew\\f[ge\fm"\\\]22VUUF)08H""", "wew,Error Token \\", 165))

    def test_166(self):
        self.assertTrue(TestLexer.test("""42..eE=2CVzBF[""", "42.,.,eE,=,2,CVzBF,[,<EOF>", 166))
        
    def test_167(self):
        self.assertTrue(TestLexer.test(""" 9%St?::5 """, "9,%,St,Error Token ?", 167))
        
    def test_168(self):
        self.assertTrue(TestLexer.test("""BBc#%!.4566e61.6e==""", "BBc,Error Token #", 168))
        
    def test_169(self):
        self.assertTrue(TestLexer.test(""":vSWjU=6""", ":,vSWjU,=,6,<EOF>", 169))
        
    def test_170(self):
        self.assertTrue(TestLexer.test(""" )W%FXbZ! """, "),W,%,FXbZ,!,<EOF>", 170))

    def test_171(self):
        self.assertTrue(TestLexer.test(""" BGj6f*Cwz2 """, "BGj6f,*,Cwz2,<EOF>", 171))
        
    def test_172(self):
        self.assertTrue(TestLexer.test("""AxeNcZ{{TT""", "AxeNcZ,{,{,TT,<EOF>", 172))
        
    def test_173(self):
        self.assertTrue(TestLexer.test("""b]GfN2x??H""", "b,],GfN2x,Error Token ?", 173))
        
    def test_174(self):
        self.assertTrue(TestLexer.test("""#V}mLt5YF.""", "Error Token #", 174))
        
    def test_175(self):
        self.assertTrue(TestLexer.test("""r2kn        2rkiah__ qw\\n""", "r2kn,2,rkiah__,qw,Error Token \\", 175))

    def test_176(self):
        self.assertTrue(TestLexer.test("""dAt:TQb.YM""", "dAt,:,TQb,.,YM,<EOF>", 176))
        
    def test_177(self):
        self.assertTrue(TestLexer.test("""(Z#w3fg$K@""", "(,Z,Error Token #", 177))
        
    def test_178(self):
        self.assertTrue(TestLexer.test("""8NW])M53z)""", "8,NW,],),M53z,),<EOF>", 178))
        
    def test_179(self):
        self.assertTrue(TestLexer.test("""{9;tV)}6{X""", "{,9,;,tV,),},6,{,X,<EOF>", 179))
        
    def test_180(self):
        self.assertTrue(TestLexer.test(""" R[j%.FAZ?x """, "R,[,j,%,.,FAZ,Error Token ?", 180))

    def test_181(self):
        self.assertTrue(TestLexer.test(""" *Tdyg)#*_n """, "*,Tdyg,),Error Token #", 181))
        
    def test_182(self):
        self.assertTrue(TestLexer.test("""c,cF=K%W8C""", "c,,,cF,=,K,%,W8C,<EOF>", 182))
        
    def test_183(self):
        self.assertTrue(TestLexer.test(""":-jn4i$.$X""", ":,-,jn4i,Error Token $", 183))
        
    def test_184(self):
        self.assertTrue(TestLexer.test("""{9VA,A3Jm)""", "{,9,VA,,,A3Jm,),<EOF>", 184))
        
    def test_185(self):
        self.assertTrue(TestLexer.test("""_[{{c[:VB_""", "_,[,{,{,c,[,:,VB_,<EOF>", 185))

    def test_186(self):
        self.assertTrue(TestLexer.test("""eRDY#Y]nfz""", "eRDY,Error Token #", 186))
        
    def test_187(self):
        self.assertTrue(TestLexer.test("""}J?ybxD/""", "},J,Error Token ?", 187))
        
    def test_188(self):
        self.assertTrue(TestLexer.test("""(B?#_E4d""", "(,B,Error Token ?", 188))
        
    def test_189(self):
        self.assertTrue(TestLexer.test("""*[#2[4rd""", "*,[,Error Token #", 189))
        
    def test_190(self):
        self.assertTrue(TestLexer.test(""" jH=k}8d_ """, "jH,=,k,},8,d_,<EOF>", 190))

    def test_191(self):
        self.assertTrue(TestLexer.test(""" gL#.w?-([@dq[-roq2 p].k'afaef] """, "gL,Error Token #", 191))
        
    def test_192(self):
        self.assertTrue(TestLexer.test("""32
                                       <gq]I-I-""", "32,<,gq,],I,-,I,-,<EOF>", 192))
        
    def test_193(self):
        self.assertTrue(TestLexer.test(""" "AbC\...]]=" """, "Illegal Escape In String: AbC\.", 193))
        
    def test_194(self):
        self.assertTrue(TestLexer.test(""";(3hwY5L""", ";,(,3,hwY5L,<EOF>", 194))
        
    def test_195(self):
        self.assertTrue(TestLexer.test("""h.;wed-1=}#}R!{+FAL""", "h,.,;,wed,-,1,=,},Error Token #", 195))

    def test_196(self):
        self.assertTrue(TestLexer.test("""'e==9.64.3203""", "Error Token '", 196))
        
    def test_197(self):
        self.assertTrue(TestLexer.test(""" lp;SFfEEWQy78t9f. """, "lp,;,SFfEEWQy78t9f,.,<EOF>", 197))
        
    def test_198(self):
        self.assertTrue(TestLexer.test(""" """ "\\\b?vn" """ """, "Error Token \\", 198))
        
    def test_199(self):
        self.assertTrue(TestLexer.test(""" a \\\\\\ """, "a,Error Token \\", 199))
