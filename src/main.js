import { createApp } from 'vue'
import App from './App.vue'
import store from './store' // Importujemy store z Vuex
import router from './router' // Importujemy router z Vue Router

createApp(App)
  .use(store) // Dodajemy store do aplikacji
  .use(router) // Dodajemy router do aplikacji
  .mount('#app')
