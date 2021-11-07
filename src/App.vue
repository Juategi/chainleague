<template>
  <div v-bind:class="{ top: show }">
    <div style="margin-top: 10px; height: 70px; width: 100%; float: left; overflow:hidden; position:relative">  
      <div @click="home">
        <img src="./assets/icon.svg" class="logo">
        <b class="title" >Chain League</b>
      </div>
      <div style="margin-top:20px" v-if="show">       
        <b class="bar" >Whitepaper</b>
        <b class="bar" @click="$refs.view.$.ctx[$route.meta.goToRoadmap.methodName]()">Roadmap</b>
        <b class="bar" @click="$refs.view.$.ctx[$route.meta.goToTeam.methodName]()">Team</b> 
        <button style="margin-left:25px; bottom:15px" @click="signup">Sign up</button>
      </div>
    </div>
  </div>
  <router-view v-slot="{ Component }">
    <component ref="view" :is="Component" />
  </router-view>

</template>

<script>

export default {
   methods: {
    signup() {
      this.show = false;
      this.$router.push({ name: 'Signup' })
    },
    home() {
      this.show = true;
      this.$router.push({ name: 'Home' })
    },
  },
  data (){
    return {
      show : true
    }
  }
}
</script>

<style>
    @import './styles.css';
</style>
