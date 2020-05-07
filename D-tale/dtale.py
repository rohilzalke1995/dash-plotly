import pandas as pd
import dtale
from pycoingecko import CoinGeckoAPI
from datetime import datetime
from convert_unix import ConvertUnixToDatetime as co

cg = CoinGeckoAPI()
def coin_market_chart_range(id = "bitcoin", vs_currency = "usd", from_timestamp = "1555459200", to_timestamp = "1587081600"):
    price = cg.get_coin_market_chart_range_by_id(id = id, vs_currency=vs_currency, to_timestamp=to_timestamp, from_timestamp=from_timestamp)
    df = pd.DataFrame(price)
    df2 = pd.DataFrame(df['prices'].values.tolist(), columns = ['time', f'{id}_price'])
    df3 = pd.DataFrame(df['prices'], columns = ['time', f'{id}_price'])
    df2['time'] = df2['time'].apply(lambda x: co(x).convert_unix())
    df2 = df2.set_index('time')

    total_volumes = []
    market_caps = []
    for keys, values in df['market_caps']:
        market_caps.append(values)
    print(df.columns)
    for key, values in df['total_volumes']:
        total_volumes.append(values)

    df2[f'{id}_market_caps'] = market_caps
    df2[f'{id}_total_volumes'] = total_volumes
    return df2

bitcoin = coin_market_chart_range()


# etherium = coin_market_chart_range(id = 'ethereum')