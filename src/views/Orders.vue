<template>
  <div style="padding: 3% 20%;" >
    <div >
       <p style="font: 25px 'Rubik'; font-weight: bold; color: #2588B2; ">Orders History</p> 
     </div>
    <div>
       <p style="font: 22px 'Rubik'; font-weight: bold; color: #d39521; cursor:pointer; padding-top:70px" @click="goback">Go back</p> 
      </div> 

      
     <div v-for="(order,i) in this.orders" :key="i" class="rectangleOrder">
        <p style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{order['time']}}</p>  
        <p style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{order['wallet']}}</p> 
        <p style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{order['clg']}} CLG</p> 
        <p style="font: 20px 'Rubik'; color: #2588B2; ">CLG price: <span style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{order['clg_price']}}$</span></p> 
        <p style="font: 20px 'Rubik';  color: #2588B2; ">Status: <span style="font: 20px 'Rubik'; font-weight: bold; color: #2588B2; ">{{order['state']}}</span></p> 
     </div>  

     
    </div>
    
</template>

<script>
import firebase from 'firebase/compat/app';

export default {
 data(){
    return {
      orders: []
    }
  },
  methods: {
    async stateChanged(){     
      var ordersRef = firebase.firestore().collection("/orders"); 
      ordersRef.where("user", "==", firebase.auth().currentUser.uid).limit(20).get()
      .then((snapshot) => {
        snapshot.forEach(doc => this.orders.push(doc.data()))
        this.orders.sort((order1, order2) => {
            if(new Date(order1['time']).getTime() < new Date(order2['time']).getTime())
                return 1
            else
                return -1
        });
      })
    },
    goback(){
      this.$router.push({ name: 'Home' })
    }
  },
  created(){
      
  },
  mounted(){
    firebase.auth().onAuthStateChanged(() =>{
        this.stateChanged()
    })
   },
}
</script>

<style scoped>
.rectangleOrder {
    margin:auto;
    height: 13%;
    width: 75%;
    background-color: #f1f0f0;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    border: 2px solid #2588B2;
    margin-top: 30px; 
    overflow:hidden; 
    position:relative
  }
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
    margin-right: 20%;
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