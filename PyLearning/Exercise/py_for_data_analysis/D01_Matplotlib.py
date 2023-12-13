from email import header
import numpy as np
import pandas as pd
from pandas import Series, DataFrame, Index, MultiIndex, PeriodIndex, HDFStore
import warnings, requests
import csv, json, lxml
from datetime import datetime
import matplotlib.pyplot as plt

from X02_mod_get_url import get_url

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.
pd.options.display.max_rows = 10 # Display no more than 10 rows.




##### MATPLOTLIB #####

# Example 1.1
data = np.arange(10)
plt.plot(data) # Simply plot, index start from 0.
plt.show()

# Example 1.2
fig = plt.figure() # Create a blank figure object.
ax1 = fig.add_subplot(2, 2, 1) # Create subplots.
ax2 = fig.add_subplot(2, 2, 2) # (2,2) represents the subplot grids.
ax3 = fig.add_subplot(2, 2, 3) # 1 or 2 or 3 choose the index of subplot.
plt.show()