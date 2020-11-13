import json
import urllib.request
import pandas as pd
import numpy as np
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


def install(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def get_daily_ts(stock, API_key):
    # Return daily closing price
    ts = TimeSeries(key=API_key, output_format='pandas')
    data, meta_data = ts.get_daily(stock)
    return data, meta_data


def get_daily_technical(stock, indicator, API_key):
    ti = TechIndicators(key=API_key, output_format='pandas')
    if indicator == "bband":
        # Return daily bband with 20 sma
        data, meta_data = ti.get_bbands(symbol=stock, interval='daily', time_period=20)
    elif indicator == "macd":
        # Return daily bband with 20 sma
        data, meta_data = ti.get_macd(symbol=stock, interval='daily', )
    return data, meta_data


def main():
    # install('alpha_vantage')
    API_key = 'ATFBYYKDGZGWGJXS'
    googl_data, googl_meta = get_daily_ts('Googl', API_key)
    print(googl_meta)


if __name__ == "__main__":
    main()
