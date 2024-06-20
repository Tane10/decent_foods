<script>
import SearchBar from './components/SearchBar.vue';
import UserProfile from './components/UserProfile.vue';
import CardComponent from './components/CardComponent.vue';
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: 'App',
  components: {
    HeaderComponent,
    SearchBar,
    UserProfile,
    CardComponent
  },
};
</script>

<template>

<!--  <nav>-->
<!--    <RouterLink to="/">Go to Home</RouterLink>-->
<!--    <RouterLink to="/about">Go to About</RouterLink>-->
<!--  </nav>-->
  <main>
    <RouterView />
  </main>

</template>

<style scoped>
/* Add component-specific styles here if needed */
</style>
