<template>
  
  <div style="height:400px; width: 100%; max-width: 2000px;">
    <div style="margin-left: 20px; width: 40%; float: left; overflow: hidden; margin-top:50px">
          <p >The first play-to-earn cryptocurrency based on League of Legends.</p>
          <p >Win tokens just by playing normal and ranked games in League of Legends.</p>
         <!-- <p style="font-weight: bold; ">Enter the Rift, enter the Blockchain.</p>  -->
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

  <div style=" height:255px; overflow: hidden;">
    <p style="font-weight: bold; font-size: 25px;">Sign up to win more CLG!</p>
    <p >Use your referral code to get more players to sign up.</p>
    <p >You will earn 10% of all the tokens they have purchased.</p>
    <p > Smart contract address:</p>   
    <p class="addressfont">0x918A0f8B19e9308B4C4aA418ecd6CBb5BE6411db</p>  
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
    <div style="width: 100%; float: left; overflow: hidden; margin: auto;  margin-top:2%;">
          <!--<p class="midf">Total launch invested</p>
          <b style="margin-top: 2%;  font-weight: bold;  " >{{Math.round(invested).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}}$</b>   -->
          <p class="midf">Phase - {{phase_name}} {{subphase}} </p>   
          <p class="midf"> <span style="color: #2588B2;"  >{{Math.round(getPhaseInvest()).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}}$</span>  of   {{Math.round(getTotalInvest()).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}}$ </p>   
          <div style="margin-top:2%">
            <img :src="getImgUrl()" v-bind:alt="pic" class="rank">
          </div>                                    
          <p class="midf">Actual price: <span style="font-weight: bold; color: #2588B2;">{{clg_price}}$</span> </p>                   
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
  <!--
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
  </div> -->
<!-- <div class="x600">
    <div style="display: flex;flex-wrap: wrap;padding: 0 4px;">
       <div style="flex: 50%; padding: 0 4px;">
          <a href="https://coinmarketcap.com" target="_blank">
            <img src="../assets/cmc.png" class="partnericon" >
          </a>
          <a href="https://coinmarketcap.com" target="_blank">
            <img src="../assets/cg.png"  class="partnericon">
          </a>
       <div style="flex: 50%;padding: 0 4px;">
          <a href="https://www.dapp.com/app/chain-league" target="_blank">
            <img src="../assets/dapp.png"  class="partnericonL">
          </a>
        </div> 
      <div style="flex: 50%;padding: 0 4px;">
        <a href="https://coinmarketcap.com" target="_blank">
          <img src="../assets/medium.png"  class="partnericon">
        </a>
        <a href="https://coinmarketcap.com" target="_blank">
          <img src="../assets/hack.png"  class="partnericon">
        </a>
      </div>
    </div>
    
</div> -->


  <div class="mid2">
        <div style="margin-bottom: 15px; ">
          <p style="font-weight: bold; font-size: 16px; ">Join our community</p>  

          <a href="https://discord.gg/DSb5kwG6wS"  target="_blank">
            <img src="../assets/dc.png" class="media">
          </a>
          
          <a href="https://t.me/+uO2m5PrKYJI3MWNk" target="_blank">
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
  created(){
    firebase.firestore().collection("/meta").limit(1).get().then((snapshot) => {
        let data = snapshot.docs[0].data();
        this.clg_price = data['clg_price']
        this.invested = data['invested']
        this.phase = data['phase'],
        this.phase_tokens = data['phase_tokens']
        var ico = {
          11: [0.0025, 2000000],
          12: [0.0030, 5000000],
          13: [0.0035, 7000000],
          14: [0.0040, 9000000],
          21: [0.0045, 10000000],
          22: [0.0050, 11000000],
          23: [0.0055, 12000000],
          24: [0.0060, 13000000],
          31: [0.0065, 14000000],
          32: [0.0070, 15000000],
          33: [0.0075, 16000000],
          34: [0.0080, 17000000],
          41: [0.0085, 18000000],
          42: [0.0090, 19000000],
          43: [0.0095, 20000000],
          44: [0.0100, 21000000],
          51: [0.0105, 22000000],
          52: [0.0110, 23000000],
          53: [0.0115, 24000000],
          54: [0.0120, 25000000],
          61: [0.0125, 26000000],
          62: [0.0130, 27000000],
          63: [0.0135, 28000000],
          64: [0.0140, 28000000],
          71: [0.0145, 29000000],
          72: [0.0150, 29000000],
          73: [0.0155, 30000000],
        }
        this.phase_total = ico[this.phase][1]
        switch(this.phase.toString().substring(0,1)){
          case "1":
            this.phase_name = "Iron"
            break;
          case "2":
            this.phase_name = "Bronze"
            break;
          case "3":
            this.phase_name = "Silver"
            break;
          case "4":
            this.phase_name = "Gold"
            break;
          case "5":
            this.phase_name = "Platinum"
            break;
          case "6":
            this.phase_name = "Diamond"
            break;
          case "7":
            this.phase_name = "Master"
            break;
          case "8":
            this.phase_name = "Grandmaster"
            break;
          case "9":
            this.phase_name = "Challenger"
            break;
          default:
            this.phase_name = "Iron"    
        }
        switch(this.phase.toString().substring(1)){
          case "1":
            this.subphase = "I"
            break;
          case "2":
            this.subphase = "II"
            break;
          case "3":
            this.subphase = "III"
            break;
          case "4":
            this.subphase = "IV"
            break;
          default:
            this.subphase = "I"    
        }
      })
      
  },
  components: {
    'vue-cookie-accept-decline': VueCookieAcceptDecline,
    'vue3-autocounter': Vue3autocounter

    },
  data(){
    return {
      clg_price: null,
      invested: 0,
      phase: 0,
      phase_name: "",
      phase_tokens: 0,
      phase_total: 0,
      subphase: ""
    }
  },
  methods: {
    getImgUrl() {
      var images = require.context('../assets/ranks/', false, /\.png$/)
      return images('./' + this.phase_name + ".png")
    },
    getPhaseInvest(){
      return this.phase_tokens*this.clg_price
    },
    getTotalInvest(){
      return this.phase_total*this.clg_price
    },
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
      console.log(this.userData['wallet'])
      if(!this.userData['on'])
        this.$router.push({ name: 'Signup' })
      else{
        if(firebase.auth().currentUser.emailVerified){
          this.$router.push({ name: 'Buy', params: this.userData })
        }
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
      //this.$router.push({ name: 'Terms' })
    },
  }

})
</script>

<style>
    @import '../styles.css';
</style>