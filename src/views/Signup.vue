<template>
   <div v-if="sign">
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Already have an account? <span style="font-weight: bold; cursor: pointer;" @click="login">Log in</span></p> 
     </div>
    <form @submit.prevent="handleSubmit">
        <div style="display: inline-block; width: 100%">
          <label>Email</label>
          <input type="email" v-model="email" required>

          <label>Referal (optional)</label>
          <input type="text" v-model="referal">

          <label>Password</label>
          <input type="password" v-model="password" required>
          <div v-if="passwordError" class="error">{{ passwordError }}</div>

          <label>Confirm password</label>
          <input type="password" v-model="cpassword" required>
          <div v-if="passwordError" class="error">{{ passwordError }}</div>

          <label>Summoner's name</label>
          <input type="text" v-model="summoners" required>

          <label>Server</label>
          <select v-model="server" required>
          <option value="EUW">EUW</option>
          <option value="EUNE">EUNE</option>
          <option value="NA">NA</option>
          <option value="KR">KR</option>
          <option value="OCE">OCE</option>
          </select>
            <div class="submit">
              <button>Continue</button>
            </div>      
        </div>
    </form>
    </div> 
  <div v-else-if="riot">
    <RiotVerification />
  </div>

  <div v-else-if="wallet">
    <Wallet/> 
  </div>
  <div v-else-if="end">
    <End v-bind:myReferal="this.myReferal"/>
  </div>
  <div class="submit" v-if="!sign">
      <button @click="handleSubmit">Continue</button>
  </div>
</template>

<script>
import RiotVerification from '../views/RiotVerification.vue'
import Wallet from '../views/Wallet.vue'
import End from '../views/End.vue'

export default {
  data() {
    return {
      email: '',
      referal:'',
      password: '',
      cpassword: '',
      summoners:'',
      server:'',
      passwordError: '',
      walletId: '',
      myReferal:'',
      sign: true,
      riot: false,
      wallet: false,
      end: false
    }
  },
  components: {
    Wallet,
    RiotVerification,
    End
  },
  methods: {
    handleSubmit() {
        this.passwordError = this.password.length > 5 || this.password != this.cpassword ?
        '' : 'Passwords must match and be at least 6 characters long'
        console.log(this.sign)
        console.log(this.riot)
        console.log(this.wallet)
        console.log(this.end)
        if(!this.passwordError && this.sign){
          this.sign = false
          this.riot = true
        }
        else if(this.riot){
          this.riot = false
          this.wallet = true
        }
        else if(this.wallet){
          this.wallet = false
          this.end = true
        }

    },
    login(){
      this.$router.push({ name: 'Login'}) 
    }
  }
}
</script>

<style scoped>
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    background: #fff;  
  }
div{
  background: #fff;    
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
    margin-right: 100px;
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

</style>