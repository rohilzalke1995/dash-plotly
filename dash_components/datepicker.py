import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from dash.dependencies import Input, Output
from alpha_vantage.timeseries import TimeSeries

API_key = ' TKJQ1Z3KLMSMIYHK'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerSingle(
        id = 'date-picker',
        date = dt(2019, 5, 3)
    ),
    html.Div(id = 'date-picker-output-container')
])

api = API_key
period = 60
ts = TimeSeries(key = api, output_format='pandas')
@app.callback(
    Output('date-picker-output-container', 'children'),
    [Input('date-picker', 'date')]
)
def render(date):
    # We will ask for a stock and we will get there daily values of that stock
    data_ts = ts.get_daily(symbol='fb', outputsize='full')
    price_df = data_ts[0][period::]
    date = dt.strptime(str(date), '%Y-%m-%d')
    price_table = price_df.index > date

    return html.Div(
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in price_df[price_table].columns],
            data=price_df[price_table].to_dict('records'),
            style_cell={'width': '300px',
                        'height': '30px',
                        'textAlign': 'left'}
        ))


if __name__ == '__main__':
    app.run_server(debug=True)