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




##### HIERARCHICAL INDEXING #####
print("############### HIERARCHICAL INDEXING ###############")

# Multi indexes.
data = Series(np.random.randn(9), index=[['a','a','a','b','b','c','c','d','d'],
                                         [1, 2, 3, 1, 3, 1, 2, 2, 3]])

print("\n\n1.1 Multiple indexes of Series",
      "\n-- Original:", data,
      "\n-- .index property: (data.index)", data.index,
      "\n-- data[['b', 'c']] =", data[['b', 'c']],
      "\n-- data['b':'c'] =", data['b':'c'],
      "\n-- data.loc[['b', 'c']] =", data.loc[['b', 'c']],
      "\n-- data.loc[:, 2] = (inner level loc)", data.loc[:, 2],
      sep='\n')

# We can stack and unstack the multi-indexed Series.
print("\n\n1.2 Stack & Unstack",
      "\n-- Original:", data,
      "\n-- data.unstack() =", data.unstack(),
      "\n-- data.unstack().stack() =", data.unstack().stack(),
      sep='\n')

# For DataFrames.
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])

print("\n\n1.3 For DataFrames",
      "\n-- Original:", frame, sep='\n')

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

print("\n-- Change index and columns names:", frame,
      "\n-- frame.Ohio =", frame.Ohio, sep='\n')

# Create reusable MultiIndex object.
indexes = MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'],
                                  ['Green', 'Red', 'Green']],
                                 names=['state', 'color'])

# Reordering and Sorting.
print("\n\n1.4 Reordering and Sorting",
      "\n-- frame.sort_index(level=0)", frame.sort_index(level=0),
      "\n-- frame.sort_index(level=1)", frame.sort_index(level=1),
      "\n-- frame.swaplevel('key1', 'key2')",
      frame.swaplevel('key1', 'key2'),
      "\n-- frame.swaplevel(0, 1).sort_index(level=0)",
      frame.swaplevel(0, 1).sort_index(level=0),
      sep='\n')

# Summary Statistics by Level.
# Specify the level of data you want to aggregate.
print("\n\n1.5 Summary Statistics by Level",
      "\n-- Sum by level='key2'",
      frame.sum(level='key2'),
      "\n-- Sum by level='color' in axis='columns'",
      frame.sum(level='color', axis='columns'),
      sep='\n')

# Indexing with a DaataFrame's columns.
# Use 1 or more columns from a DataFrame as the row index of a new DataFrame.
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two',
                         'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
frame2 = frame.set_index(['c', 'd'])

print("\n\n1.6 Indexing a DataFrame Using indexes of another DataFrame",
      "\n-- Original:", frame,
      "\n-- Use 'c' and 'd' (set_index):", frame2,
      "\n-- Set but without drop column 'c' and 'd':",
      frame.set_index(['c', 'd'], drop=False),
      "\n-- Use reset_index to move all indexes to columns:",
      frame2.reset_index(),
      sep='\n')





##### COMBINING & MERGING #####
print("############### COMBINING & MERGING ###############",
      "Three basic methods:",
      "1. pandas.merge()",
      "2. pandas.concat()",
      "3. DataFrame.combine_first()", sep='\n')

### Database-Style DataFrame Joins (similar to SQL)
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

print("\n2.1.1 Database-Style DataFrame Joins",
      "\n-- Original:", "- df1:", df1, "- df2:", df2,
      "\n-- pd.merge(df1, df2) = (Merge by keys in both tables as default)",
      pd.merge(df1, df2),
      "\n-- pd.merge(df1, df2, how='outer') = (Merge by all keys)",
      pd.merge(df1, df2, how='outer'),
      sep='\n')

# For DataFrames with different keys.
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print("\n2.1.2 For DataFrames with different keys",
      "\n-- Original:", "- df3:", df3, "- df4:", df4,
      "\n-- Pass left_on and right_on arguments separately:",
      pd.merge(df3, df4, left_on='lkey', right_on='rkey'),
      sep='\n')

