<script setup>
import { ref, onMounted } from 'vue'

const orders = ref([])

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/shipmentOrder', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    })
    const data = await response.json()
    orders.value = data
  } catch (error) {
    console.error('Błąd podczas ładowania zleceń:', error)
  }
})
</script>

<template>
  <h1>Lista zleceń spedycyjnych</h1>
  <a href="/shipmentOrder/add">Dodaj nowe zlecenie</a>
  <table border="1">
    <thead>
    <tr>
      <th>ID</th>
      <th>Numer zlecenia</th>
      <th>Odbiorca</th>
      <th>Adresat</th>
      <th>Status</th>
      <th>Akcje</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="order in orders" :key="order.id">
      <td>{{ order.id }}</td>
      <td>{{ order.order_number }}</td>
      <td>{{ order.sender }}</td>
      <td>{{ order.recipient }}</td>
      <td>{{ order.status }}</td>
      <td>
        <a :href="`/shipmentOrder/${order.id}/edit`">Edytuj</a>
        <form :action="`/shipmentOrder/${order.id}`" method="post" style="display:inline;">
          <input type="hidden" name="_method" value="DELETE">
          <button type="submit">Usuń</button>
        </form>
      </td>
    </tr>
    </tbody>
  </table>
</template>

<style scoped>

</style>
