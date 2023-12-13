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




# Commonly used functions.
'''
    较常用：
    read_csv        逗号间隔的数据
    read_table      tab间隔的数据
    read_json       json字典数据

    较不常用：
    read_fwf        固定宽度数据
    read_clipboard  剪贴板中的、tab间隔的数据
    read_excel      xls/xlsx表格数据
    read_hdf        pandas HDF5数据
    read_html       读取html中的表格数据
    read_msgpack    MessagePack二进制数据
    read_pickle     Python pickle格式
    read_sas        SAS数据库
    read_sql        SQL数据库
    read_stata      Stata格式数据
    read_feather    Feather二进制数据
'''

# Optional types of arguments for the functions above.
'''
    Indexing
        针对数据表中的其中几列进行分析，或对数据表的索引名称进行确定
    Type inference and data conversion
        数据转换或缺失值的处理
    Datetime parsing
        时间格式与根据时间对数据进行整理归纳
    Iterating
        对大数据的遍历
    Unclean data issues
        对无关数据，包括缺失数据、注释、以及其他重要性不高的数据的处理
'''

##### TEXT FORMAT #####
print("############### TEXT FORMAT ###############")

# .read_csv can perform type inference
# So we need not to specify which column is numeric, integer, boolean or string.

path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex1.csv"
df = pd.read_csv(path)
df2 = pd.read_table(path, sep=',') # Default as sep='\t'

print('\n1.1 Read files with headers.\n./examples/ex1.csv')
print("\n-- pd.read_csv(path)", df, sep='\n')
print("\n-- pd.read_table(path, sep=',')",
      "- Use optional separator (sep) argument to read csv file.", df, sep='\n')

# read .csv file without header.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex2.csv"
names = ['a', 'b', 'c', 'd', 'message']

df = pd.read_csv(path, header=None)
df2 = pd.read_csv(path, names=names)
df3 = pd.read_csv(path, names=names, index_col='message')

print('\n\n1.2 Read files without headers.\n./examples/ex2.csv')
print("\n-- pd.read_csv(path, header=None)",
      "- Column headers will take by integer indexes from 0.", df,
      "\n-- pd.read_csv(path, names=list)",
      "- Customized headers.", df2,
      "\n-- pd.read_csv(path, names=list, index_col=str)",
      "- Specify a certain column as the index.", df3,
      sep='\n')

# multiple indexes.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\csv_mindex.csv"
parsed = pd.read_csv(path, index_col=['key1', 'key2'])

print('\n\n1.3 Multiple indexes.\n./examples/csv_mindex.csv')
print("\n-- pd.read_csv(path, index_col=list)",
      "- Pass index_col argument by a list of column names to modify multiple indexes.",
      parsed, sep='\n')

# use regular expression as separator.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex3.txt"
result = pd.read_table(path, sep='\s+')

print('\n\n1.4 Regular expression as separator.\n./examples/ex3.txt')
print("\n-- pd.read_table(path, sep='\s+')",
      "- Pass argument sep='\s+' to let regular expression as separator when reading variable amount of whitespaces.",
      "- read_table() will find indexes and column headers automatically.",
      result, sep='\n')

# skip specific rows.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex4.csv"
with open(path) as f: rows = f.read()
skipped = pd.read_csv(path, skiprows=[0, 2, 3])

print('\n\n1.5 Skip specific rows.\n./examples/ex4.csv')
print("\n-- Original:", rows,
      "\n-- pd.read_csv(path, skiprows=[0, 2, 3])",
      "- Pass argument skiprows=[0, 2, 3] to skip row 0/2/3.",
      skipped, sep='\n')

# handle missing values.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex5.csv"
result = pd.read_csv(path, index_col='something')
result2 = pd.read_csv(path, index_col='something', na_values=['NULL'])

print('\n\n1.6 Handle missing values.\n./examples/ex5.csv',
      "\n-- pd.read_csv(path, index_col='something')",
      "- Pandas will save missing value or NA as NaN.", result,
      "\n-- pass argument na_values=['NULL']", result2,
      sep='\n')

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
result3 = pd.read_csv(path, index_col='something', na_values=sentinels)

