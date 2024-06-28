<template>
    <div class="deep-dream-style">
      <h2 class="title">Deep Dream Style</h2>
      <div class="rainbow-box"></div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DeepDreamStyle',
  };
  </script>
  
  <style scoped>
  .deep-dream-style {
    text-align: center; 
    padding-bottom: 20px; 
  }
  
  .title {
    font-size: 30px; 
    margin-bottom: 20px; 
    color: #333; 
  }
  
  .rainbow-box {
    width: 500px;
    height: 30px; 
    background: linear-gradient(45deg, #ff0000, #ff8c00, #fffb00, #4fff00, #00fffc, #3a00ff, #c900ff); 
    background-size: 150% 150%; 
    animation: rainbow-animation 8s linear infinite; 
    border-radius: 5px; 
    margin: 0 auto;
  }
  
  @keyframes rainbow-animation {
    0% {
      background-position: 0 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0 50%;
    }
  }
  </style>