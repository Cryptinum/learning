import pandas as pd
from pandas import Series, DataFrame, Index
import numpy as np
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
# pd.set_option('display.float_format', lambda x: '%.4f' % x) # Round to .4
warnings.filterwarnings("ignore") # Suppress warnings.




##### Re-indexing #####
print('############### 1. Re-indexing ###############')

# Create new object with the data conformed to a new index.
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e']) # Create new.
print('\n1.1 Re-indexing\n',
      '-- Original:', obj, '\n-- Re-indexed:', obj2, sep='\n')

# Forward dilling.
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')
print('\n1.2 Forward filling\n',
      '-- Original:', obj3, '\n-- Forward filled:', obj4, sep='\n')

# For DataFrame.
frame = DataFrame(np.arange(9).reshape((3, 3)),
                 index=['a', 'c', 'd'],
                 columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print('\n1.3 For DataFrames\n',
      '-- Original:', frame, '\n-- Re-indexed:', frame2, sep='\n')

states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
print('\n1.4 Re-index by column\n',
      '-- States:', states, '\n-- Re-indexed:', frame3, sep='\n')

# Fill missing values.
labels = ['1', '2', '3', '4']
states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(index=labels, columns=states, fill_value=999)
print('\n1.5 Access a part of the frame.',
      '\n-- indexes & Columns:', labels, states,
      '\n-- Filled:', frame3, sep='\n')





##### Dropping Entries from an Axis #####
print('\n\n\n\n############### 2. Dropping Entries ###############')

# Drop an entry.
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop(['d', 'c'])
print('\n2.1 Drop an entry\n',
      '-- Original:', obj, "\n-- obj.drop(['d', 'c']):", new_obj, sep='\n')

# For DataFrame.
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
new_data = data.drop(['Colorado', 'Ohio'])
# Default is axis=0, change to axis=1 or axis='columns' to drop columns.
new_data2 = data.drop('two', axis=1)
new_data3 = data.drop(['two', 'four'], axis='columns')
print('\n2.2 For DataFrame',
      '\n-- Original:', data,
      "\n-- Drop some indexes:", new_data,
      "\n-- Drop a column:", new_data2,
      "\n-- Drop some columns:", new_data3,
      sep='\n')





##### Indexing, Selection, and Filtering #####
print('\n\n\n\n############### 3. Indexing, Selection, and Filtering ###############')

### Indexing.
print('\n3.1 Indexing')

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print('\n3.1.1 Indexing',
      '\n-- Original:', obj,
      "\n-- obj['b'] = obj[1] =", obj['b'],
      '\n-- obj[2:4] =', obj[2:4],
      "\n-- obj[['b', 'a', 'd']] =", obj[['b', 'a', 'd']],
      '\n-- obj[[1,3]] =', obj[[1,3]],
      "\n-- obj[obj < 2] =", obj[obj < 2],
      sep='\n')

obj['b':'c'] = 5
print("\n-- obj['b':'c'] = 5", obj, sep='\n')

# For DataFrame.
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print('\n3.1.2 Indexing for DataFrame',
      "\n-- Original", data,
      "\n-- data['two'] =", data['two'],
      "\n-- data[['three', 'one']] =", data[['three', 'one']],
      "\n-- data[:2] =", data[:2], # Default by indexes.
      "\n-- data[data['three'] > 5] =", data[data['three'] > 5],
      "\n-- data % 3 == 0 = (Boolean)", data % 3 == 0,
      sep='\n')


### Selection.
print('\n\n3.2 Selection')
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print('\n3.2.1 Selection with loc/iloc',
      "\n-- Original", data,
      "\n-- data.loc['Colorado', ['two', 'three']] = (by label)", data.loc['Colorado',['two','three']],
      "\n-- data.iloc[[3, 1],[3, 0, 1]] = (by internal indexes)", data.iloc[[3,1],[3,0,1]],
      "\n-- data.loc[:'Utah', 'two'] = (with slicing)", data.loc[:'Utah','two'],
      "\n-- data.iloc[:, :3][data.three > 5] = (with multi filters)", data.iloc[:,:3][data.three>5],
      sep='\n')

# Properties of integer indexes.
ser = Series(np.arange(3.))
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
print('\n3.2.2 Integer Indexes',
      "\n-- ser2[-1] = (integer indexes don't have -1 index)", ser2[-1],
      "\n-- Difference among ser[:1] / ser.loc[:1] / ser.iloc[:1]:",
      '- ser[:1] =', ser[:1], '- ser.loc[:1] =', ser.loc[:1], '- ser.iloc[:1] =', ser.iloc[:1],
      '\nConclusion: .loc() is label-oriented if the axis is integer index.',
      sep='\n')





##### Arithmetic and Data Alignment #####
print('\n\n\n\n############### 4. Arithmetic and Data Alignment ###############')

index1 = Index(['a', 'c', 'd', 'e'])
index2 = Index(['a', 'c', 'e', 'f', 'g'])
s1 = Series([7.3, -2.5, 3.4, 1.5], index=index1)
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=index2)
print('\n4.1 Missing values will be NaN',
      '\n-- Original:', '- s1 =', s1, '- s2 =', s2,
      '\n-- s1 + s2 =', s1 + s2,
      sep='\n')

