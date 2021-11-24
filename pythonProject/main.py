import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred

# connecting to an online API
fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
freddata = fred.get_series('BOGZ1FL073164003Q')

print(freddata.head(5))
print(freddata.describe())

# importing csv using date column as index and sort
nasdaq = pd.read_csv('Nasdaq.csv', parse_dates=['Date'], index_col='Date')
sp500 = pd.read_csv('SP500.csv', parse_dates=['Date'], index_col='Date')
dowjones = pd.read_csv('DowJones.csv', parse_dates=['Date'], index_col='Date')

print(nasdaq.head(5))
print(sp500.head(5))
print(dowjones.head(5))

nasdaq.info()
sp500.info()
dowjones.info()

#checking for empty info
nasdaq_empty = nasdaq.isnull().sum()
sp500_empty = sp500.isnull().sum()
dowjones_empty = dowjones.isnull().sum()

print([nasdaq_empty, sp500_empty, dowjones_empty])

nas_sp = nasdaq.merge(sp500,
                          on='Date',
                          how='inner',
                          suffixes=('_nasdaq', '_sp500')).dropna()
nas_sp_dow = nas_sp.merge(dowjones, on='Date',
                          how='inner').dropna()


nas_sp_dow = nas_sp_dow.rename(columns={'Value_nasdaq': 'Nasdaq Val',
                                        'Value_sp500': 'SP500 Val',
                                        'Value': 'DowJones Val'})



# checking graph of all 3
nas_sp_dow.plot(kind = 'line')
plt.show()

# normalising chart
norm_nas_sp_dow = nas_sp_dow.div(nas_sp_dow.iloc[0]).mul(100)

norm_nas_sp_dow.plot(kind= 'line',
                     title='Normalized Stock Value')
plt.show()

nas_sp_dow['Total'] = nas_sp_dow.apply(np.sum, axis=1)
# checking merge outcome
print(nas_sp_dow)