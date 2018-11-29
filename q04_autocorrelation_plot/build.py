# %load q04_autocorrelation_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
path = './data/bitcoin.csv'
df = pd.read_csv(path,sep='\t')
df=df.set_index('Date')
df = df.drop(['Unnamed: 0'],1)
plt.switch_backend('agg')
def q04_autocorrelation_plot(path):
    autocorrelation_plot(df['Close**'])
    plt.show()

    





