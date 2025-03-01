import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# prepare the data
df = pd.read_csv('file_path')
df["name"] = pd.Series(df["name"]).str.lower()
df["date_time"] = pd.to_datetime(df["date_time"], dayfirst=True)
df = (df.groupby([df["date_time"].dt.date, "name"])[
    ["number_of_likes", "number_of_shares"]].mean().astype(int))
df = df.reset_index()

# create the app
stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    html.H1("Twitter Likes Analysis of Famous People", style={"text-align": "center"}),
        className="row",),
html.Div(
        dcc.graph(id="line-chart", figure={}), className="row"),
html.Div(
        dcc.Dropdown(
            id="my-dropdown",
            options=[{"label": x, "value": x} for x in sorted(df["name"].unique())],
            value=["taylorswift13", "cristiano", "jtimberlake"],),
            className="three columns",),
html.Div(
        html.A(
            id="my-link",
            children="Click here to visit Twitter",
            href="https://twitter.com/explore",
            target="_blank",),
            className="two columns",),
className="row",


# create the callback
@app.callback(
    Output(component_id="line-chart", component_property="figure"),
    [Input(component_id="my-dropdown", component_property="value")])

def update_graph(chosen_value):
    print(f"Values chosen by user: {chosen_value}")

    if len(chosen_value) == 0:
        return {}
    else:
        df_filter = df[df["name"].isin(chosen_value)]
        fig = px.line(
            data_frame=df_filtered,
            x="date_time",
            y="number_of_likes",
            color="name",
            log_y=True,
            labels={"number_of_likes": "Likes",
            "date_time": "Date",
            "name": "Celebrity"},)
        return fig

if __name__ == "__main__":
    app.run_server(debug=True)