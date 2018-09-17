# %load q04_autocorrelation_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')

path_1 = './data/bitcoin.csv'

def q04_autocorrelation_plot(path):
    
    # Read the datasets
    df = pd.read_csv(path)
    
    # Assign the 'Date' columns as index
    df.index = df['Date']
    df = df.drop('Date', 1)
    
    # plot the correlation. 
    pd.plotting.autocorrelation_plot(df)
    plt.show()
    #return df
    

q04_autocorrelation_plot(path= path_1)


