# %load q06_stationarity/build.py
import warnings
import pandas as pd
import numpy as np
import sys, os
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import sys, os

path = 'data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)

def q06_stationarity(path):
    res = adfuller(df['Close**'])
    stat = res[0]
    p_value = res[1]
    return stat,p_value
c = q06_stationarity(path)



