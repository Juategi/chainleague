<template>
  <div >
    <div class="top">
      <div style="width: 30%; float: left; overflow: hidden; position:relative">
        <div style="width: 20%; float: left; overflow: hidden; position:relative">
          <img src="./assets/icon.svg" class="logo"> 
        </div>
        <div style="margin-top: 30px; width: 80%; float: left; overflow: hidden; position:relative">
          <b class="title" >Chain League</b>
        </div>
      </div>
    <div style="margin-top: 50px; height: 50px; width: 70%; float: right; overflow: hidden; position:relative">
      <b class="bar">Whitepaper</b>
      <b class="bar">Roadmap</b>
      <b class="bar">Team</b>
      <button style="margin-top:10px; margin-left:10px">Sign up</button>
    </div>
    
  </div>

  <div style="height:350px; width: 1200px;">
    <div style="margin-left: 20px; width: 41%; float: left; overflow: hidden; margin-top:50px">
          <p >The first play-to-earn token based on League of Legends.</p>
          <p >Win tokens just by winning normal and ranked games in League of Legends.</p>
          <p style="font-weight: bold;">Enter the Rift, enter the Blockchain.</p>      
    </div>   

    <div style="margin-right: 20px; width: 41%; float: right; overflow: hidden; margin-top:50px">
          <p style="font-weight: bold; font-size: 25px;">We are now on pre-sale!</p>
          <p >Be one of  the first to join the project.</p>
          <div style="text-align: center; margin-right:180px">
             <button class="white" style="margin-top:10px; ">Buy tokens</button>
          </div>
    </div>  
  </div>

  <div class="mid">
      <div style="padding-right: 150px;">
        <div style="padding-top: 100px;">
        <button class="big">Sign up</button>
      </div>
      <div style="padding-top: 250px;">
        <button class="big">Log in</button>
      </div>
      </div>
  </div>
  
  <div style="height: 630px; width: 1200px;">
    <div style="margin-top: 40px; float: left; overflow: hidden; ">
            <vue3-autocounter ref='counter' :startAmount='0' :endAmount='200000' :duration='3' prefix='+' suffix=' holders' separator=',' decimalSeparator='.' :decimals='0' :autoinit='false' style="font: 40px 'Rubik' ; font-weight: bold; color:#ffffff"  @finished='alert(`Counting finished!`)' />
          <p style="margin-top: 40px; font-weight: bold; font-size: 25px">Total ICO Launch invested</p>
          <p style="margin-top: 40px; font-weight: bold;">Phase 10</p>   
          <div style="margin-top: 40px; margin-left: 30px; width: 100%; float: center; overflow: hidden;">
            <b style="font-weight: bold; font-size: 30px; ">100.350$</b>  
            <b style="font-weight: bold; font-size: 30px; color: #ffffff;" >/</b>  
            <b style="font-weight: bold; font-size: 30px; color: #ffffff; ">200.000$</b>     
          </div>   
          <div style="margin-top: 40px;  width: 100%; float: center; overflow: hidden; text-align:center; position:relative">
            <div class="rectangleWhite"></div>
            <div class="rectangleBlue" ref="bar"></div>
          </div>     
          <p style="margin-top: 40px; font-weight: bold; font-size: 30px">Actual price: 0.14$</p>  
          <div style="margin-right: 180px; margin-top: 80px; ">
            <button class="white">Buy tokens</button>
          </div>
    </div>  
  </div>

  <div class="mid2">
        <p style="font-weight: bold; font-size: 30px; ">Join our community</p>  
        <img src="./assets/dc.png" class="media" >
        <img src="./assets/ig.png" class="media" >
        <img src="./assets/fb.png" class="media" >
        <img src="./assets/tw.png" class="media" >
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

  <div class="mid3">
      
  </div>

  <div style=" height: 50px ">
        <p style="font-size: 20px; cursor: pointer;">Check the detailed Roadmap >></p>   
  </div>

  <div class="bot">
      <p style="padding-top: 250px; font-weight: bold; font-size: 35px">What is League of Legends?</p>
      <p style="font-size: 25px; cursor: pointer; color: #2588B2" href="https://www.leagueoflegends.com/">Check the website</p>     
      <p style="margin-top: 140px; font-weight: bold; font-size: 35px">+100 million players around the world</p>  
      <p style="margin-top: 140px; font-weight: bold; font-size: 20px">Disclaimer:</p>  
      <p style="font-size: 20px">We are not owned or associated with Riot Games or any of its brands  </p>        
  </div>

  <div style="height:600px; width: 1200px;">
    <div style="width: 100%; float: center; overflow: hidden; ">     
        <p style="padding-top: 10px; font-weight: bold; font-size: 35px">Team</p>   
    </div>  
    <div style="margin-top: 50px; width: 100%; float: left; overflow: hidden;">
      <div style="margin-left: 100px; width: 40%; float: left; overflow: hidden;">
        <img src="./assets/p1.png" style="width:60%; height:auto; max-width:500px; " >
        <p style="font-weight: bold; font-size: 20px">Juan Tena Gimeno</p>  
        <p style="font-size: 20px">Full-Stack & Blockchain developer</p>   
      </div>
      <div style="margin-left: 100px; width: 40%; float: right; overflow: hidden;">
        <img src="./assets/p2.png" style="width:60%; height:auto; max-width:500px;" >
        <p style="font-weight: bold; font-size: 20px">Enrique Martinez Durá</p>  
        <p style="font-size: 20px">Marketing Manager, Community Manager & Business Administrator</p> 
      </div>
    </div>
  </div>

  <div class="fodder">
    <div >
      <div style="width: 25%;  float:left; overflow: hidden;">          
        
      </div>  
      <div style="width: 25%; float: left; overflow: hidden; ">          
        <p style="font-weight: bold; font-size: 20px">Contact</p> 
         <p style="font-size: 20px; margin-top:40px;">support@chainleague.com</p>       
      </div>  
      <div style="width: 25%; float:left; overflow: hidden; ">          
        <p style="font-weight: bold; font-size: 20px">Legal</p>  
         <p style="font-size: 20px; margin-top:40px; cursor: pointer; ">Terms of Use</p>   
         <p style="font-size: 15px; margin-top:60px; ">© 2022 ChainLeague All Rights Reserved.</p>
      </div>  
      <div style="width: 25%; float: left; overflow: hidden; ">          
        <p style="font-weight: bold; font-size: 20px">Social</p> 
        <div>
          <img src="./assets/dc.png" class="mediaS" >
          <img src="./assets/ig.png" class="mediaS" >
          <img src="./assets/fb.png" class="mediaS" >
          <img src="./assets/tw.png" class="mediaS" >
        </div>   
      </div>  
    </div>

  </div>
