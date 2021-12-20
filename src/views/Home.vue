<template>
  
  <div style="height:400px; width: 100%; max-width: 2000px;">
    <div style="margin-left: 20px; width: 40%; float: left; overflow: hidden; margin-top:50px">
          <p >The first play-to-earn cryptocurrency based on League of Legends.</p>
          <p >Win tokens just by playing normal and ranked games in League of Legends.</p>
          <p style="font-weight: bold; ">Enter the Rift, enter the Blockchain.</p>  
          <div style="margin-top: 18px; ">
             <p >Powered by</p>
          </div>
          <div style="padding-top: 0px;">
            <img src="../assets/bsct.png" class="bsct" >
          </div>   
               
    </div>   


    <div style="margin-right: 20px; width: 40%; float: right; overflow: hidden; margin-top:35px">
          <p style="font-weight: bold; font-size: 20px;">We are now on pre-sale!</p>
          <p >Be one of  the first to join the project.</p>
          <!-- <p> Smart contract address:</p>   
          <p class="addressfont">0xdF7BBD62c8f6d2A1FE5F2252bC7Df37CC0994eEd</p>  
          <a href="https://www.youtube.com/watch?v=KpF41eS3YZQ" target="_blank" style="text-decoration:none">
              <p style="cursor: pointer; color: #2588B2">How to buy on Pancakeswap?</p>   
          </a>
          -->
          <NotificationGroup group="foo" >
          <div
            class="fixed inset-0 flex items-start justify-end p-6 px-4 py-6 pointer-events-none"
          >
            <div class="w-full max-w-sm">
              <Notification
                v-slot="{ notifications }"
                enter="transform ease-out duration-1300 transition"
                enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4"
                enter-to="translate-y-0 opacity-100 sm:translate-x-0"
                leave="transition ease-in duration-1500"
                leave-from="opacity-100"
                leave-to="opacity-0"
                move="transition duration-900"
                move-delay="delay-1300"
              >
                <div
                  class="flex w-full max-w-sm mx-auto mt-4 overflow-hidden bg-white rounded-lg shadow-md"
                  v-for="notification in notifications"
                  :key="notification.id"
                >
                  
                  <div class="px-4 py-2 -mx-3">
                    <div class="mx-3">
                      <p class="text-sm text-red-600" style="color: red">{{ notification.text }}</p>
                      <p class="text-sm text-red-600" style="color: red">{{ notification.text2 }}</p>
                    </div>
                  </div>
                </div>
              </Notification>
            </div>
          </div>
        </NotificationGroup>
          <div style="text-align: center; margin-right: 25%">
             <button class="white" style="margin-top:10px; "  @click="buy"  >Buy tokens</button>
          </div> 
         
                    
    </div>  
  </div>

  <div style=" height:250px; overflow: hidden;">
    <p style="font-weight: bold; font-size: 25px;">Sign up to win more CLG!</p>
    <p >Use your referral code to get more players to sign up.</p>
    <p >You will earn 10% of all the tokens they have purchased.</p>
    <!-- <img src="../assets/ga.png" class="ga" > -->
    <div style="margin-right: 10%; padding-top:20px; padding-bottom:20px" >
      <button @click="signup" v-if="!userData">Sign up</button>
    </div>
  </div>  

  <!--<div class="mid">
    <div style="height:80%; width: 100%">      
    <div style="margin-left: 35%; width: 20%; float: left; overflow: hidden; margin-top:5%">
      <vue3-autocounter ref='counter' :startAmount='0' :endAmount='200000' :duration='3' prefix='+' suffix=' holders' separator=',' decimalSeparator='.' :decimals='0' :autoinit='false' style="font: 25px 'Rubik' ; font-weight: bold; color:#ffffff"  @finished='alert(`Counting finished!`)' />
          <p class="midf">Pre-release invested</p>
           <b style="margin-top: 5%; font-weight: bold; ">0$</b>   
          <p class="midf">Phase 0 - Iron</p>                                      
          <p class="midf">Price: 0.00$</p>  
          <div style="margin-right:70%; margin-top:15%; ">
            <button class="white" onclick=" window.open('https://pancakeswap.finance/swap','_blank')" >Buy tokens</button>
          </div>
    
    </div> 
    <div style="margin-right: 20px; width: 20%; float: left; overflow: hidden; margin-top:10%">
          <img src="../assets/iro.png" class="rank">
    </div>  
    <div style="width: 20%; float: left; overflow: hidden;">
    </div>  
  </div>
  </div> -->

  <div class="mid">
    <div style="width: 100%; float: left; overflow: hidden; margin: auto;  margin-top:5%;">
          <p class="midf">Pre-release invested</p>
          <b style="margin-top: 5%; font: 25px 'Rubik'; font-weight: bold; ">23.040$</b>   
          <p style="margin-top: 9%; font-weight: bold; ">Price: 0.05$</p>  
          
    
    </div> 
  </div>

    <div class="x900">          
          <p style="font-weight: bold; font-size: 23px; margin-top: 5%">How will it work?</p>    
          <div class="how"></div>
          <!--<div style="margin-right: 20%; margin-top: 40px; ">
            <button class="big" @click="whitepaper">Whitepaper</button>
          </div>-->
    </div>  

  <div class="line">  </div>

  <div class="mid3" ref="roadmap">
      
  </div>

  <!-- <div style=" height: 50px ">
      <p style="font-size: 20px; cursor: pointer;">Check the detailed Roadmap >></p>   
  </div> -->
  
  <div class="bot">
      <p class="botf">What is League of Legends?</p>
      <a style="font-size: 20px; font-weight: bold; cursor: pointer; color: #d39521; padding-top:100px;text-decoration:none"  href="https://www.leagueoflegends.com/" target="_blank">Check the website</a>     
      <p class="botf">+180 million players around the world</p>  
      <p style="margin-top: 8%; font-weight: bold; font-size: 15px">Disclaimer:</p>  
      <p class="midf">We are not owned or associated with Riot Games or any of its brands  </p>        
  </div>

  <div class="x600" ref="team">
    <div style="width: 100%; float: center; overflow: hidden; ">     
        <p style="padding-top: 10px; font-weight: bold; font-size: 35px">Team</p>   
    </div>  
    <div style="margin-top: 50px; width: 100%; float: left; overflow: hidden;">
      <div style="width: 40%; float: left; overflow: hidden;">
        <img src="../assets/p1.png" style="width:50%; height:50%; max-width:250px; " >
        <p style="font-weight: bold; ">Juan Tena Gimeno</p>  
        <p >Full-Stack Developer</p>   
        <a href="https://www.linkedin.com/in/juan-tena-gimeno-2411191aa/" target="_blank">
          <img src="../assets/ld.png" class="mediaS" >
        </a>
        
      </div>
      <div style="width: 40%; float: right; overflow: hidden;">
        <img src="../assets/p2.jpg" style="width:50%; height:50%; max-width:250px;" >
        <p style="font-weight: bold;">Enrique Martinez Durá</p>  
        <p >Marketing Manager & Community Manager</p> 
        <a href="https://www.linkedin.com/in/enrique-mart%C3%ADnez-dur%C3%A1-308146154/" target="_blank">
          <img src="../assets/ld.png" class="mediaS" >
        </a>
      
      </div>
    </div>
  </div>



  <div class="mid2">
        <div style="margin-bottom: 15px; ">
          <p style="font-weight: bold; font-size: 18px; ">Join our community</p>  

          <a href="https://discord.gg/DSb5kwG6wS"  target="_blank">
            <img src="../assets/dc.png" class="media">
          </a>
          
          <a href="https://t.me/chainleague" target="_blank">
            <img src="../assets/tg.png" class="media" >
          </a>
          
          
          <a href="https://twitter.com/ChainLeague" target="_blank">
              <img src="../assets/tw.png" class="media" >
          </a>
        </div>
  </div>


  <div class="fodder">
    <div >
      <div class="foddericon">          
        <img src="../assets/iconw.svg" class="logoB">
      </div>  
      <div style="width: 20%; float: left; overflow: hidden; ">          
        <p style="font-weight: bold; ">Contact</p> 
         <p style=" margin-top:10%;">support@chain-league.com</p>    
          <p style=" margin-top:10%; ">© 2022 ChainLeague All Rights Reserved.</p>  
      </div>    
      <div style="width: 10%; float:left; overflow: hidden; ">          
        <p style="font-weight: bold; ">Legal</p>  
         <p style=" margin-top:20%; cursor: pointer;" @click="terms">Terms of Use</p>   
      </div>     
    </div>
  
    
  
  </div>
