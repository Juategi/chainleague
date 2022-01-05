<template>
  <div >
      <div style="height: 50px"></div>
      <b >Enter your Binance Smart Chain address</b>
      <p style="font-weight: bold; color:#F3BA2F; ">BINANCE <span style="font-weight: normal; ">SMART CHAIN</span> </p> 
       <img src="../assets/bsc.svg" class="bsc">  
      <div style="text-align: center;">
          <p>Enter the address that you will use to buy the tokens, so we will know that is you.</p>
          <p>Or leave it blank and do it later.</p>

      </div>
    
      <input type="text" v-model="walletId" >
      <div v-if="walletError" class="error">{{ walletError }}</div>

      
  </div>
  
</template>

<script>
export default {
  props: ['walletId', 'walletError'],
  watch: {
    walletError: function (newVal, oldVal) { },
    walletId: function (newVal, oldVal) { this.$emit('walletIdChange', this.walletId) },
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
    input{
        padding: 10px 10px;
        width: 70%;
        border: 1px solid #2588B2;
        border-radius: 6px;
        box-sizing: border-box;
        margin-bottom: 15px;
    }   
    .submit {
        text-align: center;
        margin-top: 30px;
        margin-right: 130px;
    }
    .bsc{
        width:30px; 
        height:30px; 
        max-width:30px; 
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