<script>
export default {
  methods: {
    logout () {
      this.$store.dispatch('logout')
      this.$router.push('/login') // Po wylogowaniu przekierowanie na stronę logowania
    },
    goToOrders () {
      this.$router.push('/shipmentOrder') // Przejście do strony zleceń
    }
  }
}
</script>

<template>
  <div class="home">
    <h2>Welcome to Freight Management</h2>
    <p>Only logged-in users can access this page.</p>
    <button @click="logout">Logout</button>
    <button @click="goToOrders">Przejdź do zleceń</button> <!-- Dodany przycisk -->
  </div>
</template>

<style scoped>
.home {
  text-align: center;
}

button {
  padding: 10px 15px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 5px;
  margin: 5px; /* Dodano odstęp między przyciskami */
}
</style>
