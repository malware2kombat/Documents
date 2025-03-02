"creates sample database for testing"

import sqlite3

conn = sqlite3.connect("test_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chart_data (
    x_value TEXT,
    y_value INTEGER
)
""")

sample_data = [("A", 30), ("B", 60), ("C", 10)]
cursor.executemany("INSERT INTO chart_data (x_value, y_value) VALUES (?, ?)", sample_data)

conn.commit()
conn.close()
print("Database created with sample data.")
