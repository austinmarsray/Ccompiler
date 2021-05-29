class Sign:
    """
    符号
    """
    def __init__(self, sign_type, sign_str='', sign_line=-1):
        """
        构造
        :param sign_type: 符号的类型
        :param sign_str: 符号的内容(可以为空)
        :param sign_line: 符号所在行数(可以为空)
        """
        self.type = sign_type
        self.str = sign_str
        self.line = sign_line

    def is_terminal_sign(self):
        """
        是不是终结符
        :return: True/False
        """
        if self.type == 'empty':
            return True
        else:
            for i in terminal_sign_type:
                if i == self.type:
                    return True
            return False

    def is_non_terminal_sign(self):
        """
        是不是非终结符
        :return: True/False
        """
        for i in non_terminal_sign_type:
            if i == self.type:
                return True
        return False

    def is_empty_sign(self):
        """
        是不是空字
        :return: True/False
        """
        return self.type == 'empty'


class Production:
    """
    产生式
    """
    def __init__(self, left_type, right_types):
        """
        产生式左边
        :param left_type: 产生式左边的符号类型
        :param right_types: 产生式右边的符号类型列表
        :param semantic_start: 语义操作关键字 - 开始
        :param semantic_children: 语义操作关键字 - 孩子
        :param semantic_end: 语义操作关键字 - 结束
        """
        self.left = Sign(left_type)
        self.right = list()
        for i in right_types:
            self.right.append(Sign(i))

        # 调试用的
        SignToChar = {
            'else': 'else',
            'if': 'if',
            'int': 'int',
            'return': 'return',
            'void': 'void',
            'while': 'while',
            'addition': '+',
            'subtraction': '-',
            'multiplication': '*',
            'division': '/',
            'bigger': '>',
            'bigger-equal': '>=',
            'smaller': '<',
            'smaller-equal': '<=',
            'equal': '==',
            'not-equal': '!=',
            'evaluate': '=',
            'semicolon': ';',
            'comma': ',',
            'left-parentheses': '(',
            'right-parentheses': ')',
            'left-bracket': '[',
            'right-bracket': ']',
            'left-brace': '{',
            'right-brace': '}',
            'id': 'id',
            'num': 'num',
            'pound': '#'
        }
        self.str = self.left.type + ' ->'
        if len(self.right) == 0:
            self.str += 'ϵ'
        else:
            for i in self.right:
                if i.is_non_terminal_sign():
                    self.str += ' ' + i.type
                else:
                    self.str += ' ' + SignToChar[i.type]


"""
1.  program -> define-list
2.  define-list -> define define-list
                 | empty
3.  define -> type ID define-type
4.  define-type -> var-define-follow
                 | fun-define-follow
5.  var-define-follow -> ;
                 | [ NUM ] ;
6.  type ->    int
             | void
7.  fun-define-follow -> ( params ) code-block
8.  params -> param-list
                | empty
9.  param-list -> param param-follow
10. param-follow -> , param param-follow
                | empty
11. param -> type ID array-subscript
12. array-subscript -> [ ]
                | empty
13. code-block -> { local-define-list code-list }
14. local-define-list -> local-var-define local-define-list
                | empty
15. local-var-define -> type ID var-define-follow
16. code-list -> code code-list
                | empty
17. code -> normal-statement
                | selection-statement
                | iteration-statement
                | return-statement
18. normal-statement -> ;
                | ID normal-statement-follow
19. normal-statement-follow -> var-follow = expression ;
                | call-follow ;
20. call-follow -> ( call-params )
21. call-params -> call-param-list
                | empty
22. call-param-list -> expression call-param-follow
23. call-param-follow -> , expression call-param-follow
                | empty
24. selection-statement -> if ( expression ) { code-list } selection-follow
25. selection-follow -> else { code-list }
                | empty
26. iteration-statement -> while ( expression ) iteration-follow
27. iteration-follow -> { code-list }
                | code
28. return-statement -> return return-follow
29. return-follow -> ;
                | expression ;
30. var-follow -> [ expression ]
                | empty
31. expression -> additive-expr expression-follow
32. expression-follow -> rel-op additive-expr
                | empty
33. rel-op ->     <=
                | <
                | >
                | >=
                | ==
                | !=
34. additive-expr -> term additive-expr-follow
35. additive-expr-follow -> add-op term additive-expr-follow
                | empty
36. add-op ->     +
                | -
37. term -> factor term-follow
38. term-follow -> mul-op factor term-follow
                | empty
39. mul-op ->     *
                | /
40. factor -> ( expression )
                | ID id-factor-follow | NUM
41. id-factor-follow -> var-follow
                | ( args )
42. args -> arg-list
                | empty
43. arg-list -> expression arg-list-follow
44. arg-list-follow -> , expression arg-list-follow
                | empty
"""


