import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred

fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
freddata = fred.get_series('BOGZ1FL073164003Q')

print(freddata.head(5))
print(freddata.describe())

nasdaq = pd.read_csv('Nasdaq.csv', parse_dates=['Date'], index_col='Date')
sp500 = pd.read_csv('SP500.csv', parse_dates=['Date'], index_col='Date')
Dowjones = pd.read_csv('DowJones.csv', parse_dates=['Date'], index_col='Date')
