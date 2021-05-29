import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import hljs from "vue3-hljs"
import "highlight.js/styles/dark.css"

createApp(App).use(store).use(router).use(ElementPlus).use(hljs).mount('#app')
