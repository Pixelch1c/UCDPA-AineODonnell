import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data
import DateTime
from fredapi import Fred

fred = Fred(api_key='52c96fa9db703fe0764c2589b15239d7')
fred.get_series('BOGZ1FL073164003Q')
