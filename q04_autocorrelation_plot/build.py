import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from pandas.plotting import lag_plot, autocorrelation_plot
from sklearn.model_selection import train_test_split

path = "./data/bitcoin.csv"
def q04_autocorrelation_plot(path):
    df = pd.read_csv(path)
    df.set_index('Date',inplace=True)
    autocorrelation_plot(df['Close**'])
    plt.show()
    #print(df)

#q04_autocorrelation_plot(path)
