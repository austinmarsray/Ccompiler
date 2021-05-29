from lex.lexical import Lexcial
from syntax.syntax import Syntax
if __name__ == '__main__':
    fp = open('./test/code2.c', 'r')
    text = fp.read()

    lexical = Lexcial()
    lexical.load_resource(text)
    lexical_success = lexical.execute()

    if lexical_success:
        result, variable, constant, tokens = lexical.get_output()

        for x in tokens:
            print(x)

        syntax = Syntax()
        syntax.put_source(tokens)
        syntax_success = syntax.execute()

        if syntax_success:
            print("语法分析成功")
        else:
            error = syntax.get_error()
            print("语法分析失败.第%d行:%s"%(error.line,error.info))
    else:
        error = lexical.get_error()
        print("词法分析失败")