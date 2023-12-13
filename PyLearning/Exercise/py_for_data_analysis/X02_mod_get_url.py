from datetime import datetime, date
import warnings

def get_url(ticker, start="20220101", end=datetime.now().strftime("%Y%m%d"), interval="1d"):
    """
        Get Yahoo Finance Daily Data from custom day to cusotm day.

        get_url(ticker, start="20220101", end=now, interval="1d")

        ticker: stock ticker, string
        start: start date, format yymmdd, 20220101 as default
        end: end date, format yymmdd, now as default
        interval: data interval, one day as default.
    """
    warnings.filterwarnings("ignore") # Suppress warnings.
    
    url = r"https://query1.finance.yahoo.com/v7/finance/download/" + str(ticker)
    x = int(datetime.strptime(start, '%Y%m%d').timestamp())
    y = int(datetime.strptime(end, '%Y%m%d').timestamp())
    url += "?period1=" + str(x) + "&period2=" + str(y) + "&interval=" + interval + "&events=history&includeAdjustedClose=true"
    
    print(f'{ticker}:\t{url}')

'''
now = datetime.strptime('20220530', '%Y%m%d')
print(int(now.timestamp()))
startv = "20220101"
endv = str(datetime.now().strftime("%Y%m%d"))
print(endv)
get_url("AAPL", start=startv, end=endv, interval="1d")
'''