<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      errorMessage: '' // Komunikat o błędzie
    }
  },
  methods: {
    register () {
      // Sprawdzamy, czy hasła są zgodne
      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Hasła muszą być takie same!'
        return
      }

      console.log('Dane do wysłania:', {
        username: this.username,
        email: this.email,
        password: this.password,
        confirm_password: this.confirmPassword
      })

      // Wysłanie danych rejestracyjnych do backendu
      axios.post('http://127.0.0.1:5000/register', {
        username: this.username,
        email: this.email,
        password: this.password,
        confirm_password: this.confirmPassword
      })
        .then(response => {
          console.log('Odpowiedź serwera:', response.data)
          this.$router.push('/login') // Przekierowanie na stronę logowania po rejestracji
        })
        .catch(error => {
          if (error.response && error.response.data) {
            this.errorMessage = error.response.data.msg || 'Wystąpił błąd'
          } else {
            this.errorMessage = 'Nie udało się połączyć z serwerem. Sprawdź połączenie.'
          }
        })
    }
  }
}
</script>

<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username</label>
        <input v-model="username" type="text" id="username" required />
      </div>
      <div>
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" required />
      </div>
      <div>
        <label for="confirm_password">Confirm Password</label>
        <input v-model="confirmPassword" type="password" id="confirm_password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<style scoped>
.register {
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

.error {
  color: red;
  font-size: 14px;
}
</style>
