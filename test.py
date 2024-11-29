import random
import datetime
import time  # Importujemy moduł time do mierzenia czasu


# Funkcja pomocnicza do uzyskania dni do pierwszej niedzieli w miesiącu
def get_days_to_first_sunday(year, month):
    first_day = datetime.date(year, month, 1)
    first_sunday = (6 - first_day.weekday()) % 7 + 1  # Wyliczenie pierwszej niedzieli
    return list(range(1, first_sunday + 1))  # Zwracamy listę dni przed pierwszą niedzielą


# Funkcja do generowania losowych danych dla expenses
def generate_expenses(num_entries=1000):
    expenses = {}
    categories = ['food', 'fuel']
    current_date = datetime.date(2023, 1, 1)

    while num_entries > 0:
        year_month = current_date.strftime('%Y-%m')
        if year_month not in expenses:
            expenses[year_month] = {}

        days_in_month = get_days_to_first_sunday(current_date.year, current_date.month)

        for day in days_in_month:
            day_key = str(day).zfill(2)  # Formatowanie klucza "01", "02", ...
            if day_key not in expenses[year_month]:
                expenses[year_month][day_key] = {}

            for category in categories:
                num_expenses = random.randint(1, 5)  # Losowa liczba wydatków w danej kategorii
                expenses[year_month][day_key].setdefault(category, [])
                expenses[year_month][day_key][category].extend(
                    [round(random.uniform(1, 100), 2) for _ in range(num_expenses)]
                )

                num_entries -= num_expenses
                if num_entries <= 0:
                    break

        current_date = (current_date.replace(day=1) + datetime.timedelta(days=32)).replace(
            day=1)  # Przechodzimy do następnego miesiąca

        if num_entries <= 0:
            break

    return expenses


# Funkcja do obliczania mediany z wykorzystaniem QuickSelect (solution2)
def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Losowanie indeksu dla pivotu (unikamy pierwszego i ostatniego elementu)
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return quick_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


def solution1(expenses):
    all_expenses = []
    for month_year, days in expenses.items():
        year, month = map(int, month_year.split('-'))
        days_to_first_sunday = get_days_to_first_sunday(year, month)

        for day in days_to_first_sunday:
            day_key = str(day).zfill(2)  # Formatowanie klucza "01", "02", ...
            if day_key in days:
                # Zbieranie wydatków z tego dnia
                daily_expenses = [item for sublist in days[day_key].values() for item in sublist]
                all_expenses.extend(daily_expenses)

    if not all_expenses:
        return None

    all_expenses.sort()  # Sortowanie wydatków w celu obliczenia mediany
    mid = len(all_expenses) // 2
    if len(all_expenses) % 2 != 0:
        return all_expenses[mid]
    else:
        return (all_expenses[mid - 1] + all_expenses[mid]) / 2


def solution2(expenses):
    all_expenses = []
    for month_year, days in expenses.items():
        year, month = map(int, month_year.split('-'))
        first_sunday_days = get_days_to_first_sunday(year, month)

        for day in first_sunday_days:
            day_key = str(day).zfill(2)  # Formatowanie klucza "01", "02", ...
            if day_key in days:
                # Zbieranie wydatków z tego dnia
                daily_expenses = [item for sublist in days[day_key].values() for item in sublist]
                all_expenses.extend(daily_expenses)

    if not all_expenses:
        return None

    n = len(all_expenses)
    if n % 2 == 1:
        return quick_select(all_expenses, n // 2)  # Dla nieparzystej liczby elementów
    else:
        left = quick_select(all_expenses, n // 2 - 1)  # Dla parzystej liczby elementów
        right = quick_select(all_expenses, n // 2)
        return (left + right) / 2


# Pomiar czasu wykonania aplikacji
start_time = time.time()  # Zaczynamy mierzenie czasu

# Generowanie 1000 wydatków
expenses = generate_expenses(2000000)

# Pomiar czasu dla solution1
start_time_solution1 = time.time()
median_solution1 = solution1(expenses)
end_time_solution1 = time.time()

# Pomiar czasu dla solution2
start_time_solution2 = time.time()
median_solution2 = solution2(expenses)
end_time_solution2 = time.time()

# Zatrzymanie mierzenia czasu
end_time = time.time()  # Zakończenie pomiaru czasu

# Wyświetlanie wyników
print(f"Mediana dla solution1: {median_solution1}")
print(f"Czas wykonania dla solution1: {end_time_solution1 - start_time_solution1:.4f} sekund")

print(f"Mediana dla solution2: {median_solution2}")
print(f"Czas wykonania dla solution2: {end_time_solution2 - start_time_solution2:.4f} sekund")

# Czas całkowity
print(f"Czas całkowity wykonania aplikacji: {end_time - start_time:.4f} sekund")
