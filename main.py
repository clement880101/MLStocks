import pandas as pd
import numpy as np
import sys
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

def get_daily_ts(stock, API_key):
    # Return daily type of historical data
    ts = TimeSeries(key=API_key, output_format='pandas')
    data, meta_data = ts.get_daily(stock)
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    return data, meta_data


def get_daily_technical(stock, indicator, API_key, period=-1):
    ti = TechIndicators(key=API_key, output_format='pandas')
    if indicator == "bband":
        # Return daily bband with 20 sma
        if(period <= 0):
            period = 20
        data, meta_data = ti.get_bbands(symbol=stock, interval='daily', time_period=period)
    elif indicator == "macd":
        # Return daily macd
        data, meta_data = ti.get_macd(symbol=stock, interval='daily')
    elif indicator == "rsi":
        # Return daily rsi
        if (period <= 0):
            period = 14
        data, meta_data = ti.get_rsi(symbol=stock, interval='daily', time_period=period)
    elif indicator == "cci":
        # Return daily rsi
        if (period <= 0):
            period = 20
        data, meta_data = ti.get_cci(symbol=stock, interval='daily', time_period=period)
    elif indicator == "aroon":
        # Return daily rsi
        if (period <= 0):
            period = 14
        data, meta_data = ti.get_aroon(symbol=stock, interval='daily', time_period=period)
    else:
        sys.exit('Failed to input a valid indicator')

    return data, meta_data

def merge(left, right):
    left.join(right, how='inner')
    return left

def main():
    API_key = 'ATFBYYKDGZGWGJXS'
    data1, meta1 = get_daily_technical('googl', 'macd', API_key)
    data2, meta2 = get_daily_technical('googl', 'bband', API_key)
    print(data1)
    print(data2)
    data = merge(data1, data2)
    print(data)



if __name__ == "__main__":
    main()
