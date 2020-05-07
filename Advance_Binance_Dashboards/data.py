from binance.client import Client
import pandas as pd
from datetime import datetime
from pandas import DataFrame as df
import keys

def price_binance():
    #api_keys and api_secret are stored in keys.py file in the same folder, donot post it on github.
    client = Client(api_key = keys.pkey, api_secret = keys.skey)

    #getting kline/candelstics from python-binance documentation

    candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)

    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    dataframe_final_date.columns = ['date']

    final_df = candles_data_frame.join(dataframe_final_date)
    final_df.set_index('date', inplace=True)
    final_df.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_value', 'no_of_trades', 'taker_by_base', 'taker_by_quotes']
    return final_df

print(price_binance())
