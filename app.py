from dash import Dash, dcc, html, Input, Output, callback
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
    "Sales": df1['sales'],
    "Region": df1['region']
})

fig = px.line(df, x="Year", y="Sales", color="Region")

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
        id='line-graph',
        figure=fig
    ),
    html.Br(),
    html.Label('Select Region', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.RadioItems(id='regions-radio', options=[
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'All'}
    ], value='All'),
])


@callback(
    Output('line-graph', 'figure'),
    Input('regions-radio', 'value'))
def update_graph(selected_region):
    if selected_region == 'All':
        df_filtered = df1
    else:
        df_filtered = df1[df1['region'] == selected_region]

    # Plotting
    fig = px.line(df_filtered, x="date", y="sales", color="region")
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
