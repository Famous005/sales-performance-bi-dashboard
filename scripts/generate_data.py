
import csv
import random
from pathlib import Path
from datetime import date, timedelta

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def save_csv(filename, fieldnames, rows):
    path = RAW_DIR / filename
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Created {path.name}: {len(rows)} records")


# 1. Regions
regions = [
    {"region_id": 1, "region_name": "North Central"},
    {"region_id": 2, "region_name": "North West"},
    {"region_id": 3, "region_name": "North East"},
    {"region_id": 4, "region_name": "South West"},
    {"region_id": 5, "region_name": "South East"},
    {"region_id": 6, "region_name": "South South"},
]

save_csv("regions.csv", list(regions[0]), regions)


# 2. Customers
first_names = [
    "Amina", "David", "Grace", "Ibrahim", "Mary",
    "John", "Fatima", "Samuel", "Blessing", "Musa",
    "Esther", "Daniel", "Zainab", "Peter", "Joy"
]

last_names = [
    "Abdullahi", "Okafor", "Bello", "Adeyemi", "James",
    "Mohammed", "Eze", "Yusuf", "Olawale", "Garba"
]

cities = {
    1: ["Minna", "Bida", "Abuja"],
    2: ["Kano", "Kaduna", "Sokoto"],
    3: ["Maiduguri", "Yola", "Bauchi"],
    4: ["Lagos", "Ibadan", "Abeokuta"],
    5: ["Enugu", "Owerri", "Abakaliki"],
    6: ["Port Harcourt", "Uyo", "Warri"],
}

segments = ["Consumer", "Corporate", "Small Business"]

customers = []

for customer_id in range(1, 101):
    region_id = random.choice(list(cities))
    customers.append({
        "customer_id": customer_id,
        "customer_name": (
            f"{random.choice(first_names)} "
            f"{random.choice(last_names)}"
        ),
        "city": random.choice(cities[region_id]),
        "region_id": region_id,
        "customer_segment": random.choice(segments),
    })

save_csv("customers.csv", list(customers[0]), customers)


# 3. Products
product_catalogue = [
    ("Laptop", "Electronics", 650000),
    ("Smartphone", "Electronics", 350000),
    ("Tablet", "Electronics", 220000),
    ("Monitor", "Electronics", 180000),
    ("Keyboard", "Accessories", 25000),
    ("Mouse", "Accessories", 12000),
    ("Headphones", "Accessories", 45000),
    ("Printer", "Electronics", 160000),
    ("Office Chair", "Furniture", 95000),
    ("Office Desk", "Furniture", 180000),
    ("Bookshelf", "Furniture", 110000),
    ("Notebook", "Stationery", 3500),
    ("Pen Pack", "Stationery", 2500),
    ("Paper Pack", "Stationery", 8000),
    ("Stapler", "Stationery", 6500),
    ("Router", "Networking", 75000),
    ("Network Switch", "Networking", 125000),
    ("Ethernet Cable", "Networking", 5000),
    ("External Drive", "Storage", 85000),
    ("Flash Drive", "Storage", 15000),
    ("SSD", "Storage", 120000),
    ("Webcam", "Accessories", 55000),
    ("Projector", "Electronics", 450000),
    ("Filing Cabinet", "Furniture", 135000),
    ("Power Bank", "Electronics", 40000),
]

products = []

for product_id, (name, category, price) in enumerate(
    product_catalogue, start=1
):
    products.append({
        "product_id": product_id,
        "product_name": name,
        "category": category,
        "unit_price": price
    })

save_csv("products.csv", list(products[0]), products)


# 4. Sales transactions
sales = []

start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)
date_range = (end_date - start_date).days

number_of_orders = 455
number_of_transactions = 1200

# Give every order one customer and one order date
orders = {}

for order_number in range(1, number_of_orders + 1):
    orders[f"ORD-{10000 + order_number}"] = {
        "customer_id": random.randint(1, 100),
        "order_date": (
            start_date + timedelta(days=random.randint(0, date_range))
        ).isoformat()
    }

# Every order gets at least one sales line
order_ids = list(orders.keys())

# Distribute the remaining sales lines across existing orders
order_ids += random.choices(
    list(orders.keys()),
    k=number_of_transactions - number_of_orders
)

random.shuffle(order_ids)

for transaction_id, order_id in enumerate(order_ids, start=1):
    product = random.choice(products)
    quantity = random.randint(1, 8)
    discount_pct = random.choice([0, 0, 0.05, 0.10, 0.15])

    order = orders[order_id]

    gross_sales = product["unit_price"] * quantity
    sales_amount = round(
        gross_sales * (1 - discount_pct), 2
    )

    sales.append({
        "transaction_id": transaction_id,
        "order_id": order_id,
        "order_date": order["order_date"],
        "customer_id": order["customer_id"],
        "product_id": product["product_id"],
        "quantity": quantity,
        "unit_price": product["unit_price"],
        "discount_pct": discount_pct,
        "sales_amount": sales_amount,
    })

save_csv("sales.csv", list(sales[0]), sales)
