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


def get_daily_technical(stock, indicator, API_key, period=20):
    ti = TechIndicators(key=API_key, output_format='pandas')
    if indicator == "bband":
        # Return daily bband with 20 sma
        data, meta_data = ti.get_bbands(symbol=stock, interval='daily', time_period=period)
    elif indicator == "macd":
        # Return daily macd
        data, meta_data = ti.get_macd(symbol=stock, interval='daily')
    elif indicator == "macd":
        # Return daily macd
        data, meta_data = ti.get_macd(symbol=stock, interval='daily')
    else:
        sys.exit('Failed to input a valid indicator')

    return data, meta_data


def main():
    API_key = 'ATFBYYKDGZGWGJXS'
    googl_data, googl_meta = get_daily_ts('Googl', API_key)
    print(googl_data)
    print(googl_meta)


if __name__ == "__main__":
    main()
