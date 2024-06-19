<script>
export default {
  name: 'UserProfile',
  // methods:{
  //   goToUserProfile() {
  //     this.$router.push('/user')
  //   },
  // }
};
</script>


<template>
  <div class="user-profile">
    <div class="container border p-1 align-center align-middle">

      <div class="user-profile-link borderless">
        <div class="row">
          <div class="col">
            <img src="https://via.placeholder.com/50" alt="User Profile" class="user-profile-img">
          </div>
        </div>
        <div class="row">
          <div class="col">
            <p class="text-center"> User Profile</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


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
