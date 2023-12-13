import numpy as np
import pandas as pd
from pandas import Series, DataFrame, Index, HDFStore
import warnings, requests
import csv, json, lxml
from datetime import datetime
import matplotlib.pyplot as plt

from X02_mod_get_url import get_url

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.
pd.options.display.max_rows = 10 # Display no more than 10 rows.




##### MISSING DATA #####
print("############### MISSING DATA ###############")

### Basic ###
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print("\n1.1 Missing data will be referred as 'not available' (NA)",
      "\n-- Original:", string_data,
      "\n-- string_data.isnull()", string_data.isnull(),
      sep='\n')

# None will treat as None.
string_data[0] = None
print("\n-- string_data[0] = None", string_data, sep='\n')

# Drop missing data.
# inplace=True will replace with the modified data, i.e. without copy.
string_data.dropna(axis='rows', how='all', inplace=True)
print("\n-- string_data.dropna()", string_data, sep='\n')


### Filter Missing Data ###
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
print("\n\n1.2.1 Filter missing data",
      "\n-- Original:", data,
      "\n-- Drop by function: data.dropna()", data.dropna(),
      "\n-- Drop by index filtering: data[data.notnull()]", data[data.notnull()],
      sep='\n')

# For DataFrame
data = DataFrame([[1., 6.5, 3., NA],
                  [1., NA, NA, NA],
                  [NA, NA, NA, NA],
                  [NA, 6.5, 3., NA]])

print("\n1.2.2 For DataFrame",
      "\n-- Original:", data,
      "\n-- Dropped by data.dropna()", data.dropna(),
      "\n-- Drop only all NA rows: data.dropna(how='all')", data.dropna(how='all'),
      "\n-- Drop only all NA columns: data.dropna(axis=1, how='all')", data.dropna(axis=1, how='all'),
      "\n-- Drop rows have less than 2 values: data.dropna(thresh=2)", data.dropna(thresh=2),
      sep='\n')


### Filling Missing Data ###
df = pd.DataFrame(np.random.randn(5, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA

print("\n\n1.3.1 Filling missing data",
      "\n-- Original:", df,
      "\n-- Fill by 0: df.fillna(0)", df.fillna(0),
      "\n-- Fill separate values: df.fillna({1: 0.5, 2: 0})", df.fillna({1: 0.5, 2: 1}),
      "\n-- Fill by repeated values: df.fillna(method='bfill', limit=2)", df.fillna(method='bfill', limit=2),
      "\n-- Fill by mean: df.fillna(df.mean())", df.fillna(df.mean()),
      sep='\n')





##### DATA TRANSFORMATION #####
print("\n\n\n\n############### DATA TRANSFORMATION ###############")

### Removing Duplicates ###
data = DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                  'k2': [1, 1, 2, 3, 3, 4, 4]})

print("\n2.1 Removing Duplicates",
      "\n-- Original:", data,
      "\n-- data.duplicated()", data.duplicated(),
      "\n-- Drop the duplicated data: data.drop_duplicates()", data.drop_duplicates(),
      sep='\n')

data['v1'] = range(7)
print("\n-- Drop by header: data.drop_duplicates(['k1'])", data.drop_duplicates(['k1']),
      "\n-- data.drop_duplicates(['k1', 'k2'], keep='last')", data.drop_duplicates(['k1', 'k2'], keep='last'),
      sep='\n')


### Function and Mapping ###
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                           'Pastrami', 'corned beef', 'Bacon',
                           'pastrami', 'honey ham', 'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print("\n\n2.2 Function and Mapping",
      "\n-- Original:", data, sep='\n')

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
} # We want to indicate the type of animal that each food came from.

lowercased = data['food'].str.lower()
data['animal'] = lowercased.map(meat_to_animal)

print("\n-- Mapped:", data, sep='\n')


### Replacing Values ###
data = pd.Series([1., -999., 2., -999., -1000., 3.])

