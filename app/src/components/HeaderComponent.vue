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
            <img src="https://via.placeholder.com/100x60" alt="Logo">
          </a>
        </div>
        <div class="col-8">
          <search-bar class="flex-grow-1 mx-3"></search-bar>
        </div>
        <div class="col-1">
          <user-profile></user-profile>
        </div>
        <div class="col-1 border text-center">
            <img src="https://via.placeholder.com/100x60" alt="basket" class=".basket-profile-img">
            <p>Basket</p>
        </div>
      </div>
<!--      <div class="d-flex justify-content-between align-items-center py-3">-->
<!--        <a href="#" class="d-flex align-items-center text-dark text-decoration-none">-->
<!--          <img src="https://via.placeholder.com/100x60" alt="Logo">-->
<!--        </a>-->
<!--      </div>-->
    </div>
  </header>
</template>

<!--<template>-->


<!--  <div class="d-flex justify-content-between align-items-center py-3 mb-4 lg-4 border-bottom">-->
<!--    <a href="#" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">-->
<!--      <img src="https://via.placeholder.com/100x60" alt="Logo">-->
<!--    </a>-->
<!--    <search-bar class="col-md-6"></search-bar>-->
<!--    <user-profile class="col-md-3"></user-profile>-->
<!--  </div>-->

<!--</template>-->


<style scoped>
/* Add component-specific styles here if needed */

</style>
