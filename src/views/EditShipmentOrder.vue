<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()
const order = ref({})

onMounted(async () => {
  try {
    const response = await axios.get(`http://localhost:5000/shipment_orders/${route.params.id}`)
    order.value = response.data
  } catch (error) {
    console.error('Błąd podczas pobierania zlecenia:', error)
  }
})

const updateOrder = async () => {
  try {
    await axios.put(`http://localhost:5000/shipment_orders/${order.value.id}`, order.value)
    alert('Zlecenie zostało zaktualizowane')
    // Przekierowanie po zapisaniu
    window.location.href = '/shipment_orders'
  } catch (error) {
    console.error('Błąd podczas aktualizacji zlecenia:', error)
    alert('Wystąpił błąd podczas aktualizacji zlecenia')
  }
}
</script>

<template>
  <h1>Edytuj zlecenie spedycyjne</h1>
  <form @submit.prevent="updateOrder">
    <label for="order_number">Numer zlecenia:</label>
    <input type="text" id="order_number" v-model="order.order_number" required><br>
    <label for="sender">Odbiorca:</label>
    <input type="text" id="sender" v-model="order.sender" required><br>
    <label for="recipient">Adresat:</label>
    <input type="text" id="recipient" v-model="order.recipient" required><br>
    <label for="status">Status:</label>
    <input type="text" id="status" v-model="order.status"><br>
    <button type="submit">Zaktualizuj zlecenie</button>
  </form>
  <a href="/shipment_orders">Powrót do listy zleceń</a>
</template>

<style scoped>

</style>
