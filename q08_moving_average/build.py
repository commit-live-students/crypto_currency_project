# %load q08_moving_average/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')
path = './data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)


def q08_moving_average(path):
    df['20d'] = pd.rolling_mean(df['Close**'],window=1)
    df['100d'] = pd.rolling_mean(df['Close**'],window = 1)
    df.plot(['Close**','20d','100d'])
    plt.show()
    return df


c = q08_moving_average(path)

c


