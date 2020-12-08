# MLStocks

## Data Collection
#### Compile.py
For compiling daily data

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

**merge(left, right)**<br />
Combine two dataframes<br />

**compile(stock)**<br />
Create a CSV file for all stock in the list

**combine_df(stock_names, stocks_data)**<br />
Merge dataframe of different stocks together to
Com.csv

## Data We Used

#### Aapl.csv, Amzn.csv, Fb.csv, Googl.csv, Msft.csv
Contains all technical indicators and prices we are intersted in compiled using compile.py from Alpha Vantage.

#### Com.csv
CSV that contains all of the data from all of the stocks we are looking at

## Machine Learning
#### LSTM_rnn.py
Predict stock using LSTM RNN.

#### gru.py
Predict stock using GRU RNN.

## RNN scripts
#### (LSTM/GRU_rnn.py) Functions:
**to_dataframe(csv)
  #returns dataframe 
  
**reverse_order(df)**<br />
  #returns df reveresed order

**remove_dates(df)**<br />
  #returns dataframe with dates removed and saves dates in a dictionary
  
**split_data(df, date_value)**<br />
  #returns two dataframes 1. before and 2. after date value 
 
**create_xy(date,scope, target_column)**<br />
  #returns x matrixes with data from within the scope of days we consider.
  ex. scope = 5 returns x in batches of 5 days and 
  target_column sets the y variable collected (which comes from day 6)
  
### Rnn Class
**__init__(self,rows_size,columns_size)**<br />
creates the RNN object 

**structure(self, layers, units_for_layers, dropouts_for_layers):**<br />
creates structure for the RNN object

**summary(self):**<br />
returns model summary showing the structure

**train(self, xTrain, yTrain, epochs, batch_size, optimizer, ada_low_lr=None, ada_high_lr=None)**<br />
train the model by feeding it data, epochs, batch_size, and choose optimizer
if optimizer is ada_boost then ada_low_lr/high_lr are needed otherwise you can use common
optimizers like 'adam' or 'relu'

**predict(self, input_data)**<br />
return predictions

**compile(stock)**<br />
Create a CSV file for all stock in the list

**combine_df(stock_names, stocks_data)**<br />
Merge dataframe of different stocks together to
Com.csv

## Our Results

#### rnn_GRU_MSFT data folder
Folder contains our result for predicting MSFT stock prices under different hyperparameters using GRU and MSFT data only.

#### rnn_GRU_MSFT_Combined data folder
Folder contains our result for predicting MSFT stock prices under different hyperparameters using GRU and combined data (with 4 other tech stocks).

#### rnn_LSTM MSFT_combined data folder
Folder contains our result for predicting MSFT stock prices under different hyperparameters using LSTM and combined data (with 4 other tech stocks).

#### rnn_LSTM_MSFT data folder
Folder contains our result for predicting MSFT stock prices under different hyperparameters using LSTM and MSFT data only.

