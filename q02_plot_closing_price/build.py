# %load q02_plot_closing_price/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.model_selection import train_test_split
plt.switch_backend('agg')

def q02_plot_closing_price(path):
    data.plot(  x='Date', y='Close**' )
    return
    


path = './data/bitcoin.csv'
data = pd.read_csv(path, index_col=0)


#data.cumsum()
data.plot(  x='Date', y='Close**' )
plt.figure();
plt.show()
plt.show()
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts.plot()
plt.show()

