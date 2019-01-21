# %load q08_moving_average/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')

path = 'data/bitcoin.csv'

def q08_moving_average(path):

    df = pd.read_csv(path)
    df = df.drop(['Unnamed: 0'],1)
    df.set_index('Date',inplace=True)
    df['20d']  = df['Close**'].rolling(window=20).mean()
    df['100d'] = df['Close**'].rolling(window=100).mean()
    plt.plot(df['Close**'])
    plt.plot(df['20d'])
    plt.plot(df['100d'])
    plt.show()
    return df

# df = q08_moving_average(path)



