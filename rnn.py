from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import theano
from keras.models import Sequential


def scale_data(df):
    # scale data
    scaled_data = MinMaxScaler(df)
    return scaled_data


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("xTrain",
                        help="filename for features of the training data")
    parser.add_argument("yTrain",
                        help="filename for labels associated with training data")


if __name__ == "__main__":
    main()
