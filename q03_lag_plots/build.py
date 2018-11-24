# %load q03_lag_plots/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')

path = './data/bitcoin.csv'

def q03_lag_plots(path,n_lags):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    lag_plot(df,lag=n_lags)
    plt.show()

# q03_lag_plots(path,4)