</div>
</template>

<script>
import Vue3autocounter from 'vue3-autocounter';

scroll = false

export default ({
  created () {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll);
  },
  components: {
    'vue3-autocounter': Vue3autocounter
  },
  data(){
    return {
     
    }
  },
  methods: {
    handleScroll(event) {
      if(!scroll){
        this.$refs.counter.start(); 
        this.$refs.bar.style.width= "30vw";
        scroll = true
      }
      else
        window.removeEventListener('scroll', this.handleScroll);
    }
},
  

})
</script>

<style>
#app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    background: #050617;  
}


div{
  margin:0 auto;
}

b{
  font: 20px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  padding-right: 20px;
}

p{
  font: 20px 'Rubik' ;
  color: #ffffff;
}

b.bar{
  cursor: pointer; 
  padding-right: 100px;
}

b.bar:hover{
  color: #15a0db;
}


button{
  font: 15px 'Rubik' ;
  font-weight: bold;
  color: #ffffff;
  background: #2588B2;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 2px solid #ffffff;
  position: absolute;
  width: 150px;
  height: 40px;
  cursor: pointer;
}

button:hover {
  transform: scale(1.1) 
}

button.white{
  font: 20px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  background: #ffffff;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 2px solid #2588B2;
  width: 180px;
  height: 60px;
}

button.white:hover {
  transform: scale(1.2)
}

