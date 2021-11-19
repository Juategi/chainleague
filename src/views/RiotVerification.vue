<template>
  <div style="height: 1000px">
      <div style="height: 50px"></div>
      <b >Enter this validation code in the League of Legends client</b>
      <p>We need to validate that you are the owner of the account to avoid possible fraud. 
        You will need to have an account with level 30 or more</p>
      <div class="rectangle">
          <b>{{ verification }}</b>
      </div>
      <div style="margin-top:40px">
          <b >How to do it?</b>
      </div>
      <p>Go to settings by clicking on the icon in the upper right corner of the client.</p>
      <img src="../assets/riot1.png" class="riot1" >
      <p>Then look for the VERIFICATION part scrolling down the menu, enter the code and press SAVE.</p>
      <img src="../assets/riot2.png" class="riot2" >
      <p>After performing these steps press Continue.</p>

      <div v-if="verificationError" class="error">{{ verificationError }}</div>
      
  </div>
  
</template>

<script>
export default {
  props: ['verification', 'verificationError'],
  watch: {
    verificationError: function (newVal, oldVal) {   },
  },
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
        margin: 10px auto;
        text-align: center;
        padding: 20px;
    }

    body{
        margin: 0;
    }
    p{
        display: inline-block;
        font: 15px 'Rubik' ;
        color: #2588B2;
        padding: 5px 10px;
        width: 100%;
        margin-bottom: 5px;
    }
    .rectangle {
        height: 40px;
        width: 240px;
        color:white;
        background-color: white;
        border: 1px solid #2588B2;
        border-radius:7px;
        display: flex;
        justify-content:center;
        align-items: center;
    }

    .riot1{
        width:400px; 
        height:100px; 
        max-width:400px; 
        margin-top: 15px;
    }

    .riot2{
        width:400px; 
        height:350px; 
        max-width:400px; 
        margin-top: 15px;
    }

    .submit {
        text-align: center;
        margin-top: 30px;
        margin-right: 130px;
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
    font-size: 1em;
    font-weight: bold;
  }
    
</style>