print("\n-- Set some values as NA.", result3, sep='\n')




### Read text files in pieces ###
print("\n\n\n\n############### Read text files in pieces ###############")

path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex6.csv"
result = pd.read_csv(path)
result2 = pd.read_csv(path, nrows=5)

print('\n2.1 Read first some rows.',
      "\n-- Original:", result,
      "\n-- Pass nrows=5 to read first 5 rows.", result2, sep='\n')

# specify a chunksize as a number of rows.
# split to pieces with certain number of rows.
chunker = pd.read_csv(path, chunksize=1000)
tot = Series([])
for piece in chunker:
    # count number of unique values.
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
print("\n\n2.2 Use chunk to reduce RAM usage.",
      "\n-- Count number of unique values.", tot, sep='\n')




### Write data to text format. ###
print("\n\n\n\n############### Write data to text format ###############")

path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex5.csv"
data = pd.read_csv(path)

out_path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\out.csv"
data.to_csv(out_path)

out_path2 = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\out2.csv"
data.to_csv(out_path2, sep='|')

out_path3 = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\out3.csv"
data.to_csv(out_path3, na_rep='NULL')

out_path4 = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\out4.csv"
data.to_csv(out_path4, index=False, header=False)

out_path5 = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\out5.csv"
data.to_csv(out_path5, index=False, columns=['a', 'b', 'c'])

print("\n3.1 Write data to a comma separated file.",
      "\n-- data.to_csv(out_path)", pd.read_csv(out_path),
      "\n-- use other delimiters (sep='|').", pd.read_csv(out_path2, sep='|'),
      "\n-- save NA as NULL (na_rep='NULL').", pd.read_csv(out_path3, na_values=['NULL']),
      "\n-- save without labels (index=False, header=False).", pd.read_csv(out_path4, header=None),
      "\n-- save part columns (index=False, columns=['a', 'b', 'c']).", pd.read_csv(out_path5, header=None),
      sep='\n')

# for series.
dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\tseries.csv"
ts.to_csv(path, header=False)

print("\n3.2 Write series to file.",
      "\n-- Original:", ts,
      "\n-- ts.to_csv(path)", pd.read_csv(path, header=None),
      sep='\n')




### Delimited formats. ###
print("\n\n\n\n############### Delimited formats ###############")

path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex7.csv"
with open(path) as f:
    lines = list(csv.reader(f))
    header, values = lines[0], lines[1:]
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    print(data_dict)

# define a csv format.
class my_dialect(csv.Dialect):
    lineteminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

# use the method below to read with custom format.
# with open(path) as f:
#     reader = csv.reader(f, dialect=my_dialect)

# use the method below to write with custom format.
# with open('mydata.csv', 'w') as f:
#     writer = csv.writer(f, dialect=my_dialect)
#     writer.writerow(('one', 'two', 'three'))
#     writer.writerow(('1', '2', '3'))
#     writer.writerow(('4', '5', '6'))
#     writer.writerow(('7', '8', '9'))




### JSON data. ###
print("\n\n\n\n############### JSON data ###############")

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
result = json.loads(obj)
df = DataFrame(result['siblings'], columns=['name', 'age'])

print("\n4.1 JSON format.",
      "\n-- Original:", result,
      "\n-- Save parts to a DataFrame.", df,
      sep='\n')

# from files
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\example.json"
with open(path) as f: j = f.read()
data = pd.read_json(path)

print("\n\n4.2 JSON files.",
      "\n-- Original:", j,
      "\n-- pd.read_json(path)", data,
      "\n-- data.to_json()", data.to_json(),
      "\n-- data.to_json(orient='records')", data.to_json(orient='records'),
      sep='\n')




### XML and HTML data. ###
print("\n\n\n\n############### XML and HTML data ###############")

# read_html() will automatically search for tabular data.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\fdic_failed_bank_list.html"
save_path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\fdic_failed_bank_list.csv"

tables = pd.read_html(path)
failures = tables[0]
failures.to_csv(save_path)

close_timestamps = pd.to_datetime(failures['Closing Date'])
years = close_timestamps.dt.year.value_counts()

