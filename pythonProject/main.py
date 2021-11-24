import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred

# connecting to an online API
fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
freddata = fred.get_series('BOGZ1FL073164003Q')

freddata.dropna(inplace=True)

print(freddata.head(5))
print(freddata.describe())


# importing csv using date column as index and sort
nasdaq = pd.read_csv('Nasdaq.csv',
                     parse_dates=['Date'],
                     index_col='Date',
                     na_values='n/a')

sp500 = pd.read_csv('SP500.csv',
                    parse_dates=['Date'],
                    index_col='Date',
                    na_values='n/a')

dowjones = pd.read_csv('DowJones.csv',
                       parse_dates=['Date'],
                       index_col='Date',
                       na_values='n/a')

print(nasdaq.head(5))
print(sp500.head(5))
print(dowjones.head(5))

nasdaq.info()
sp500.info()
dowjones.info()

# checking for empty info
nasdaq_empty = nasdaq.isnull().sum()
sp500_empty = sp500.isnull().sum()
dowjones_empty = dowjones.isnull().sum()
print([nasdaq_empty, sp500_empty, dowjones_empty])

# Using merge instead of concat to utilize Dict knowledge
nas_sp = nasdaq.merge(sp500,
                      on='Date',
                      how='inner',
                      suffixes=('_nasdaq', '_sp500')).dropna()

nas_sp_dow = nas_sp.merge(dowjones, on='Date',
                          how='inner').dropna()

# renaming columns
nas_sp_dow = nas_sp_dow.rename(columns={'Value_nasdaq': 'Nasdaq_Val',
                                        'Value_sp500': 'SP500_Val',
                                        'Value': 'DowJones_Val'})
for index, row in nas_sp_dow.iterrows():
    print(row['Nasdaq_Val'], row['SP500_Val'], row['DowJones_Val'])

# normalising chart
norm_nas_sp_dow = nas_sp_dow.div(nas_sp_dow.iloc[0]).mul(100)

norm_nas_sp_dow.plot(kind= 'line',
                     title='Normalized Stock Value')
plt.show()

# Adding Total Column
nas_sp_dow['Total'] = nas_sp_dow.apply(np.sum, axis=1)

nas_sp_dow.plot(kind='line')
plt.show()

yr_index_f = nas_sp_dow.asfreq(freq='Y',
                             method= 'ffill')
mt_index_f = nas_sp_dow.asfreq(freq='M',
                             method='ffill')
yr_index_b = nas_sp_dow.asfreq(freq='Y',
                             method='bfill')
mt_index_b = nas_sp_dow.asfreq(freq='M',
                             method='bfill')

print([mt_index_f, yr_index_f, mt_index_b, yr_index_b])
print(nas_sp_dow.head())


mt_index_f.plot(kind='line', title='FwdFill Index Value by month')
plt.show()

yr_index_f.plot(kind='line', title='FwdFill Index Value by year')
plt.show()

mt_index_b.plot(kind='line', title='BwdFill Index Value by month')
plt.show()

yr_index_b.plot(kind='line', title='BwdFill Index Value by year')
plt.show()

#for value in nas_sp_dow['Nasdaq Val']:
    #(nas_sp_dow['Nasdaq Val']*100 / nas_sp_dow["Total"])

nas_mean = nas_sp_dow.groupby(by='Date').mean()
print(nas_mean)

nas_sp_dow["shifted_nas1"] = nas_sp_dow['Nasdaq_Val'].shift(1)
nas_sp_dow["shifted_SP1"] = nas_sp_dow['SP500_Val'].shift(1)
nas_sp_dow["shifted_Dow1"] = nas_sp_dow['DowJones_Val'].shift(1)

nas_sp_dow['Nas % Change'] = nas_sp_dow['Nasdaq_Val'].div(nas_sp_dow["shifted_nas1"]).sub(1).mul(100)
nas_sp_dow['SP500 % Change'] = nas_sp_dow['SP500_Val'].div(nas_sp_dow["shifted_SP1"]).sub(1).mul(100)
nas_sp_dow['Dowjones % Change'] = nas_sp_dow['DowJones_Val'].div(nas_sp_dow["shifted_Dow1"]).sub(1).mul(100)

print(nas_sp_dow)
# saving to csv
nas_sp_dow.to_csv('Stocks combined.csv')

nas_sp_dow[['Nas % Change', 'SP500 % Change', 'Dowjones % Change']].plot(kind=line)
plt.show()