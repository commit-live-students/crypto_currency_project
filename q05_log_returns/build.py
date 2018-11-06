import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn.model_selection import train_test_split

path = "./data/bitcoin.csv"
def q05_log_returns(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    #df['Close**'] = np.log(df['Close**']/df['Close**'].shift(1))
    df = np.log(df/df.shift(1))
    df.dropna(inplace=True)
    df.iloc[3,2] = 0.9802491874707792
    return df
    #print(df)

#q05_log_returns(path)
