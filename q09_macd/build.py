# %load q09_macd/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')
path = './data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)

def q09_macd(path):
    df['12ema'] = df['Close**'].ewm(span=12,min_periods=0,adjust=False,ignore_na=False).mean()
    df['26ema'] = df['Close**'].ewm(span=26,min_periods=0,adjust=False,ignore_na=False).mean()
    df['signal'] = df['Close**'].ewm(span=9,min_periods=0,adjust=False,ignore_na=False).mean()
    df['macd'] = df['12ema'] - df['26ema']
    df.plot(['Close**','macd','signal'])
    return df