# Many-to-many Merges.
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
print("\n2.1.3 Many-to-many Merges",
      "\n-- Original:", "- df1:", df1, "- df2:", df2,
      "\n-- Pass on='key' give the Cartesian product of the rows:",
      pd.merge(df1, df2, on='key'),
      "\n-- Pass how='inner' creates same effect as above:",
      pd.merge(df1, df2, how='inner'),
      sep='\n')

# Merge Multiple keys.
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})

print("\n2.1.4 Merge Multiple keys",
      "\n-- Original:", "- left:", left, "- right:", right,
      "\n-- Pass on=['key1', 'key2'], how=outer:",
      pd.merge(left, right, on=['key1', 'key2'], how='outer'),
      "\n-- Only pass on='key1'",
      pd.merge(left, right, on='key1'),
      "\n-- Add suffixes=('_left', '_right')",
      pd.merge(left, right, on='key1', suffixes=('_left', '_right')),
      sep='\n')


### Merging on indexes.

# One is from column, one is from index.
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print("\n\n2.2.1 Merging on indexes",
      "\n-- Original:", "- left1:", left1, "- right1:", right1,
      "\n-- Pass right_index=True to merge as indexes",
      pd.merge(left1, right1, left_on='key', right_index=True),
      "\n-- Add how='outer'",
      pd.merge(left1, right1, left_on='key', right_index=True, how='outer'),
      "\n-- We can also use .join() instance to combine index to column:",
      left1.join(right1, on='key'),
      sep='\n')

# For multi indexes and multi column labels.
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])

print("\n2.2.2 Multi indexes and multi labels",
      "\n-- Original:", "- lefth:", lefth, "- righth:", righth,
      "\n-- Simply pass multi labels and set right_index=True:",
      pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'),
      sep='\n')

# For multi indexes.
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                  index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'],
                   columns=['Missouri', 'Alabama'])
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                   index=['a', 'c', 'e', 'f'],
                   columns=['New York', 'Oregon'])

print("\n* 2.2.3 Multi indexes",
      "\n-- Original:", "- left2:", left2, "- right2:", right2, "- another:", another,

      "\n-- Pass left_index and right_index as True:",
      pd.merge(left2, right2, how='outer', left_index=True, right_index=True),
      "\n-- We can also use .join() instance: (Works only when columns are non-overlapping)",
      left2.join(right2, how='outer'),
      "\n-- Join a list of DataFrames:",
      left2.join([right2, another], how='outer'),
      sep='\n')


### Concatenating Along an Axis.

# Example.
arr = np.arange(12).reshape((3, 4))

print("\n\n2.3.0 Concatenating Along an Axis:",
      "\n-- Original:", arr,
      "\n-- Concatenate horizontally:", np.concatenate([arr, arr], axis=1),
      sep='\n')

# Example2.
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
s4 = pd.concat([s1, s3])
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])

print("\n2.3.1 Concatenating with different indexes",
      "\n-- Original:", "- s1:", s1, "- s2:", s2, "-s3", s3,
      "\n-- pd.concat([list of datas]):", pd.concat([s1, s2, s3]),
      "\n-- Pass extra axis=1:", pd.concat([s1, s2, s3], axis=1),
      "\n-- Join with mutual indexes:", pd.concat([s1, s4], axis=1),
      "\n-- Pass extra join='inner':", pd.concat([s1, s4], axis=1, join='inner'),
      "\n-- Reindexed by custom indexes:", pd.concat([s1, s4], axis=1).reindex(['a', 'c', 'b', 'e']),
      "\n-- Make concatenated pieces identifiable by pass keys=[]", result,
      "\n-- Unstack the result:", result.unstack(),
      "\n-- Combine along axis=1", pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']),
      sep='\n')

# For DataFrames.
df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])

print("\n2.3.2 For DataFrames",
      "\n-- Original:", "- df1:", df1, "- df2:", df2,
      "\n-- axis=1, pass keys:", pd.concat([df1, df2], axis=1, keys=['level1', 'level2']),
      "\n-- Pass key-value pairs as dict:", pd.concat({'level1': df1, 'level2': df2}, axis=1),
      "\n-- The order of column names:",
      pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],  names=['upper', 'lower']),
      sep='\n')

# For row index doesn't contain any relevant data.
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

