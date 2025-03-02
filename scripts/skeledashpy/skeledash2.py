import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, Response

# Flask server instance for image rendering
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.DARKLY])

# Function to convert matplotlib figures to PNG images for Dash
def fig_to_uri(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

# Sample function for Red Team chart
def red_team_chart():
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10), color='red', marker='o', linestyle='--')
    ax.set_title("Red Team Data Visualization")
    return fig_to_uri(fig)

# Sample function for Blue Team chart
def blue_team_chart():
    fig, ax = plt.subplots()
    ax.bar(range(5), np.random.randint(1, 10, 5), color='blue')
    ax.set_title("Blue Team Metrics")
    return fig_to_uri(fig)

# App layout
app.layout = dbc.Container([
    html.H1("Red & Blue Team Dashboard", className="text-center text-primary mb-4"),
    
    # Red Team Section
    html.H3("Red Team Analysis"),
    html.Img(id="red-chart", src=red_team_chart(), style={"width": "80%"}),
    
    # Blue Team Section
    html.H3("Blue Team Analysis"),
    html.Img(id="blue-chart", src=blue_team_chart(), style={"width": "80%"})
])

if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8050, debug=True)
