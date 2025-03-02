import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import json
import requests
import sqlite3  # For database support

# Scatter Plot "Network Vulnerabilities"
def redscatterplot():
    x = np.random.randint(1, 10, 20)  # CVSS Scores
    y = np.random.randint(1, 50, 20)  # Affected Hosts
    fig, ax = plt.subplots()
    ax.scatter(x, y, c='red', marker='x')
    ax.set_xlabel("CVSS Score")
    ax.set_ylabel("Number of Affected Hosts")
    ax.set_title("Vulnerabilities by CVSS Score")
    return fig

# Box Plot "I.D.S. Reaction Times" 
def redboxplot():
    data = [np.random.randint(1, 20, 10) for _ in range(3)]  # Different attack vectors
    fig, ax = plt.subplots()
    ax.boxplot(data, labels=["SQLi", "XSS", "DDoS"])
    ax.set_xlabel("Attack Type")
    ax.set_ylabel("Reaction Time (s)")
    ax.set_title("IDS Reaction Time Distribution")
    return fig

# Radar Chart "Attack Tool Comparison"
def redradarchart():
    from math import pi
    categories = ["Stealth", "Speed", "Impact", "Difficulty"]
    values = [3, 4, 5, 2]
    values += values[:1]  # Close the radar shape
    angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
    angles += angles[:1]
    
    fig, ax = plt.subplots(subplot_kw={'polar': True})
    ax.fill(angles, values, color='red', alpha=0.4)
    ax.plot(angles, values, color='red', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Comparison of Attack Tools")
    return fig

# Network Graph "Attack Paths"
def rednetworkgraph():
    G = nx.Graph()
    nodes = ["Attacker", "Firewall", "Web Server", "Database", "Admin"]
    G.add_edges_from([("Attacker", "Firewall"), ("Firewall", "Web Server"), ("Web Server", "Database"), ("Database", "Admin")])
    
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=2000, font_size=10)
    ax.set_title("Attack Path Visualization")
    return fig


#Step Plot "Attack Progression"
def redstepplot():
    x = np.arange(5)
    y = [1, 2, 3, 4, 5]  # Stages of attack
    fig, ax = plt.subplots()
    ax.step(x, y, where='mid', color='red', linewidth=2, label="Attack Stages")
    ax.set_xticklabels(["Recon", "Exploitation", "Privilege Esc.", "Persistence", "Exfiltration"])
    ax.set_xlabel("Attack Phase")
    ax.set_ylabel("Progress Level")
    ax.set_title("Stages of a Simulated Attack")
    ax.legend()
    return fig
 
 # generates all above plots in one import
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import json
import requests
import sqlite3  # For database support

# Scatter Plot "Network Vulnerabilities"
def redscatterplot():
    x = np.random.randint(1, 10, 20)  # CVSS Scores
    y = np.random.randint(1, 50, 20)  # Affected Hosts
    fig, ax = plt.subplots()
    ax.scatter(x, y, c='red', marker='x')
    ax.set_xlabel("CVSS Score")
    ax.set_ylabel("Number of Affected Hosts")
    ax.set_title("Vulnerabilities by CVSS Score")
    return fig

# Box Plot "I.D.S. Reaction Times"
def redboxplot():
    data = [np.random.randint(1, 20, 10) for _ in range(3)]  # Different attack vectors
    fig, ax = plt.subplots()
    ax.boxplot(data, labels=["SQLi", "XSS", "DDoS"])
    ax.set_xlabel("Attack Type")
    ax.set_ylabel("Reaction Time (s)")
    ax.set_title("IDS Reaction Time Distribution")
    return fig

# Radar Chart "Attack Tool Comparison"
def redradarchart():
    from math import pi
    categories = ["Stealth", "Speed", "Impact", "Difficulty"]
    values = [3, 4, 5, 2]
    values += values[:1]  # Close the radar shape
    angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={'polar': True})
    ax.fill(angles, values, color='red', alpha=0.4)
    ax.plot(angles, values, color='red', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Comparison of Attack Tools")
    return fig

# Network Graph "Attack Paths"
def rednetworkgraph():
    G = nx.Graph()
    nodes = ["Attacker", "Firewall", "Web Server", "Database", "Admin"]
    G.add_edges_from([("Attacker", "Firewall"), ("Firewall", "Web Server"), ("Web Server", "Database"), ("Database", "Admin")])

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='red', edge_color='black', node_size=2000, font_size=10)
    ax.set_title("Attack Path Visualization")
    return fig

# Step Plot "Attack Progression"
def redstepplot():
    x = np.arange(5)
    y = [1, 2, 3, 4, 5]  # Stages of attack
    fig, ax = plt.subplots()
    ax.step(x, y, where='mid', color='red', linewidth=2, label="Attack Stages")
    ax.set_xticks(x)  # Fix for deprecated set_xticklabels without explicit ticks
    ax.set_xticklabels(["Recon", "Exploitation", "Privilege Esc.", "Persistence", "Exfiltration"])
    ax.set_xlabel("Attack Phase")
    ax.set_ylabel("Progress Level")
    ax.set_title("Stages of a Simulated Attack")
    ax.legend()
    return fig

# Function to generate all plots for PenDash
def redALLplts():
    return {
        "scatterplot": redscatterplot(),
        "boxplot": redboxplot(),
        "radarchart": redradarchart(),
        "networkgraph": rednetworkgraph(),
        "stepplot": redstepplot()
    }

# Main execution block
if __name__ == "__main__":
    plots = redALLplts()
    for title, fig in plots.items():
        fig.show()


#reminder above functions have to input data same as "def blue bar chart"
'''def blue_bar_chart(x_labels, y_values):
    """Creates a blue bar chart from given labels and values."""
    ax.bar(x_labels, y_values, color='blue')
    ax.title("Blue Bar Chart")
    ax.show()'''

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

# Main execution block
if __name__ == "__main__":
    plots = redALLplts()
    for title, fig in plots.items():
        fig.show()
 
