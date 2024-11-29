import { createRouter, createWebHistory } from 'vue-router'
import store from '../store' // Importujemy store z Vuex

// Importujemy komponenty stron
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue' // Dodajemy import Register.vue

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter: (to, from, next) => {
      if (store.state.user) {
        next()
      } else {
        next('/login')
      }
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register', // Dodajemy trasę do rejestracji
    name: 'Register',
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router