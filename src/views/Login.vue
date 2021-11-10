<template>
  <div >
    <b>Log in</b>
    <form @submit.prevent="handleSubmit">
        <div style="display: inline-block; width: 100%">
          <label>Email</label>
          <input type="email" v-model="email" required>

          <label>Password</label>
          <input type="password" v-model="password" required>
          <div v-if="passwordError" class="error">{{ passwordError }}</div>
          <div v-if="loginError" class="error">{{ loginError }}</div>

            <div @click="forgot">
                <p style="font: 20px 'Rubik'; color: #2588B2; text-align: center; cursor:pointer">I forgot my password</p> 
            </div>

            <div class="submit">
              <button>Continue</button>
            </div>      
        </div>
    </form>
    </div> 
</template>

<script>
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';

export default {
    data() {
    return {
      email: '',
      password: '',
      passwordError: '',
      loginError: ''
    }
  },
    methods: {
    handleSubmit() {
      console.log(this.sign)
        this.passwordError = this.password.length > 5 ?
        '' : 'Passwords must match and be at least 6 characters long'
      if (!this.passwordError) {
          firebase.auth().signInWithEmailAndPassword(this.email, this.password).then((data) => {
          console.log('Successfully logged in!');
          this.$router.push({ name: 'Home'}) 
        })
        .catch(error => {
          switch (error.code) {
          case 'auth/invalid-email':
              this.loginError = 'Invalid email'
              break
          case 'auth/user-not-found':
              this.loginError = 'No account with that email was found'
              break
          case 'auth/wrong-password':
              this.loginError = 'Incorrect password'
              break
          default:
              this.loginError = 'Email or password was incorrect'
              break
        }
        });
      }  
    },
    forgot(){
      this.$router.push({ name: 'Forgot'}) 
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
    margin-right: 140px;
}

form {
    max-width: 500px;
    margin: 10px auto;
    background: white;
    text-align: left;
    padding: 20px;
  }
  
  .loader {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #2588B2; 
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
    margin-top: 100px;
    background: #fff;  
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  .error {
    color: #ff0062;
    margin-top: 10px;
    font-size: 0.8em;
    font-weight: bold;
  }
</style>