# 所有终结符的类型
terminal_sign_type = [
    'else',
    'if',
    'int',
    'return',
    'void',
    'while',
    'addition',
    'subtraction',
    'multiplication',
    'division',
    'bigger',
    'bigger-equal',
    'smaller',
    'smaller-equal',
    'equal',
    'not-equal',
    'evaluate',
    'semicolon',
    'comma',
    'left-parentheses',
    'right-parentheses',
    'left-bracket',
    'right-bracket',
    'left-brace',
    'right-brace',
    'id',
    'num',
    # 在这之前添加非终结符类型，请务必不要动 'pound'
    'pound'
]

# 所有非终结符的类型
non_terminal_sign_type = [
    'program',
    'define-list',
    'define',
    'define-type',
    'var-define-follow',
    'type',
    'fun-define-follow',
    'params',
    'param-list',
    'param-follow',
    'param',
    'array-subscript',
    'code-block',
    'local-define-list',
    'local-var-define',
    'code-list',
    'code',
    'normal-statement',
    'normal-statement-follow',
    'call-follow',
    'call-params',
    'call-param-list',
    'call-param-follow',
    'selection-statement',
    'selection-follow',
    'iteration-statement',
    'iteration-follow',
    'return-statement',
    'return-follow',
    # 'eval-statement',
    # 'var',
    'var-follow',
    'expression',
    'expression-follow',
    'rel-op',
    'additive-expr',
    'additive-expr-follow',
    'add-op',
    'term',
    'term-follow',
    'mul-op',
    'factor',
    'id-factor-follow',
    'args',
    'arg-list',
    'arg-list-follow'
]

