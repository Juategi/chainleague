<template>
  <div v-bind:class="{ top: $route.name == 'Home' || $route.name == 'Whitepaper'}"  ref="top">
    <div style="margin-top: 10px; height: 70px; width: 100%; float: left; overflow:hidden; position:relative">  
      <div @click="home" v-if="$route.name != 'NotFound'">
        <img src="./assets/icon.svg" class="logo">
        <b class="title" >Chain League</b>
      </div>
      <div style="margin-top:20px" v-if="$route.name == 'Home' || $route.name == 'Whitepaper'">       
        <b class="bar" @click="whitepaper">Whitepaper</b>
        <b class="bar" @click="roadmap">Roadmap</b>
        <b class="bar" @click="team">Team</b> 
        <button style="margin-left:25px; bottom:15px" @click="signup" v-if="!userData">Sign up</button>
        <button style="margin-left:25px; bottom:15px" @click="signOut" v-else>Sign out</button>
      </div>
    </div>
    <div class="rectangleInfo" v-if="userData">
      <p style="color: #050617;  ">{{ userData['summoners'] }} <span style="font-weight: bold;"> {{ userData['server'] }} </span> </p>
      <p style="color: #050617;  font: 17px 'Rubik' ;">Referal: </p>
      <p style="color: #050617;  font: 15px 'Rubik' ;">{{ userData['myreferal'] }} </p>
      <div style="width: 100%;">
        <div >
            <div style="float: left; overflow:hidden; margin-left: 115px;">
              <p style="color:#F3BA2F; font: 18px 'Rubik; font-weight: bold; '">BSC <span style="font-weight: normal; ">Wallet</span> </p> 
            </div>
            <div style="float: left; margin-top: 18px; margin-left: 8px">
              <img src="./assets/bsc.svg" class="bscS"> 
            </div>
          </div>
        <div style="width: 40%; float: right; overflow:hidden; position:relative; margin-top: 20px; ">
           <img src="./assets/edit.png" class="edit" @click="editWallet" v-if="walletDisabled">
           <img src="./assets/save.png" class="edit" @click="saveWallet" v-else>
        </div>
      </div>
      <input type="text" v-model="wallet" :disabled="walletDisabled" style="width=300px">
    </div>
  </div>
  <router-view v-slot="{ Component }" :userData="userData">
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
    async whitepaper() {
      await this.$router.push({ name: 'Whitepaper' })
        var element = this.$refs['top'];
        var top = element.offsetTop;
        window.scrollTo(0, top);
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
    editWallet(){
      this.walletDisabled = false
    },
    saveWallet(){
      var usersRef = firebase.firestore().collection("/users");
      if(this.wallet.length != 42 || this.wallet.substr(0,2) != '0x')
          alert("Address format incorrect")
      else{
        usersRef.doc(firebase.auth().currentUser.uid).set({      
          wallet: this.wallet,
          email: this.userData['email'],
          referal: this.userData['referal'],          
          summoners: this.userData['summoners'],
          server: this.userData['server'],
          myreferal: this.userData['myreferal'],
        })
        this.walletDisabled = true
      }  
    },
    async stateChanged(){     
      if(firebase.auth().currentUser){
        const userId = firebase.auth().currentUser.uid
        var usersRef = firebase.firestore().collection("/users");
        usersRef.doc(userId).get().then((snapshot) => { this.userData = snapshot.data(); this.wallet = this.userData['wallet']})
      }
      else{
        this.userData = null
      }
    }
  },
  data(){
    return {
      userData: null,
      wallet: null,
      walletDisabled: true
    }
  }
}
</script>

<style>
    @import './styles.css';
</style>
