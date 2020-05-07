import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from collections import Counter
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Word Count Graph"),
    dcc.Graph(id = 'word-graph', animate = True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Textarea(
        id = 'text-area',
        value = '',
        placeholder='Common words...',
        style={'width':'100%', 'height':'50%'},
    ),

])
@app.callback(
    Output('word-graph', 'figure'),
    [Input('text-area', 'value')]
)
def display_graph(value):
    word_list = value.split()
    word_dict = Counter(word_list)
    x = list(word_dict.keys())
    y = list(word_dict.values())

    graph = go.Bar(
        x=x,
        y=y,
        name='word-count',
        type='bar',
        marker=dict(color='lightgreen')
    )
    plot_bgcolor='rgba(0,0,0,0)',

    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis = dict(type = 'category'),
        yaxis = dict(range=[min(y), max(y)]),
        font = dict(color='white')
    )

    return {'data':[graph], 'layout':layout}

if __name__ == '__main__':
    app.run_server(debug=True)




