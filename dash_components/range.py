import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def transform_value(value):
    return 10 ** value

app.layout = html.Div([
    html.H1("Slider"),
    dcc.RangeSlider(
        id = 'slider-slider',
        max = 30,
        min = 0,
        step= 0.5,
        value=[5, 10],

    ),
    html.Div(id = 'slider-output-container')
])
@app.callback(
    Output('slider-output-container', 'children'),
    [Input('slider-slider', 'value')]
)
def display_value(value):
   return [f'You have selected {value[1]}-{value[0]} = {value[1]-value[0]}']

if __name__ == '__main__':
    app.run_server(debug=True)