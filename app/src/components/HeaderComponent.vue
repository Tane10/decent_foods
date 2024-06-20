<script>
import UserProfile from "@/components/UserProfile.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: 'HeaderComponent',
  components: {SearchBar, UserProfile},
};
</script>
<template>
  <header class="header bg-light p-2">
    <div class="container-fluid justify-content-between align-content-md-between">
      <div class="row justify-content-between">
        <div class="col-1">
          <a href="#" class="d-flex align-items-center text-dark text-decoration-none">
            <img src="/logo.png" alt="Logo" class="w-100" />
          </a>
        </div>
        <div class="col-8">
          <search-bar class="flex-grow-1 mx-3"></search-bar>
        </div>
        <div class="col-1">
          <user-profile></user-profile>
        </div>
        <div class="col-1 border text-center">
            <img src="/add-to-cart.png" alt="basket" class="w-25">
            <p>Basket</p>
        </div>
      </div>
    </div>
  </header>
</template>


<style scoped>
/* Add component-specific styles here if needed */

</style>
