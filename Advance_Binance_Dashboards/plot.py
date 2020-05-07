import plotly.offline as py
import plotly.graph_objects as go
from data import price_binance

trace_table = go.Table(
    domain = dict(x = [0, 0.6],
                  y = [0, 1.0]),

    columnwidth = [50] + [20, 20, 20],
    columnorder = [0, 1,2,3],
    header = dict(height = 50,
                  values = [['<b>Date </b>'], ['<b>Open Price</b>'], ['<b>High Price</b>'], ['<b>Low Price</b>'], ['<b>Closing Price</b>'], ['<b>Volume</b>'], ['<b>No Of Trades</b>']],
                  line = dict(color = 'rgb(50, 50, 50)'),
                  align = ['left']*5,
                  font = dict(color = ['rgb(45, 45, 45)']),
                  fill = dict(color = 'rgb(135, 193, 238)')
                  ),
    cells = dict(values = [price_binance().index[:], price_binance()['open'], price_binance()['high'], price_binance()['low'], price_binance()['close'], price_binance()['volume'], price_binance()['no_of_trades']],
                 line = dict(color = '#106784'),
                 align = ['left']*5,
                 font = dict(color = ['rgb(45, 45, 45)']),
                 format = [None] + [', .2f'] * 2 + [', .4f'],

                 suffix = [None] * 3,
                 height = 27,
                 fill = dict(color = ['rgb(135, 193, 238)', 'rgba(128, 222, 249, 0.65)']))

)
trace = go.Ohlc(
    x = price_binance().index[:],
    open = price_binance()['open'],
    high = price_binance()['high'],
    low = price_binance()['low'],
    close = price_binance()['close']
)
trace2 = go.Scatter(x = price_binance().index[:],
    y = price_binance()['volume'],
    xaxis = 'x2',
    yaxis = 'y2',
    line = dict(width = 2, color = 'yellow'),
    name = 'volume',

)

trace3 = go.Scatter(x = price_binance().index[:],
    y = price_binance()['no_of_trades'],
    xaxis = 'x3',
    yaxis = 'y3',
    line = dict(width = 2, color = 'purple'),
    name = 'no_of_trades'
)
axis = dict(
    showline = True,
    zeroline = False,
    showgrid = True,
    mirror = True,
    ticklen = 4,
    gridcolor ='#ffffff',
    tickfont = (dict(size = 10)),


)
layout = dict(
    width = 950,
    height = 800,
    autosize = True,
    title = 'trade Data',
    margin = dict(t=90),
    showlegend = True,
    xaxis1 = dict(axis, **dict(domain = [0.55, 1], anchor = 'y1', showticklabels = False)),
    xaxis2 = dict(axis, **dict(domain = [0.55, 1], anchor = 'y2', showticklabels = True)),
    xaxis3 = dict(axis, **dict(domain = [0.55, 1], anchor = 'y1', showticklabels = True)),
    #
    yaxis1 = dict(axis, **dict(domain = [0.66, 1], anchor = 'x1', hoverformat = '.2f')),
    yaxis2 = dict(axis, **dict(domain = [0.3 + 0.03, 0.63], anchor = 'x2', hoverformat = '.2f')),
    yaxis3 = dict(axis, **dict(domain = [0.0, 0.3], anchor = 'x3', hoverformat = '.2f')),

)

fig = dict(data = [trace_table, trace, trace2, trace3], layout = layout)


py.plot(fig, filename = 'table1.html')
