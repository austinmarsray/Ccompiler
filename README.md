编译原理试验：词法分析+语法分析(LL(1))

项目：

- C编译器前端+RESTful API
- 代码编辑器+结果展示

后端项目目录解析：

```
│   app.py						# 后端启动文件
│   error.py					# 编译器前端报错类
│   requirements.txt			# 环境配置
│   test.py						# 编译器前端测试主函数
│
├───lex							# 词法分析部分
│   │   constants.py			# 词法分析使用常量
│   │   lexical.py				# 词法分析主体部分
│   │   Token.py				# Token类
│   │   __init__.py
│
├───syntax						# 语法分析部分
│   │   rule.py					# 文法规则
│   │   syntax.py				# 语法分析主体
│   │   __init__.py
│
└───test						# 测试代码
        code.c					
        code2.c
```

