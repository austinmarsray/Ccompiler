
<template>
  <v-ace-editor
    v-model:value="Output"
    @init="editorInit"
    lang="c_cpp"
    theme="monokai"
    :options="{ fontSize: 20}"
    :readonly='true'
    style="postion: absolute;height: 740px;" />
</template>


<script>
import { VAceEditor } from 'vue3-ace-editor';
import 'ace-builds/src-noconflict/mode-c_cpp.js';
import 'ace-builds/src-noconflict/theme-monokai';

export default ({
  data(){
    return {
      // lexOutput: this.$store.state.lexOutput
    }
  },
  computed: {
    Output(){
      // console.log(this.$store.state.lexOutput);
      return this.$store.state.Output;
    }
  },
  components: {
    VAceEditor,
  },
})
</script>

<style scoped>

</style>
