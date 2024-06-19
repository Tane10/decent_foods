<script>
import UserProfile from "@/components/UserProfile.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: 'HeaderComponent',
  components: {SearchBar, UserProfile},
};
</script>
<template>
  <header class="header bg-light">
    <div class="container-fluid">
      <div class="d-flex justify-content-between align-items-center py-3">
        <a href="#" class="d-flex align-items-center text-dark text-decoration-none">
          <img src="https://via.placeholder.com/100x60" alt="Logo">
        </a>
        <search-bar class="flex-grow-1 mx-3"></search-bar>
        <user-profile></user-profile>
      </div>
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
