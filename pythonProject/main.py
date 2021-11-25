import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fredapi import Fred
from matplotlib import style

# connecting to an online API
fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
freddata = fred.get_series('BOGZ1FL073164003Q')
freddataDF = fred.get_series_all_releases('BOGZ1FL073164003Q')

freddata = freddata.dropna(inplace=True)

print("Below is the Head and Description of the FRED data pulled from an API:")
print(freddataDF.head(5))
print(freddataDF.describe(datetime_is_numeric=True))
print("\n\n\n")


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

print("Below is the head data pulled from 3 different CSV's representing NASDAQ, SP500 and DOWJONES:")
print(nasdaq.head(5))
print(sp500.head(5))
print(dowjones.head(5))
print("\n\n\n")


print("Below is the info pulled from the 3 CSV's:")
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

nas_sp_dow = nas_sp.merge(dowjones,
                          on='Date',
                          how='inner').dropna()

# renaming columns
nas_sp_dow = nas_sp_dow.rename(columns={'Value_nasdaq': 'Nasdaq_Val',
                                        'Value_sp500': 'SP500_Val',
                                        'Value': 'DowJones_Val'})

nas_sp_dow = nas_sp_dow.asfreq(freq='Y',
                             method='ffill')

#initial plotting of values
nas_sp_dow.plot(kind= 'box', title = 'Initial Comparison')
plt.show()

# normalising chart
norm_nas_sp_dow = nas_sp_dow.div(nas_sp_dow.iloc[0]).mul(100)

norm_nas_sp_dow.plot(kind='line', style='--',
                     title='Normalized Stock Value')
plt.show()

# Adding Total Column
nas_sp_dow['Total'] = nas_sp_dow.apply(np.sum, axis=1)

nas_sp_dow.plot(kind='line')
plt.show()

nas_sp_dow = nas_sp_dow.drop(columns='Total')

for column in nas_sp_dow:
    sns.distplot(nas_sp_dow[column],
                 hist=True,
                 kde= True,
                 label=column,
                 rug=True)

    plt.show()