index_sum = index1.union(index2)
s1 = s1.reindex(index=index_sum, fill_value=0)
s2 = s2.reindex(index=index_sum, fill_value=0)
s = s1 + s2
print('\n4.2 Prevent NaN when doing arithmetic',
      '\n-- Use fill_value property in reindex method to prevent NaN:', s, sep='\n')

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print('\n-- Use fill_value property in add method to prevent NaN:',
      '- df1 =', df1, '- df2 =', df2, '\n- df1 + df2 =', df1 + df2,
      '\n- df1.add(df2, fill_value=0) =', df1.add(df2, fill_value=0),
      sep='\n')

'''
    # Operators.
    add, radd
    sub, rsub
    div, rdiv
    floordiv, rfloordiv
    mul, rmul
    pow, rpow
'''

# Operations between DataFrame and Series.
frame = DataFrame(np.arange(12.).reshape((4, 3)),
                  columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
series3 = frame['d']

print('\n4.3 Operations between DataFrame and Series',
      '\n-- Original:', '- frame =', frame, '- series =', series,
      '\n-- frame - series = (match by columns, broadcasting down the rows)', frame - series,
      '\n-- frame + series2 = (invalid numbers)', frame + series2,
      "\n-- frame.sub(series3, axis='index') = (match by indexes)",
      '- series3 =', series3, '- result =', frame.sub(series3, axis='index'),
      sep='\n')




##### Function Application and Mapping #####
print('\n\n\n\n############### 5. Function Application and Mapping ###############')

# NumPy nfuncs.
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print('\n5.1 NumPy ufuncs',
      '\n-- Original:', frame,
      '\n-- np.abs(frame) =', np.abs(frame),
      sep='\n')

# Custom functions.
f = lambda x: x.max() - x.min()
print('\n5.2 Custom functions',
      '\n-- Original:', frame,
      '\n-- frame.apply(f) =', frame.apply(f), # default run by column.
      "\n-- frame.apply(f, axis='columns') =", frame.apply(f, axis='columns'),
      sep='\n')

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
print("\n-- Use block function:", frame.apply(f), sep='\n')

# Custom mappings.
format = lambda x: '%.2f' % x
print('\n5.3 Custom mappings',
      '\n-- Original:', frame,
      '\n-- frame.applymap(format) =', frame.applymap(format),
      "\n-- frame['e'].map(format) =", frame['e'].map(format),
      sep='\n')




##### Sorting and Ranking #####
print('\n\n\n\n############### 6. Sorting and Ranking ###############')

### Sort by index.
print('\n6.1 Sort by index')

obj = Series(range(4), index=['d', 'a', 'b', 'c'])

print('\n6.1.1 Sort by index',
      '\n-- Original:', obj,
      '\n-- obj.sort_index() =', obj.sort_index(),
      sep='\n')

# For DataFrames.
frame = DataFrame(np.arange(8).reshape((2, 4)),
                  index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])

print('\n6.1.2 For DataFrames',
      '\n-- Original:', frame,
      '\n-- frame.sort_index() =', frame.sort_index(),
      '\n-- frame.sort_index(axis=1) =', frame.sort_index(axis=1),
      '\n-- frame.sort_index(axis=1, ascending=False) =', frame.sort_index(axis=1, ascending=False),
      sep='\n')

# Multi sort keys.
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

print('\n\n6.1.3 Multi sort keys',
      '\n-- Original:', frame,
      "\n-- frame.sort_values(by='b')", frame.sort_values(by='b'),
      "\n-- frame.sort_values(by=['a', 'b'])", frame.sort_values(by=['a', 'b']),
      sep='\n')



### Sort by value.
print('\n\n6.2 Sort by value')

obj = Series([4, 7, -3, 2])

print('\n6.2.1 Sort by value',
      '\n-- Original:', obj,
      '\n-- obj.sort_values() =', obj.sort_values(),
      sep='\n')

# Missing values will sort at end by default.
obj = Series([4, np.nan, 7, np.nan, -3, 2])

print('\n6.2.2 Missing values',
      '\n-- Original:', obj,
      '\n-- obj.sort_values() =', obj.sort_values(),
      sep='\n')


### Rank 返回值的顺序位次，默认若相同则取平均值.
print('\n\n6.3 Rank')

obj = Series([7, -5, 7, 4, 2, 0, 4])

print('\n6.3.1 Rank',
      '\n-- Original:', obj,
      '\n-- obj.rank() = (default by mean rank)', obj.rank(),
      "\n-- obj.rank(method='first') = (先出现的先赋)", obj.rank(method='first'),
      "\n-- obj.rank(ascending=False, method='max') = (顺延式)", obj.rank(ascending=False, method='min'),
      sep='\n')

# For DataFrame.
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})

print('\n6.3.2 For DataFrame',
      '\n-- Original:', frame,
      "\n-- frame.rank(axis='index')", frame.rank(axis='index'),
      "\n-- frame.rank(axis='columns')", frame.rank(axis='columns'),
      sep='\n')




##### Duplicate Labels #####
print('\n\n\n\n############### 7. Duplicate Labels ###############')

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

print('\n7.1 For Series',
      '\n-- Original:', obj,
      "\n-- obj.index.is_unique =", obj.index.is_unique,
      "\n-- obj['a'] =", obj['a'],
      "\n-- obj['c'] =", obj['c'],
      sep='\n')

df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])

print('\n7.2 For DataFrame',
      '\n-- Original:', df,
      "\n-- df.loc['b'] =", df.loc['b'],
      sep='\n')