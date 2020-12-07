import pandas as pd
import sys
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time


def get_daily_ts(stock, API_key):
    # Return daily type of historical data
    ts = TimeSeries(key=API_key, output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(stock, outputsize="full")
    data.columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume',
                    'dividend', 'split_coefficent']
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
    elif indicator == "ad":
        data, meta_data = ti.get_ad(symbol=stock, interval='daily')
    elif indicator == "adx":
        if (period <= 0):
            period = 20
        data, meta_data = ti.get_adx(symbol=stock, interval='daily', time_period=period)
    elif indicator == "sma":
        if (period <= 0):
            period = 40
        data, meta_data = ti.get_sma(symbol=stock, interval='daily', time_period=period)
    else:
        sys.exit('Failed to input a valid indicator')

    return data, meta_data


def merge(left, right):
    return pd.concat(objs=[left, right], join="inner", axis=1)


def compile(stock):
    # Keys: ##ATFBYYKDGZGWGJXS##, ##AUV1J66PW0AGIHP3##
    API_key = 'AUV1J66PW0AGIHP3'

    print("Waiting for 1 minute cooldown")
    time.sleep(60)

    print("Start Compiling...")
    comp, meta = get_daily_ts(stock, API_key)
    data, meta = get_daily_technical(stock, 'bband', API_key, 20)
    comp = merge(comp, data)

    data, meta = get_daily_technical(stock, 'macd', API_key)
    comp = merge(comp, data)

    data, meta = get_daily_technical(stock, 'rsi', API_key, 14)
    comp = merge(comp, data)

    data, meta = get_daily_technical(stock, 'cci', API_key, 20)
    comp = merge(comp, data)

    # Alpha Vantage only allows 5 pulls per minute
    print("Waiting for 1 minute cooldown")
    time.sleep(60)

    data, meta = get_daily_technical(stock, 'aroon', API_key, 14)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'ad', API_key)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'adx', API_key, 20)
    comp = merge(comp, data)
    data, meta = get_daily_technical(stock, 'sma', API_key, 40)
    comp = merge(comp, data)


    comp = comp.add_prefix(stock + '_')
    data, meta = get_daily_ts('SPY', API_key)
    data = data.add_prefix('SPY_')

    print('Done with stock: ' + stock)
    merge(comp, data).to_csv(stock + ".csv")
    return comp


def combine_df(stocks_names, stocks_data):
    # Keys: ##ATFBYYKDGZGWGJXS##, ##AUV1J66PW0AGIHP3##
    API_key = 'AUV1J66PW0AGIHP3'
    print("Combining dataframe")
    df = stocks_data[0]
    if len(stocks_names) > 1:
        # we join each stock to the df by inner and on the date axis
        for x in range(1, len(stocks_names)):
            df = merge(df, stocks_data[x])
    # Put SP500 data into df
    print("Waiting for 1 minute cooldown")
    time.sleep(60)
    data, meta = get_daily_ts('SPY', API_key)
    data = data.add_prefix('SPY_')
    df = merge(df, data)

    df.to_csv("Com.csv")
    return df


def main():
    stocks_names = ['Msft', 'Aapl', 'Googl', 'Fb', 'Amzn']
    stocks_data = []
    for stock in stocks_names:
        stocks_data.append(compile(stock))
    combine_df(stocks_names, stocks_data)


if __name__ == "__main__":
    main()
