class Token:
    """
    Token
    """
    def __init__(self, token_type='', token_str='', token_line=-1):
        """
        构造
        :param token_type: Token 的类型
        :param token_str: Token 的内容
        :param token_line: Token 所在行数
        """
        self.type = token_type
        self.str = token_str
        self.line = token_line

    def __str__(self):
        return "<%s,%s,%d>"%(self.type,self.str,self.line)