<template>
<div class="wrapper">
    <el-row>
        <el-page-header @back="goBack" content="预测分析表" :fixed=true></el-page-header>
    </el-row>
    <el-row>
    <el-table
      :data="tableData"
      stripe="true"
      border="true"
      height="720"
      style="width: 100%">
      <el-table-column
        fixed
        type="index"
        width="150"
        :index="indexMethod">
      </el-table-column>
      <el-table-column
        v-for="column in coloumArr"
        :key="column.prop"
        :prop="column.prop"
        :label="column.label"
        width="200">
    </el-table-column>
    </el-table>
    </el-row>
</div>
</template>

<script>
import {request} from '../request/request'
import { ElMessage } from 'element-plus'
  export default {
    data() {
      return {
        IndexArr: [],
        coloumArr: [],
        tableData: [], 
      }
    },
    created() {
        request({url: '/table',method: 'post'})
          .then(res => {
            console.log("success")
            this.IndexArr = res.data.index;
            this.coloumArr = res.data.coloum;
            this.tableData = res.data.tableData;
          })
          .catch(err => {
            ElMessage.error('与服务器失去连接');
          })
      },
    methods: {
      indexMethod(index) {
        return this.IndexArr[index];
      },
      goBack(){
        this.$router.push("/home")
      }
    }
  };
</script>

<style>
.wrapper{
    height: 100%;
    width: 100%;
    background-color: #fff;
}
</style>
