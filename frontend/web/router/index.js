import Vue from 'vue'
import Router from 'vue-router'
export const routerOptions = [
  { path: '/', component: 'HelloWorld' },
  { path: '/welcome', component: 'Welcome' },
  { path: '/login', component: 'Login' },
  { path: '/register', component: 'Register' },
  { path: '/admin', component: 'Admin' },
  { path: '/cluster', component: 'Cluster' },
  { path: '/home', component: 'Home' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  base: process.env.BASE_URL,
  mode: 'history'
})
