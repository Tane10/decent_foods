<script>
import Navbar from './components/Navbar.vue';
import SearchBar from './components/SearchBar.vue';
import UserProfile from './components/UserProfile.vue';
import CardComponent from './components/CardComponent.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    SearchBar,
    UserProfile,
    CardComponent
  },
  data() {
    return {
      cards: [
        { id: 1, imageSrc: 'https://via.placeholder.com/150', title: 'Card Title 1', description: 'This is a card.' },
        { id: 2, imageSrc: 'https://via.placeholder.com/150', title: 'Card Title 2', description: 'This is a card.' },
        { id: 3, imageSrc: 'https://via.placeholder.com/150', title: 'Card Title 3', description: 'This is a card.' }
      ]
    };
  }
};
</script>

<template>
  <div class="container-fluid">
    <header class="d-flex justify-content-between align-items-center py-3 mb-4 border-bottom">
      <a href="#" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">
        <img src="https://via.placeholder.com/100" alt="Logo">
      </a>
      <search-bar class="col-md-6"></search-bar>
      <user-profile class="col-md-3"></user-profile>
    </header>

    <navbar></navbar>

    <div class="row">
      <card-component
          v-for="card in cards"
          :key="card.id"
          :image-src="card.imageSrc"
          :title="card.title"
          :description="card.description"
      ></card-component>
    </div>
  </div>
</template>



<style scoped>
/* Add component-specific styles here if needed */
</style>
