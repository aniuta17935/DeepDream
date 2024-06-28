<template>
  <div>
    <deep-dream-style />
    <image-uploader @image-selected="handleImageSelected" />
    <div v-if="selectedImage">
      <deep-dream-slider @level-changed="handleLevelChanged" />
      <button @click="sendRequest" class="custom-button">Stylize</button>
    </div>
    <div v-if="loading" class="loading-animation">
      <p>Loading...</p>
    </div>
    <div v-if="resultImageUrl && !loading" class="result-container">
      <img :src="resultImageUrl" alt="Результат DeepDream" style="max-width: 100%; margin-top: 10px;" />
      <div class="result-actions">
        <a :href="resultImageUrl" download="deepdream_image.jpg">Save image</a>
      </div>
    </div>
  </div>
</template>

<script>
import ImageUploader from './ImageUploader.vue';
import DeepDreamSlider from './DeepDreamSlider.vue';
import DeepDreamStyle from './DeepDreamStyle.vue';
import axios from 'axios';

export default {
  components: {
    ImageUploader,
    DeepDreamSlider,
    DeepDreamStyle
  },
  data() {
    return {
      selectedImage: null,
      dreamLevel: 5,
      resultImageUrl: null,
      loading: false,
    };
  },
  methods: {
    handleImageSelected(file) {
      this.selectedImage = file;
    },
    handleLevelChanged(level) {
      this.dreamLevel = level;
    },
    async sendRequest() {
      this.loading = true;

      try {
        const formData = new FormData();
        formData.append('content_image', this.selectedImage);
        formData.append('level', this.dreamLevel);

        const response = await axios.post('http://localhost:5000/stylize-image', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          responseType: 'json',
        });

        const imageUrl = `data:image/jpeg;base64,${response.data.stylized_image}`;
        this.resultImageUrl = imageUrl;
      } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.custom-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #f44336;
  color: white;
  font-size: 22px;
  cursor: pointer;
  border-radius: 5px;
  border: 2px solid #f44336;
  text-align: center;
  transition: background-color 0.3s, color 0.3s;
  width: 300px;
  font-family: Avenir, Helvetica, Arial, sans-serif;

}

.custom-button:hover {
  background-color: white;
  color:  #d32f2f;
  text-decoration: none;
}

.custom-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.loading-animation {
  text-align: center;
  margin-top: 20px;
}

.loading-animation p {
  font-size: 16px;
  color: #666;
}

.result-container {
  margin-top: 20px;
  text-align: center;
}

.result-container .result-actions {
  margin-top: 10px; 
}

.result-container a {
  display: inline-block;
  padding: 10px 20px;
  background-color: #f44336;
  color: white;
  font-size: 22px;
  cursor: pointer;
  border-radius: 5px;
  border: 2px solid #f44336;
  text-align: center;
  transition: background-color 0.3s, color 0.3s;
  text-decoration: none;  
  width: 250px;
}

.result-container a:hover {
  background-color: white;
  color:  #d32f2f;
  text-decoration: none;
}
</style>