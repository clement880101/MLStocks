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
        if (period <= 0):
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
    # print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'macd', API_key)
    # print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'rsi', API_key, 14)
    # print(data)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'cci', API_key, 20)
    # print(data)
    comp = merge(comp, data)
    # Alpha Vantage only allows 5 pulls per minute
    print("Waiting for 1 minute cooldown")
    time.sleep(60)
    data, meta = get_daily_technical(stock, 'aroon', API_key, 14)
    comp = merge(comp, data)
    print('Done with stock: ' + stock)
    print(comp.head(1))
    # Add more data here

    comp.to_csv(stock + ".csv")
    return comp


# makes a list of out n arguments
def make_list(*args):
    list = []
    for stock in args:
        list.append(str(stock))
    return list


def create_df(stocks_names, stocks_data):
    # add name as a prefix to each column for each stock
    for x in range(len(stocks_names)):
        stocks_data.add_prefix(stocks_names[x] + '_')

    df = stocks_data[0]
    if len(stocks_names) > 1:
        # we join each stock to the df by inner and on the date axis
        for x in range(start=1, stop=len(stocks_names)):
            df = pd.concat(objs=[df, stocks_data[x]], join='inner', axis=1)

    return df


def main():
    stocks_names = make_list('Aapl', 'Googl', 'Msft')
    stocks_data = []
    for stock in stocks_names:
        stocks_data.append(compile(stock))
    df = create_df(stocks_names, stocks_data)
    # Add symbols here to generate more csv
    print(df.head(1))


if __name__ == "__main__":
    main()
