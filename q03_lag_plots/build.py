# %load q03_lag_plots/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.switch_backend('agg')

from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split

path_1 = './data/bitcoin.csv'
n_lags_1 = 4

def q03_lag_plots(path, n_lags):
    
    # read the Datasets
    df = pd.read_csv(path)
    
    # Set the date column as index
    df.index = df['Date']
    df = df.drop('Date', 1)
    
    # plot the dataset to check whether it shows some patter or not.
    pd.plotting.lag_plot(df.index, lag=n_lags)
    plt.show()
    #return df



q03_lag_plots(path_1, n_lags = n_lags_1)


