products = [
    {"name": "Ноутбук", "price": 30000},
    {"name": "Мишка", "price": 500},
    {"name": "Монітор", "price": 8000},
    {"name": "Клавіатура", "price": 1200},
]

names_products = [n["name"] for n in products] # List comprehension — список тільки назв товарів
names_products_most_1000 = [n["name"] for n in products if n["price"] > 1000] # List comprehension — список назв товарів дорожче 1000
names_products_dict = {n["name"]: n["price"] for n in products}
print(names_products)
print(names_products_most_1000)
print(names_products_dict)