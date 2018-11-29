# %load q05_log_returns/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')
path = './data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df['Date'] = pd.to_datetime(df['Date'])
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)
def q05_log_returns(path):
    df['Close**'] = np.log(df['Close**'])
    df.plot(['Close**'])
    plt.show()
    return df
    




