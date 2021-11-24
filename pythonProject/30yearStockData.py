import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred

#connecting to an online API
fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
freddata = fred.get_series('BOGZ1FL073164003Q')

print(freddata.head(5))
print(freddata.describe())

#importing csv using date column as index and sort 
nasdaq = pd.read_csv('Nasdaq.csv', parse_dates=['Date'], index_col='Date')
sp500 = pd.read_csv('SP500.csv', parse_dates=['Date'], index_col='Date')
dowjones = pd.read_csv('DowJones.csv', parse_dates=['Date'], index_col='Date')

print(nasdaq.head(5))
print(sp500.head(5))
print(dowjones.head(5))

nasdaq.info()
sp500.info()
dowjones.info()


