<template>
  <div >
      <div style="height: 50px"></div>
      <b >Congratulations your account has been created!</b>
      <b> Here is your referal code. </b>
      <div style="text-align: center;">
        <p>{{myReferal}}</p>
      </div>
  </div>
</template>

<script>
export default {
  props: ['myReferal'],
  watch: {
    myReferal: function (newVal, oldVal) {   },
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
        font: 25px 'Rubik' ;
        color: #2588B2;
        padding: 5px 10px;
        width: 100%;
        margin-bottom: 5px;
    } 
</style>