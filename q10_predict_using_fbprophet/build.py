import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from fbprophet import Prophet

def q10_predict_using_fbprophet(path):
    df = pd.read_csv(path)
    df_p = pd.DataFrame()
    df_p['ds'] = df['Date']
    df_p['y'] = df['Close']
    m = Prophet(daily_seasonality=False)
    m.fit(df_p)
    future = m.make_future_dataframe(periods=7)
    forecast = m.predict(future)
    return forecast['yhat']
    
