# %load q06_stationarity/build.py
import pandas as pd
import numpy as np
import sys, os
from statsmodels.tsa.stattools import adfuller


path = 'data/bitcoin.csv'


def q06_stationarity(path):
    df = pd.read_csv(path, index_col=1)

    df.drop(df.columns[0], axis=1 ,inplace=True)
    df.rename(columns={'Close**':'Close'}, inplace=True)
    result = adfuller(df.Close)
    
    return (result[0],result[1])

q06_stationarity(path)
df = pd.read_csv(path, index_col=1)

df.drop(df.columns[0], axis=1 ,inplace=True)
df.rename(columns={'Close**':'Close'}, inplace=True)

result = adfuller(df.Close)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
result

