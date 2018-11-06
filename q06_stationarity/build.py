import pandas as pd
import numpy as np
import sys, os
from statsmodels.tsa.stattools import adfuller


path = 'data/bitcoin.csv'
def q06_stationarity(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    ans = adfuller(df['Close**'])
    return ans[0],ans[1]

#q06_stationarity(path)
