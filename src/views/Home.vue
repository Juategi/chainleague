<template>
  <div style="height:370px; width: 100%;">
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
          <div style="text-align: center; margin-right:120px">
             <button class="white" style="margin-top:10px; " onclick=" window.open('https://pancakeswap.finance/swap','_blank')">Buy tokens</button>
          </div>
          <div >
            <img src="../assets/uni.png" class="uni" >
          </div>
          
    </div>  
  </div>

  <div style=" height:400px; overflow: hidden; margin-top:50px">
    <p style="font-weight: bold; font-size: 30px;">Sign up to win our give away!</p>
    <p >Participate in our give away, the more referals you get, the more chances of winning</p>
    <p >You will also need to have at least 100 CLG in your wallet</p>
    <img src="../assets/ga.png" class="ga" >
    <div style="margin-right: 130px; padding-top:20px; padding-bottom:20px" >
      <button  @click="signup" v-if="!userData">Sign up</button>
    </div>
    <p style="margin-top: 40px;">We will distribute the prize among 10 winners, they will receive their CLG in their wallets on March 2022</p>      
  </div>  

  <div class="mid">
    <div style="height:80%; width: 100%">      
    <div style="margin-left: 35%; width: 20%; float: left; overflow: hidden; margin-top:5%">
      <!--<vue3-autocounter ref='counter' :startAmount='0' :endAmount='200000' :duration='3' prefix='+' suffix=' holders' separator=',' decimalSeparator='.' :decimals='0' :autoinit='false' style="font: 25px 'Rubik' ; font-weight: bold; color:#ffffff"  @finished='alert(`Counting finished!`)' /> -->
          <p style="margin-top: 5%; font-weight: bold; ">Total ICO Launch invested</p>
           <b style="margin-top: 5%; font-weight: bold; ">0$</b>   
          <p style="margin-top: 15%; font-weight: bold;">Phase 0 - Iron</p>                                      
          <p style="margin-top: 15%; font-weight: bold; ">Actual price: 0.00$</p>  
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
  </div>

    <div class="x900">          
          <p style="font-weight: bold; font-size: 26px">How will it work?</p>    
          <div class="how"></div>
          <div style="margin-right: 20%; margin-top: 40px; ">
            <button class="big" @click="whitepaper">Whitepaper</button>
          </div>
    </div>  

  <div class="line">  </div>

  <div class="mid3" ref="roadmap">
      
  </div>

  <div style=" height: 50px ">
        <p style="font-size: 20px; cursor: pointer;">Check the detailed Roadmap >></p>   
  </div>
  
  <div class="bot">
      <p style="padding-top: 10%; font-weight: bold; font-size: 26px">What is League of Legends?</p>
      <a style="font-size: 18px; cursor: pointer; color: #ffffff" href="https://www.leagueoflegends.com/" target="_blank">Check the website</a>     
      <p style="margin-top: 8%; font-weight: bold; font-size: 26px">+180 million players around the world</p>  
      <p style="margin-top: 8%; font-weight: bold; font-size: 17px">Disclaimer:</p>  
      <p style="font-size: 17px">We are not owned or associated with Riot Games or any of its brands  </p>        
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
        <img src="../assets/ld.png" class="mediaS" onclick=" window.open('https://www.linkedin.com/in/juan-tena-gimeno-2411191aa/','_blank')">
      </div>
      <div style="width: 40%; float: right; overflow: hidden;">
        <img src="../assets/p2.jpg" style="width:50%; height:50%; max-width:250px;" >
        <p style="font-weight: bold;">Enrique Martinez Durá</p>  
        <p >Marketing Manager & Community Manager</p> 
        <img src="../assets/ld.png" class="mediaS" onclick=" window.open('https://www.linkedin.com/in/enrique-mart%C3%ADnez-dur%C3%A1-308146154/','_blank')">
      </div>
    </div>
  </div>



  <div class="mid2">
        <p style="font-weight: bold; font-size: 18px; ">Join our community</p>  
        <img src="../assets/dc.png" class="media" >
        <img src="../assets/ig.png" class="media" >
        <img src="../assets/tg.png" class="media" >
        <img src="../assets/fb.png" class="media" >
        <img src="../assets/tw.png" class="media" >
        
  </div>


  <div class="fodder">
    <div >
      <div style="width: 10%;  float:left; overflow: hidden;">          
        <img src="../assets/iconw.svg" class="logoB">
      </div>  
      <div style="width: 20%; float: left; overflow: hidden; ">          
        <p style="font-weight: bold; font-size: 20px">Contact</p> 
         <p style="font-size: 20px; margin-top:40px;">support@chainleague.com</p>    
          <p style="font-size: 15px; margin-top:60px; ">© 2022 ChainLeague All Rights Reserved.</p>  
      </div>    
      <div style="width: 10%; float:left; overflow: hidden; ">          
        <p style="font-weight: bold; font-size: 20px">Legal</p>  
         <p style="font-size: 20px; margin-top:40px; cursor: pointer; ">Terms of Use</p>   
      </div>     
    </div>

  </div>
</template>

<script>
import Vue3autocounter from 'vue3-autocounter';
import { useRouter } from 'vue-router'

scroll = false

export default ({
  name: 'Home',
  props: ['userData'],
  mounted(){
    //this.$refs.counter.start();
  },
  components: {
    'vue3-autocounter': Vue3autocounter
  },
  
  setup(){
    const router = useRouter()

    const goto = (refName) => {
      var element = this.$refs[refName];
      var top = element.offsetTop;
      window.scrollTo(0, top);
    }
    
    const signup = ()  => {
      console.log(router)
      router.push({ name: 'Signup' })
    }

    //return{goto, signup}
  },

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
    whitepaper() {
      this.$router.push({ name: 'Whitepaper' })
    },
  }

})
</script>

<style>
    @import '../styles.css';
</style>