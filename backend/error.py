"""
错误
"""


class Error:
    """
    错误
    """
    def __init__(self, error_info):
        """
        构造
        :param error_info: 错误信息
        """
        self.info = error_info


class LexicalError(Error):
    """
    词法错误
    """
    def __init__(self, error_info, error_line, error_coloum):
        """
        构造
        :param error_info: 错误信息
        :param error_line: 错误行数
        """
        super().__init__("\n词法分析错误:\n"+error_info)
        self.line = error_line
        self.coloum = error_coloum


class SyntaxRuleError(Error):
    """
    语法分析规则错误
    """
    def __init__(self, error_info):
        """
        构造
        :param error_info: 信息
        """
        super().__init__(error_info)


class SyntaxError(Error):
    """
    语法错误
    """
    def __init__(self, error_info, error_line):
        """
        构造
        :param error_info: 错误信息
        :param line: 错误行数
        """
        super().__init__("\n语法分析错误:\n"+error_info)
        self.line = error_line