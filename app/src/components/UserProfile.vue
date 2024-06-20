<script>
export default {
  name: 'UserProfile',
  props:[]
};
</script>


<template>
  <div class="user-profile">
    <div class="container border p-1 align-center align-middle justify-content-center">
      <div class="user-profile-link borderless">
        <div class="row">
          <div class="col">
            <p>Welcome</p>
            <img src="/user.png" alt="User Profile" class="w-25">
            <p>Sign in / Register</p>
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
