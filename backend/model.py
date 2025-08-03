from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf
import pandas as pd
import datetime as dateTime
import numpy as np

"""
Method for getting stcok data from the yfinance library.
"""
def getStockData(ticker : str, period):

    dataFrame = yf.download(ticker, period = period)
    dataFrame = dataFrame[["Close"]].reset_index()

    dataFrame["Date"] = pd.to_datetime(dataFrame.index)
    dataFrame["Date_Ordinal"] = dataFrame["Date"].map(dateTime.datetime.toordinal)

    print(dataFrame)
    return dataFrame
    

getStockData("AAPL", "1y")