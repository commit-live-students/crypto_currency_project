# %load q04_autocorrelation_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')

path = './data/bitcoin.csv'

def q04_autocorrelation_plot(path):
    
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    autocorrelation_plot(df['Close**'])
    plt.show()

# q04_autocorrelation_plot(path)


