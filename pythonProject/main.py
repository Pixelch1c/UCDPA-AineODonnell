import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data
import DateTime
from fredapi import Fred

fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
series = 'BOGZ1FL073164003Q'
start = date(2000, 1, 1)
stkdata = DataReader(series, 'fred', start)

stkdata.info()
