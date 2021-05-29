from lex.Token import Token
from lex.constants import Constants
from error import LexicalError

class Lexcial:
    def __init__(self):
        # 报错行列
        self.mRow = 1
        self.mLine = 0
        self.error = None

        self.TOKENIZE_CONSENQUENCE = 1

        self.currentState = 'A'
        self.buf = ''
        self.text = ''

        self.result = list()
        self.tokens = list()
        self.variable = list()
        self.constant = list()

        self.constants = Constants()

    def load_resource(self, resource):
        self.text = resource

    def initialize(self):
        self.currentState = 'A'
        self.buf = ''

    def get_output(self):
        return self.result, self.variable, self.constant, self.tokens

    def get_error(self):
        return self.error

    def tokenizer(self,ch):
        while True:
            if self.currentState == 'A':
                if (ch == ' ' or ch == '\n' or ch == '\t' or ch == '\r'):
                    self.currentState = 'A'
                    return
                elif (ch in self.constants.letterSet or ch == '_'):  # 开始为下划线或者字母
                    self.buf = self.buf + ch
                    self.currentState = 'B'  # 标识符方向
                    return
                elif (ch in self.constants.digitSet):  # 数字开始
                    self.buf = self.buf + ch
                    self.currentState = 'C'  # 整数
                    return
                elif (ch == '\''):
                    self.buf = self.buf + ch
                    self.currentState = 'D'  # 字符常量
                    return
                elif (ch == '\"'):
                    self.buf = self.buf + ch
                    self.currentState = 'G'  # 字符串常量
                    return
                elif (ch == '/'):
                    self.buf = self.buf + ch
                    self.currentState = 'K'  # 不确定，先按照注释处理
                    return
                ######################### 操作符部分 #########################
                elif (ch == '+'):
                    self.buf = self.buf + ch
                    self.currentState = 'A+'
                    return
                elif (ch == '-'):
                    self.buf = self.buf + ch
                    self.currentState = 'A-'
                    return
                elif (ch == '*'):
                    self.buf = self.buf + ch
                    self.currentState = 'A*'
                    return
                elif (ch == '&'):
                    self.buf = self.buf + ch
                    self.currentState = 'A&'
                    return
                elif (ch == '^'):
                    self.buf = self.buf + ch
                    self.currentState = 'A^'
                    return
                elif (ch == '|'):
                    self.buf = self.buf + ch
                    self.currentState = 'A|'
                    return
                elif (ch == '='):
                    self.buf = self.buf + ch
                    self.currentState = 'A='
                    return
                elif (ch == '!'):
                    self.buf = self.buf + ch
                    self.currentState = 'A!'
                    return
                elif (ch == '>'):
                    self.buf = self.buf + ch
                    self.currentState = 'A>'
                    return
                elif (ch == '<'):
                    self.buf = self.buf + ch
                    self.currentState = 'A<'
                    return
                elif (ch in self.constants.boardSet):
                    self.result.append((self.constants.KeyIndex[ch], "--"))
                    self.tokens.append(Token(self.constants.TokenIndex[ch], ch, self.mRow))
                    self.initialize()
                    return
                # elif (ch == '$'):
                #     self.buf = self.buf + ch
                #     self.currentState = '$'
                else:
                    self.error = LexicalError("不可识别的字符",self.mRow,self.mLine)
                    self.TOKENIZE_CONSENQUENCE = 0
                    return

            ############## 状态B: 标识符或关键字 #################
            elif self.currentState == 'B':
                if (ch == '_' or ch in self.constants.letterSet or ch in self.constants.digitSet):
                    self.buf = self.buf + ch
                    self.currentState = 'B'
                    return
                else:  # 完整的标识符或者关键字后面是space等符号，代表前者已经输入结束
                    if (self.buf in self.constants.keywordSet):
                        self.result.append((self.constants.KeyIndex[self.buf], "--"))
                        self.tokens.append(Token(self.buf, self.buf, self.mRow))
                    else:
                        if self.buf not in self.variable:
                            self.variable.append(self.buf)
                            self.result.append((61, "variable[%d]" % (len(self.variable) - 1)))
                            self.tokens.append(Token('id', self.buf, self.mRow))
                        else:
                            self.result.append((61, "variable[%d]" % (self.variable.index(self.buf) + 1)))
                            self.tokens.append(Token('id', self.buf, self.mRow))
                    self.initialize()
                    continue

            ############## 状态C：数字 #################
            elif self.currentState == 'C':
                if (ch in self.constants.digitSet):
                    self.buf = self.buf + ch
                    self.currentState = 'C'
                    return
                else:  # 可接受状态
                    self.result.append((62, "%s" % (bin(int(self.buf)).replace('0b', ''))))
                    self.tokens.append(Token('num', "%s" % (bin(int(self.buf)).replace('0b', '')), self.mRow))
                    self.initialize()
                    continue

            ############## 状态D： #################
            elif self.currentState == 'D':
                if (ch != '\'' and ch != '\\'):  # 正确的接收字符
                    self.buf = self.buf + ch
                    self.currentState = 'E'
                    return
                elif (ch != '\'' and ch == '\\'):  # 接收的转义字符
                    self.buf = self.buf + ch
                    self.currentState = 'F'
                    return
                else:
                    self.error = LexicalError('空白或无效的字符',self.mRow,self.mLine)
                    return

            ##############     状态E        #################
            elif self.currentState == 'E':
                if (ch == '\''):
                    self.buf = self.buf + ch
                    self.currentState = 'H'
                    continue
                else:
                    self.error = LexicalError('字符常量长度大于一',self.mRow,self.mRow)
                    return

            ##############     状态H        #################
            elif self.currentState == 'H':
                self.constant.append(self.buf)
                self.result.append((71, "constant[%d]" % (len(self.constant) - 1)))
                self.tokens.append(Token(71, self.buf, self.mRow))
                self.initialize()
                return

            ##############     状态F         #################
            elif self.currentState == 'F':
                if (ch in self.constants.switchCharSet):
                    self.buf = self.buf + ch
                    self.currentState = 'E'
                    return
                else:
                    self.error = LexicalError('无效的转义字符',self.mRow,self.mRow)
                    return

            ##############     状态G         #################
            elif self.currentState == 'G':
                if (ch != '\"' and ch != '\\'):  # 接收正常字符
                    self.buf = self.buf + ch
                    self.currentState = 'G'
                    return
                elif (ch != '\'' and ch == '\\'):  # 接收转义字符
                    self.buf = self.buf + ch
                    self.currentState = 'I'
                    return
                elif (ch == '\"'):  # 结束
                    self.buf = self.buf + ch
                    self.currentState = 'J'

            ##############     状态I         #################
            elif self.currentState == 'I':
                if (ch in self.constants.switchCharSet):
                    self.buf = self.buf + ch
                    self.currentState = 'G'
                    return
                else:
                    self.error = LexicalError('无效的转义字符',self.mRow,self.mRow)
                    return

            ##############     状态J         #################
            elif self.currentState == 'J':
                self.constant.append(self.buf)
                self.result.append((71, "constant[%d]" % (len(self.constant) - 1)))
                self.tokens.append(Token('', self.buf, self.mRow))
                self.initialize()
                return

            ##############     状态K         #################
            elif self.currentState == 'K':
                if (ch == '*'):
                    self.buf = self.buf[0:len(self.buf) - 1]  # 是注释，退去上一个/
                    self.currentState = 'L'
                    return
                elif (ch == '/'):  # 单行注释
                    self.buf = self.buf[0:len(self.buf) - 1]  # 是注释，退去上一个/
                    self.currentState = 'O'
                    return
                elif (ch == '='):
                    self.buf = self.buf + ch
                    self.currentState = 'B='
                    return
                else:
                    self.result.append((5, "--"))
                    self.tokens.append(Token('division', self.buf, self.mRow))
                    self.initialize()
                    continue

            ##############     状态L         #################
            elif self.currentState == 'L':
                if (ch != '*'):
                    self.currentState = 'L'
                    return
                elif (ch == '*'):
                    self.currentState = 'M'
                    return
            ##############     状态M         #################
            elif self.currentState == 'M':
                if (ch == '/'):
                    self.currentState = 'N'
                    return
                else:
                    self.currentState = 'L'

            ##############     状态N         #################
            elif self.currentState == 'N':
                self.currentState = 'A'
                return

            ##############     状态O         #################
            elif self.currentState == 'O':  # 单行注释，遇到换行结束
                if (ch == '\n'):
                    self.currentState = 'A'
                    return
                else:
                    self.currentState = 'O'
                    return

            ##############     状态A+         #################
            elif self.currentState == 'A+':
                if (ch == '+'):
                    self.buf = self.buf + ch
                    self.result.append((19, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.initialize()
                    return
                elif (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((26, "--"))
                    self.tokens.append(Token('add-equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((6, "--"))
                    self.tokens.append(Token('addition', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A-         #################
            elif self.currentState == 'A-':
                if (ch == '-'):
                    self.buf = self.buf + ch
                    self.result.append(('', "--"))
                    self.tokens.append(Token(20, self.buf, self.mRow))
                    self.initialize()
                    return
                elif (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append(('sub-equal', "--"))
                    self.tokens.append(Token(25, self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((7, "--"))
                    self.tokens.append(Token('subtraction', self.buf, self.mRow))
                    self.initialize()
                    continue

            ##############     状态A*         #################
            elif self.currentState == 'A*':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((24, "--"))
                    self.tokens.append(Token('mutiply-equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((8, "--"))
                    self.tokens.append(Token('multiplication', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A&         #################
            elif self.currentState == 'A&':
                if (ch == '&'):
                    self.buf = self.buf + ch
                    self.result.append((28, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((9, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A^         #################
            elif self.currentState == 'A^':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((23, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((10, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A|         #################
            elif self.currentState == 'A|':
                if (ch == '|'):
                    self.buf = self.buf + ch
                    self.result.append((27, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((11, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A=         #################
            elif self.currentState == 'A=':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((18, "--"))
                    self.tokens.append(Token('equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((12, "--"))
                    self.tokens.append(Token('evaluate', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A!         #################
            elif self.currentState == 'A!':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((21, "--"))
                    self.tokens.append(Token('not-equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((13, "--"))
                    self.tokens.append(Token('', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A>         #################
            elif self.currentState == 'A>':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((17, "--"))
                    self.tokens.append(Token('bigger-equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((14, "--"))
                    self.tokens.append(Token('bigger', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue

            ##############     状态A<         #################
            elif self.currentState == 'A<':
                if (ch == '='):
                    self.buf = self.buf + ch
                    self.result.append((16, "--"))
                    self.tokens.append(Token('smaller-equal', self.buf, self.mRow))
                    self.initialize()
                    return
                else:
                    self.result.append((15, "--"))
                    self.tokens.append(Token('smaller', self.buf, self.mRow))
                    self.buf = ""
                    self.currentState = 'A'
                    continue
                    
    def execute(self):
        for i in range(0, len(self.text)):
            self.mLine = self.mLine + 1
            self.tokenizer(self.text[i])
            if (self.TOKENIZE_CONSENQUENCE == 0):
                return False
            if (self.text[i] == '\n' or self.text[i] == '\r'):
                self.mRow += 1
                self.mLine = 0
        return True