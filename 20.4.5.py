import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

max_price_order = {'id': '', 'price': 0}
max_quantity_order = {'id': '', 'quantity': 0}

orders_by_date = {}
orders_per_user = {}
spent_per_user = {}

total_price = 0
total_quantity = 0
total_orders_count = len(orders)

for order_num, data in orders.items():
    price = data['price']
    quantity = data['quantity']
    date = data['date']
    user_id = data['user_id']

    if price > max_price_order['price']:
        max_price_order = {'id': order_num, 'price': price}

    if quantity > max_quantity_order['quantity']:
        max_quantity_order = {'id': order_num, 'quantity': quantity}

    orders_by_date[date] = orders_by_date.get(date, 0) + 1

    orders_per_user[user_id] = orders_per_user.get(user_id, 0) + 1
    spent_per_user[user_id] = spent_per_user.get(user_id, 0) + price

    total_price += price
    total_quantity += quantity

max_orders_date = max(orders_by_date, key=orders_by_date.get)

top_user_by_count = max(orders_per_user, key=orders_per_user.get)

top_user_by_spent = max(spent_per_user, key=spent_per_user.get)

avg_order_price = total_price / total_orders_count
avg_item_price = total_price / total_quantity

print(f"1. Самый дорогой заказ: {max_price_order['id']} ({max_price_order['price']})")
print(f"2. Заказ с макс. количеством товаров: {max_quantity_order['id']} ({max_quantity_order['quantity']} шт.)")
print(f"3. День с самым большим кол-вом заказов: {max_orders_date}")
print(f"4. Пользователь с макс. кол-вом заказов: {top_user_by_count}")
print(f"5. Пользователь с макс. суммой трат: {top_user_by_spent}")
print(f"6. Средняя стоимость заказа: {round(avg_order_price, 2)}")
print(f"7. Средняя стоимость товара: {round(avg_item_price, 2)}")