
<template>
  <v-ace-editor
    v-model:value="content"
    @init="editorInit"
    lang="c_cpp"
    theme="monokai"
    :options="{ fontSize: 20}"
    style="postion: absolute;height: 100%;" />
</template>


<script>
import { VAceEditor } from 'vue3-ace-editor';
import 'ace-builds/src-noconflict/mode-c_cpp.js';
import 'ace-builds/src-noconflict/theme-monokai';

export default ({
  data(){
    return {
      content: this.$store.state.content
    }
  },
  watch: {
    content: function (newval, oldVal) {
      this.$store.commit("contentChange",newval);
    }
  },
  components: {
    VAceEditor,
  },
})
</script>

<style scoped>

</style>
