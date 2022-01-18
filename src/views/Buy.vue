<template>
  <div style="padding: 3% 20%;" v-if="!end">
     <div >
       <p style="font: 25px 'Rubik'; font-weight: bold; color: #2588B2; ">Buy tokens</p> 
     </div>
      <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">A new Coinbase Commerce tab will open, so you can buy with different cryptocurrencies the amount of CLG you want.</p> 
     </div>   
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">CLG price: <span style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{clg_price}} $</span></p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; "> Keep in mind that until the payment is confirmed, the price of CLG may vary if there is a phase change, so the amount of CLG will be adjusted.</p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">If the payment is done successfully, you will see the tokens in your account.</p> 
     </div>
    
       <p id="pay" style="font: 22px 'Rubik'; font-weight: bold; color: #d39521; cursor:pointer; padding-top:70px" v-if="!loading && !buying" @click="cbuy">Buy</p> 
        <div class="loading" v-if="loading "></div>  
    </div>   

    
</template>

<script>
import firebase from 'firebase/compat/app';

export default {
 data(){
    return {
      clg: null,
      clg_price: null,
      bnb_price: 400,
      countDown: 20,
      meta: firebase.firestore().collection("/meta"),
      wallet: null,
      end: false,
      loading: false,
      buying: false,
      source: ""
    }
  },
  methods: {
    isNumber: function(evt) {
      evt = (evt) ? evt : window.event;
      var charCode = (evt.which) ? evt.which : evt.keyCode;
      if ((charCode > 31 && (charCode < 48 || charCode > 57)) ) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
    countDownTimer() {
      if(this.countDown > 0) {
          setTimeout(() => {
              this.countDown -= 1
              this.countDownTimer()
          }, 1000)
      }
      else{
        this.meta.limit(1).get().then((snapshot) => {let data = snapshot.docs[0].data(); this.clg_price = data['clg_price']})
        this.countDown = 20
        this.countDownTimer()
      }
    },
    goback() {
      this.$router.push({ name: 'Home' })
    },
    async cbuy() {
      this.loading = true
      const pay = document.getElementById('pay'); 
      firebase.auth().currentUser.uid
      const res = await fetch('https://us-central1-chain-league.cloudfunctions.net/createCharge');
      const data = await res.json();

      //this.source = data.hosted_url

      window.open(data.hosted_url, '_blank');
      //pay.innerHTML = `<a href="${data.hosted_url}">Pay Now!</a>`
      //this.loading = false
      //this.buying = true
    },
    async buy() {
      var ready = true
      var ordersRef = firebase.firestore().collection("/orders"); 
      var orders = 0
      if((!firebase.auth().currentUser)){
        alert("Please Sign up")
        ready = false
      }
      else if(!firebase.auth().currentUser.emailVerified){
        alert("Please verify your email first")
        ready = false
      }
      await ordersRef
      .where("user", "==", firebase.auth().currentUser.uid)
      .where("state", "==", "processing")
      .get().then((snapshot) => {
        snapshot.forEach(doc => orders++)
        if(orders >= 5){
          alert("You have 5 orders processing already! Wait until they are processed")
          ready = false
        }
      }) 
      if(this.clg_price == null)
        ready = false     
      this.meta.limit(1).get().then((snapshot) => {
        let data = snapshot.docs[0].data(); 
        if(data['clg_price'] != this.clg_price){
          alert("CLG price has changed!")
          ready = false
        }
        this.clg_price = data['clg_price']
      })
      if(this.clg < 200){
        alert("Minimum of 200 CLG")
        ready = false
      }
      if(this.wallet === ''){
        alert("Wallet is empty!")
        ready = false
      }
      if(ready)  {
        var ordersRef = firebase.firestore().collection("/orders");    
        var date = (new Date()).toISOString().replace("T", " ")
        await ordersRef.add({
          user: firebase.auth().currentUser.uid,
          clg: this.clg,          
          clg_price: this.clg_price,
          state: "processing",
          time: date.substring(0, date.length - 5),
          wallet: this.wallet,
        })
        .catch(function(error) {
          alert("An error ocurred, try again please")
           console.log(error);
        });  
        console.log("Order in process");
        this.end = true
        
      }
    },
    async stateChanged(){     
      if(firebase.auth().currentUser){
        const userId = firebase.auth().currentUser.uid
        var usersRef = firebase.firestore().collection("/users");
        usersRef.doc(userId).get().then((snapshot) => { var userData = snapshot.data(); this.wallet = userData['wallet']})
      }
      else{
        this.userData = {'on' : false}
      }
    }
  },
  async created(){
    this.meta.limit(1).get().then((snapshot) => {let data = snapshot.docs[0].data(); this.clg_price = data['clg_price']})
    //this.countDownTimer()
  },
  mounted(){
    firebase.auth().onAuthStateChanged(() =>{
      this.stateChanged()
    })
   },
}
</script>

<style scoped>
  .loading {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #2588B2; 
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
    margin-top: 100px;
    background-color: #ffffff;  
  }

  #app, #app iframe {
    height: 80vh;
    width: 64vw;
    border: none;
    box-sizing: border-box;
  }
  body {
    margin: 0;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); } 
  }

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    background: #ffffff;  
  }
div{
  background-color: #ffffff;    
}

body{
  margin: 0;
}



input{
    padding: 10px 10px;
    width: 100%;
    border: 1px solid #2588B2;
    border-radius: 6px;
    box-sizing: border-box;
    margin-bottom: 15px;
}



select {
    margin-left: 20px;
    padding: 10px 10px;
    width: 20%;
    border: 1px solid #2588B2;
    border-radius: 6px;
    box-sizing: border-box;
    margin-bottom: 15px;
}

label {
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    font: 15px 'Rubik' ;
    color: #2588B2;
    letter-spacing: 1px;
  }

.submit {
    text-align: center;
    margin-top: 100px;
    margin-right: 20%;
}

.wallet{
  font: 15px 'Rubik'; 
  font-weight: bold;
   color: #2588B2; 
}

form {
    max-width: 500px;
    margin: 10px auto;
    background: white;
    text-align: left;
    padding: 20px;
  }
  
  .error {
    color: #ff0062;
    margin-top: 10px;
    font-size: 0.8em;
    font-weight: bold;
  }

  @media screen and (max-width: 660px){
    .submit {
      text-align: center;
      margin-top: 100px;
      margin-right: 30%;
  }

  .wallet{
    font: 10px 'Rubik'; 
    font-weight: bold;
    color: #2588B2; 
  }
}


</style>