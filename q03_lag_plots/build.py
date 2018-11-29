# %load q03_lag_plots/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
from pandas.plotting import lag_plot
plt.switch_backend('agg')
path= './data/bitcoin.csv'
path = './data/bitcoin.csv'
df=pd.read_csv(path,sep='\t')
df['Date'] = pd.to_datetime(df['Date'])
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)
def q03_lag_plots(path, n_lags=4):
    lag_plot(df,lag=4)
    plt.show()

c=q03_lag_plots(path,n_lags=4)
c



