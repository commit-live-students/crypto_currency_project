# %load q01_scrape_date/build.py
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401'

def q01_scrape_date(web):
    # Reading the html web link using pd.read_html()
    df = pd.read_html(web)
    
    # Extracting the web link to DataFrame
    df = pd.DataFrame(df[0])
    
    # Setting the Date columns if Dataframe using pd.to_Dateime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sorting the df value on the bases of 'Date' as ascending order.
    df = df.sort_values(by = 'Date', ascending=True)
    
    # saving the DataFrame to using the to_csv()
    df.to_csv('./data/bitcoin.csv')
    #df['']
    return (df)




    

q01_scrape_date(url)


