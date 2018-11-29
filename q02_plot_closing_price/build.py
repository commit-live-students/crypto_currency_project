# %load q02_plot_closing_price/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.model_selection import train_test_split
path = './data/bitcoin.csv'
def q02_plot_closing_price(path):
    df = pd.read_csv(path,sep='\t')
    df=df.set_index('Date')
    df = df.drop(['Unnamed: 0'],1)
    df.plot(['Close**'])
c = q02_plot_closing_price(path)



