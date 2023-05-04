# Generated from c:\Users\Admin\Desktop\HCMUT\HK222\PPL\Asm2\asignment2-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\7\2\u008a\n\2\f\2\16\2\u008d\13\2\3\2\5\2\u0090")
        buf.write("\n\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0098\n\3\f\3\16\3\u009b")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\u00a5\n\4\f")
        buf.write("\4\16\4\u00a8\13\4\3\4\3\4\6\4\u00ac\n\4\r\4\16\4\u00ad")
        buf.write("\7\4\u00b0\n\4\f\4\16\4\u00b3\13\4\3\4\3\4\5\4\u00b7\n")
        buf.write("\4\3\5\3\5\3\5\7\5\u00bc\n\5\f\5\16\5\u00bf\13\5\5\5\u00c1")
        buf.write("\n\5\3\5\3\5\5\5\u00c5\n\5\3\5\6\5\u00c8\n\5\r\5\16\5")
        buf.write("\u00c9\5\5\u00cc\n\5\3\5\3\5\3\5\3\5\7\5\u00d2\n\5\f\5")
        buf.write("\16\5\u00d5\13\5\3\5\3\5\5\5\u00d9\n\5\3\5\6\5\u00dc\n")
        buf.write("\5\r\5\16\5\u00dd\5\5\u00e0\n\5\3\6\3\6\5\6\u00e4\n\6")
        buf.write("\3\7\3\7\7\7\u00e8\n\7\f\7\16\7\u00eb\13\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\5\b\u00f2\n\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\6:\u01b0")
        buf.write("\n:\r:\16:\u01b1\3:\3:\3;\3;\5;\u01b8\n;\3;\3;\3;\7;\u01bd")
        buf.write("\n;\f;\16;\u01c0\13;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@")
        buf.write("\3A\3A\7A\u01cf\nA\fA\16A\u01d2\13A\3A\5A\u01d5\nA\3A")
        buf.write("\3A\3B\3B\7B\u01db\nB\fB\16B\u01de\13B\3B\3B\3B\3B\3B")
        buf.write("\3\u0099\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\2\25")
        buf.write("\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24")
        buf.write("-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64")
        buf.write("m\65o\66q\67s8u9w\2y\2{\2}\2\177:\u0081;\u0083<\3\2\20")
        buf.write("\3\2\f\f\3\3\f\f\3\2\62\62\4\2GGgg\4\2--//\n\2$$\61\61")
        buf.write("^^ddhhppttvv\6\2\f\f\17\17$$^^\5\2\n\f\16\17\"\"\4\2C")
        buf.write("\\c|\3\2\62;\3\2aa\3\2\63;\4\3\f\f\17\17\n\2$$))^^ddh")
        buf.write("hppttvv\2\u01f5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\3\u0085\3\2\2\2\5\u0093\3\2\2\2\7\u00b6\3\2\2\2\t\u00df")
        buf.write("\3\2\2\2\13\u00e3\3\2\2\2\r\u00e5\3\2\2\2\17\u00f1\3\2")
        buf.write("\2\2\21\u00f3\3\2\2\2\23\u00f6\3\2\2\2\25\u00f8\3\2\2")
        buf.write("\2\27\u00fd\3\2\2\2\31\u0103\3\2\2\2\33\u010b\3\2\2\2")
        buf.write("\35\u010e\3\2\2\2\37\u0113\3\2\2\2!\u0119\3\2\2\2#\u011f")
        buf.write("\3\2\2\2%\u0123\3\2\2\2\'\u012c\3\2\2\2)\u012f\3\2\2\2")
        buf.write("+\u0137\3\2\2\2-\u013e\3\2\2\2/\u0145\3\2\2\2\61\u014a")
        buf.write("\3\2\2\2\63\u0150\3\2\2\2\65\u0155\3\2\2\2\67\u0159\3")
        buf.write("\2\2\29\u0162\3\2\2\2;\u0165\3\2\2\2=\u016d\3\2\2\2?\u0173")
        buf.write("\3\2\2\2A\u0175\3\2\2\2C\u0177\3\2\2\2E\u0179\3\2\2\2")
        buf.write("G\u017b\3\2\2\2I\u017d\3\2\2\2K\u0180\3\2\2\2M\u0183\3")
        buf.write("\2\2\2O\u0186\3\2\2\2Q\u0189\3\2\2\2S\u018b\3\2\2\2U\u018d")
        buf.write("\3\2\2\2W\u0190\3\2\2\2Y\u0193\3\2\2\2[\u0195\3\2\2\2")
        buf.write("]\u0198\3\2\2\2_\u019a\3\2\2\2a\u019c\3\2\2\2c\u019e\3")
        buf.write("\2\2\2e\u01a0\3\2\2\2g\u01a2\3\2\2\2i\u01a4\3\2\2\2k\u01a6")
        buf.write("\3\2\2\2m\u01a8\3\2\2\2o\u01aa\3\2\2\2q\u01ac\3\2\2\2")
        buf.write("s\u01af\3\2\2\2u\u01b7\3\2\2\2w\u01c1\3\2\2\2y\u01c3\3")
        buf.write("\2\2\2{\u01c5\3\2\2\2}\u01c7\3\2\2\2\177\u01c9\3\2\2\2")
        buf.write("\u0081\u01cc\3\2\2\2\u0083\u01d8\3\2\2\2\u0085\u0086\7")
        buf.write("\61\2\2\u0086\u0087\7\61\2\2\u0087\u008b\3\2\2\2\u0088")
        buf.write("\u008a\n\2\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008f\3")
        buf.write("\2\2\2\u008d\u008b\3\2\2\2\u008e\u0090\t\3\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\b\2\2\2\u0092")
        buf.write("\4\3\2\2\2\u0093\u0094\7\61\2\2\u0094\u0095\7,\2\2\u0095")
        buf.write("\u0099\3\2\2\2\u0096\u0098\13\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\u009b\3\2\2\2\u0099\u009a\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\b\3\2\2\u00a0\6\3\2\2\2\u00a1\u00b7\t\4\2")
        buf.write("\2\u00a2\u00a6\5}?\2\u00a3\u00a5\5y=\2\u00a4\u00a3\3\2")
        buf.write("\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00b1\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9")
        buf.write("\u00ab\5{>\2\u00aa\u00ac\5y=\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00b0\3\2\2\2\u00af\u00a9\3\2\2\2\u00b0\u00b3\3")
        buf.write("\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\b\4\3\2\u00b5")
        buf.write("\u00b7\3\2\2\2\u00b6\u00a1\3\2\2\2\u00b6\u00a2\3\2\2\2")
        buf.write("\u00b7\b\3\2\2\2\u00b8\u00c0\5\7\4\2\u00b9\u00bd\5k\66")
        buf.write("\2\u00ba\u00bc\5y=\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3")
        buf.write("\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00b9\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00cb\3\2\2\2\u00c2\u00c4\t\5\2\2")
        buf.write("\u00c3\u00c5\t\6\2\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c8\5y=\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c2\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\b")
        buf.write("\5\4\2\u00ce\u00e0\3\2\2\2\u00cf\u00d3\5k\66\2\u00d0\u00d2")
        buf.write("\5y=\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d8\t\5\2\2\u00d7\u00d9\t\6\2\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\3")
        buf.write("\2\2\2\u00da\u00dc\5y=\2\u00db\u00da\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00b8\3\2\2\2\u00df\u00cf\3\2\2\2")
        buf.write("\u00e0\n\3\2\2\2\u00e1\u00e4\5\37\20\2\u00e2\u00e4\5/")
        buf.write("\30\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\f")
        buf.write("\3\2\2\2\u00e5\u00e9\7$\2\2\u00e6\u00e8\5\17\b\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00ec\u00ed\7$\2\2\u00ed\u00ee\b\7\5\2\u00ee\16")
        buf.write("\3\2\2\2\u00ef\u00f2\5\21\t\2\u00f0\u00f2\5\23\n\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\20\3\2\2\2\u00f3")
        buf.write("\u00f4\7^\2\2\u00f4\u00f5\t\7\2\2\u00f5\22\3\2\2\2\u00f6")
        buf.write("\u00f7\n\b\2\2\u00f7\24\3\2\2\2\u00f8\u00f9\7c\2\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write("\26\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7m\2\2\u0102")
        buf.write("\30\3\2\2\2\u0103\u0104\7d\2\2\u0104\u0105\7q\2\2\u0105")
        buf.write("\u0106\7q\2\2\u0106\u0107\7n\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("\u0109\7c\2\2\u0109\u010a\7p\2\2\u010a\32\3\2\2\2\u010b")
        buf.write("\u010c\7f\2\2\u010c\u010d\7q\2\2\u010d\34\3\2\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f\u0110\7n\2\2\u0110\u0111\7u\2\2\u0111")
        buf.write("\u0112\7g\2\2\u0112\36\3\2\2\2\u0113\u0114\7h\2\2\u0114")
        buf.write("\u0115\7c\2\2\u0115\u0116\7n\2\2\u0116\u0117\7u\2\2\u0117")
        buf.write("\u0118\7g\2\2\u0118 \3\2\2\2\u0119\u011a\7h\2\2\u011a")
        buf.write("\u011b\7n\2\2\u011b\u011c\7q\2\2\u011c\u011d\7c\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\"\3\2\2\2\u011f\u0120\7h\2\2\u0120")
        buf.write("\u0121\7q\2\2\u0121\u0122\7t\2\2\u0122$\3\2\2\2\u0123")
        buf.write("\u0124\7h\2\2\u0124\u0125\7w\2\2\u0125\u0126\7p\2\2\u0126")
        buf.write("\u0127\7e\2\2\u0127\u0128\7v\2\2\u0128\u0129\7k\2\2\u0129")
        buf.write("\u012a\7q\2\2\u012a\u012b\7p\2\2\u012b&\3\2\2\2\u012c")
        buf.write("\u012d\7k\2\2\u012d\u012e\7h\2\2\u012e(\3\2\2\2\u012f")
        buf.write("\u0130\7k\2\2\u0130\u0131\7p\2\2\u0131\u0132\7v\2\2\u0132")
        buf.write("\u0133\7g\2\2\u0133\u0134\7i\2\2\u0134\u0135\7g\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136*\3\2\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\u013a\7v\2\2\u013a\u013b\7w\2\2\u013b")
        buf.write("\u013c\7t\2\2\u013c\u013d\7p\2\2\u013d,\3\2\2\2\u013e")
        buf.write("\u013f\7u\2\2\u013f\u0140\7v\2\2\u0140\u0141\7t\2\2\u0141")
        buf.write("\u0142\7k\2\2\u0142\u0143\7p\2\2\u0143\u0144\7i\2\2\u0144")
        buf.write(".\3\2\2\2\u0145\u0146\7v\2\2\u0146\u0147\7t\2\2\u0147")
        buf.write("\u0148\7w\2\2\u0148\u0149\7g\2\2\u0149\60\3\2\2\2\u014a")
        buf.write("\u014b\7y\2\2\u014b\u014c\7j\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7n\2\2\u014e\u014f\7g\2\2\u014f\62\3\2\2\2\u0150")
        buf.write("\u0151\7x\2\2\u0151\u0152\7q\2\2\u0152\u0153\7k\2\2\u0153")
        buf.write("\u0154\7f\2\2\u0154\64\3\2\2\2\u0155\u0156\7q\2\2\u0156")
        buf.write("\u0157\7w\2\2\u0157\u0158\7v\2\2\u0158\66\3\2\2\2\u0159")
        buf.write("\u015a\7e\2\2\u015a\u015b\7q\2\2\u015b\u015c\7p\2\2\u015c")
        buf.write("\u015d\7v\2\2\u015d\u015e\7k\2\2\u015e\u015f\7p\2\2\u015f")
        buf.write("\u0160\7w\2\2\u0160\u0161\7g\2\2\u01618\3\2\2\2\u0162")
        buf.write("\u0163\7q\2\2\u0163\u0164\7h\2\2\u0164:\3\2\2\2\u0165")
        buf.write("\u0166\7k\2\2\u0166\u0167\7p\2\2\u0167\u0168\7j\2\2\u0168")
        buf.write("\u0169\7g\2\2\u0169\u016a\7t\2\2\u016a\u016b\7k\2\2\u016b")
        buf.write("\u016c\7v\2\2\u016c<\3\2\2\2\u016d\u016e\7c\2\2\u016e")
        buf.write("\u016f\7t\2\2\u016f\u0170\7t\2\2\u0170\u0171\7c\2\2\u0171")
        buf.write("\u0172\7{\2\2\u0172>\3\2\2\2\u0173\u0174\7-\2\2\u0174")
        buf.write("@\3\2\2\2\u0175\u0176\7/\2\2\u0176B\3\2\2\2\u0177\u0178")
        buf.write("\7,\2\2\u0178D\3\2\2\2\u0179\u017a\7\61\2\2\u017aF\3\2")
        buf.write("\2\2\u017b\u017c\7\'\2\2\u017cH\3\2\2\2\u017d\u017e\7")
        buf.write("(\2\2\u017e\u017f\7(\2\2\u017fJ\3\2\2\2\u0180\u0181\7")
        buf.write("~\2\2\u0181\u0182\7~\2\2\u0182L\3\2\2\2\u0183\u0184\7")
        buf.write("?\2\2\u0184\u0185\7?\2\2\u0185N\3\2\2\2\u0186\u0187\7")
        buf.write("#\2\2\u0187\u0188\7?\2\2\u0188P\3\2\2\2\u0189\u018a\7")
        buf.write(">\2\2\u018aR\3\2\2\2\u018b\u018c\7@\2\2\u018cT\3\2\2\2")
        buf.write("\u018d\u018e\7>\2\2\u018e\u018f\7?\2\2\u018fV\3\2\2\2")
        buf.write("\u0190\u0191\7@\2\2\u0191\u0192\7?\2\2\u0192X\3\2\2\2")
        buf.write("\u0193\u0194\7#\2\2\u0194Z\3\2\2\2\u0195\u0196\7<\2\2")
        buf.write("\u0196\u0197\7<\2\2\u0197\\\3\2\2\2\u0198\u0199\7*\2\2")
        buf.write("\u0199^\3\2\2\2\u019a\u019b\7+\2\2\u019b`\3\2\2\2\u019c")
        buf.write("\u019d\7}\2\2\u019db\3\2\2\2\u019e\u019f\7\177\2\2\u019f")
        buf.write("d\3\2\2\2\u01a0\u01a1\7]\2\2\u01a1f\3\2\2\2\u01a2\u01a3")
        buf.write("\7_\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7?\2\2\u01a5j\3\2\2")
        buf.write("\2\u01a6\u01a7\7\60\2\2\u01a7l\3\2\2\2\u01a8\u01a9\7.")
        buf.write("\2\2\u01a9n\3\2\2\2\u01aa\u01ab\7=\2\2\u01abp\3\2\2\2")
        buf.write("\u01ac\u01ad\7<\2\2\u01adr\3\2\2\2\u01ae\u01b0\t\t\2\2")
        buf.write("\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4")
        buf.write("\b:\2\2\u01b4t\3\2\2\2\u01b5\u01b8\5w<\2\u01b6\u01b8\5")
        buf.write("{>\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01be")
        buf.write("\3\2\2\2\u01b9\u01bd\5w<\2\u01ba\u01bd\5y=\2\u01bb\u01bd")
        buf.write("\5{>\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bfv\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c2\t\n\2\2\u01c2x\3\2\2\2\u01c3\u01c4\t\13\2\2\u01c4")
        buf.write("z\3\2\2\2\u01c5\u01c6\t\f\2\2\u01c6|\3\2\2\2\u01c7\u01c8")
        buf.write("\t\r\2\2\u01c8~\3\2\2\2\u01c9\u01ca\13\2\2\2\u01ca\u01cb")
        buf.write("\b@\6\2\u01cb\u0080\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf")
        buf.write("\5\17\b\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d3\u01d5\t\16\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\bA\7\2\u01d7")
        buf.write("\u0082\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9\u01db\5\17\b\2")
        buf.write("\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01df\u01e0\7^\2\2\u01e0\u01e1\n\17\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2\u01e3\bB\b\2\u01e3\u0084\3\2\2\2")
        buf.write("\35\2\u008b\u008f\u0099\u00a6\u00ad\u00b1\u00b6\u00bd")
        buf.write("\u00c0\u00c4\u00c9\u00cb\u00d3\u00d8\u00dd\u00df\u00e3")
        buf.write("\u00e9\u00f1\u01b1\u01b7\u01bc\u01be\u01d0\u01d4\u01dc")
        buf.write("\t\b\2\2\3\4\2\3\5\3\3\7\4\3@\5\3A\6\3B\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SL_CMT = 1
    MUL_CMT = 2
    INTLIT = 3
    FLOATLIT = 4
    BOOLEANLIT = 5
    STRINGLIT = 6
    AUTO = 7
    BREAK = 8
    BOOLEAN = 9
    DO = 10
    ELSE = 11
    FALSE = 12
    FLOAT = 13
    FOR = 14
    FUNCTION = 15
    IF = 16
    INTEGER = 17
    RETURN = 18
    STRING = 19
    TRUE = 20
    WHILE = 21
    VOID = 22
    OUT = 23
    CONTINUE = 24
    OF = 25
    INHERIT = 26
    ARRAY = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    AND = 33
    OR = 34
    DBL_EQ = 35
    UEQ = 36
    LESS = 37
    MOR = 38
    LESS_EQ = 39
    MOR_EQ = 40
    EXCLAM = 41
    DBL_COLON = 42
    LB = 43
    RB = 44
    CUR_LB = 45
    CUR_RB = 46
    SQU_LB = 47
    SQU_RB = 48
    EQ = 49
    DOT = 50
    COMMA = 51
    SEMI = 52
    COLON = 53
    WS = 54
    ID = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'!'", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'='", "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SL_CMT", "MUL_CMT", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "DBL_EQ", "UEQ", 
            "LESS", "MOR", "LESS_EQ", "MOR_EQ", "EXCLAM", "DBL_COLON", "LB", 
            "RB", "CUR_LB", "CUR_RB", "SQU_LB", "SQU_RB", "EQ", "DOT", "COMMA", 
            "SEMI", "COLON", "WS", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "SL_CMT", "MUL_CMT", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "STRINGLIT", "STRINGCHAR", "ESC", "SAFECODEPOINT", "AUTO", 
                  "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "DBL_EQ", 
                  "UEQ", "LESS", "MOR", "LESS_EQ", "MOR_EQ", "EXCLAM", "DBL_COLON", 
                  "LB", "RB", "CUR_LB", "CUR_RB", "SQU_LB", "SQU_RB", "EQ", 
                  "DOT", "COMMA", "SEMI", "COLON", "WS", "ID", "CHAR", "DIGIT", 
                  "UNDERSCORE", "NON_ZERO", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.INTLIT_action 
            actions[3] = self.FLOATLIT_action 
            actions[5] = self.STRINGLIT_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	if (self.text[-1] in ['\n', '\r']): 
            		raise UncloseString(self.text[1:-1]) 
            	else: 
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:])

     


