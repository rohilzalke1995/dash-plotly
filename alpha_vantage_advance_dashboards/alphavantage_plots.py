import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import key
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from plotly import graph_objs as go


app = dash.Dash()
app.layout = html.Div([
    html.P('Enter a stock'),
    dcc.Input(id = 'input-box', type = 'text', value = '', placeholder='Enter a stock'),
    html.Button('SUBMIT', id = 'submit-val'),
    dcc.Graph(animate=True, id = 'candel-graph', style={"backgroundColor": "#1a2d46", 'color':'#ffffff'},),
    html.Div([

        html.P('Developed By:'),
        html.A('Rohil Zalke', href = 'https://github.com/rohilzalke1995?tab=repositories'),

    ]),
    

    #dcc.Graph(id = 'stock-graph', automate = True)

])

api_key = ' TKJQ1Z3KLMSMIYHK'
period = 60
ts = TimeSeries(key=api_key, output_format='pandas')#This ts is helping us to connect to API
ti = TechIndicators(key=api_key, output_format='pandas')
@app.callback(
    Output('candel-graph', 'figure'),
    [Input('submit-val', 'n_clicks')],
    [State('input-box', 'value')]
)
def update_graph(n_clicks, input_value):
    data_ts = ts.get_intraday(input_value.upper(), interval='1min', outputsize='full')

    # indicator

    # data_ti, meta_data_ti = ti.get_bbands(symbol = stock.upper(), interval='1min', time_period=period, series_type='close')
    data_ti, meta_data_ti = ti.get_rsi(symbol=input_value.upper(), interval='1min', time_period=period,
                                       series_type='close')

    df = data_ts[0]

    df = df.iloc[::-1][period::]
    df.index = pd.Index(map(lambda x: str(x)[:-3], df.index))
    df.index.name = 'Date'

    df2 = data_ti
    df2.index = pd.Index(map(lambda x: str(x)[:-3], df2.index))
    df2.index.name = 'Date'
    total_df = pd.merge(df, df2, on="Date")

    open = []
    for i in total_df['1. open']:
        open.append(float(i))

    close = []
    for c in total_df['4. close']:
        close.append(float(c))

    low = []
    for l in total_df['3. low']:
        low.append(float(l))

    high = []
    for h in total_df['2. high']:
        high.append(float(h))

    rsi = []
    for r, l in zip(total_df['RSI'], low):
        rsi.append(l - (l / r))
    #sell_scatter
    high_rsi_value = []
    high_rsi_time = []

    for value, time, l in zip(total_df['RSI'], total_df.index, low):
        if value > 60:
            high_rsi_value.append(l - (l / value))
            high_rsi_time.append(time)

    #but scatter
    low_rsi_value = []
    low_rsi_time = []
    for value, time, l in zip(total_df['RSI'], total_df.index, low):
        if value < 35:
            low_rsi_value.append(l - (l / value))
            low_rsi_time.append(time)

    scatter_sell = go.Scatter(
        x = high_rsi_time,
        y = high_rsi_value,
        mode = 'markers',
        name = 'sell'
    )
    scatter_buy = go.Scatter(
        x = low_rsi_time,
        y = low_rsi_value,
        mode = 'markers',
        name = 'buy'
    )
    rsi_graph = go.Scatter(
        x = total_df.index,
        y = rsi
    )
    buyside = go.Candlestick(
        x = total_df.index,
        open = open,
        close = close,
        high = high,
        low = low,
        increasing={'line': {'color': '#00CC94'}},
        decreasing = {'line': {'color':'#BD0013'}},
        name = 'candlestick'


    )
    data = [buyside, rsi_graph, scatter_buy, scatter_sell]
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis = dict(type = 'category'),
        yaxis = dict(range = [min(rsi), max(high)]),
        font = dict(color = 'white')
      )
    return {'data':data, 'layout':layout}
if __name__ == '__main__':
    app.run_server(port=8085, debug=True)