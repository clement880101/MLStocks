# MLStocks

##compile.py 
For compiling daily data
### Alpha Vantage Related Functions
**get_daily_ts(stock, API_key):**<br />
Returns daily opening, closing, highest, 
and lowest price, as well as daily volume.<br /><br />

**get_daily_technical(stock, indicator, API_key, *period*):**<br />
Returns data for different types of indicators. Period is an optional
variable specifying period of calculation if applicable.<br /><br />
Supported indicators include:
- 'bband'; Bollinger Band; Default period = 20
- 'macd'; Moving Average Convergence Divergence; Period not used
- 'rsi'; Relative Strength Index; Default period = 14
- 'cci'; Commodity Channel Index; Default period = 20
- 'aroon'; Aroon; Default period = 14
- 'ad'; Chaikin A/D line; Period not used
- 'adx'; Average Directional Movement Index; Default period = 20
- 'sma'; Simple Moving Average; Default period = 40

### Other Functions
**merge(left, right)**<br />
Combine two dataframes<br />

**compile(stock)** Incomplete<br />
Combine all data we want on a stock 
and return a dataframe. A csv file will also
be created.

**combine_df(stock_names, stocks_data)**<br />
Merge dataframe of different stocks together to
Combined_Stock_Data.csv

##rnn (Recurrent Neural Network)
