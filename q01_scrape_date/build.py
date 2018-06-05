import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401"

def q01_scrape_date(url):
    #Scrape the given url using pandas.read_html().
    #You will get a list of which you need to extract
    #the first element to get a dataframe. Store it in a dataframe
    elementlst = pd.read_html(url)
    data = elementlst[0]

    #Change the Date column to datetime format using pandas.to_datetime()
    data['Date']  = pd.to_datetime(  data['Date'] )

    #Sort the Date column in ascending order
    data.sort_values (by='Date', ascending=True, inplace=True)

    #Save the processed dataframe to a csv file, the location to store the file should be ./data/bitcoin.csv
    data.to_csv('./data/bitcoin.csv')

    return data

print (q01_scrape_date(url)[0:3])