button.big{
  font: 20px 'Rubik' ;
  font-weight: bold;
  color: #ffffff;
  background: #2588B2;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 2px solid #ffffff;
  width: 220px;
  height: 60px;
}

button.big:hover {
  transform: scale(1.2) 
}

.title{
  font: 35px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  cursor: pointer; 
}

.logo{
  width:60px; 
  height:60px; 
  max-width:100px; 
  padding-right: 20px;
  padding-top: 20px;
  cursor: pointer; 
}

img.media{
   width:80px; 
   height:auto; 
   max-width:80px; 
   margin-right: 30px; 
   margin-top: 15px; 
   position:relative; 
   cursor: pointer; 
}

img.mediaS{
   width:50px; 
   height:auto; 
   max-width:50px; 
   margin-right: 10px; 
   margin-top: 5px; 
   position:relative; 
   cursor: pointer; 
}

img.media:hover{
  transform: scale(1.2)
}

img.mediaS:hover{
  transform: scale(1.2)
}

.top{
  background: url("./assets/B1.png");
  background-size: 100%;
  height: 500px;
  min-height: 500px;
  min-width: 1200px;
  max-width: 2000px;
  background-repeat: no-repeat;
  margin:0 auto;
}

.mid{
  background: url("./assets/B2.png");
  background-size: 100%;
  height: 400px;
  min-height: 500px;
  min-width: 1200px;
  max-width: 2000px;
  background-repeat: no-repeat;
  margin:0 auto;
}

.mid2{
  background: url("./assets/B3.png");
  background-size: 100%;
  height: 200px;
  min-height: 200px;
  min-width: 1200px;
  max-width: 2000px;
  margin:0 auto;
  background-repeat: no-repeat;
}

.mid3{
  background: url("./assets/B5.png");
  background-size: 100%;
  height: 600px;
  width: 1100px;
  min-height: 600px;
  min-width: 1100px;
  max-width: 1100px;
  margin:0 auto;
  background-repeat: no-repeat;
}

.how{
  background: url("./assets/B7.png");
  background-size: 100%;
  height: 600px;
  min-height: 600px;
  min-width: 900px;
  max-width: 900px;
  margin:0 auto;
  margin-top: 20px; 
  background-repeat: no-repeat;
}

.bot{
  background: url("./assets/B4.png");
  background-size: 100%;
  height: 800px;
  min-height: 800px;
  min-width: 1300px;
  max-width: 2000px;
  margin:0 auto;
  background-repeat: no-repeat;
}

.fodder{
  background: url("./assets/B6.png");
  background-size: 100%;
  height: 200px;
  min-height: 200px;
  min-width: 1700px;
  max-width: 2000px;
  margin:0 auto;
  background-repeat: no-repeat;
}

.line{
  background: #ffffff;
  height: 2px;
  width: 3000px;
  margin-bottom: 50px; 
  margin-top: 20px;
}


.rectangleWhite {
  margin:auto;
  height: 40px;
  width: 800px;
  background-color: #ffffff;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
}
.rectangleBlue {
  margin:auto;
  height: 40px;
  background-color: #2588B2;
  transition: width 4s linear;
  transition-delay: 0s;
  position: absolute;
  top: 0;
  left: 0;
  margin-left: 195px;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
}


.page{
  height: 6200px;
}

@media screen and (max-width: 1100px){

  body {
   transform: scale(0.7);
   transform-origin: 0 0;
   background: #050617;   
  }

}


@media screen and (max-width: 700px){

  body {
   transform: scale(0.4);
   transform-origin: 0 0;
   background: #050617;   
  }

  .page{
    height: 200px;
  }
}



/*@media screen and (max-width: 1400px){

  b{
  font: 20px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 60px;
}

.title{
  font: 40px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 120px;
}

}

@media screen and (max-width: 960px){

  b{
  font: 15px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 45px;
}

.title{
  font: 30px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 90px;
}

}

 @media screen and (max-width: 700px){

  b{
  font: 10px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 30px;
}

.title{
  font: 20px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;0
}

}

@media screen and (max-width: 560px){

  b{
  font: 5px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 15px;
}

.title{
  font: 10px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 30px;
}
  

} */


</style>
