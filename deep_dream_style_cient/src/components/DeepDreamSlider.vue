<template>
  <div class="container">
    <div class="dream-level-slider">
      <label for="dreamLevel" class="slider-label">Select DeepDream level:</label>
      <vue-slider v-model="dreamLevel" :min="0" :max="9" @change="sliderChanged" />
    </div>
  </div>
</template>

<script>
import VueSlider from 'vue3-slider';

export default {
  components: {
    VueSlider,
  },
  data() {
    return {
      dreamLevel: 7,
    };
  },
  methods: {
    sliderChanged() {
      this.$emit('level-changed', this.dreamLevel);
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center; 
}

.dream-level-slider {
  text-align: center;
  width: 500px; 
  margin-bottom: 20px;
}

.slider-label {
  display: block; 
  margin-bottom: 10px;
  margin-top: 10px;
  font-size: 22px; 
}
</style>