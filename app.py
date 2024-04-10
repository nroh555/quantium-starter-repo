from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

# Read the CSV files
df1 = pd.read_csv("data/output.csv")
df1 = df1.sort_values(by="date")

df = pd.DataFrame({
    "Year": df1['date'],
    "Sales": df1['sales']
})

fig = px.line(df, x="Year", y="Sales")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales of Pink Morsel Before and After Price Increase on 15th January 2021',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
