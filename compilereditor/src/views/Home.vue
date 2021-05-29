<template>
  <el-row>
    <el-col :span="11">
      <Editor></Editor>
    </el-col>
    <el-col :span="2">
      <Menu/>
    </el-col>
    <el-col :span="11">
      <Output/>
    </el-col>

  </el-row>
</template>

<script>
import Editor from '../components/Editor'
import Output from "../components/Output"
import Menu from "../components/Menu"
export default {
  name: 'Home',
  components: {
    Editor,
    Output,
    Menu
  }
}
</script>

<style>
.body {
  margin: 0px !important;
  background-color: #272822;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px !important;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
