import dash
import plotly.offline as py
import datetime
import plotly.graph_objects as go
import pandas_datareader as web

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2020, 3, 1)

FB = web.DataReader('FB', 'yahoo', start, end)
TW = web.DataReader('TWTR', 'yahoo', start, end)
APL = web.DataReader('AAPL', 'yahoo', start, end)


trace1 = go.Ohlc(
    x = FB.index[:],
    high = FB['High'],
    low = FB['Low'],
    open = FB['Open'],
    close = FB['Close'],
    name = 'FB',
    increasing = dict(line = dict(color = 'green')),
    decreasing = dict(line = dict(color = 'red'))
)



trace2 = go.Ohlc(
    x = TW.index[:],
    high = TW['High'],
    low = TW['Low'],
    open = TW['Open'],
    close = TW['Close'],
    name = 'TW',
    increasing = dict(line = dict(color = 'green')),
    decreasing = dict(line = dict(color = 'red'))
)


trace3 = go.Ohlc(
    x = APL.index[:],
    high = APL['High'],
    low = APL['Low'],
    open = FB['Open'],
    close = APL['Close'],
    name = 'APL',
    increasing = dict(line = dict(color = 'green')),
    decreasing = dict(line = dict(color = 'red'))
)
data = [trace1, trace2, trace3]
layout = {
    'title': 'facebook vs twitter vs apple',
    'yaxis': {'title': 'price per stock'},
    'xaxis': {'title': 'date'}
}

fig = dict(data = data, layout = layout)
py.plot(fig, filename = 'text1.html')