</template>

<script>
import Vue3autocounter from 'vue3-autocounter';
import { useRouter } from 'vue-router'
import firebase from 'firebase/compat/app';
import Notifications from 'notiwind'
import VueCookieAcceptDecline from 'vue-cookie-accept-decline'

scroll = false

export default ({
  name: 'Home',
  props: ['userData'],
  mounted(){
    //this.$refs.counter.start();
  },
  components: {'vue-cookie-accept-decline': VueCookieAcceptDecline},
  
  methods: {
    goToTeam() {
      var element = this.$refs['team'];
      var top = element.offsetTop;
      window.scrollTo(0, top);
    },
    goToRoadmap() {
      var element = this.$refs['roadmap'];
      var top = element.offsetTop;
      window.scrollTo(0, top);
    },
    signup() {
      this.$router.push({ name: 'Signup' })
    },
    buy() {
      if(!this.userData)
        this.$router.push({ name: 'Signup' })
      else{
        if(firebase.auth().currentUser.emailVerified)
          this.$router.push({ name: 'Buy', params: this.userData })
        else{
          this.$notify({
            group: "foo",
            title: "Warning",
            text: "Please verify your email to buy tokens! ",
            text2: "If you already did, please refresh the page"
          }, 2000) 
        }
      }
    },
    whitepaper() {
      this.$router.push({ name: 'Whitepaper' })
    },
    terms() {
      this.$router.push({ name: 'Terms' })
    },
  }

})
</script>

<style>
    @import '../styles.css';
</style>