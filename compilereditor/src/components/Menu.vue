<template>
  <box class="box">
    <el-row>
      <el-button type="primary" @click="lex">词法分析</el-button>
    </el-row>
    <el-row>
        <el-button type="warning" @click="showtable">预测分析表</el-button>
    </el-row>
    <el-row>
        <el-button type="success" @click="syntax">语法分析</el-button>
    </el-row>
    <!-- <el-row>
      <el-button round @click="changeText">测试代码</el-button>
    </el-row> -->
  </box>
</template>

<script>
import {request} from '../request/request'
import { ElMessage } from 'element-plus'
export default({
  data(){
    return {
      times : 0
    }
  },
  methods: {
    lex() {
      request({url: '/lex',method: 'post',params: {code:this.$store.state.content}})
        .then(res => {
          if(res.data.state == "success"){
            let ansArr = res.data.lex;
            let tmp = "";
            if(ansArr.length == 0){
              tmp = tmp + "empty\n";
            }
            else{
              for (let i=0;i<ansArr.length;i++){
                tmp = tmp + '<' + String(ansArr[i][0]) + "," + String(ansArr[i][1]) + ">\n";
              }
            }
            // variable部分
            let variable = res.data.variable;
            tmp = tmp + "Variable:\n\t["
            for (let i=0;i<variable.length;i++){
              tmp = tmp + String(variable[i]);
              if(i != variable.length - 1){
                tmp = tmp+',';
              }
            }
            tmp = tmp + "]\n";

            // constant部分
            let constant = res.data.constant;
            tmp = tmp + "Constant:\n\t["
            for (let i=0;i<constant.length;i++){
              tmp = tmp + String(constant[i]);
              if(i != constant.length - 1){
                tmp = tmp+',';
              }
            }
            tmp = tmp + "]\n";

            this.$store.commit("OutputChange",tmp)
          }
          else{
            this.$store.commit("OutputChange",res.data.error)
          }
        })
        .catch(err => {
          ElMessage.error('与服务器失去连接');
        })
    },
    syntax() {
      request({url: '/syntax',method: 'post',params: {code:this.$store.state.content}})
        .then(res => {
          if(res.data.state == "success"){
            this.$store.commit("OutputChange","语法分析通过");
          }
          else{
            this.$store.commit("OutputChange",res.data.error);
          }
        })
        .catch(err => {
          ElMessage.error('与服务器失去连接');
        })
    },
    showtable(){
      this.$router.push('/table')
    },
    // changeText(){
    //   this.times++;
    //   if(this.times%2 == 1){
    //     request({url: '/test1',method: 'post'})
    //     .then(res => {
    //         let text = "int main()\n{\n\tint a[5];\n\tint k;\n    k=5;\n\twhile(k){\n\t    a[k] = k*(1000-2);\n\t    k = k - 1;\n    }\n\treturn 0;\n}"
    //         this.$store.commit("contentChange",text);
    //         console.log(this.$store.state.content)
    //       }
    //     )
    //   }
    //   else{
    //     request({url: '/test0',method: 'post'})
    //     .then(res => {
    //         let text = "/* A program to perform Euclid s Algorithm to compute gcd. */\
    //         \nint gcd(int u, int v) {\n    if (v == 0) {\n        return u;\n    } \
    //         else {\n        return gcd(v, u-u/v*v);\n    }\n    /* u-u/v*v* == u mod v */\n}\n\nint main() \
    //         {\n    int x;\n    int y;\n    x = 34;\n    y = 16;\n    output(gcd(x, y));\n    return 0;\n}"
    //         this.$store.commit("contentChange",text);
    //         console.log(this.$store.state.content)
    //       }
    //     )
    //   }
    // }
  }
})
</script>

<style>
  .el-row {
    margin-bottom: 20px;
  }
  .box {
    margin-top: 70%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>