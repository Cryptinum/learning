import pandas as pd
from pandas import Series, DataFrame, Index
import numpy as np
import warnings

import csv
from datetime import datetime

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
# pd.set_option('display.float_format', lambda x: '%.4f' % x) # Round to .4
warnings.filterwarnings("ignore") # Suppress warnings.




# Pandas built-in statistical methods can handle missing data.
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])

print('##### Missing values handling.')
print('\n-- Original:', df,
      '\n-- df.sum() = (see NaN as 0)', df.sum(),
      "\n-- df.sum((axis='columns') = (min_count=0 as default)", df.sum(axis='columns'),
      "\n-- df.mean(axis='columns', skipna=False) =", df.mean(axis='columns', skipna=False),
      "\n-- df.idxmax() =", df.idxmax(),
      "\n-- df.cumsum() = (skip NaN as default)", df.cumsum(),
      sep='\n')

# Summarization of a dataframe.
print('\n\n\n##### Summarization.')
print('\n-- Original', df, '\n-- df.describe()', df.describe(), sep='\n')

obj = Series(['a', 'a', 'b', 'c'] * 4)
print('\n### For non-numeric data.')
print('\n-- Original:', obj, '\n-- obj.describe()', obj.describe(), sep='\n')

'''
    Series和DataFrame的统计methods

    count 非NaN值计数
        Number of non-NA values
    describe 给出统计摘要
        Compute set of summary statistics for Series or each DataFrame column
    min, max 最值
        Compute minimum and maximum values
    argmin, argmax 最值的指标（先出现的优先）
        Compute index locations (integers) at which minimum or maximum value obtained, respectively
    idxmin, idxmax 最值的指标（先出现的优先）（DataFrame专用）
        Compute index labels at which minimum or maximum value obtained, respectively
    quantile 分位数（q=0.5为默认值）（竖着优先）
        Compute sample quantile ranging from 0 to 1
    sum 和
        Sum of values
    mean 均值
        Mean of values
    median 中位数
        Arithmetic median (50% quantile) of values
    mad 平均离差
        Mean absolute deviation from mean value
    prod 积
        Product of all values
    var 样本方差
        Sample variance of values
    std 样本标准差
        Sample standard deviation of values
    skew 样本偏度（三阶标准矩）
        Sample skewness (third moment) of values
    kurt 样本峰度（四阶标准矩）
        Sample kurtosis (fourth moment) of values
    cumsum 累积和
        Cumulative sum of values
    cummin, cummax 累积极值
        Cumulative minimum or maximum of values, respectively
    cumprod 累积积
        Cumulative product of values
    diff 一阶差分（period=1、即相邻做差为默认）
        Compute first arithmetic difference (useful for time series)
    pct_change 计算百分比增减（period=1、即环比为默认）
        Compute percent changes
'''




##### Correlation and Covariance #####
print('\n\n\n\n##### Correlation and Covariance')
from X02_mod_get_url import get_url
tickers = ['AAPL', 'IBM', 'MSFT', 'GOOG']
'''
for ticker in tickers:
    get_url(ticker, '20220101')
'''

# read data.
all_data = {}
for ticker in tickers:
    path = f"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\{ticker}.csv"
    all_data[ticker] = pd.read_csv(path, index_col='Date')
    # Set date as index.
    # all_data[ticker].Date = pd.to_datetime(all_data[ticker].Date)
    # all_data[ticker].set_index('Date', inplace=True)

# construct dataframes.
price = DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

#print(); print(price)
#print(); print(volume)

price_pct = price.pct_change()
print('\nPrice percentage change:')
print(price_pct.tail())

print(f'\nCorrelation of MSFT and IBM:\t{price_pct.MSFT.corr(price_pct.IBM)}')
print(f'\nCovariance of MSFT and IBM:\t{price_pct.MSFT.cov(price_pct.IBM)}')

# Calculate all corr or cov automatically.
print('\nCorrelation matrix:')
print(price_pct.corr())
print('\nCovariance matrix:')
print(price_pct.cov())

# Calculate single stock's corr with others.
print('\nCorrelation matrix of IBM:')
print(price_pct.corrwith(price_pct.IBM))

print('\nCorrelation matrix with volume (Correspond stocks):')
print(price_pct.corrwith(volume))





##### Unique Values, Value Counts, and Membership #####
print('\n\n\n\n##### Unique Values, Value Counts, and Membership')

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print('\n-- Original:', obj,
      '\n-- Unique values:', obj.unique(),
      '\n-- Unique values: (sorted)', sorted(obj.unique()),
      '\n-- Count values: (obj.value_counts())', obj.value_counts(),
      '\n-- pd.value_counts(obj.values, sort=False)', pd.value_counts(obj.values, sort=False),
      "\n-- Specify b and c: (obj.isin(['b', 'c']))", obj.isin(['b', 'c']),
      "\n-- Filter by b and c", obj[obj.isin(['b', 'c'])],
      sep='\n')

to_match = Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = Series(['c', 'b', 'a'])
print('\n\n\n-- Original:', to_match, unique_vals,
      '\n-- Matched indexes:', pd.Index(unique_vals).get_indexer(to_match),
      sep='\n')

data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
print('\n\n\n-- Original:', data,
      '\n-- 统计结果(注意index的不同)：', data.apply(pd.value_counts).fillna(0),
      sep='\n')