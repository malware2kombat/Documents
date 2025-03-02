'''BLUE imports:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
'''
''' RED imports:
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
'''

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from blueplts.bluecharts import load_json_data, load_db_data

# Initialize Dash app
app = dash.Dash(__name__)

# Load Data
x_json, y_json = load_json_data("data.json")
x_db, y_db = load_db_data("my_database.db", "chart_data")

# Create Plots using Plotly
fig_bar = px.bar(x=x_json, y=y_json, labels={"x": "Categories", "y": "Values"}, title="Bar Chart from JSON")
fig_pie = px.pie(names=x_db, values=y_db, title="Pie Chart from Database")

# Layout for the Dashboard
app.layout = html.Div(children=[
    html.H1("Skeledash Dashboard"),
    
    html.Div([
        html.H3("Bar Chart (JSON Data)"),
        dcc.Graph(figure=fig_bar)
    ]),

    html.Div([
        html.H3("Pie Chart (Database Data)"),
        dcc.Graph(figure=fig_pie)
    ])
])

# Run Dash App
if __name__ == '__main__':
    app.run_server(debug=True)
