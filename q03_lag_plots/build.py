# %load q03_lag_plots/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split

path = './data/bitcoin.csv'

def q03_lag_plots(path, n_lags):
    data = pd.read_csv(path)
    data.set_index('Date', inplace=True)
    pd.plotting.lag_plot(lag= n_lags, series=data['Close**'] )
    return
    



ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
Data = pd.read_csv(path)
Data.set_index('Date', inplace=True)
n_lags =10
pd.plotting.lag_plot(lag= n_lags, series=Data['Close**'] )
plt.show()

