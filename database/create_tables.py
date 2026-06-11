from database_connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    sales_amount REAL,
    inventory INTEGER
)
""")

conn.commit()

print("Sales Table Created Successfully")

conn.close()