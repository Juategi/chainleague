<template>
  <div style="height:1300px; width: 100%; ">
    <div style="overflow: hidden; margin-top:5%; margin: auto;" >
          <p style="font-weight: bold; ">Whitepaper</p>  
    </div>   
    <div style="overflow: hidden; margin-top:5%; margin: auto;" >
          <p style="font-weight: bold; cursor:pointer; color: #d39521" @click="download">Download</p>  
    </div> 
     <div style="width:80%; height:80%">
      <object
        :data='url'
        type="application/pdf"
        width="80%"
        height="80%"
      >

        <iframe
          :src='url'
          width="80%"
          height="80%"
        >
        <p>This browser does not support PDF!</p>
        </iframe>

      </object>
    </div>
      
  </div>   

</template>

<script>
import axios from "axios";

export default {
  data(){
    return {
      url: 'https://firebasestorage.googleapis.com/v0/b/chain-league.appspot.com/o/WhitepaperEnglish.pdf?alt=media&token=6bbb8649-fd54-4043-83c3-515f6f5fd8c5',
    }
  },
  methods:{
    download(){
      axios.get(this.url, { responseType: 'blob' })
      .then(response => {
        const blob = new Blob([response.data], { type: 'application/pdf' })
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download = "whitepaper.pdf"
        link.click()
        URL.revokeObjectURL(link.href)
      }).catch(console.error)
    }
  }
}
</script>
 
<style>

</style>