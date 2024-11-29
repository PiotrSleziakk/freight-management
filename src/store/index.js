import { createStore } from 'vuex'

// Tworzymy Vuex Store
const store = createStore({
  state () {
    return {
      user: null // null oznacza, że użytkownik nie jest zalogowany
    }
  },
  mutations: {
    // Mutacja do ustawiania danych użytkownika
    setUser (state, user) {
      state.user = user
    },
    // Mutacja do usuwania danych użytkownika (wylogowanie)
    logout (state) {
      state.user = null
    }
  },
  actions: {
    // Akcja do logowania
    login ({ commit }, user) {
      // Można tu podłączyć backend do sprawdzania danych
      commit('setUser', user)
    },
    // Akcja do wylogowania
    logout ({ commit }) {
      commit('logout')
    }
  }
})

export default store
