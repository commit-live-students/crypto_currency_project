# %load q09_macd/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.switch_backend('agg')


path = 'data/bitcoin.csv'

def q09_macd(path):
    
    df = pd.read_csv(path)
    df = df.drop(['Unnamed: 0'],1)
    df.set_index('Date',inplace=True)
    df['12ema'] = round(df['Close**'].ewm(span=12,adjust=False).mean(),0)
    df['26ema'] = round(df['Close**'].ewm(span=26,adjust=False).mean(),0)
    df['signal'] = round(df['Close**'].ewm(span=9,adjust=False).mean(),0)
    df['macd'] = df['12ema'] - df['26ema']
    plt.plot(df['Close**'])
    plt.plot(df['macd'])
    plt.plot(df['signal'])
    plt.show()
    return df

# df = q09_macd(path)


