import io
import requests
import pandas as pd
from datetime import datetime

import warnings

def pull_stock(ticker, start="2022-01-01", end="2022-02-02", interval="1d"):
    
    warnings.filterwarnings("ignore") # Suppress warnings.
    
    url = r"https://query1.finance.yahoo.com/v7/finance/download/" + str(ticker)
    referer = r"https://finance.yahoo.com/quote/" + str(ticker) + r"/history"
    x = int(datetime.strptime(start, '%Y-%m-%d').timestamp())
    y = int(datetime.strptime(end, '%Y-%m-%d').timestamp())
    url += "?period1=" + str(x) + "&period2=" + str(y) + "&interval=" + interval + "&events=history&includeAdjustedClose=true"
    referer += "?period1=" + str(x) + "&period2=" + str(y) + "&interval=" + interval + "&frequency=1d&filter=history"
    
    print(f'{ticker}:\t{url}')
    '''
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        'referer': referer,
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    '''
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    
    r = requests.get(url, headers=headers, verify=True)
    pd1 = pd.read_csv(io.StringIO(r.text), index_col=0, parse_dates=True, encoding="utf-8", error_bad_lines=False)
    return pd1

#使用AAPL测试
now = datetime.strptime('2022-05-30', '%Y-%m-%d')
print(int(now.timestamp()))
startv = "2022-01-03"
endv = str(datetime.now().strftime("%Y-%m-%d"))
print(endv)
data = pull_stock("AAPL", start=startv, end=endv, interval="1d")
print(data)