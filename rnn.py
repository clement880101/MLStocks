import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from keras_adabound import AdaBound
from matplotlib import pyplot as plt


# helper functions
def to_dataframe(csv):
    # returns dataframe
    df = pd.read_csv(csv, date_parser=True)
    return df


def reverse_order(df):
    # reverse order of data so earliest day is day 0
    reversed_df = df[::-1].reset_index(drop=True)
    return reversed_df


def remove_dates(df):
    # stores dates in a dictionary
    dates = {}
    for i in range(test_df.shape[0]):
        date = test_df.iloc[i]['date']
        dates[date] = i

    df = df.drop(['date'], axis=1)

    return dates, df


def scale_data(df):
    # scale data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)

    # save this value to convert stock prediction to nominal data
    upscale_value = 1 / scaler.scale_[0]
    return scaled_data, scaler, upscale_value


def split_data(df, date_value):
    df_before = df[df['date'] < date_value].copy()
    df_after = df[df['date'] >= date_value].copy()
    return df_before, df_after


def create_xy(data, scope):
    x = []
    y = []
    for i in range(scope, data.shape[0]):
        # the xTest will have an array of the last x "scope" days of data
        # yTest will be the the opening value of the next day
        x.append(data[i - scope:i])
        y.append(data[i, 0])

    # the length of x is the data length - scope
    # in each x there is a batch size of x "scope" points
    return np.array(x), np.array(y)


# recurrent neural network

class Rnn:
    # set values for Rnn object
    def __init__(self, optimizer, rows_size, columns_size, low_bound=None, high_bound=None):
        self.low_bound = 0
        self.high_bound = 0
        self.optimizer = optimizer
        self.rows_size = rows_size
        self.columns_size = columns_size
        if optimizer == 'adabound':
            self.low_bound = low_bound
            self.high_bound = high_bound
        self.model = None

    # train function for Rnn class
    def create(self, layers, units_for_layers, dropouts_for_layers):
        # initilize Sequential rnn
        self.model = Sequential()
        # add first layer and define input shape
        self.model.add(
            LSTM(units_for_layers[0], activation='relu', return_sequences=True, input_shape=(self.rows, self.columns)))
        self.model.add(Dropout(dropouts_for_layers[0]))
        # for adding additional layers
        if layers > 2:
            for i in range(1, layers - 1):
                return_setting = True
                if i == layers - 2: return_setting = False
                self.model.add(LSTM(units_for_layers[i], activation='relu', return_sequences=return_setting))
                self.model.add(Dropout(dropouts_for_layers[i]))

        # final endpoint for rnn layers
        self.model.add(Dense(units=1))
        return None

    def summary(self):
        return self.model.summary()

    def train(self, xTrain, yTrain, epochs, batch_size, optimizer, ada_low_lr=None, ada_high_lr=None):
        # compiles model that was created
        if optimizer != 'adaboost':
            self.model.compile(optimizer=optimizer, loss='mean_squared_error')
        else:
            self.model.compile(optimizer=AdaBound(lr=ada_low_lr, final_lr=ada_high_lr), loss='mean_squared_error')
        # fit model to data
        self.model.fit(xTrain, yTrain, epochs=epochs, batch_size=batch_size)

    def predict(self, input_data):
        y_hat = self.model.predict(input_data)
        return y_hat


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset",
                        help="filename for dataset")
    parser.add_argument("target_stock_indicator",
                        help="stock indicator that will be used to find label column: 'stock_open'")
    csv = parser[0]
    target_stock = parser[1]  # for now first stock should be the target

    # arrange df and split by date
    df = reverse_order(csv)
    training_data, test_data = split_data(df, '2020-01-01')

    # store date labels and drop columns
    dates_train, training_data = remove_dates(training_data)
    dates_test, test_data = remove_dates(test_data)

    # scale_data on training data and get scaler with value
    training_data, scaler, upscale_value = scale_data(training_data)
    test_data = scaler.transform(test_data)

    # create xTrain,yTrain.. and xTest,yTest
    # each x in xTrain will be an array of x days
    xTrain, yTrain = create_xy(training_data, 60)
    xTest, yTest = create_xy(test_data, 60)

    # create training and test sets

    row_size, column_size = xTrain.shape[1], xTrain.shape[2]
    network = Rnn('adaboost', row_size, column_size, 1e-3, 0.01)

    units = [40, 60, 80]
    dropouts = [0.2, 0.4, 0.5]
    network.structure(layers=4, units_for_layers=units, dropout_values=dropouts)
    print(network.summary())


if __name__ == "__main__":
    main()
