import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data
from fredapi import Fred

fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')

LTGBdata = fred.get_series('IRLTLT01IEM156N')

print(LTGBdata.head())
print (LTGBdata.describe())