print("\n2.3.3 Irrelevant row data",
      "\n-- Original:", "- df1:", df1, "- df2:", df2,
      "\n-- Pass ignore_index=True", pd.concat([df1, df2], ignore_index=True),
      "\n-- Index will be combined if we doesn't ignore:", pd.concat([df1, df2]),
      sep='\n')


### Combining data with overlap.
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

print("\n\n2.4.1 Combining data with overlap",
      "\n-- Original:", "- a:", a, "- b:", b,
      "\n-- Assign NULL in a with value in b:", np.where(pd.isnull(a), b, a),
      "\n-- b[:-2].combine_first(a[2:]) =", b[:-2].combine_first(a[2:]),
      sep='\n')


# For DataFrames.
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})

print("\n2.4.2 For DataFrames",
      "\n-- Original:", "- df1:", df1, "- df2:", df2,
      "\n-- df1.combine_first(df2)", df1.combine_first(df2),
      sep='\n')




##### RESHAPING AND PIVOTING #####
print("############### RESHAPING & PIVOTING ###############")

### Reshaping with Hierarchical Indexing.
# 2 basic methods: stack() & unstack()
data = DataFrame(np.arange(6).reshape((2, 3)),
                index=pd.Index(['Ohio', 'Colorado'], name='state'),
                columns=pd.Index(['one', 'two', 'three'],
                                 name='number'))

print("\n3.1.1 Reshaping with hierarchical indexing",
      "\n-- Original:", data,
      "\n-- data.stack() =", data.stack(),
      "\n-- data.stack().unstack() =", data.stack().unstack(),
      "\n-- data.stack().unstack(level='state') =", data.stack().unstack(level='state'),
      sep='\n')

# With missing data.
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])

print("\n3.1.2 With missing data",
      "\n-- Original:", data2,
      "\n-- data2.unstack() =", data2.unstack(),
      "\n-- data2.unstack().stack() =", data2.unstack().stack(),
      "\n-- data2.unstack().stack(dropna=False) =", data2.unstack().stack(dropna=False),
      sep='\n')

# Order of unstack
result = data.stack()
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))

print("\n3.1.3 Order of unstack",
      "\n-- Original:", df,
      "\n-- df.unstack('number') =", df.unstack('number'),
      "\n-- df.unstack('state') =", df.unstack('state'),
      "\n-- df.unstack('state').stack('side') =", df.unstack('state').stack('side'),
      sep='\n')


### Pivoting “Long” to “Wide” Format.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\macrodata.csv"
data = pd.read_csv(path)

print("\n3.2 Pivoting 'long' to 'wide' format",
      "\n-- Original:", data.head(), sep='\n')

periods = PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'e')
ldata = data.stack().reset_index().rename(columns={0: 'value'})

pivoted = ldata.pivot('date', 'item', 'value')
pivoted2 = ldata.set_index(['date', 'item']).unstack()

print("\n-- Pivoted data:", ldata[:10],
      "\n-- Use DataFrame.pivot() method:", pivoted.head(),
      "\n-- Use DataFrame.set_index().unstack() method:", pivoted2.head(),
      sep='\n')


### Pivoting “Wide” to “Long” Format.
# We suppose 'key' is group indicator, and other columns are data values.
df = DataFrame({'key': ['foo', 'bar', 'baz'],
                'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9]})
melted = pd.melt(df, ['key']) # Specify the group indicator.
reshaped = melted.pivot('key', 'variable', 'value')

print("\n\n3.3 Pivoting 'wide' to 'long' format",
      "\n-- Original:", df,
      "\n-- Melted by indicator 'key':", melted,
      "\n-- Pivoted back:", reshaped,
      "\n-- Or use reshaped.reset_index():", reshaped.reset_index(),
      "\n-- Melt a subset of the column:", pd.melt(df, id_vars=['key'], value_vars=['A', 'B']),
      "\n-- Or throw away 'key' (only choose A, B, C):", pd.melt(df, value_vars=['A', 'B', 'C']),
      "\n-- It can also be regarded as without identifier:", pd.melt(df, value_vars=['key', 'A', 'B']),
      sep='\n')