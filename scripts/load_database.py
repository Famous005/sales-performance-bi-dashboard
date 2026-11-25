
import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
DB_PATH = BASE_DIR / "data" / "processed" / "sales_analytics.db"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_PATH)
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

# Start with a clean database
cursor.executescript("""
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS regions;

CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY,
    region_name TEXT NOT NULL
);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL,
    region_id INTEGER NOT NULL,
    customer_segment TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL
);

CREATE TABLE sales (
    transaction_id INTEGER PRIMARY KEY,
    order_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    discount_pct REAL NOT NULL,
    sales_amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

# Load CSV files into their respective tables
tables = {
    "regions": "regions.csv",
    "customers": "customers.csv",
    "products": "products.csv",
    "sales": "sales.csv",
}

for table_name, filename in tables.items():
    file_path = RAW_DIR / filename

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        placeholders = ", ".join(["?"] * len(columns))
        column_names = ", ".join(columns)

        query = (
            f"INSERT INTO {table_name} "
            f"({column_names}) VALUES ({placeholders})"
        )

        rows = [
            tuple(row[column] for column in columns)
            for row in reader
        ]

        cursor.executemany(query, rows)
        print(f"Loaded {len(rows)} records into {table_name}")

connection.commit()
connection.close()

print(f"\nDatabase created successfully: {DB_PATH}")
