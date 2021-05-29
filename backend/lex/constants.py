class Constants:
    def __init__(self):
        self.letterSet = { 'a','b','c','d','e','f','g','h','i','j','k','l','m',
                        'n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',}
        self.digitSet = {'0','1','2','3','4','5','6','7','8','9'}
        self.blankCharSet = {' ', '\n', '\t'}
        self.switchCharSet = {'b', 'n', 't', '\'', '\"','\\'}
        # 由ANSI标准定义的C语言关键字共32个：
        self.keywordSet = {'auto','double','int','struct','break','else','long','switch','case','enum',
                        'register','typedef','char','extern','return','union','const','float','short','unsigned',
                        'continue','for','signed','void','default','goto','sizeof','volatile','do','if',
                        'while','static'
                        }
        self.boardSet = {';',',', '(', ')', '.', '{', '}','[',']'}
        self.KeyIndex = {'int':29,
                    'double':30,
                    'float':31,
                    'long':32,
                    'short':33,
                    'char':34,
                    'signed':35,
                    'unsigned':36,
                    'void':37,
                    'auto':38,
                    'enum':39,
                    'const':40,
                    'static':41,
                    'register':42,
                    'struct':43,
                    'break':44,
                    'if':45,
                    'else':46,
                    'switch':47,
                    'case':48,
                    'typedef':49,
                    'extern':50,
                    'return':51,
                    'union':52,
                    'continue':53,
                    'for':54,
                    'default':55,
                    'goto':56,
                    'sizeof':57,
                    'volatile':58,
                    'do':59,
                    'while':60,
                    ',':63,
                    ';':64,
                    '(':65,
                    ')':66,
                    '[':67,
                    ']':68,
                    '{':69,
                    '}':70
                    }
        self.TokenIndex = {
            ',': 'comma',
            ';': 'semicolon',
            '(': 'left-parentheses',
            ')': 'right-parentheses',
            '[': 'left-bracket',
            ']': 'right-bracket',
            '{': 'left-brace',
            '}': 'right-brace'
        }