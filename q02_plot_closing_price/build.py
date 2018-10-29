# %load q02_plot_closing_price/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.switch_backend('agg')
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.model_selection import train_test_split

path_1 = './data/bitcoin.csv'

def q02_plot_closing_price(path):
    
    # readinf the csv file
    df = pd.read_csv(path)
    
    # Set the date as index
    df.index = df['Date']
    df = df.drop('Date', 1)
    
    # Ploting the graph date against price
    df[['Open*', 'High','Low','Close**','Volume','Market Cap']].plot()
    plt.show()
    #return df

q02_plot_closing_price(path_1)


