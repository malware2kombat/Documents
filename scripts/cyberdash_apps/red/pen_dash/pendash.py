# Red Team Dashboard (Pen Dash)

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import base64
import io
from redplts.redALLplts import redALLplts
# Convert Matplotlib Figure to Base64
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Generate Figures
plots = redALLplts()
images = {name: fig_to_base64(fig) for name, 
                fig in plots.items()}

# App Layout
app.layout = dbc.Container([
    html.H1("Pen Dash - Red Team Dashboard", className="text-center text-danger mb-4"),
    
# Dynamically generate sections for each plot
    *[
        html.Div([
            html.H3(name.replace("_", " ").title()),
            html.Img(src=img, style={"width": "100%"})
        ], className="mb-4") for name, img in images.items()
    ]
])

if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8050, debug=True)
