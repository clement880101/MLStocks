import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from keras_adabound import AdaBound
from matplotlib import pyplot as plt

upscale_value = 0

def scale_data(df):
    # scale data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)

    # save this value to convert stock prediction to nominal data
    upscale_value = scaler.scale_[0]
    return scaled_data, upscale_value


def reverse_order(df):
    # reverse order of data so earliest day is day 0
    reversed_df = df[::-1].reset_index(drop=True)
    return reversed_df


def to_dataframe(csv):
    # returns dataframe
    df = pd.read_csv(csv, date_parser=True)
    return df

def split_data():


class Rnn:
    # set values for Rnn object
    def __init__(self, data, scope):
        self.data = data
        self.scope = scope
        self.upscale_value = 0

    def make_batches(self):


    # train function for Rnn class
    def train(self, units_selected_array, dropouts_selected_array, lr_low, lr_high):
        model = Sequential()
            for i in range(len(units_selected_array) - 1):
                model.add(LSTM(units = units_selected_array[i], activation = self.optimizer,))



    def predict(self, ):








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
    target_stock = parser[1]

    data = scale_data(to_dataframe(csv))
    scale


if __name__ == "__main__":
    main()
