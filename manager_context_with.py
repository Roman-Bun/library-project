products = [
    {"name": "Ноутбук", "price": 30000},
    {"name": "Мишка", "price": 500},
    {"name": "Монітор", "price": 8000},
    {"name": "Клавіатура", "price": 1200},
]

def write_products(products, file_name):
    with open (file_name, "w") as f:
        for product in products:
            f.write(f"{product['name']}: {product['price']} грн\n")

def read_products(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()

# Записуємо
write_products(products, "products.txt")

# Зчитуємо
for line in read_products("products.txt"):
    print(line)
