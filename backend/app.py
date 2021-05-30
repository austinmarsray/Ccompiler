from flask import Flask,request,jsonify
from lex.lexical import Lexcial
from syntax.syntax import Syntax,PredictingAnalysisTable
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True,origins="*")  # 设置跨域
@app.route('/')
def panel():
    pass

@app.route('/api/lex',methods=["POST"])
def lex_analysis():
    # 传回的数据
    text = request.args.get("code").replace("\r\n","\n")

    # 词法分析
    lexical = Lexcial()
    lexical.load_resource(text)
    lexical_success = lexical.execute()

    if lexical_success:
        result, variable, constant,tokens = lexical.get_output()
        return jsonify({"state":"success","lex":result,"variable":variable,"constant":constant})
    else:
        error = lexical.get_error()
        return jsonify({"state":"failure","error":"第%d行,第%d列: %s"%(error.line,error.coloum,error.info)})

@app.route('/api/syntax',methods=["POST"])
def syntax_analysis():
    # 传回的数据
    text = request.args.get("code").replace("\r\n","\n")

    # 词法分析
    lexical = Lexcial()
    lexical.load_resource(text)
    lexical_success = lexical.execute()

    if lexical_success:
        result, variable, constant, tokens = lexical.get_output()
        syntax = Syntax()
        syntax.put_source(tokens)
        syntax_success = syntax.execute()

        if syntax_success:
            return jsonify({"state":"success"})
        else:
            error = syntax.get_error()
            return jsonify({"state":"failure","error":"第%d行: %s"%(error.line,error.info)})
    else:
        error = lexical.get_error()
        return jsonify({"state":"failure","error":"第%d行,第%d列: %s"%(error.line,error.coloum,error.info)})




@app.route('/api/table',methods=["POST"])
def get_predictTable():
    Ptable = PredictingAnalysisTable()
    Ptable.compile()
    IndexArr,ColoumArr= Ptable.get_index_coloum()
    tableData = Ptable.get_table()

    # 非终结符
    IndexArr = [x.type for x in IndexArr]
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
    # 终结符
    ColoumArr = [x.type for x in ColoumArr]
    ColoumSet = [{'prop':x,'label':SignToChar[x]} for x in ColoumArr]

    # 预测分析表
    tableSet = list()
    for Row in tableData:
        d = dict()
        for i in range(len(Row)):
            if Row[i]:
                d={**d,**{ColoumArr[i]:Row[i].str}}
            else:
                d={**d,**{ColoumArr[i]:''}}
        tableSet.append(d.copy())

    return jsonify({"index": IndexArr,"coloum": ColoumSet,"tableData":tableSet})

# @app.route('/api/test1',methods=["POST"])
# def test1():
#     fp = open('./test/code.c', 'r')
#     text = fp.read()
#     return jsonify({"code": text})
#
# @app.route('/api/test0',methods=["POST"])
# def test0():
#     fp = open('./test/code2.c', 'r')
#     text = fp.read()
#     return jsonify({"code": text})

if __name__ == '__main__':
    app.run(debug=True)