# %load q04_autocorrelation_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split


def q04_autocorrelation_plot(path):
    data = pd.read_csv(path, index_col=0)
    data.set_index('Date', inplace=True)
    pd.plotting.autocorrelation_plot( series=data['Close**'] )
    return

    



path = './data/bitcoin.csv'
data = pd.read_csv(path, index_col=0)
data.set_index('Date', inplace=True)
pd.plotting.autocorrelation_plot( series=data['Close**'] )
plt.show()

