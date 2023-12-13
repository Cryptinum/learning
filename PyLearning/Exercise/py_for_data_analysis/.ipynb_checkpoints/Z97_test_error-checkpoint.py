import os
import io
import urllib
import requests
import pandas as pd
from datetime import datetime

import warnings

def download(url):
    filename = url.split('/')[-1]
    mk = "E:/存储下载的文件的地址"
    dest_dir = os.path.join(mk, filename)
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, dest_dir)
    except Exception as e:
        print(e)
        print("is wrong ")

def pull_stock(ticker, start="2022-01-01", end="2022-02-02", interval="1d"):
    
    warnings.filterwarnings("ignore") # Suppress warnings.
    
    url = r"https://query1.finance.yahoo.com/v7/finance/download/" + str(ticker)
    referer = r"https://finance.yahoo.com/quote/" + str(ticker) + r"/history"
    x = int(datetime.strptime(start, '%Y-%m-%d').timestamp())
    y = int(datetime.strptime(end, '%Y-%m-%d').timestamp())
    url += "?period1=" + str(x) + "&period2=" + str(y) + "&interval=" + interval + "&events=history&includeAdjustedClose=true"
    referer += "?period1=" + str(x) + "&period2=" + str(y) + "&interval=" + interval + "&frequency=1d&filter=history"
    
    print(f'{ticker}:\t{url}')

    download(url)
    '''
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        'cookie': "OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiWjdST0xMNE5BR05VVE1PV1pRNlFBM1BGTkUiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJkbjJpWkRwWVdBbDMifX0.IwamZmE4QbQlSOzqqLOzP51DL4RKiEBdTdxxtgiA7filVgzKlJ6Ujv8XuBVNTY_9_8Sd3UFotwTAIC_VP3ba8YB6I56V0vj3dfkYzNHTiwzE_kocqpEMJ5aD4sBm7s6dEeEszP2R5_La-mqAtPQ9Ajt1t5TU78CvSBLDLE5vClE; T=af=JnRzPTE2NTc3MDMyNjgmcHM9ZHp5Z0g3TE9GM2ZNV1hqTHpEOGZ6US0t&d=bnMBeWFob28BZwFaN1JPTEw0TkFHTlVUTU9XWlE2UUEzUEZORQFhYwFBQXpFTDhEZwFhbAFxd2VydHl6YWNpdW1AZ21haWwuY29tAXNjAW1icl9yZWdpc3RyYXRpb24BZnMBbkp1ZnI1Uml6b3RrAXp6AWt0b3ppQkE3RQFhAVFBRQFsYXQBa3RvemlCAW51ATA-&kt=EAASwAMM0oYSFwx71uFRE4psQ--~I&ku=FAATnJ3DcTmb.QRSdVHp0Y8x6xwZfZRL1caG33yk2F8fmj.bWjEgqvDLkWFDDyyLJerHS1RKzFMhFka2BIBBcOburfYRF4sjRQQQSWjx4AT6gd6o8LQLVdctIMYZCAXrI47M6meDTNTFFTkujpVmk6dTnrvFw.IyjsvcSHZO5JjL6g-~E; F=d=4ed_WIY9vMWyfulLPDAn7BUzVLxtmmXXdl9Rh0iRu90A2aRVf6DX_TLc; PH=l=en-US; Y=v=1&n=6nonvrq6u7vij&l=alfbd3h2nm9aavn53ol5dkgghx5m6kxpcikfjot7/o&p=n32vvhk00000000&r=1ae&intl=us; GUC=AQEABwJiz9NjokIZ6QQ7&s=AQAAADx6lOG6&g=Ys6LdQ; A1=d=AQABBEplSl4CEE_v6bWzJ0TTslUmIohehdYFEgEABwLTz2KiY9yia3sB_eMBAAcINdNOXRqDbCQID9ohx4BLNFR7DPb9SSPNZwkBBwoB5w&S=AQAAAjUdyHvadvEHDWuvsOhGRoE; A3=d=AQABBEplSl4CEE_v6bWzJ0TTslUmIohehdYFEgEABwLTz2KiY9yia3sB_eMBAAcINdNOXRqDbCQID9ohx4BLNFR7DPb9SSPNZwkBBwoB5w&S=AQAAAjUdyHvadvEHDWuvsOhGRoE; ucs=lbit=1; A1S=d=AQABBEplSl4CEE_v6bWzJ0TTslUmIohehdYFEgEABwLTz2KiY9yia3sB_eMBAAcINdNOXRqDbCQID9ohx4BLNFR7DPb9SSPNZwkBBwoB5w&S=AQAAAjUdyHvadvEHDWuvsOhGRoE&j=WORLD; cmp=t=1657784962&j=0&u=1---; thamba=1; PRF=t=AAPL%2BSPY%2BGOOG",
        'referer': referer,
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    '''
    #r = requests.get(url, headers=headers, verify=True)
    #pd1 = pd.read_csv(io.StringIO(r.text), index_col=0, parse_dates=True, encoding="utf-8", error_bad_lines=False)
    #return pd1

#使用AAPL测试
now = datetime.strptime('2022-05-30', '%Y-%m-%d')
print(int(now.timestamp()))
startv = "2022-01-03"
endv = str(datetime.now().strftime("%Y-%m-%d"))
print(endv)
pull_stock("AAPL", start=startv, end=endv, interval="1d")
