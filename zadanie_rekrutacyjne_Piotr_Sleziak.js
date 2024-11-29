// function solution1 (expenses) {
//   const allExpenses = collectExpenses(expenses) // Zbieranie wydatków
//   if (allExpenses.length === 0) return null // Jeśli brak wydatków, zwróć null
//
//   // Sortowanie wydatków i obliczenie mediany
//   allExpenses.sort((a, b) => a - b) // Sortowanie rosnące
//   const mid = Math.floor(allExpenses.length / 2) // Indeks środkowego elementu
//   return allExpenses.length % 2 === 0
//     ? (allExpenses[mid - 1] + allExpenses[mid]) / 2 // Średnia dwóch środkowych (dla parzystej długości)
//     : allExpenses[mid] // Środkowy element (dla nieparzystej długości)
// }
//
// function solution2 (expenses) {
//   const allExpenses = collectExpenses(expenses) // Zbieranie wydatków
//   if (allExpenses.length === 0) return null // Jeśli brak wydatków, zwróć null
//
//   // Quickselect do wyznaczenia mediany
//   const quickSelect = (arr, k) => {
//     const pivot = arr[Math.floor(Math.random() * arr.length)]
//     const lows = arr.filter(x => x < pivot)
//     const highs = arr.filter(x => x > pivot)
//     const pivots = arr.filter(x => x === pivot)
//
//     if (k < lows.length) return quickSelect(lows, k)
//     else if (k < lows.length + pivots.length) return pivot
//     else return quickSelect(highs, k - lows.length - pivots.length)
//   }
//
//   const mid = Math.floor(allExpenses.length / 2)
//   if (allExpenses.length % 2 === 0) {
//     // Średnia dwóch środkowych elementów dla parzystej długości
//     const lowerMedian = quickSelect(allExpenses, mid - 1)
//     const upperMedian = quickSelect(allExpenses, mid)
//     return (lowerMedian + upperMedian) / 2
//   } else {
//     // Środkowy element dla nieparzystej długości
//     return quickSelect(allExpenses, mid)
//   }
// }
//
// const expenses = {
//   '2023-01':
//     {
//       '01':
//       {
//         food: [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
//         fuel: [210.22]
//       },
//       '09':
//       {
//         food: [11.9],
//         fuel: [190.22]
//       }
//     },
//   '2023-03':
//     {
//       '07':
//       {
//         food: [20, 11.9, 30.20, 11.9]
//       },
//       '04':
//         {
//           food: [10.20, 11.50, 2.5],
//           fuel: []
//         }
//     },
//   '2023-04': {}
// }
//
// // Iterujemy przez wszystkie miesiące
// function collectExpenses (expenses) {
//   const daysOfInterest = [1, 2, 3, 4, 5, 6, 7] // Dni do pierwszej niedzieli w miesiącu
//   const result = [] // Przechowujemy tutaj wszystkie wydatki spełniające kryteria
//
//   for (const month in expenses) {
//     // Iterujemy przez wszystkie dni w danym miesiącu
//     for (const day in expenses[month]) {
//       // Sprawdzamy, czy dzień należy do dni od 1 do 7
//       if (daysOfInterest.includes(parseInt(day))) {
//         const dayExpenses = Object.values(expenses[month][day] || {}).flat()
//         result.push(...dayExpenses)
//       }
//     }
//   }
//   return result
// }
//
// // Funkcja pomocnicza do testowania
// function testSolution (solution, expenses, name) {
//   console.log(`\n=== Test dla ${name} ===`)
//   const allExpenses = collectExpenses(expenses) // Pobierz całą tablicę wydatków
//   const sortedExpenses = [...allExpenses].sort((a, b) => a - b) // Posortowana kopia
//   const result = solution(expenses) // Oblicz medianę
//   console.log('Tablica wydatków (przed sortowaniem):', allExpenses)
//   console.log('Tablica wydatków (posortowana):', sortedExpenses)
//   console.log('Mediana:', result)
// }
//
// // Testowanie obu rozwiązań
// testSolution(solution1, expenses, 'Rozwiązanie 1')
// testSolution(solution2, expenses, 'Rozwiązanie 2')
//
// console.log(solution1(expenses))
// console.log(solution2(expenses))

