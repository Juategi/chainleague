<template>
   <div v-if="sign">
     <div >
       <p style="font: 20px 'Rubik'; color: #2588B2; ">Already have an account? <span style="font-weight: bold; cursor: pointer;" @click="login">Log in</span></p> 
     </div>
    <form @submit.prevent="handleSubmit">
        <div style="display: inline-block; width: 100%">
          <label>Email</label>
          <input type="email" v-model="email" required>
          <div v-if="emailError" class="error">{{ emailError }}</div>

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
          <div v-if="summonerError" class="error">{{summonerError }}</div>

          <label>Server</label>
          <select v-model="server" required>
          <option value="EUW">EUW</option>
          <option value="EUN">EUNE</option>
          <option value="NA">NA</option>
          <option value="KR">KR</option>
          <option value="OC">OCE</option>
          <option value="BR">EUW</option>
          <option value="JP">EUNE</option>
          <option value="RU">NA</option>
          <option value="TR">KR</option>
          <option value="LA">OCE</option>
          </select>
            <div class="submit">
              <button>Continue</button>
            </div>      
        </div>
    </form>
    </div> 
  <div v-else-if="riot">
    <RiotVerification :verification="this.verification" :verificationError="this.verificationError"/>
  </div>

  <div v-else-if="wallet">
    <Wallet :walletId="this.walletId" :walletError="this.walletError" @walletIdChange="updateWallet"/> 
  </div>
  <div v-else-if="end">
    <End :myReferal="this.myReferal"/>
  </div>
  <div class="submit" v-if="!sign">
      <button @click="handleSubmit">Continue</button>
  </div>
</template>

<script>
import RiotVerification from '../views/RiotVerification.vue'
import Wallet from '../views/Wallet.vue'
import End from '../views/End.vue'
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

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
      summonerError: '',
      emailError: '',
      verification: '',
      verificationError: '',
      walletError: '',
      sign: false,
      riot: false,
      wallet: true,
      end: false
    }
  },
  components: {
    Wallet,
    RiotVerification,
    End
  },
  methods: {
    updateWallet(id){
      this.walletId = id
    },
    async handleSubmit() {
        this.passwordError = this.password.length > 5 || this.password != this.cpassword ?
        '' : 'Passwords must match and be at least 6 characters long'
        var usersRef = firebase.firestore().collection("/users");
        if(!this.passwordError && this.sign){      
          const query1 = await usersRef.where('summoners', '==', this.summoners).where('server', '==', this.server).get();
          const query2 = await usersRef.where('email', '==', this.email).get();
          if(!query1.empty){
            this.summonerError = "Already exists an account with that Summoner's name in the same server"
          }
          else{
            this.summonerError = ""
          }
          if(!query2.empty){
            this.emailError = "Already exists an account with that email"
          }
          else{
             this.emailError = ""
          }
          if(query1.empty && query2.empty){
            this.verification = Math.random().toString(36).slice(4).toUpperCase();
            this.sign = false
            this.riot = true
          }
        }                   
        else if(this.riot){ 
          const key = '?api_key=RGAPI-43fb775e-043e-446f-985c-da8b9c211ad7'
          const serverUrl =  this.server.toLowerCase() == 'RU' ||  this.server.toLowerCase() == 'KR' ?  this.server.toLowerCase() :  this.server.toLowerCase() +'1'
          const summonerQuery = 'https://' + serverUrl + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + this.summoners + key
          var result = await fetch(summonerQuery, {headers: { }}).catch((err) => {this.verificationError = "Summoner not found, try again"; return})
          const summoner = await result.json()
          const summonerId = summoner['id']
          const codeQuery = "https://" + serverUrl + ".api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/" + summonerId + key
          result = await fetch(codeQuery, {headers: { }}).catch((err) => {this.verificationError = "Code not found, try again"; return})
          const code = await result.json()     
          if(code == this.verification){
            this.riot = false
            this.wallet = true
          }   
          else{
            this.verificationError = "Code don't match, try again";
          }
        }
        else if(this.wallet){
          console.log(this.walletId)
          var accept = false
          if(this.walletId){
            if(this.walletId.length != 42 || this.walletId.substr(0,2) != '0x'){
              this.walletError = "Address format incorrect";
            }
            else{
              accept = true
            }
          }
          else{
            accept = true
          }
          if(accept){
            firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then((data) => {
              console.log('Successfully registered!');
              usersRef.doc(data.user.uid).set({
                email: this.email,
                referal: this.referal,          
                summoners: this.summoners,
                server: this.server,
                wallet: this.walletId,
                myReferal: this.myReferal,
            })
            .then(function(docRef) {
                console.log("User created with ID: ", docRef);
            })
            .catch(function(error) {
                console.error("Error adding User: ", error);
            });           
            }).catch(error => {
              console.log(error.code)
              alert(error.message);
            }); 
            this.wallet = false
            this.end = true
          }
          
        }
        else if(this.end){   
          this.$router.push({ name: 'Home'}) 
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
    margin-right: 150px;
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