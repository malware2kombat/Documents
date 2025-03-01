import dash
from dash import dcc, html
from dash import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import nmap
import subprocess

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# nmap scan function
def run_nmap_scan(target="192.168.1.1"):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV --open')

    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                results.append({
                    "Target": host,
                    "Port": port,
                    "Service": nm[host][proto][port]['name'],
                    "Version": nm[host][proto][port].get("version", "Unknown")})
    return pd.DataFrame(results)

# Metasploit session data
def get_metasploit_sessions():
    try:
        output = subprocess.check_output(["msfconsole", "-q", "-x", "sessions -l; exit"], text=True)              
        return output.stdout
    except Exception as e:
        return f"Error: {e}"

# simulate web app scan results
def web_scan_results():
    return pd.DataFrame({
        "URL": ["http://example.com", "http://target.com"],
        "Vuln Found": ["SQL Injection", "XSS"],
        "Risk Level": ["High", "Medium"]
    })

# Run scans
nmap_df = run_nmap_scan()
web_df = web_scan_results()
metasploit_sessions = get_metasploit_sessions()

if not  nmap_df.empty:
    nmap_figure = px.bar(nmap_df, x="Port", y="Target", color="Service", barmode="group", 
                            title="Open Ports & Services"),
else:
    nmap_figure = px.bar(title="No Open Ports Found")
# app layout
app.layout = dbc.Container([
    html.H1("P.T. Dash", className="text-center text-primary mb-4"),

    #Nmap scan results
    html.H3("Live Nmap Scan"),
    dcc.Graph(figure=nmap_figure),
        
    
    # Web app scan results
    html.H3("Web App Scan Results"),
    dcc.Graph(
        figure=px.bar(web_df, x="URL", y="Risk Level", color="Vuln Found", 
        title="Web Vulnerabilities")),

    # Metasploit sessions
    html.H3("Metasploit Sessions"),
    html.Pre(metasploit_sessions, style={"white-space": "pre-wrap", "background-color": "black", 
                                         "color": "lime"})
])

@app.callback(
    [Output("nmap-graph", "figure"),
     Output("web-graph", "figure"),
     Output("metasploit-output", "children"),
     Output("nmap-data", "data"),
     Output("web-data", "data"),
     Output("metasploit-data", "data")],  # Stores updated results
    Input("scan-btn", "n_clicks"),  # Triggers when button is clicked
    State("target-ip", "value")  # Uses input value as scan target
)
def update_scan(n_clicks, target_ip):
    if n_clicks == 0:
        return dash.no_update  # Prevents running scan on startup

    nmap_df = run_nmap_scan(target_ip)
    web_df = web_scan_results()
    metasploit_output = get_metasploit_sessions()

    # Generate Figures dynamically
    nmap_fig = px.bar(nmap_df, x="Port", y="Target", color="Service", barmode="group", title="Open Ports & Services") if not nmap_df.empty else px.bar(title="No Open Ports Found")
    web_fig = px.bar(web_df, x="URL", y="Risk Level", color="Vuln Found", title="Web Vulnerabilities")

    return nmap_fig, web_fig, metasploit_output, nmap_df.to_dict(), web_df.to_dict(), metasploit_output  # Updates UI with results

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port=8050, debug=True)