print("\n\n2.3 Replacing Values",
      "\n-- Original:", data,
      "\n-- Replace by data.replace([-999, -1000], [np.nan, 0]):", data.replace([-999, -1000], [np.nan, 0]),
      sep='\n')


### Renaming Axis Indexes ###
data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])


print("\n\n2.4 Renaming Axis Indexes",
      "\n-- Original:", data, sep='\n')

transform = lambda x: x[:4].upper() # Maintain first 4 chars as upper case.
data.index = data.index.map(transform) # Use .index property.

print("\n-- Transformed:", data,
      "\n-- Use .rename() method to rename index/columns:", data.rename(index=str.title, columns=str.upper),
      "\n-- Rename separately:", data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}),
      sep='\n')


### Discretization and Binning ###
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100] # As interval edges.

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# (] by default, pass right=False to change to [).
cats = pd.cut(ages, bins, labels=group_names)

print("\n\n2.5.1 Discretization and Binning",
      "\n-- Original data:", ages,
      "\n-- Interval edges", bins,
      "\n-- Intervals of each ages included (Categorical object):", cats,
      "\n-- Interval indexes of each data:", cats.codes,
      "\n-- Intervals:", cats.categories,
      "\n-- Summarize by pd.value_counts(cats):", pd.value_counts(cats),
      sep='\n')

# Pass integer bins to create equal length interval.
data = np.random.rand(20)
cats = pd.cut(data, 4, precision=2) # Limit the decimal precision to two digits.

print("\n2.5.2 Create Euqal Length Interval",
      "\n-- Original data:", data,
      "\n-- pd.cut(data, 4, precision=2)", cats,
      "\n-- Summarize by pd.value_counts(cats):", pd.value_counts(cats),
      sep='\n')

# Quantile cutting.
data = np.random.randn(1000)
cats = pd.qcut(data, 4) # Cut by 25%,50%,75% quantiles.
cats2 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]) # Cut by custom quantiles.

print("\n2.5.3 Quantile cutting",
      "\n-- Original data (sample):", data[:10],
      "\n-- Cut by pd.qcut(data, 4):", cats,
      "\n-- Summary:", pd.value_counts(cats),
      "\n-- Cut by pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]):", cats2,
      "\n-- Summary:", pd.value_counts(cats2),
      sep='\n')


### Detecting and Filtering Outliers ###
data = pd.DataFrame(np.random.randn(1000, 4)) # 4 columns.
col = data[2] # 3rd column.

print("\n\n2.6 Detecting and Filtering Outliers",
      "\n-- Original data (sample):", data.head(),
      "\n-- Summary:", data.describe(),
      "\n-- Find element exceeding 3 by col[np.abs(col) > 3]:", col[np.abs(col) > 3],
      "\n-- Find the rows where the elements exceeding 3 locates by data[(np.abs(data) > 3).any(1)]", data[(np.abs(data) > 3).any(1)],
      sep='\n')

data[np.abs(data) > 3] = np.sign(data) * 3

print("\n-- Set the exceeding data to 3sigma",
      "MIN:", data.min(), "MAX:", data.max(), sep='\n')


### Permutation and Random Sampling ###
# numpy.random.permutation()
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5) # A randomly generated permutation sequence.

print("\n\n2.7.1 Permutation and Random Sampling",
      "\n-- Original:", df,
      "\n-- Random ordering: np.random.permutation(5)", sampler,
      "\n-- Reorder by df.take(sampler)", df.take(sampler),
      "\n-- Or we can reorder directly by DataFrame(np.random.permutation(df)):", DataFrame(np.random.permutation(df)),
      sep='\n')

choices = Series([-1, -2, -3, -4, -5])
draws = choices.sample(n=10, replace=True)
print("\n2.7.2 Randomly Draw Rows",
      "\n-- Original", df,
      "\n-- Draw random rows by df.sample(n=3)", df.sample(n=3),
      "\n-- Randomly draw a series of numbers:", draws,
      sep='\n')


### Computing Indicator/Dummy Variables ###
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})

