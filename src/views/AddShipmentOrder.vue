<script setup>
import { ref } from 'vue'

const orderNumber = ref('')
const sender = ref('')
const recipient = ref('')
const status = ref('W trakcie przygotowania')

const addOrder = async () => {
  const orderData = {
    order_number: orderNumber.value,
    sender: sender.value,
    recipient: recipient.value,
    status: status.value
  }
  console.log('Token:', localStorage.getItem('token'))

  try {
    const response = await fetch('http://127.0.0.1:5000/shipmentOrder', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('token')}` // Dodanie tokenu JWT
      },
      body: JSON.stringify(orderData)
    })
      .then(response => response.json())
      .then(data => console.log('Sukces:', data))
      .catch(error => console.error('Error:', error))

    console.log('Odpowiedź:', response)

    const data = await response.json()

    if (response.ok) {
      alert('Zlecenie dodane pomyślnie!')
      console.log('Sukces:', data)
    } else {
      alert(`Błąd: ${data.msg || 'Nieznany błąd'}`)
      console.error('Odpowiedź błędu:', data)
    }
  } catch (error) {
    console.error('Błąd podczas wysyłania żądania:', error)
  }
}
</script>

<template>
  <h1>Dodaj zlecenie spedycyjne</h1>
  <form @submit.prevent="addOrder">
    <label for="order_number">Numer zlecenia:</label>
    <input v-model="orderNumber" type="text" id="order_number" name="order_number" required><br>
    <label for="sender">Nadawca:</label>
    <input v-model="sender" type="text" id="sender" name="sender" required><br>
    <label for="recipient">Adresat:</label>
    <input v-model="recipient" type="text" id="recipient" name="recipient" required><br>
    <button type="submit">Dodaj zlecenie</button>
  </form>
  <a href="/shipmentOrder">Powrót do listy zleceń</a>
</template>

<style scoped>

</style>
