// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import routerOptions from './router'

Vue.config.productionTip = false
Vue.use(VueRouter)
/* eslint-disable no-new */

const router = new VueRouter({
  mode: 'history',
  routes: routerOptions.router.routes
})

new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
}).$mount('#app')