print("\n\n2.8.1 Dummy Variables",
      "\n-- Original:", df,
      "\n-- Dummy variables: pd.get_dummies(df['key'])", pd.get_dummies(df['key']),
      sep='\n')

# Give a prefix to the header.
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)

print("\n-- Prefixed:", dummies,
      "\n-- Joined with df[['data1']]:", df_with_dummy, sep='\n')

'''
## Multiple indicators.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\movielens\movies.dat"
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(path, sep='::', header=None, names=mnames)

print("\n2.8.2 Multiple Indicators",
      "\n-- Original data (sample):", movies[:10], sep='\n')

# Collect all unique genres of movies.
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = np.sort(pd.unique(all_genres))
print("\n-- Genres:", genres, sep='\n')

zero_matrix = np.zeros((len(movies), len(genres)))
dummies = DataFrame(zero_matrix, columns=genres)

for i, genre in enumerate(movies.genres):
    # Split into a list, then get all indexes of the elements in the list.
    indices = dummies.columns.get_indexer(genre.split('|'))
    dummies.iloc[i, indices] = 1
print("\n-- Dummies:", dummies, sep='\n')

## Combine dummies with .cut()
values = np.random.rand(10)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
dummies = pd.get_dummies(pd.cut(values, bins))

print("\n2.8.3 Combine Dummies with .cut()",
      "\n-- Original:", values,
      "\n-- Cutted:", pd.cut(values, bins),
      "\n-- Dummies:", dummies,
      sep='\n')
'''




##### STRING MANIPULATION #####
print("\n\n\n\n############### STRING MANIPULATION ###############")

### String Object Methods ###
val = 'a,b, guido'
vals = val.split(',')
pieces = [x.strip() for x in val.split(',')]

first, second, third = pieces
print("\n3.1 String Object Methods (Page 213)",
      "\n-- Original:", val,
      "\n-- Split by val.split(',')", vals,
      "\n-- Remove spaces and tabs", pieces,
      "\n-- Format by first + '::' + second + '::' + third", first + '::' + second + '::' + third,
      "\n-- Or use '::'.join(pieces)", '::'.join(pieces),
      "\n-- val.index() will return the index of substring in the string.", val.index(','),
      "\n-- val.find() will return -1 if raise exception.", val.find(':'),
      "\n-- val.count() can count number of a particular substring.", val.count(','),
      "\n-- val.replace(',', '::')", val.replace(',', '::'),
      "\n-- val.replace(',', '')", val.replace(',', ''),
      sep='\n')


### Regular Expressions ###
import re

text = "foo bar\t baz \tqux"
regex = re.compile('\s+')

print("\n\n3.2.1 Regular Expressions (Regex)",
      "\n-- Original:", text,
      "\n-- re.split('\s+', text)", re.split('\s+', text),
      "\n-- re.compile('\s+').split(text)", re.compile('\s+').split(text),
      "\n-- re.compile('\s+').findall(text)", re.compile('\s+').findall(text),
      sep='\n')

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
# re.IGNORECASE makes the regex case-insensitive.
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.search(text)

print("\n3.2.2 Use Regex to find email address",
      "\n-- Found:", regex.findall(text),
      "\n-- Search for the first match string:", text[m.start():m.end()],
      "\n-- Replace the pattern with the new string:", regex.sub('REDACTED', text),
      sep='\n')

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@right.net')

print("\n-- Use another regex pattern:", m,
      "\n-- Grouped: (m.groups())", m.groups(),
      "\n-- Found:", regex.findall(text),
      "\n-- Formatted:", regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text),
      sep='\n')


### Vectorized String Functions ###
# A column containing strings will sometimes have missing data.
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = Series(data)

print("\n\n3.3 Vecorized String Functions",
      "\n-- Original:", data,
      "\n-- data.isnull()", data.isnull(),
      "\n-- data.str.contains('gmail')", data.str.contains('gmail'),
      "\n-- Use regular expression:", data.str.findall(pattern, flags=re.IGNORECASE),
      "\n-- If the string can be regexed:", data.str.match(pattern, flags=re.IGNORECASE),
      sep='\n')