function solution1 (expenses) {
  // Funkcja pomocnicza do uzyskania dni do pierwszej niedzieli włącznie
  function getDaysToFirstSunday (year, month) {
    const days = []
    for (let day = 1; day <= 7; day++) {
      const date = new Date(year, month - 1, day)
      days.push(day)
      if (date.getDay() === 0) { // Niedziela
        break
      }
    }
    return days
  }

  const allExpenses = []
  for (const [monthYear, days] of Object.entries(expenses)) {
    const [year, month] = monthYear.split('-').map(Number)
    const daysToFirstSunday = getDaysToFirstSunday(year, month)

    for (const day of daysToFirstSunday) {
      const dayKey = day.toString().padStart(2, '0') // Formatowanie klucza "01", "02", ...
      if (days[dayKey]) {
        const dailyExpenses = Object.values(days[dayKey]).flat() // Pobranie wszystkich wydatków
        allExpenses.push(...dailyExpenses)
      }
    }
  }

  if (allExpenses.length === 0) return null

  allExpenses.sort((a, b) => a - b) // Sortowanie wydatków
  const mid = Math.floor(allExpenses.length / 2)
  return allExpenses.length % 2 !== 0
    ? allExpenses[mid]
    : (allExpenses[mid - 1] + allExpenses[mid]) / 2
}

function solution2 (expenses) {
  // Funkcja pomocnicza do uzyskania dni do pierwszej niedzieli włącznie
  function getDaysToFirstSunday (year, month) {
    const days = []
    for (let day = 1; day <= 7; day++) {
      const date = new Date(year, month - 1, day)
      days.push(day)
      if (date.getDay() === 0) { // Niedziela
        break
      }
    }
    return days
  }

  // QuickSelect do znajdowania k-tego najmniejszego elementu
  function quickSelect (arr, k) {
    if (arr.length === 1) return arr[0] // Jeśli tylko jeden element, zwróć go

    const pivot = arr[Math.floor(arr.length / 2)]
    const lows = arr.filter(x => x < pivot)
    const highs = arr.filter(x => x > pivot)
    const pivots = arr.filter(x => x === pivot)

    if (k < lows.length) {
      return quickSelect(lows, k)
    } else if (k < lows.length + pivots.length) {
      return pivot
    } else {
      return quickSelect(highs, k - lows.length - pivots.length)
    }
  }

  const allExpenses = []
  for (const [monthYear, days] of Object.entries(expenses)) {
    const [year, month] = monthYear.split('-').map(Number)
    const daysToFirstSunday = getDaysToFirstSunday(year, month)

    for (const day of daysToFirstSunday) {
      const dayKey = day.toString().padStart(2, '0') // Formatowanie klucza "01", "02", ...
      if (days[dayKey]) {
        const dailyExpenses = Object.values(days[dayKey]).flat() // Pobranie wszystkich wydatków
        allExpenses.push(...dailyExpenses)
      }
    }
  }

  if (allExpenses.length === 0) return null // Brak wydatków

  const n = allExpenses.length
  if (n % 2 === 1) {
    // Jeśli nieparzysta liczba elementów, znajdź środkowy element
    return quickSelect([...allExpenses], Math.floor(n / 2))
  } else {
    // Jeśli parzysta liczba elementów, znajdź dwa środkowe i wylicz ich średnią
    const left = quickSelect([...allExpenses], n / 2 - 1)
    const right = quickSelect([...allExpenses], n / 2)
    return (left + right) / 2
  }
}

const expenses = {
  '2023-01': { // pierwsza niedziela
    '01': {
      food: [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
      fuel: [210.22]
    },
    '09': {
      food: [11.9],
      fuel: [190.22]
    }
  },
  '2023-03': {
    '07': {
      food: [20, 11.9, 30.20, 11.9]
    },
    '04': { // pierwsza sobota
      food: [10.20, 11.50, 2.5],
      fuel: []
    }
  },
  '2023-04': {}
}

console.log(solution1(expenses)) // Oczekiwany wynik: mediana wydatków
console.log(solution2(expenses)) // Oczekiwany wynik: mediana wydatków
