'''COPIED FROM "blueALLplts.py" MAKE CHANGES FOR RED''' 

import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
import sqlite3  # For database support

def blue_bar_chart(x_labels, y_values):
    """Creates a blue bar chart from given labels and values."""
    plt.bar(x_labels, y_values, color='blue')
    plt.title("Blue Bar Chart")
    plt.show()

# Load CSV
def load_csv_data(filename):
    """Loads data from a CSV file and returns x and y lists."""
    df = pd.read_csv(filename)
    return df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist()  # Assumes first column is X, second is Y

# Load JSON
def load_json_data(filename):
    """Loads data from a JSON file and returns x and y lists."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['x'], data['y']  # Assumes JSON has {"x": [...], "y": [...]}

# Load from API
def load_api_data(url):
    """Fetches data from an API and returns x and y lists."""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Assuming API returns {"x": [...], "y": [...]}
        return data['x'], data['y']
    else:
        raise Exception(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

# Load from SQLite Database
def load_db_data(db_name, table_name):
    """Fetches data from a SQLite database and returns x and y lists."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT x_value, y_value FROM {table_name}")
    data = cursor.fetchall()
    
    conn.close()
    
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]
    
    return x_values, y_values

if __name__ == "__main__":
    # Example 1: Hardcoded Data
    x1 = ["Item A", "Item B", "Item C"]
    y1 = [10, 25, 15]
    blue_bar_chart(x1, y1)

    # Example 2: Load from CSV
    x_csv, y_csv = load_csv_data("sales_data.csv")
    blue_bar_chart(x_csv, y_csv)

    # Example 3: Load from JSON
    x_json, y_json = load_json_data("data.json")
    blue_bar_chart(x_json, y_json)

    # Example 4: Load from API
    api_url = "https://example.com/data.json"  # Replace with actual API
    try:
        x_api, y_api = load_api_data(api_url)
        blue_bar_chart(x_api, y_api)
    except Exception as e:
        print(e)

    # Example 5: Load from SQLite Database
    x_db, y_db = load_db_data("my_database.db", "chart_data")
    blue_bar_chart(x_db, y_db)
