import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Upload Image",style = {'text-align':'center'}),
    dcc.Upload(
        id = 'image-upload',
        children = html.Div([
            'Drag And Drop or ',
            html.A('Select File'),
        ]),
        style= {
            'width':'100%',
            'height':'60px',
            'border-style':'solid',
            'lineWidth':'1px',
            'text-align':'center',
            'margin': '10px',

        },
        multiple=True
    ),
    html.Div(id = 'image-upload-output')
])

def parse(contents, filename, date):
    return html.Div([
        html.H6(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.Img(src=contents, style={'width': '500px', 'height': '400px'}),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
                     'whiteSpace': 'pre-wrap',
                     'wordBreak': 'break-all'
                 })

    ])


@app.callback(
    Output('image-upload-output', 'children'),
    [Input('image-upload', 'contents')],
    [State('image-upload', 'filename'),
     State('image-upload', 'last_modified')]
)

def upload_image(list_of_contents, list_of_filename, list_of_date):
    if list_of_contents is not None:
        children = [
            parse(c, n, d) for c, n, d in zip(list_of_contents, list_of_filename, list_of_date)]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)


