<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-link v-bind:to="'/login'">Link</router-link>
    <Button></Button>
  </div>
</template>

<script>
import Vue from 'vue'
import { httpVueLoader } from 'httpVueLoader'
// httpVueLoader.register(Vue, '../elements/Button.vue')

Vue({
  components: {
    'Button': httpVueLoader('../elements/Button.vue')
  }
})
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
