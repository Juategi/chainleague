<template>
  <div style="height:1500px; width: 100%;">
    <div style="overflow: hidden; margin-top:50px">
          <p style="font-weight: bold; ">Whitepaper</p>  
    </div>   
    
     <div>
      <object
        data='https://pdfjs-express.s3-us-west-2.amazonaws.com/docs/choosing-a-pdf-viewer.pdf'
        type="application/pdf"
        width="1000"
        height="1300"
      >

        <iframe
          src='https://pdfjs-express.s3-us-west-2.amazonaws.com/docs/choosing-a-pdf-viewer.pdf'
          width="1000"
          height="1300"
        >
        <p>This browser does not support PDF!</p>
        </iframe>

      </object>
    </div>
    
  </div>   

</template>

<script>
export default {
}
</script>
 
<style>

</style>