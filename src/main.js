import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Vue3Autocounter from 'vue3-autocounter';

createApp(App).use(router).component('vue3-autocounter', Vue3Autocounter).mount('#app')
