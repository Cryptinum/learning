import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller # ADF单位根检验
from statsmodels.tsa.stattools import q_stat, acf # 白噪声检验:Ljung-Box检验
from statsmodels.tsa.arima.model import ARIMA # ARIMA模型
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf # 自相关和偏自相关

import plotly.graph_objects as go

import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.



# 导入数据，数据来源Yahoo Finance
path = r"D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\GOOG.csv"
goog = pd.read_csv(path)

# 转换索引为日期
goog.Date = pd.to_datetime(goog.Date)
goog.set_index('Date', inplace=True)
# 建立日期索引的频率信息以正常预测
goog.index = pd.DatetimeIndex(goog.index).to_period('M')

# 开盘价
goog_open = goog['Open']
#goog_close = goog['Close']

plt.rcParams['font.sans-serif'] = ['simhei'] # 字体为黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号 # 时序图的绘制

goog_open.plot(linewidth=1, label='开盘价')
#goog_close.plot(linewidth=1, label='收盘价')

plt.xticks(rotation=45) #坐标角度旋转
plt.xlabel('日期') #横、纵坐标以及标题命名
plt.ylabel('价格')
plt.title('谷歌/Alphabet(NASDAQ:GOOG)开盘价', loc='center', fontsize=18)
plt.legend(loc="best")
#plt.show()

# ADF检验，结果大于1%的、5%的、10%的，p显著不接近0，故拒绝原假设
result = adfuller(goog_open)
print("\nresult is\n{}".format(result))

result_format = pd.Series(result[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])
for k, v in result[4].items():
    result_format['Critical Value (%s)' % k] = v
result_format['The maximized information criterion if autolag is not None.'] = result[5]
print("\nresult_fromat is\n{}".format(result_format))

print("\n\n===== adfuller()的回归模型系数 =====")
[t, p, c, r] = adfuller(x=goog_open, regression='ctt', regresults=True)

print("r.resols.summary() is")
print(r.resols.summary())

print("\nr.resols.params are")
print(r.resols.params)

# 进行一阶差分以平稳化，结果显著小于1%的、5%的和10%的，且p显著接近0，一阶差分可用
goog_open_1diff = goog_open.diff(1).dropna()
result1 = adfuller(goog_open_1diff)
print("\n\n\n\n\nresult is\n{}".format(result1))

# 展示一阶差分的时序
goog_open_1diff.plot(linewidth=1, label='开盘价（一阶差分）')
plt.xticks(rotation=45) #坐标角度旋转
plt.xlabel('日期') #横、纵坐标以及标题命名
plt.ylabel('价格')
plt.title('谷歌/Alphabet(NASDAQ:GOOG)开盘价（一阶差分）', loc='center', fontsize=18)
plt.legend(loc="best")
#plt.show()

# 白噪声检验
# 显示第一个到第11个白噪声检验的p值
print('\n\n差分前')
LjungBox = q_stat(acf(goog_open)[1:12],len(goog_open))[1]
print(LjungBox)
print('\n\n差分后')
LjungBox = q_stat(acf(goog_open_1diff)[1:12],len(goog_open_1diff))[1]
print(LjungBox)

#白噪声检验通过，直接确定模型
model = ARIMA(goog_open, order=(1,1,0)) # 自回归与一阶差分(1,1,0)
result = model.fit()
print('\n\n\n===== 结果 =====',
      result.summary(), sep='\n') # 提取模型信息

plot_acf(goog_open_1diff, use_vlines=True, lags=30) # 自相关函数图，滞后30阶
#plt.show()

plot_pacf(goog_open_1diff, use_vlines=True, lags=30) #偏自相关函数图，滞后30阶
#plt.show()

# 最小化AIC
train_results = sm.tsa.arma_order_select_ic(goog_open_1diff, ic=['aic', 'bic'], trend='n', max_ar=8, max_ma=8)
print('\n\n\nAIC', train_results.aic_min_order) #建立AIC值最小的模型
# print('BIC', train_results.bic_min_order)
model = ARIMA(goog_open, order=(2,1,2)).fit()
print(model.summary()) #提取模型系数等信息，保留三位小数；summary2保留四位小数

# 显著性检验
print('\n\n\n显著性检验')
print(model.conf_int())


import math
stdresid = model.resid/math.sqrt(model.sigma2) #标准化残差
plt.rcParams['font.sans-serif'] = ['simhei'] #字体为黑体
plt.rcParams['axes.unicode_minus'] = False #正常显示负号
plt.plot(stdresid) #标准化残差序列图
plt.xticks(rotation=45) #坐标角度旋转
plt.xlabel('日期') #横、纵坐标以及标题命名
plt.ylabel('标准化残差')
plt.title('标准化残差序列图',loc='center')
plt.show()

plot_acf(stdresid,lags=30) 
plt.show()

LjungBox = q_stat(acf(stdresid)[1:13],len(stdresid))
LjungBox[1][-1] #LjungBox检验的最后一个P值，大于0.05，通过白噪声检验

a = model.forecast(10)
fig, ax = plt.subplots(figsize=(6, 4))
ax = goog_open.ix['2022-01':].plot(ax=ax)
plt.show()
fig = model.plot_predict(5,280)