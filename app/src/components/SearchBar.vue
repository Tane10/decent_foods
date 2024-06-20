<script>
export default {
  name: 'SearchBar',
  methods: {
    searchProducts(product) {
      alert(`searching for: ${product}`)
      // if cards.title.includes(product) => return
    }
  }

};
</script>

<template>
  <div class="input-group mb-3 ma">
    <input v-model="product" type="text" class="form-control" placeholder="Search">
    <button @click="searchProducts(product)" class="btn btn-primary">Search</button>
  </div>
</template>


<style scoped>
/* Add component-specific styles here if needed */
</style>
