<template>
  <div v-bind:class="{ top: $route.name == 'Home' || $route.name == 'Whitepaper'}">
    <div style="margin-top: 10px; height: 70px; width: 100%; float: left; overflow:hidden; position:relative">  
      <div @click="home" v-if="$route.name != 'NotFound'" ref="top">
        <img src="./assets/icon.svg" class="logo">
        <b class="title" >Chain League</b>
      </div>
      <div style="margin-top:20px" v-if="$route.name == 'Home' || $route.name == 'Whitepaper'">       
        <b class="bar" @click="whitepaper">Whitepaper</b>
        <b class="bar" @click="roadmap">Roadmap</b>
        <b class="bar" @click="team">Team</b> 
        <button style="margin-left:25px; bottom:15px" @click="signup" v-if="!user">Sign up</button>
        <button style="margin-left:25px; bottom:15px" @click="signOut" v-else>Sign out</button>
      </div>
    </div>
  </div>
  <router-view v-slot="{ Component }" :user="user">
    <component ref="view" :is="Component" />
  </router-view>

</template>

<script>
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

export default {
  mounted(){
    firebase.auth().onAuthStateChanged(() =>{
      this.stateChanged()
    })
   },
   methods: {
    signup() {
      this.$router.push({ name: 'Signup' })
    },
    home() {
      this.$router.push({ name: 'Home' })
    },
    whitepaper() {
      this.$router.push({ name: 'Whitepaper' })
    },
    roadmap() {
      this.$router.push({ name: 'Home' }).then(()=> this.$refs.view.$.ctx[this.$route.meta.goToRoadmap.methodName]())
    },
    team() {
      this.$router.push({ name: 'Home' }).then(()=> this.$refs.view.$.ctx[this.$route.meta.goToTeam.methodName]())
    },
    signOut() {
      firebase.auth().signOut().then(
        () => {console.log("out!!")
          this.$router.push({ name: 'Home' })
        }
      )
      
    },
    stateChanged(){     
      if(firebase.auth().currentUser)
        this.user = true;
      else
        this.user = false
      console.log(this.user)
    }
  },
  data(){
    return {
      user: false
    }
  }
}
</script>

<style>
    @import './styles.css';
</style>
