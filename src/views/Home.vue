<template>
  <div style="height:370px; width: 1200px;">
    <div style="margin-left: 20px; width: 40%; float: left; overflow: hidden; margin-top:50px">
          <p >The first play-to-earn cryptocurrency based on League of Legends.</p>
          <p >Win tokens just by winning normal and ranked games in League of Legends.</p>
          <p style="font-weight: bold; ">Enter the Rift, enter the Blockchain.</p>  
          <div style="margin-top: 18px; ">
             <p >Powered by</p>
          </div>
          <div >
            <div style="float: left; overflow:hidden; margin-left: 115px;">
              <p style="font-weight: bold; color:#F3BA2F; ">BINANCE <span style="font-weight: normal; ">SMART CHAIN</span> </p> 
            </div>
            <div style="float: left; margin-top: 18px; margin-left: 13px">
              <img src="../assets/bsc.svg" class="bsc"> 
            </div>
          </div>
         
    </div>   


    <div style="margin-right: 20px; width: 40%; float: right; overflow: hidden; margin-top:50px">
          <p style="font-weight: bold; font-size: 25px;">We are now on pre-sale!</p>
          <p >Be one of  the first to join the project.</p>
          <div style="text-align: center; margin-right:180px">
             <button class="white" style="margin-top:10px; ">Buy tokens</button>
          </div>
          <div style="padding-top: 120px;">
            <img src="../assets/uni.png" class="uni" >
          </div>
          
    </div>  
  </div>

  <div style=" height:370px; overflow: hidden; margin-top:50px">
    <p style="font-weight: bold; font-size: 30px;">Sign up to win our give away!</p>
    <p >Participate in our give away, the more referals you get, the more chances of winning</p>
    <img src="../assets/ga.png" class="ga" >
    <div style="margin-right: 130px; padding-top:20px; padding-bottom:20px" >
      <button  @click="signup">Sign up</button>
    </div>
    <p style="margin-top: 40px;">We will distribute the prize among 10 winners, they will receive their CLG in their wallets on March 2022</p>      
  </div>  

  <div class="mid">
      <div style="height:360px; width: 1200px;">
    <div style="width: 40%; float: left; overflow: hidden;">
    </div>   

    <div style="margin-left: 400px; width: 20%; float: left; overflow: hidden; margin-top:50px">
      <vue3-autocounter ref='counter' :startAmount='0' :endAmount='200000' :duration='3' prefix='+' suffix=' holders' separator=',' decimalSeparator='.' :decimals='0' :autoinit='false' style="font: 25px 'Rubik' ; font-weight: bold; color:#ffffff"  @finished='alert(`Counting finished!`)' />
          <p style="margin-top: 40px; font-weight: bold; font-size: 15px">Total ICO Launch invested</p>
           <b style="margin-top: 10px; font-weight: bold; font-size: 20px; ">100.350$</b>   
          <p style="margin-top: 40px; font-weight: bold;">Phase 10 - Diamond</p>                                      
          <p style="margin-top: 40px; font-weight: bold; font-size: 20px">Actual price: 0.14$</p>  
          <div style="margin-right: 180px; margin-top: 40px; ">
            <button class="white">Buy tokens</button>
          </div>
    
    </div> 
    <div style="margin-right: 20px; width: 20%; float: left; overflow: hidden; margin-top:150px">
          <img src="../assets/dia.png" class="rank">
    </div>  
    <div style="width: 20%; float: left; overflow: hidden;">
    </div>  
  </div>
  </div>

  <div style="height:950px; width: 1200px;">
    <div style="width: 100%; overflow: hidden; ">          
          <p style="font-weight: bold; font-size: 40px">How will it work?</p>    
          <div class="how"></div>
          <div style="margin-right: 220px; margin-top: 40px; ">
            <button class="big">Whitepaper</button>
          </div>
    </div>  
  </div>

  <div class="line">  </div>

  <div class="mid3" ref="roadmap">
      
  </div>

  <div style=" height: 50px ">
        <p style="font-size: 20px; cursor: pointer;">Check the detailed Roadmap >></p>   
  </div>
  
  <div class="bot">
      <p style="padding-top: 200px; font-weight: bold; font-size: 35px">What is League of Legends?</p>
      <p style="font-size: 25px; cursor: pointer; color: #ffffff" href="https://www.leagueoflegends.com/">Check the website</p>     
      <p style="margin-top: 140px; font-weight: bold; font-size: 35px">+180 million players around the world</p>  
      <p style="margin-top: 140px; font-weight: bold; font-size: 20px">Disclaimer:</p>  
      <p style="font-size: 20px">We are not owned or associated with Riot Games or any of its brands  </p>        
  </div>

  <div style="height:600px; width: 1200px;" ref="team">
    <div style="width: 100%; float: center; overflow: hidden; ">     
        <p style="padding-top: 10px; font-weight: bold; font-size: 35px">Team</p>   
    </div>  
    <div style="margin-top: 50px; width: 100%; float: left; overflow: hidden;">
      <div style="margin-left: 100px; width: 40%; float: left; overflow: hidden;">
        <img src="../assets/p1.png" style="width:60%; height:auto; max-width:500px; " >
        <p style="font-weight: bold; font-size: 20px">Juan Tena Gimeno</p>  
        <p style="font-size: 20px">Full-Stack Developer</p>   
      </div>
      <div style="margin-left: 100px; width: 40%; float: right; overflow: hidden;">
        <img src="../assets/p2.png" style="width:60%; height:auto; max-width:500px;" >
        <p style="font-weight: bold; font-size: 20px">Enrique Martinez Durá</p>  
        <p style="font-size: 20px">Marketing Manager & Community Manager</p> 
      </div>
    </div>
  </div>



  <div class="mid2">
        <p style="font-weight: bold; font-size: 30px; ">Join our community</p>  
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
  mounted(){
    this.$refs.counter.start();
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
    }
  }

})
</script>

<style>
    @import '../styles.css';
</style>