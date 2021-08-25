<template>
  <v-form @submit="login" id="login">
    <label for="user_email"><span>*</span>Email</label>
    <input v-model="body.user_email" class="box1 border1" type="email" /><br />
    <label for="password"><span>*</span>Password</label>
    <input v-model="body.password" type="password" class="box1 border2" /><br />
    <ejs-button cssClass="e-flat" v-on:click="login">Login</ejs-button>
  </v-form>
</template>
<script type="text/javascript">
import { UserController } from '../controllers/user_controller'
import { ButtonPlugin } from '@syncfusion/ej2-vue-buttons'
import Vue from 'vue'
Vue.use(ButtonPlugin)

console.log('Hi')
export default {
  data () {
    return {
      body: {},
      data: {}
    }
  },
  mounted () {
    console.log('mounted')
  },
  // derryjey79@gmail.com Goodbye@12
  computed: {
    login: function () {
      UserController.login(this.body)
      return 'Hi'
    }
  }
}
console.log('Enjoy')
</script>
<style scoped>
#login {
  background-color: blue;
  background-image: "../assets/images/gall3.jpg";
}
</style>
<!--<style scoped src=""></style>
<style scoped src="../assets/css/style.css"></style>
<style scoped src="../assets/css/overlay.css"></style>
<style scoped src="../assets/css/grid.min.css"></style>
<style scoped src="../assets/css/owl.carousel.css"></style>
<style scoped src="../assets/css/lightgallery.min.css"></style>
<style scoped src="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"></style>
<style scoped src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"></style> -->
