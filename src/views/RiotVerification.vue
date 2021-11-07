<template>
  <div >
      <div style="height: 50px"></div>
      <b >Enter this validation code in the League of Legends client</b>
      <p>We need to validate that you are the owner of the account to avoid possible fraud.</p>
      <div class="rectangle">
          <b>AF12GBT4</b>
      </div>
      <div style="margin-top:40px">
          <b >How to do it?</b>
      </div>
      <p>Go to settings by clicking on the icon in the upper right corner of the client.</p>
      <img src="../assets/riot1.png" class="riot1" >
      <p>Then look for the VERIFICATION part scrolling down the menu, enter the code and press SAVE.</p>
      <img src="../assets/riot2.png" class="riot2" >
      <p>After performing these steps press Continue.</p>
      
  </div>
  
</template>

<script>
export default {
  props: ['email','referal','password', 'cpassword','summoners','server', 'walletId'],
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
    
</style>