<template>
  <div style="padding: 3% 20%;">
     <div >
       <p style="font: 25px 'Rubik'; font-weight: bold; color: #2588B2; ">Buy tokens</p> 
     </div>
      <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">This is the wallet you are sending the tokens from, if you want to use another or if it is empty, please go to the main page, once the payment is in process you won't be able to change it.</p> 
     </div>
     <div >
       <p style="font: 18px 'Rubik'; font-weight: bold; color: #2588B2; ">Your wallet:</p> 
     </div>
      <div >
       <p style="font: 15px 'Rubik'; font-weight: bold; color: #2588B2; ">{{$route.params['wallet'] }}</p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Please select the amount of CLG tokens you want to buy, it must be at least 200.</p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">CLG price: <span style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{clg_price}} $</span></p> 
     </div>
    <div >
      <input v-model="clg" @keypress="isNumber($event)">
    </div>
    <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">{{(clg * clg_price).toFixed(2)}} $</p> 
     </div>
    <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Binance Coin (BNB) price: <span style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{bnb_price}} $</span></p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Amount of BNB to deposit: {{(clg * clg_price/bnb_price).toFixed(5)}}</p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Please send that amount of BNB to the following address. If you send a different number, we will adjust the amount of CLG you will receive.</p> 
     </div>
     <div >
       <p style="font: 16px 'Rubik'; font-weight: bold; color: #2588B2; ">0x71C7656EC7ab88b098defB751B7401B5f6d8976F</p> 
     </div>
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">When the payment is sent press Done. If we don't recieve the payment after a while, the order will be cancelled.</p> 
     </div>
     <div class="submit" >
      <button class="formbutton" @click="handleSubmit">Done</button>
  </div> 
    </div>   
    
</template>

<script>
export default {
 data(){
    return {
      clg: 0,
      clg_price: 0.05,
      bnb_price: 400,
      countDown: 20
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
        //Updatear precios

        this.countDown = 20
        this.countDownTimer()
      }
  }
  },
  created(){
    this.countDownTimer()
  }
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
    margin-right: 10%;
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
}


</style>