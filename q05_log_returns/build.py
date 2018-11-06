# %load q05_log_returns/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg') 
from sklearn.model_selection import train_test_split


def q05_log_returns(path):
    path = './data/bitcoin.csv'
    df = pd.read_csv(path, index_col=1)

    df.drop(df.columns[0], axis=1 ,inplace=True)
    df.drop(df.index[0],axis=0,inplace=True)
    df.rename(columns={'Close**':'Close'}, inplace=True)
    df['Close'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
    df.Close.plot()
    return df
    


path = './data/bitcoin.csv'
df = pd.read_csv(path, index_col=1)

#data.set_index('Date', inplace=True)
#pd.plotting.autocorrelation_plot( series=data['Close**'] )
df.drop(df.columns[0], axis=1 ,inplace=True)
df.drop(df.index[0],axis=0,inplace=True)
df.rename(columns={'Close**':'Close'}, inplace=True)
df['Close'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
df.Close.plot()
plt.show()


