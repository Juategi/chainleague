<template>
  <div class="top">
    <div style="margin-top: 1.3vmin; width: 100%; float: left; overflow: hidden;">
      <!-- <img src="./assets/icon.png" style="width:8%; height:auto; max-width:100px; margin-right: 100px; position:relative;" > -->
      <b class="title" >Chain League</b>
      <b >Whitepaper</b>
      <b >Roadmap</b>
      <b >Community</b>
      <button>Sign up</button>
    </div>
    
  </div>

  <div style="height:30vh; ">
    <div style="margin-left: 100px; width: 40%; float: left; overflow: hidden;">
          <p >The first play-to-earn token based on League of Legends.</p>
          <p >Win tokens just by winning normal and ranked games in League of Legends.</p>
          <p style="font-weight: bold;">Enter the Rift, enter the Blokchain.</p>      
    </div>   

    <div style="margin-right: 100px; width: 40%; float: right; overflow: hidden;">
          <p style="font-weight: bold; font-size: 3vmin;">We are now on pre-sale!</p>
          <p >Be one of  the first to join the project.</p>
          <button class="white">Buy tokens</button>
    </div>  
  </div>

  <div class="mid">
      <div style="padding-top: 5%;">
        <button class="big">Sign up</button>
      </div>
      <div style="padding-top: 12%;">
        <button class="big">Log in</button>
      </div>
  </div>
  
  <div style="height:55vh;">
    <div style="margin-top: 5vh; width: 100%; float: center; overflow: hidden; ">
            <vue3-autocounter ref='counter' :startAmount='0' :endAmount='200000' :duration='3' prefix='+' suffix=' holders' separator=',' decimalSeparator='.' :decimals='0' :autoinit='false' style="font: 4vmin 'Rubik' ; font-weight: bold; color:#ffffff"  @finished='alert(`Counting finished!`)' />
          <p style="margin-top: 5vh; font-weight: bold; font-size: 3vmin">Total ICO Launch invested</p>
          <p style="margin-top: 5vh; font-weight: bold;">Phase 10</p>   
          <div style="margin-top: 5vh; margin-left: 2vmin; width: 100%; float: center; overflow: hidden;">
            <b style="font-weight: bold; font-size: 3vmin; ">100.350$</b>  
            <b style="font-weight: bold; font-size: 3vmin; color: #ffffff;" >/</b>  
            <b style="font-weight: bold; font-size: 3vmin; color: #ffffff; ">200.000$</b>     
          </div>   
          <div style="margin-top: 5vh;  width: 100%; float: center; overflow: hidden; text-align:center; position:relative">
            <div class="rectangleWhite"></div>
            <div class="rectangleBlue" ref="bar"></div>
          </div>     
          <p style="margin-top: 5vh; font-weight: bold; font-size: 3vmin">Actual price: 0.14$</p>  
          <button class="white">Buy tokens</button>
    </div>  
  </div>

  <div class="mid2">
      <img src="./assets/dc.png" style="width:8%; height:auto; max-width:100px; margin-right: 100px; position:relative;" >
      <img src="./assets/ig.png" style="width:8%; height:auto; max-width:100px; margin-right: 100px; position:relative;" >
      <img src="./assets/fb.png" style="width:20%; height:auto; max-width:100px; margin-right: 100px; position:relative;" >
      <img src="./assets/tw.png" style="width:8%; height:auto; max-width:100px; margin-right: 100px; position:relative;" >
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

b{
  font: 10px 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 6vw;
}

p{
  font: 25px 'Rubik' ;
  color: #ffffff;
}

button{
  font: 1.5vmin 'Rubik' ;
  font-weight: bold;
  color: #ffffff;
  background: #2588B2;
  border: 0vw solid rgba(255,255,255,1);
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 0.2vw solid #ffffff;
  width: 8vw;
  height: 3vw;
  
}

button.white{
  font: 1.6vmin 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  background: #ffffff;
  border: 0vm solid rgba(255,255,255,1);
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 0.2vw solid #2588B2;
  width: 14vw;
  height: 4vw;
  
}

button.big{
  font: 2.5vmin 'Rubik' ;
  font-weight: bold;
  color: #ffffff;
  background: #2588B2;
  border: 0vw solid rgba(255,255,255,1);
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
  overflow: hidden;
  border: 0.2vw solid #ffffff;
  width: 28vw;
  height: 7vw;
}

.title{
  font: 3vmin 'Rubik' ;
  font-weight: bold;
  color: #2588B2;
  margin-right: 200px;
  left: 50px;
}

#logo{
  width: min(50vw, 200px);
}

.top{
  background: url("./assets/B1.png");
  background-size: 100%;
  height: 50vh;
  background-repeat: no-repeat;
}

.mid{
  background: url("./assets/B2.png");
  background-size: 100%;
  height: 33vh;
  background-repeat: no-repeat;
}

.mid2{
  background: url("./assets/B3.png");
  background-size: 100%;
  height: 20vh;
  background-repeat: no-repeat;
}

h1 {
  font-size: 5.9vw;
}
h2 {
  font-size: 3.0vh;
}
p {
  font-size: 2vmin;
}
b {
  font-size: 2vmin;
}
button{
  font-size: 1,5vmin;
}
button.white{
  font-size: 1,7vmin;
}

.rectangleWhite {
  margin:auto;
  height: 3.5vh;
  width: 60vw;
  background-color: #ffffff;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
}
.rectangleBlue {
  margin:auto;
  height: 3.5vh;
  width: 0vw;
  background-color: #2588B2;
  transition: width 4s linear;
  transition-delay: 0s;
  position: absolute;
  top: 0;
  left: 0;
  margin-left: 18vw;
  border-top-left-radius: 80px;
  border-top-right-radius: 80px;
  border-bottom-left-radius: 80px;
  border-bottom-right-radius: 80px;
}



@media screen and (max-width: 1400px){

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
  color: #2588B2;
  margin-right: 60px;
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
  

}


</style>
