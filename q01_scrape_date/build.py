# %load q01_scrape_date/build.py
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401'

def q01_scrape_date(url):
    df_source = pd.read_html(url)
    df = pd.DataFrame(df_source[0])
    df['Date'] = pd.to_datetime(df.Date)
    df = df.sort_values(by='Date')
    df.to_csv('./data/bitcoin.csv')
    return df


