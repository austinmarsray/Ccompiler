<template>
  <keep-alive>
    <router-view/>
  </keep-alive>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
.body {
  height: 760px;
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
  width: 100%;
  height: 100%;
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
