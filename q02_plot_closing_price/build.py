# %load q02_plot_closing_price/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os
plt.switch_backend('agg')

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.model_selection import train_test_split


def q02_plot_closing_price(path):
    df = pd.read_csv(path,index_col=['Date']).iloc[:,1:]
    plt.plot(df['Close**'])

path = './data/bitcoin.csv'
q02_plot_closing_price(path)

