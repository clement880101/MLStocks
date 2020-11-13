import pandas as pd
import numpy as np
import sys
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time

def get_daily_ts(stock, API_key):
    # Return daily type of historical data
    ts = TimeSeries(key=API_key, output_format='pandas')
    data, meta_data = ts.get_daily(stock)
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    return data, meta_data


def get_daily_technical(stock, indicator, API_key, period=-1):
    ti = TechIndicators(key=API_key, output_format='pandas')
    if indicator == "bband":
        if(period <= 0):
            period = 20
        data, meta_data = ti.get_bbands(symbol=stock, interval='daily', time_period=period)
    elif indicator == "macd":
        data, meta_data = ti.get_macd(symbol=stock, interval='daily')
    elif indicator == "rsi":
        if (period <= 0):
            period = 14
        data, meta_data = ti.get_rsi(symbol=stock, interval='daily', time_period=period)
    elif indicator == "cci":
        if (period <= 0):
            period = 20
        data, meta_data = ti.get_cci(symbol=stock, interval='daily', time_period=period)
    elif indicator == "aroon":
        if (period <= 0):
            period = 14
        data, meta_data = ti.get_aroon(symbol=stock, interval='daily', time_period=period)
    else:
        sys.exit('Failed to input a valid indicator')

    return data, meta_data

def merge(left, right):
    return left.join(right, how='inner')

def compile(stock):
    API_key = 'ATFBYYKDGZGWGJXS'
    print("Start Compiling...")
    comp, meta = get_daily_ts(stock, API_key)
    data, meta = get_daily_technical(stock, 'bband', API_key, 20)
    print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'macd', API_key)
    print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'rsi', API_key, 14)
    print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'cci', API_key, 20)
    print(data)
    comp = merge(comp, data)
    # Alpha Vantage only allows 5 pulls per minute
    print("Waiting for 1 minute cooldown")
    time.sleep(60)
    data, meta = get_daily_technical(stock, 'aroon', API_key, 14)
    comp = merge(comp, data)
    print(comp)
    # Add more data here

    comp.to_csv(stock+".csv")
    return comp

def main():
    comp = compile('googl')
    # Add symbols here to generate more csv
    print(comp)


if __name__ == "__main__":
    main()
