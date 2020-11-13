# MLStocks

### Alpha Vantage Related Functions
**get_daily_ts(stock, API_key):**<br />
Returns daily opening, closing, highest, 
and lowest price, as well as daily volume.<br /><br />

**get_daily_technical(stock, indicator, API_key, *period*):**<br />
Returns data for different types of indicators. Period is an optional
variable specifying period of calculation if applicable.<br /><br />
Supported indicators include:
- 'bband'; Bollinger Band; Default period = 20
- 'macd'; Moving Average Convergence Divergence; Period not in use
- 'rsi'; Relative Strength Index; Default period = 14
- 'cci'; Commodity Channel Index; Default period = 20
- 'aroon'; Aroon; Default period = 14

### Other Functions
**merge(left, right)**<br />
Combine two dataframes<br />

**compile(stock)** Incomplete<br />
Combine all data we want on the stock 
and save it as stockname.csv

**create_df(stock_names, stocks_data)**<br />
Adds stock name as a prefix to all columns in each stock dataframe 
and combines dataframes together on date. 
