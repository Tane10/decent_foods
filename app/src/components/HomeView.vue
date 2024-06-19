<script>
import Navbar from '@/components/Navbar.vue';
import SearchBar from '@/components/SearchBar.vue';
import UserProfile from '@/components/UserProfile.vue';
import CardComponent from '@/components/CardComponent.vue';
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
    Navbar,
    SearchBar,
    UserProfile,
    CardComponent
  },
  data() {

    return {
      cards: [
        {
          id: 1,
          cost: 2000,
          sellersUuid: '3NzZifS4T6yC24ERpYzMd6kF3N5GfRRW6Y',
          description: 'High-quality laptop for professional use',
          title: 'Laptop',
          deleted: null,
          imageSrc: 'https://via.placeholder.com/150'
        },
        {
          id: 2,
          cost: 500,
          sellersUuid: '2PwX6KuUC1w6FkTkZ7EsBfT6LpJHn43aC8',
          description: 'Stylish headphones with noise cancellation',
          title: 'Headphones',
          deleted: null,
          imageSrc: 'https://via.placeholder.com/150'
        },
        {
          id: 3,
          cost: 1500,
          sellersUuid: '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71',
          description: 'Classic novel loved by readers worldwide',
          title: 'Book',
          deleted: null,
          imageSrc: 'https://via.placeholder.com/150'
        },
        {
          id: 4,
          cost: 100,
          sellersUuid: '4D2b61U4hX5CijWE2f7vB8e5T4U72h39Ls',
          description: 'Compact umbrella for rainy days',
          title: 'Umbrella',
          deleted: 1,
          imageSrc: 'https://via.placeholder.com/150'
        },
        {
          id: 5,
          cost: 700,
          sellersUuid: '5EoV2r5iN8mFkXyF1hR8T4bZ4X2Uj9iKtD',
          description: 'Elegant watch for formal occasions',
          title: 'Watch',
          deleted: null,
          imageSrc: 'https://via.placeholder.com/150'
        }
      ]
    };
  }
};
</script>

<template>
  <div class="container-fluid max-width">
    <p>
      <strong>Current route path:</strong> {{ $route.fullPath }}
    </p>
    <header-component/>
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
