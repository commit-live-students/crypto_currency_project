# %load q07_make_stationary/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
path = './data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df['Date'] = pd.to_datetime(df['Date'])
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)

plt.switch_backend('agg')

def q07_make_stationary(path):
    df['lClose'] = np.log(df['Close**'])
    moving_avg = pd.rolling_mean(df['lClose'],window=12)
    df['sClose']= df['lClose'] - moving_avg
    return df
    
    



