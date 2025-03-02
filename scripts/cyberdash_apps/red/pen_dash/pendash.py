# Red Team Dashboard (Pen Dash)

## Project Structure:
```
~/Documents/scripts/cyberdash_apps/red/
├── pen_dash/
│   └── pendash.py  # Main Dash app
├── redplts/
│   ├── redALLplts.py  # All plotting functions
│   ├── rednetworkgraph.py
│   ├── redscatterplot.py
│   ├── redboxplot.py
│   ├── redradarchart.py
│   ├── redstepplot.py
```

## 🔹 `pendash.py` (Dash App Template)
```python
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import base64
import io
from redplts.redALLplts import plot_scatter, plot_network, plot_box

# Convert Matplotlib Figure to Base64
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Generate Figures
scatter_img = fig_to_base64(plot_scatter())
network_img = fig_to_base64(plot_network())
box_img = fig_to_base64(plot_box())

# App Layout
app.layout = dbc.Container([
    html.H1("Pen Dash - Red Team Dashboard", className="text-center text-danger mb-4"),
    
    html.H3("Scatter Plot"),
    html.Img(src=scatter_img, style={"width": "100%"}),
    
    html.H3("Network Graph"),
    html.Img(src=network_img, style={"width": "100%"}),
    
    html.H3("Box Plot"),
    html.Img(src=box_img, style={"width": "100%"})
])

if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8050, debug=True)
```

## 🔹 Next Steps
- Modify `redALLplts.py` to include `plot_scatter()`, `plot_network()`, and `plot_box()`.
- Ensure each function returns a `matplotlib.figure.Figure` object.
- Extend `pendash.py` to include additional plots dynamically.
