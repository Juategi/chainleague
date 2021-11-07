import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Vue3Autocounter from 'vue3-autocounter';
//import firebase from "firebase";
import { initializeApp } from "firebase/app";
import './styles.css';

const firebaseConfig = {

    apiKey: "AIzaSyB36moh1l8sirq8A9QAzhNSxkX75_-xKOg",

    authDomain: "chain-league.firebaseapp.com",

    projectId: "chain-league",

    storageBucket: "chain-league.appspot.com",

    messagingSenderId: "578027211981",

    appId: "1:578027211981:web:c76bb4a51b3f73e44a2d84"

};


initializeApp(firebaseConfig);

//createApp(App).use(router).component('vue3-autocounter', Vue3Autocounter).mount('#app')
createApp(App).use(router).mount('#app')
