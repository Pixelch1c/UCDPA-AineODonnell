import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data

from fredapi import Fred
fred=(api_key='52c96fa9db703fe0764c2589b15239d7')
from pandas_datareader.data import DataReader
from datetime import date

freddata = Fred.get_series('')

pd.read_csv()