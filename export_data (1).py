import pandas as pd
import mysql.connector

# DB connection (adjust password if needed)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jassmof7",
    database="smart_inventory"
)

# Export each table
tables = ["products", "customers", "orders", "order_items"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    df.to_csv(f"{table}.csv", index=False)
    print(f"{table}.csv exported")

conn.close()