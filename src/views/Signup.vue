<template>
<div>
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
          <div v-if="refError" class="error">{{ refError }}</div>

          <label>Password</label>
          <input type="password" v-model="password" required>
          <div v-if="passwordError" class="error">{{ passwordError }}</div>

          <label>Confirm password</label>
          <input type="password" v-model="cpassword" required>
          <div v-if="passwordError" class="error">{{ passwordError }}</div>
          <!--
          <label>If you enter a Summoner's name and a Server you will need to verificate your account</label>

          <label>Summoner's name (optional)</label>
          <input type="text" v-model="summoners">
          <div v-if="summonerError" class="error">{{summonerError }}</div>

          <label>Server (optional)</label>
          <select v-model="server" >
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
          -->
            
            <div style="padding-top: 30px;  text-align: center;" v-if="!loading">
              <p style="font: 20px 'Rubik'; color: #2588B2; font-weight: bold; cursor: pointer;" @click="handleSubmit">Continue</p> 
            </div>  
            <div class="loading" v-if="loading && sign"></div>    
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
  <div style="padding-top: 30px;  text-align: center;" v-if="!sign && !loading">
    <p style="font: 20px 'Rubik'; color: #2588B2; font-weight: bold; cursor: pointer;" @click="handleSubmit">Continue</p> 
  </div>  
  <div class="loading" v-if="loading && !sign"></div>  
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
      refError: '',
      walletId: '',
      myReferal:'',
      summonerError: '',
      emailError: '',
      verification: '',
      verificationError: '',
      walletError: '',
      sign: true,
      riot: false,
      wallet: false,
      end: false,
      loading: false
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
        if(this.sign){
          this.loading = true
          this.passwordError = this.password.length > 5 && this.password == this.cpassword ?
          '' : 'Passwords must match and be at least 6 characters long'
          if(this.referal != '' && this.referal.substring(0,4) != 'clg_' && this.referal.length != 32){
            this.refError = "The code format is not correct"
          } else{
            this.refError = ''
          }
          if(this.passwordError == '' && this.refError == ''){
            var usersRef = firebase.firestore().collection("/users");
            firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then((data) => {
              console.log('Successfully registered!');
              this.myReferal = "clg_" + data.user.uid
              data.user.sendEmailVerification()
              usersRef.doc(data.user.uid).set({
                email: this.email,
                referal: this.referal,          
                //summoners: this.summoners,
                //server: this.server,
                //wallet: this.walletId,
                myreferal: this.myReferal
            })
            .then(function(docRef) {
                console.log("User created with ID: ", docRef);
                this.loading = false;
                this.end = true
                this.sign = false
            })
            .catch(function(error) {
                console.error("Error adding User: ", error);
            });           
            }).catch(error => {
              console.log(error.code)
              alert(error.message);
            });           
          }
          else{
            this.loading = false
          }
        }   
        else if(this.end){
          this.$router.push({ name: 'Home'}) 
        }
        /*
        this.loading = true
        this.passwordError = this.password.length > 5 && this.password == this.cpassword ?
        '' : 'Passwords must match and be at least 6 characters long'
        var usersRef = firebase.firestore().collection("/users");
        if(!this.passwordError && this.sign){  
          var query1
          if(this.summoners != '' && this.server != ''){
            query1 = await usersRef.where('summoners', '==', this.summoners).where('server', '==', this.server).get();
          }
          const query2 = await usersRef.where('email', '==', this.email).get();
          if(query1 != null && !query1.empty){
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
          if((query1 == null || query1.empty ) && query2.empty){
            this.verification = Math.random().toString(36).slice(4).toUpperCase();
            if(this.summoners == '' || this.server == ''){
                this.summoners = ''
                this.server = ''
                //this.wallet = true
                this.end = true
            }
            else{
              this.riot = true
            }
            this.sign = false
          }
        }                   
        else if(this.riot && this.summoners != '' && this.server != ''){ 
          const key = '?api_key=' + process.env.VUE_APP_RIOT_API_KEY
          const serverUrl =  this.server.toLowerCase() == 'RU' ||  this.server.toLowerCase() == 'KR' ?  this.server.toLowerCase() :  this.server.toLowerCase() +'1'
          const summonerQuery = 'https://' + serverUrl + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + this.summoners + key
          var result = await fetch(summonerQuery, {headers: { }}).catch((err) => {
            console.log(err)
            this.verificationError = "Summoner not found or probably the server is too busy, try later"
            this.loading = false;
            return
            })
          const summoner = await result.json()
          const summonerId = summoner['id']
          const level = summoner['summonerLevel']
          if(level < 30){
            this.verificationError = "Level 30 required"
            this.loading = false;
            return
          }
          const codeQuery = "https://" + serverUrl + ".api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/" + summonerId + key
          result = await fetch(codeQuery, {headers: { }}).catch((err) => {this.verificationError = "Code not found, try again"; this.loading = false; return})
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
              var usersRef = firebase.firestore().collection("/users");
              usersRef.where("wallet", "==", this.walletId).get()
              .then((snapshot) => {
                  var used = false
                  snapshot.forEach(doc => used = true)
                  if(used){
                    this.walletError = "Wallet already used";                
                    accept = false
                  }
                  else{
                    accept = true                   
                  }
                }); 
            }
          }
          else{
            accept = true
          }
          console.log(accept)
          if(accept){
            firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then((data) => {
              console.log('Successfully registered!');
              this.myReferal = "clg_" + data.user.uid
              data.user.sendEmailVerification()
              usersRef.doc(data.user.uid).set({
                email: this.email,
                referal: this.referal,          
                summoners: this.summoners,
                server: this.server,
                wallet: this.walletId,
                myreferal: this.myReferal
            })
            .then(function(docRef) {
                console.log("User created with ID: ", docRef);
                this.wallet = false
                this.end = true
            })
            .catch(function(error) {
                console.error("Error adding User: ", error);
                this.loading = false;
            });           
            }).catch(error => {
              console.log(error.code)
              alert(error.message);
              this.loading = false;
            });
            this.wallet = false
            this.end = true
          }
        }
        else if(this.end){   
          firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then((data) => {
            console.log('Successfully registered!');
            this.myReferal = "clg_" + data.user.uid
            data.user.sendEmailVerification()
            usersRef.doc(data.user.uid).set({
              email: this.email,
              referal: this.referal,          
              //summoners: this.summoners,
              //server: this.server,
              //wallet: this.walletId,
              myreferal: this.myReferal
          })
          .then(function(docRef) {
              console.log("User created with ID: ", docRef);
              this.wallet = false
              this.end = true
          })
          .catch(function(error) {
              console.error("Error adding User: ", error);
              this.loading = false;
          });           
          }).catch(error => {
            console.log(error.code)
            alert(error.message);
            this.loading = false;
          });                    
          //this.$router.push({ name: 'Home'}) 
        }
        this.loading = false

        */
    },
    login(){
      this.$router.push({ name: 'Login'}) 
    }
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