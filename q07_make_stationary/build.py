# %load q07_make_stationary/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

path = 'data/bitcoin.csv'

def q07_make_stationary(path):
    df = pd.read_csv(path, index_col=1)

    df.drop(df.columns[0], axis=1 ,inplace=True)
    df.rename(columns={'Close**':'Close'}, inplace=True)
    df['lClose'] = np.log(df.Close)
    moving_avg = pd.rolling_mean(df.lClose, window=12)
    df['sClose'] = df.lClose-moving_avg
    return df

q07_make_stationary(path)

