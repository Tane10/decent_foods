<script>
export default {
  name: 'CardComponent',
  props: ['imageSrc', 'title', 'description', 'cost'],
  methods: {
    buyNow(){
      alert("added to basket")
    }
  }
};
</script>

<template>
  <div class="col-md-2 mt-3 ml-4">
    <div class="card mb-3 border-dark-subtle shadow-sm">
      <img :src="imageSrc" class="card-img-top" alt="Card image">
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
        <p class="card-text">{{ description }}</p>
        <p class="card-text text-body-emphasis">{{ cost }}</p>
        <div class="row align-content-center justify-content-center">
          <div class="col">
            <button @click="buyNow" class="btn btn-warning btn-lg">Add to basket </button>
          </div>
          </div>
        </div>
      </div>
    </div>

</template>


<style scoped>
/* Add component-specific styles here if needed */
</style>
