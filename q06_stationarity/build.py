# %load q06_stationarity/build.py
import pandas as pd
import numpy as np
import sys, os
from statsmodels.tsa.stattools import adfuller

path = 'data/bitcoin.csv'

def q06_stationarity(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    ans = adfuller(df['Close**'])
    test_stat = ans[0]
    p_value = ans[1]
    return test_stat,p_value

# q06_stationarity(path)


