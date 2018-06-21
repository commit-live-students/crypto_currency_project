import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401"

def q01_scrape_date(url):
    df = pd.read_html(url)[0]
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date',inplace=True)
    df.set_index('Date',inplace=True)
    df.to_csv("./data/bitcoin.csv")
    df['Date'] = df.index
    return df

#q01_scrape_date(url)
