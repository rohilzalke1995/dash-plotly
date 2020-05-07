import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import dash_table
import base64
import io
import pandas as pd
import datetime
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Upload CSV or XLS",style = {'text-align':'center'}),
    dcc.Upload(
        id = 'file-upload',
        children = html.Div([
            'Drag And Drop or',
            html.A('Select File', style = {'text-align':'center'}),
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
    html.Div(id = 'file-upload-output')
])

def parse(contents, filename, date):
    context_type, context_string = contents.split(',')
    decoded = base64.b64decode(context_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There is an error in the filename -- {e}'
        ])

    return html.Div([
        html.H5(filename),
        html.H5(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
        ),
        html.Hr()
    ])

@app.callback(
    Output('file-upload-output', 'children'),
    [Input('file-upload', 'contents')],
    [State('file-upload', 'filename'),
     State('file-upload', 'last_modified')]

)

def update_table(list_of_content, list_of_file, list_of_date):
    if list_of_content is not None:
        children = [
            parse(c, n, d) for c, n, d in
            zip(list_of_content, list_of_file, list_of_date)]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)
