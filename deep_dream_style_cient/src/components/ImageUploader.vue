<template>
  <div>
    <label for="fileUpload" class="custom-file-upload">
      Select file
      <input id="fileUpload" type="file" @change="onFileChange" accept="image/*" style="display: none;" />
    </label>
    <div v-if="imageUrl">
      <img :src="imageUrl" alt="Выбранное изображение" style="max-width: 500px; margin-top: 10px;" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: null,
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file && /\.(jpg|jpeg|png|gif)$/i.test(file.name)) {
        this.imageUrl = URL.createObjectURL(file);
        this.$emit('image-selected', file);
      } else {
        alert('Разрешены только изображения (jpg/jpeg/png/gif)');
      }
    },
  },
};
</script>

<style scoped>
.custom-file-upload {
  display: inline-block;
  padding: 10px 20px;
  background-color: #f44336;
  color: white;
  font-size: 18px;
  cursor: pointer;
  border-radius: 5px;
  border: 2px solid #f44336;
  text-align: center;
  transition: background-color 0.3s, color 0.3s;
  width: 250px;
  font-size: 22px; 
}

.custom-file-upload:hover {
  background-color: white;
  color:  #d32f2f;
}

#fileUpload {
  display: none;
}

</style>