# %load q09_macd/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg') 

path = './data/bitcoin.csv'

def q09_macd(path):
    df = pd.read_csv(path, index_col=1)
    df.drop(df.columns[0], axis=1 ,inplace=True)
    df.rename(columns={'Close**':'Close'}, inplace=True)

    df['12ema'] = df.Close.ewm(span =12,adjust = False).mean()
    df['26ema'] = df.Close.ewm(span =26, adjust = False).mean()
    df['signal'] = df.Close.ewm(span = 9, adjust = False).mean()
    df['macd'] = df['12ema']- df['26ema']
    
    df[['Close', 'macd','signal']].plot()
    df['signal'] = df['signal'].round(0)    
    return df


df = pd.read_csv(path, index_col=1)
df.drop(df.columns[0], axis=1 ,inplace=True)
df.rename(columns={'Close**':'Close'}, inplace=True)

df['12ema'] = df.Close.ewm(span =12,adjust = False).mean()
df['26ema'] = df.Close.ewm(span =26, adjust = False).mean()
df['signal'] = df.Close.ewm(span = 9, adjust = False).mean()
df['macd'] =  df['12ema']- df['26ema']
df[['Close', 'macd','signal']].plot()
plt.show()
df['signal'] = df['signal'].round(0)
df
df.iloc[:,8]

