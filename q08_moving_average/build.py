# %load q08_moving_average/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg') 


path = './data/bitcoin.csv'

def q08_moving_average(path): 
    df = pd.read_csv(path, index_col=1)

    df.drop(df.columns[0], axis=1 ,inplace=True)
    df.rename(columns={'Close**':'Close'}, inplace=True)

    df['20d'] = df.rolling(window=20).mean()['Close']
    df['100d'] = df.rolling(window=100).mean()['Close']
    
    df[['Close','20d','100d']].plot()

    return df

#q08_moving_average(path)

df = pd.read_csv(path, index_col=1)

df.drop(df.columns[0], axis=1 ,inplace=True)
df.rename(columns={'Close**':'Close'}, inplace=True)


df['20d'] = df.rolling(window=20).mean()['Close']
df['100d'] = df.rolling(window=100).mean()['Close']
#df[['Close','20d','100d']].plot()
#plt.show()

