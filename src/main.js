import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Notifications from 'notiwind'
//import firebase from "firebase";
import firebase from 'firebase/compat/app';

/*import './styles.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'*/

const firebaseConfig = {

    apiKey: "AIzaSyB36moh1l8sirq8A9QAzhNSxkX75_-xKOg",

    authDomain: "chain-league.firebaseapp.com",

    projectId: "chain-league",

    storageBucket: "chain-league.appspot.com",

    messagingSenderId: "578027211981",

    appId: "1:578027211981:web:c76bb4a51b3f73e44a2d84"

};



firebase.initializeApp(firebaseConfig);
let init = false;
/*firebase.auth().onAuthStateChanged(() =>{
    console.log("changed!!");
    console.log(firebase.auth().currentUser)
    if(firebase.auth().currentUser){
        Vue.prototype.$user =  firebase.auth().currentUser
    } 
})*/
createApp(App).use(router).use(Notifications).mount('#app')
//createApp(App).use(router).component('vue3-autocounter', Vue3Autocounter).mount('#app')
