import re

# Словари для хранения данных
pizza_orders = {}  # Количество заказов по пиццам
date_revenue = {}  # Выручка по датам
all_orders = []  # Список всех заказов (для поиска самого дорогого)
total_price = 0  # Общая стоимость заказов
total_orders = 0  # Количество заказов

print("Введите заказы (дд.мм.гггг Пицца Цена). Для завершения введите 'Конец рабочего дня'.")

while True:
    line = input()
    
    if line == "Конец рабочего дня":
        break

    # Разделяем строку по запятой, точке с запятой или пробелу
    parts = re.split(r'[ ,;]+', line, maxsplit=2)
    
    if len(parts) != 3:
        print(f"Ошибка: строка '{line}' не соответствует формату (дата, название, цена)")
        continue

    date, pizza, price = parts

    # Проверяем формат даты (должен быть дд.мм.гггг или дд/мм/гггг)
    if not re.match(r'^\d{2}[\./]\d{2}[\./]\d{4}$', date):
        print(f"Ошибка: некорректный формат даты в строке '{line}'")
        continue

    # Нормализация даты (замена / на .)
    date = date.replace("/", ".")

    # Убираем кавычки у названия пиццы
    pizza = pizza.strip("\"'")

    # Нормализация цены (замена запятой на точку)
    price = price.replace(",", ".")

    try:
        price = float(price)  # Преобразуем в число
    except ValueError:
        print(f"Ошибка: некорректная цена в строке '{line}'")
        continue

    # Считаем заказы по пиццам
    pizza_orders[pizza] = pizza_orders.get(pizza, 0) + 1

    # Считаем выручку по датам
    date_revenue[date] = date_revenue.get(date, 0) + price

    # Запоминаем все заказы
    all_orders.append((date, pizza, price))

    total_price += price
    total_orders += 1

# Вывод результатов

# а) Список пицц по популярности
print("\nСписок пицц по популярности:")
sorted_pizzas = sorted(pizza_orders.items(), key=lambda x: x[1], reverse=True)
for pizza, count in sorted_pizzas:
    print(f"{pizza}: {count} заказов")

# б) Выручка по датам (хронологический порядок)
print("\nВыручка по датам:")
sorted_dates = sorted(date_revenue.items())
for date, revenue in sorted_dates:
    print(f"{date}: {revenue:.2f} руб.")

# в) Самый дорогой заказ
if all_orders:
    most_expensive_order = max(all_orders, key=lambda x: x[2])
    print("\nСамый дорогой заказ:")
    print(f"Дата: {most_expensive_order[0]}, Пицца: {most_expensive_order[1]}, Цена: {most_expensive_order[2]:.2f} руб.")
else:
    print("\nСамый дорогой заказ: нет данных.")

# г) Средняя стоимость заказа
average_price = total_price / total_orders if total_orders else 0
print(f"\nСредняя стоимость заказа: {average_price:.2f} руб.")