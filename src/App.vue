<template>
  <title>
    Chain League
  </title>
  
  <div v-bind:class="{ top: $route.name == 'Home' || $route.name == 'Whitepaper'}"  ref="top">
    <div class="topinf">  
      
      <div @click="home" v-if="$route.name != 'NotFound'">
        <img src="./assets/icon.svg" class="logo">
        <b class="title" >Chain League</b>
      </div>
      
      <div style="margin-top:2%" v-if="$route.name == 'Home'">       
         <b class="bar" @click="whitepaper">Whitepaper</b>      
         <b class="bar" @click="roadmap">Roadmap</b>
        <b class="bar" @click="team">Team</b> 
        <button class="btop" @click="signup" v-if="!userData">Sign up</button>
        <button class="btop" @click="signOut" v-else>Sign out</button>
      </div>
      
    </div>
    <div class="rectangleInfo" v-if="userData && ($route.name == 'Home' )">
      <p style="color: #050617;  ">{{ userData['summoners'] }} <span style="font-weight: bold;"> {{ userData['server'] }} </span> </p>
      <p style="color: #050617; font: 15px 'Rubik;">Tokens: {{userData['tokens']}}</p>
      <p style="color: #050617; font: 15px 'Rubik; font-weight: bold; color: #2588B2; cursor:pointer;" @click="orders">Orders history</p>
      <p style="color: #050617; ">Referal: </p>
      <p style="color: #050617; font: 13px 'Rubik;">{{ userData['myreferal'] }} </p>
      <div style="width: 100%;">
        <div >
            <div style="float: left; overflow:hidden; margin-left: 10%;">
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
      <input type="text" v-model="wallet" :disabled="walletDisabled" style="width:80%">
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
import CookieLaw from 'vue-cookie-law'

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
      //window.location.replace("http://localhost:8080/#/")
      //this.$router.go(-1)
      this.$router.push({ name: 'Home' })
    },
    async whitepaper() {
      await this.$router.push({ name: 'Whitepaper' })
        var element = this.$refs['top'];
        var top = element.offsetTop;
        window.scrollTo(0, top);
    },
    roadmap() {
      //this.$router.push({ name: 'Home' }).then(()=> this.$refs.view.$.ctx[this.$route.meta.goToRoadmap.methodName]())
      if(window.innerWidth >= 1100)
        window.scrollTo(0, 2400)
      else if(window.innerWidth < 1100 && window.innerWidth >= 660)
        window.scrollTo(0, 1900)
      else if(window.innerWidth < 660)
        window.scrollTo(0, 1500)
    },
    team() {
      //this.$router.push({ name: 'Home' }).then(()=> this.$refs.view.$.ctx[this.$route.meta.goToTeam.methodName]())
      if(window.innerWidth >= 1100)
        window.scrollTo(0, 3800)
      else if(window.innerWidth < 1100 && window.innerWidth >= 660)
        window.scrollTo(0, 2600)
      else if(window.innerWidth < 660)
        window.scrollTo(0, 2000)
    },
    orders() {
      this.$router.push({ name: 'Orders' })
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
      this.oldWallet = this.wallet
    },
    saveWallet(){
      if(this.wallet !== this.oldWallet){
        var usersRef = firebase.firestore().collection("/users");
        if((this.wallet.length != 42 && this.wallet.length != 0) || (this.wallet.substr(0,2) != '0x' && this.wallet.length != 0)){
            alert("Address format incorrect")
        }
        else{
          usersRef.doc(firebase.auth().currentUser.uid).set({      
            wallet: this.wallet,
            email: this.userData['email'],
            referal: this.userData['referal'],          
            summoners: this.userData['summoners'],
            server: this.userData['server'],
            myreferal: this.userData['myreferal'],
          })
          this.userData['wallet'] = this.wallet
          this.walletDisabled = true
        } 
      }    
    },
    async stateChanged(){     
      if(firebase.auth().currentUser){
        const userId = firebase.auth().currentUser.uid
        var usersRef = firebase.firestore().collection("/users");
        await usersRef.doc(userId).get().then((snapshot) => { this.userData = snapshot.data(); this.wallet = this.userData['wallet']})
        
        var ordersRef = firebase.firestore().collection("/orders")
        this.userData['tokens'] = 0
        ordersRef.where("user", "==", firebase.auth().currentUser.uid)
        .where("state", "==", "done").get()
        .then((snapshot) => {
          snapshot.forEach(doc => this.userData['tokens'] += doc.data()['clg'])
        })
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
      oldWallet: null,
      walletDisabled: true
    }
  },
  components: { CookieLaw },
}
</script>

<style>
    @import './styles.css';
</style>