print("\n5.1 HTML files.",
      "\n-- Original:", tables,
      "\n-- Choose the table:", failures,
      "\n-- Header of the table:", failures.columns,
      "\n-- Number of bank failures by year:", years,
      sep='\n')


# use lxml pack to read XML data.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\mta_perf\Performance_MNR.xml"

from lxml import objectify
with open(path) as f:
    parsed = objectify.parse(f)
    root = parsed.getroot()

data = []
skip_fileds = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
# root.INDICATOR returns a generator yielding each <INDICATOR> XML element.
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fileds: # exclude some tags.
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = DataFrame(data)
save_path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\mta_perf\Performance_MNR.csv"
perf.to_csv(save_path)

print("\n\n5.2 XML files.",
      "\n-- Sample data read directly from XML file:", data[0],
      "\n-- Converted data", perf,
      sep='\n')






##### BINARY FORMAT #####
print("\n\n\n\n############### BINARY FORMAT ###############")

### save as pickle format. ###
# ATTENTION: pickle is only recommended as a short-term storage format.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex1.csv"
frame = pd.read_csv(path)

save_path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\frame_pickle"
frame.to_pickle(save_path)

read_frame = pd.read_pickle(save_path)
print("\n6.1 Pickle data.",
      "\n-- Original:", frame,
      "\n-- Saved as pickle then read:", read_frame,
      sep='\n')

### HDF5 data ###
# We can use PyTables or h5py libraries.
# Or use pandas built-in methods.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\mydata.h5"

frame = DataFrame({'a': np.random.randn(100)})
store = HDFStore(path)
store['obj1'] = frame
store['obj1_col'] = frame['a']

store.put('obj2', frame, format='table')

print("\n\n6.2 HDF5 data.",
      "\n-- An object in the data.", store['obj1'],
      "\n-- Select parts.", store.select('obj2', where=['index >= 10 and index <= 15']),
      sep='\n')

store.close()

frame.to_hdf(path, 'obj3', format='table')
frame = pd.read_hdf(path, 'obj3', where=['index < 5'])
print("\n-- Use pandas built-in method.", frame, sep='\n')






##### MS EXCEL FILES #####
print("\n\n\n\n############### MS EXCEL FILES ###############")

# .read_excel() function
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex1.xlsx"
xlsx = pd.ExcelFile(path)

read_xlsx = pd.read_excel(xlsx, 'Sheet1')

print("\n7.1 Read from MS Excel file.",
      "\n-- pd.read_excel(pd.ExcelFile(path), 'Sheet1')", read_xlsx,
      sep='\n')

# write to excel.
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\ex2.xlsx"
writer = pd.ExcelWriter(path)

frame.to_excel(writer, 'Sheet1')
writer.save()






##### WEB APIs #####
print("\n\n\n\n############### WEB APIs ###############")

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json() # pull data.

path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\examples\pandas.json"
with open(path, 'w') as f:
    json.dump(data, f, indent=4)

print("\n-- Url: https://api.github.com/repos/pandas-dev/pandas/issues",
      f"\n-- resp = requests.get(url) = {resp}",
      "\n-- data = resp.json() (Choose data[0] as sample.)", data[0],
      sep='\n')

# save part data to a dataframe
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print("\n-- Issues:", issues, sep='\n')






##### DATABASE #####
print("\n\n\n\n############### DATABASE ###############")

import sqlite3

# create sql database.
query = """CREATE TABLE test (a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);"""
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\mydata.sqlite"
con = sqlite3.connect(path)

exe = con.execute(query)
print("\n-- Executed query: ", exe, sep='\n')
con.commit()

# insert a few rows of data.
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

# select data.
cursor = con.execute('select * from test')
rows = cursor.fetchall()
frame = DataFrame(rows, columns=[x[0] for x in cursor.description])

print("\n-- Selected:", rows,
      "\n-- Cursor discription:", cursor.description,
      "\n-- Read rows:", frame,
      sep='\n')

# use sqla library.
# import sqlalchemy as sqla
# db = sqla.create_engine('sqlite:///mydata.sqlite')
# read = pd.read_sql('select * from test', db)

# delete sql database.
# import os
# path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\mydata.sqlite"
# os.remove(path)