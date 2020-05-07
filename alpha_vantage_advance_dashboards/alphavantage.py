import key
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

stock = input("Which stock you want to search? ")
def rsi_df(stock=stock):
    api_key = key.API_key
    period = 60
    ts = TimeSeries(key=api_key, output_format='pandas')#This ts is helping us to connect to API
    data_ts = ts.get_intraday(stock.upper(), interval='1min', outputsize='full')

    #indicator
    ti = TechIndicators(key=api_key, output_format='pandas')
    #data_ti, meta_data_ti = ti.get_bbands(symbol = stock.upper(), interval='1min', time_period=period, series_type='close')
    data_ti, meta_data_ti = ti.get_rsi(symbol=stock.upper(), interval='1min', time_period=period,
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
        rsi.append(l-(l/r))

    high_rsi_value = []
    high_rsi_time = []

    for value, time, l in zip(total_df['RSI'], total_df.index, low):
        if value>60:
            high_rsi_value.append(l-(l/value))
            high_rsi_time.append(time)

    low_rsi_value = []
    low_rsi_time = []
    for value, time, l in zip(total_df['RSI'], total_df.index, low):
        if value<35:
            low_rsi_value.append(l-(l/value))
            low_rsi_time.append(time)

    return print(total_df.columns)

rsi_df()