# 文法产生式
productions = [
    # 0
    Production('program', ['define-list']),
    # 1
    Production('define-list', ['define', 'define-list']),
    Production('define-list', []),
    # 2
    Production('define', ['type', 'id', 'define-type']),
    # 3
    Production('define-type', ['var-define-follow']),
    Production('define-type', ['fun-define-follow']),
    # 4
    Production('var-define-follow', ['semicolon']),
    Production('var-define-follow', ['left-bracket', 'num', 'right-bracket', 'semicolon']),
    # 5
    Production('type', ['int']),
    Production('type', ['void']),
    # 6
    Production('fun-define-follow', ['left-parentheses', 'params', 'right-parentheses', 'code-block']),
    # 7
    Production('params', ['param-list']),
    Production('params', []),
    # 8
    Production('param-list', ['param', 'param-follow']),
    # 9
    Production('param-follow', ['comma', 'param', 'param-follow']),
    Production('param-follow', []),
    # 10
    Production('param', ['type', 'id', 'array-subscript']),
    # 11
    Production('array-subscript', ['left-bracket', 'right-bracket']),
    Production('array-subscript', []),
    # 12
    Production('code-block', ['left-brace', 'local-define-list', 'code-list', 'right-brace']),
    # 13
    Production('local-define-list', ['local-var-define', 'local-define-list']),
    Production('local-define-list', []),
    # 14
    Production('local-var-define', ['type', 'id', 'var-define-follow']),
    # 15
    Production('code-list', ['code', 'code-list']),
    Production('code-list', []),
    # 16
    Production('code', ['normal-statement']),
    Production('code', ['selection-statement']),
    Production('code', ['iteration-statement']),
    Production('code', ['return-statement']),
    # Production('normal-statement', ['eval-statement', 'semicolon']),
    # Production('normal-statement', ['semicolon']),
    # 17
    Production('normal-statement', ['semicolon']),
    Production('normal-statement', ['id', 'normal-statement-follow']),
    # 18
    Production('normal-statement-follow', ['var-follow', 'evaluate', 'expression', 'semicolon']),
    Production('normal-statement-follow', ['call-follow', 'semicolon']),
    # 19
    Production('call-follow', ['left-parentheses', 'call-params', 'right-parentheses']),
    # 20
    Production('call-params', ['call-param-list']),
    Production('call-params', []),
    # 21
    Production('call-param-list', ['expression', 'call-param-follow']),
    # 22
    Production('call-param-follow', ['comma', 'expression', 'call-param-follow']),
    Production('call-param-follow', []),
    # 23
    Production('selection-statement',
               ['if', 'left-parentheses', 'expression', 'right-parentheses', 'left-brace',
                'code-list', 'right-brace', 'selection-follow']),
    # 24
    Production('selection-follow', ['else', 'left-brace', 'code-list', 'right-brace']),
    Production('selection-follow', []),
    # 25
    Production('iteration-statement', ['while', 'left-parentheses', 'expression',
                                       'right-parentheses', 'iteration-follow']),
    # 26
    Production('iteration-follow', ['left-brace', 'code-list', 'right-brace']),
    Production('iteration-follow', ['code']),
    # 27
    Production('return-statement', ['return', 'return-follow']),
    # 28
    Production('return-follow', ['semicolon']),
    Production('return-follow', ['expression', 'semicolon']),
    # Production('eval-statement', ['var', 'evaluate', 'expression']),
    # Production('var', ['id', 'var-follow']),
    # 29
    Production('var-follow', ['left-bracket', 'expression', 'right-bracket']),
    Production('var-follow', []),
    # 30
    Production('expression', ['additive-expr', 'expression-follow']),
    # 31
    Production('expression-follow', ['rel-op', 'additive-expr']),
    Production('expression-follow', []),
    # 32
    Production('rel-op', ['smaller-equal']),
    Production('rel-op', ['smaller']),
    Production('rel-op', ['bigger']),
    Production('rel-op', ['bigger-equal']),
    Production('rel-op', ['equal']),
    Production('rel-op', ['not-equal']),
    # 33
    Production('additive-expr', ['term', 'additive-expr-follow']),
    # 34
    Production('additive-expr-follow', ['add-op', 'term', 'additive-expr-follow']),
    Production('additive-expr-follow', []),
    # 35
    Production('add-op', ['addition']),
    Production('add-op', ['subtraction']),
    # 36
    Production('term', ['factor', 'term-follow']),
    # 37
    Production('term-follow', ['mul-op', 'factor', 'term-follow']),
    Production('term-follow', []),
    # 38
    Production('mul-op', ['multiplication']),
    Production('mul-op', ['division']),
    # 39
    Production('factor', ['left-parentheses', 'expression', 'right-parentheses']),
    Production('factor', ['id', 'id-factor-follow']),
    Production('factor', ['num']),
    # 40
    Production('id-factor-follow', ['var-follow']),
    Production('id-factor-follow', ['left-parentheses', 'args', 'right-parentheses']),
    # 41
    Production('args', ['arg-list']),
    Production('args', []),
    # 42
    Production('arg-list', ['expression', 'arg-list-follow']),
    Production('arg-list-follow', ['comma', 'expression', 'arg-list-follow']),
    Production('arg-list-follow', [])
]

# 文法开始符号
grammar_start = Sign('program')