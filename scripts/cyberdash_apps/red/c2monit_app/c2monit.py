from flask import Flask, request, jsonify
import dash
from dash import dcc
from dash import html
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix='/dashboard/')

# Placeholder for C2 logs
c2_logs = []

def generate_plot():
    if not c2_logs:
        return ''
    
    timestamps = [log.get("timestamp", "Unknown") for log in c2_logs]
    values = list(range(len(c2_logs)))
    
    plt.figure(figsize=(6, 4))
    plt.plot(values, timestamps, marker='o', linestyle='-')
    plt.xlabel("Entries")
    plt.ylabel("Timestamps")
    plt.title("C2 Log Activity")
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    
    return f'data:image/png;base64,{encoded_image}'

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify({'logs': c2_logs})

@app.route('/logs', methods=['POST'])
def add_log():
    data = request.json
    c2_logs.append(data)
    return jsonify({'message': 'Log added', 'log': data}), 201

dash_app.layout = html.Div([
    html.H1("C2 Monitoring Dashboard"),
    dcc.Graph(id='c2-graph', figure={}),
    html.Img(id='c2-plot', src='')
])

@dash_app.callback(
    dash.dependencies.Output('c2-plot', 'src'),
    [dash.dependencies.Input('c2-graph', 'id')]
)
def update_graph(_):
    return generate_plot()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)