import pandas as pd
from pandas import Series, DataFrame, Index
import numpy as np
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
# pd.set_option('display.float_format', lambda x: '%.4f' % x) # Round to .4
warnings.filterwarnings("ignore") # Suppress warnings.




##### PANDAS DATA STRUCTURES #####

### Series ###

## Create a Series object.
print('############### Example 1.1 ###############')
obj = Series([4, 7, -5, 3])
print('', 'A sample panda object:', obj, sep='\n')

# Customize indexes.
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index = ['d', 'b', 'a', 'c'] # This method can assign indexes independently.
print('', 'indexes customization:', obj2,
      f'indexes: {obj2.index}', sep='\n')

# Refer value / Change value through different methods.
obj2['d'] = 6
print('', 'c, a, d =', obj2[['c', 'a', 'd']], sep='\n') # Use list of indexes.
print('', 'obj2 > 0:', obj2[obj2>0], sep='\n')

print('\nRefer by indexes:')
print("Is 'b' in obj2? ", 'b' in obj2)
print("Is 'e' in obj2? ", 'e' in obj2)

# Batch calculating.
print('', 'obj * 2 =', obj*2, '\nnp.exp(obj2) = ', np.exp(obj2), sep='\n')


## Another sample.
print('\n\n\n\n############### Example 1.2 ###############')
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print('', 'Another sample panda object:', obj3, sep='\n')

# Invalid revoking returns ERROR.
states = ['California', 'Ohio', 'Oregon', 'Texas'] # No 'California' in obj3.
obj4 = Series(sdata, index=states)
print('', 'Invalid revoking returns NaN:', obj4, sep='\n')
print('** Because ** (pd.notnull(obj4)):', pd.notnull(obj4), sep='\n')

# It can be added by index.
print('', 'obj3 + obj4 =', obj3+obj4, sep='\n') # NaN + [number] = NaN

# Give 'name' attribute to an object.
obj4.name = 'population'
obj4.index.name = 'state'
print('', 'Object with name:', obj4, sep='\n')



### DATA FRAME ###

# A data frame can be thought of a dict of Series share the same index.

## Create a DataFrame object.
print('\n\n\n\n############### Example 2.1 ###############')

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'population': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = DataFrame(data) # indexes generates automatically as same as Series.
print(frame) # It will print more neatly on browser.
print('', 'frame.head() selects only the first five rows:',
      frame.head(), sep='\n')

# Customize order.
frame = DataFrame(data, columns=['year', 'state', 'population'])
print('', 'Specified order:', frame, sep='\n')

# Invalid revoking returns ERROR.
frame2 = DataFrame(data, columns=['year', 'state', 'population', 'debt'],
                   index=['one', 'two', 'three', 'four','five', 'six'])
print('', 'Missing values returns NaN:', frame2,
      f'Columns: {frame2.columns}', sep='\n')

# Assign invalid numbers.
frame2['debt'] = 16.5
print('', 'Use scalar value to assign the same value:', frame2, sep='\n')

frame2['debt'] = np.arange(1., 7.) # Use decimal to save as floats.
print('', 'Use array to assign the same value:', frame2, sep='\n')

frame2['eastern'] = frame2.state == 'Ohio' # Assign to a non-exist column.
print('', 'Assign to a non-exist column will create it:', frame2, sep='\n')

# Delete a column.
del frame2['eastern']

# 2 methods to partly retrieve.
print('', '2 methods to partly retrive',
      "by dict (frame['column']):", frame2['state'],
      'by attribute (frame.column):', frame2.year, sep='\n')

# Retrieve data in a specific index.
print('', "frame2.loc['three']", frame2.loc['three'], sep='\n')


## Create a DataFrame from a dictionary.
print('\n\n\n\n############### Example 2.2 ###############')

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# pandas will interpret the outer dict keys as the columns,
#   and the inner keys as the indexes.
# Use .sort_index() method to sort indexes in ascending order.
frame3 = DataFrame(pop).sort_index()
print('', frame3, sep='\n')

# Reverse tags.
print('', frame3.T, sep='\n')

# DataFrame slicing.
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
print('', DataFrame(pdata), sep='\n')

# Give tag/name to row/column indexes.
frame3.index.name = 'year'; frame3.columns.name = 'state'
print('', frame3, frame3.columns, frame3.index, sep='\n')



### INDEX OBJECTS ###

# Holding axis labels and other metadata.
print('\n\n\n\n############### Example 3.1 ###############')

obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index

print('', obj, index, sep='\n')
print(index[1:])

# Customize indexes by class Index.
labels = Index(np.arange(3))
print('', labels, sep='\n')

obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2, sep='\n')

# pandas index can contain duplicate labels.
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print('', 'Duplicate labels:', dup_labels, sep='\n')

# Index methods and properties.
'''
    Index.append()
         .difference()
         .intersection()
         .union()
         .isin()
         .delete()
         .drop()
         .insert()
         .is_monotonic() # Index monotonic increasing.
         .is_unique() # If the index has unique values.
         .unique()
'''



### MULTIINDEX
print('\n\n\n\n############### Example 4.1 ###############')
tuples = [('cobra', 'mark i'), ('cobra', 'mark ii'),
          ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
          ('viper', 'mark ii'), ('viper', 'mark iii')]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20], [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
print('', 'Multi-index:', df, sep='\n')