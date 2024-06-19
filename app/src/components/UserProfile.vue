<template>
  <div class="user-profile">
    <a href="#" class="user-profile-link">
      <img src="https://via.placeholder.com/50" alt="User Profile" class="user-profile-img">
      User Profile
    </a>
  </div>
</template>

<script>
export default {
  name: 'UserProfile'
};
</script>

<style scoped>
.user-profile {
  display: flex;
  align-items: center;
}

.user-profile-img {
  border-radius: 50%;
  margin-right: 10px;
}
</style>
