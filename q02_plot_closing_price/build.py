# %load q02_plot_closing_price/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os
plt.switch_backend('agg')

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.model_selection import train_test_split

path = './data/bitcoin.csv'

def q02_plot_closing_price(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    plt.plot(df.index, df['Close**'])
    plt.show()
    
q02_plot_closing_price(path)




