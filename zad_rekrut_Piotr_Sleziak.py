import datetime

# Funkcja pomocnicza do uzyskania dni do pierwszej niedzieli w miesiącu
def get_days_to_first_sunday(year, month):
    first_day = datetime.date(year, month, 1)
    first_sunday = (6 - first_day.weekday()) % 7 + 1  # Wyliczenie pierwszej niedzieli
    return list(range(1, first_sunday + 1))  # Zwracamy listę dni przed pierwszą niedzielą

# Funkcja do obliczania mediany z wykorzystaniem QuickSelect
def quick_select(arr, k):
    # Funkcja pomocnicza do partitioningu
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

    return None

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

    all_expenses.sort()
    mid = len(all_expenses) // 2
    if len(all_expenses) % 2 != 0:
        return all_expenses[mid]
    else:
        return (all_expenses[mid - 1] + all_expenses[mid]) / 2


def solution2(expenses):
    # QuickSelect może być stosowany do znalezienia mediany bez konieczności pełnego sortowania danych,
    # co czyni go bardziej efektywnym, jeśli chodzi o pamięć i czas obliczeń.
    # Zaletą jest oszczędność pamięci, ponieważ nie musimy przechowywać pełnej posortowanej listy.
    # Wadą algorytmu QuickSelect jest to, że w najgorszym przypadku (gdy pivot jest źle dobrany)
    # czas wykonania może wynieść O(N^2), co sprawia, że może być mniej wydajny w przypadku
    # nieoptymalnych danych wejściowych.
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


# Przykładowe dane do testów
expenses = {
    '2023-01': {  # pierwsza niedziela
        '01': {
            'food': [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            'fuel': [210.22]
        },
        '09': {
            'food': [11.9],
            'fuel': [190.22]
        }
    },
    '2023-03': {
        '07': {
            'food': [20, 11.9, 30.20, 11.9]
        },
        '04': {  # pierwsza sobota
            'food': [10.20, 11.50, 2.5],
            'fuel': []
        }
    },
    '2023-04': {}
}

# Testowanie rozwiązań
print("Solution 1 (Nieoptymalizowane):", solution1(expenses))
print("Solution 2 (Zoptymalizowane - Algorytm QuickSelect):", solution2(expenses))
