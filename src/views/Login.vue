<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      password: '',
      errorMessage: '' // Błąd logowania
    }
  },
  methods: {
    login () {
      // Wyślij dane logowania do backendu
      axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password
      })
        .then(response => {
          const token = response.data.access_token
          // Zapisz token w LocalStorage
          localStorage.setItem('token', token)

          // Zaktualizuj stan w Vuex
          this.$store.dispatch('login', { username: this.username })

          // Przekierowanie na stronę główną po udanym logowaniu
          this.$router.push('/')
        })
        .catch(error => {
          this.errorMessage = 'Invalid credentials' // Ustaw komunikat o błędzie
          console.error('Login error:', error)
        })
    }
  }
}
</script>

<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username</label>
        <input v-model="username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" required />
      </div>
      <button type="submit">Login</button>
      <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p> <!-- Wyświetlanie błędu -->
    </form>
  </div>
</template>

<style scoped>
/* Styl dla formularza logowania */
.login {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

input {
  width: 100%;
  padding: 8px;
  margin: 10px 0;
}

button {
  padding: 10px 15px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
}

p {
  font-size: 14px;
  color: red;
}
</style>
