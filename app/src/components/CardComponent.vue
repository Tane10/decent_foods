<script>
export default {
  name: 'CardComponent',
  props: ['imageSrc', 'title', 'description']
};
</script>

<template>
  <div class="col-md-3 mt-3 ml-4">
    <div class="card mb-3">
      <img :src="imageSrc" class="card-img-top" alt="Card image">
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
        <p class="card-text">{{ description }}</p>
        <a href="#" class="btn btn-primary">Details</a>
      </div>
    </div>
  </div>
</template>


<style scoped>
/* Add component-specific styles here if needed */
</style>
