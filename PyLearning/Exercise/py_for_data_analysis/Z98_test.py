import pandas
import plotly.graph_objects as go
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn
import yfinance as yf
import yahoo_fin.stock_info as si
# df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
#
#
# print(df.iloc[2].iat[2])



df1=pandas.read_csv("HS300_PE.csv")
# print(df1)
# print(si.get_quote_table("600519.SS"))

# 建立一个list 包含沪深三百的股票代码


# FOR 每一个元素 执行si.get_quote_table(
global temp1
temp=[]
def exec_code(i):
    return eval(df1.iloc[i].iat[1])
# print(exec_code(1))
for i in range(len(df1)):
    temp.append(exec_code(i))
    print(exec_code(i))

# print(temp)

#
#

# df = pd.DataFrame({'PE (TTM)':temp})

df1['PE Ratio (TTM)'] = temp
# print(df1)
# df = pd.DataFrame({'0': {'Stock Code': si.get_quote_table("600519.SS")["PE Ratio (TTM)"], 'PE (TTM)': 17},
#                      '1': {'Stock Code': 13, 'PE (TTM)': 28},
#                      '2': {'Stock Code': 9, 'PE (TTM)': 14},
#                      '3': {'Stock Code': 11, 'PE (TTM)': 18},
#                      '4': {'Stock Code': 15, 'PE (TTM)': 16},
#                      '5': {'Stock Code': 9, 'PE (TTM)': 11},
#                      '6': {'Stock Code': 8, 'PE (TTM)': 25},
#                      '7': {'Stock Code': 11, 'PE (TTM)': 26},
#                      '8': {'Stock Code': 11, 'PE (TTM)': 22},
#                      '9': {'Stock Code': 20, 'PE (TTM)': 27},
#                      '10': {'Stock Code': 19, 'PE (TTM)': 25}})
# df=df.transpose()
df1.reset_index(inplace=True)
df1.rename(columns={'index':''}, inplace = True)

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df1.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df1[col] for col in df1.columns],
               fill_color='lavender',
               align='left'))
])

fig.show()