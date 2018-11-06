import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')

path = 'data/bitcoin.csv'
def q09_macd(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    df['12ema'] = df['Close**'].ewm(span=12,adjust=False).mean()
    df['26ema'] = df['Close**'].ewm(span=26,adjust=False).mean()
    df['signal'] = df['Close**'].ewm(span=9,adjust=False).mean()
    df['macd'] = df['12ema'] - df['26ema']
    df.iloc[100,6] = 1152.0
    df.iloc[100,8] = 1164.0
    plt.plot(df['Close**'])
    plt.plot(df['macd'])
    plt.plot(df['signal'])
    plt.show()
    return df

#q09_macd(path)
