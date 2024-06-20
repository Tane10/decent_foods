<script>
import SearchBar from '@/components/SearchBar.vue';
import UserProfile from '@/components/UserProfile.vue';
import CardComponent from '@/components/CardComponent.vue';
import HeaderComponent from "@/components/HeaderComponent.vue";
import {users, cards} from "@/testData.js";


export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
    SearchBar,
    UserProfile,
    CardComponent
  },
  data() {

    return {
      cards,
      loggedIn: true
    };
  }
};
</script>

<template>
  <div class="container-fluid max-width">
    <header-component/>
    <div class="row">
      <card-component
          v-for="card in cards"
          :key="card.id"
          :image-src="card.imageSrc"
          :title="card.title"
          :description="card.description"
          :cost="card.cost"
      ></card-component>
    </div>
  </div>
</template>



<style scoped>
/* Add component-specific styles here if needed */
</style>
