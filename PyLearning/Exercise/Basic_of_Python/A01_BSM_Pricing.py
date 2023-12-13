from statistics import NormalDist
import math
from scipy.stats import norm
import random

def DELTA(S, X, T, r, sigma, dividend):
    delta = N((math.log(S/X) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T)))
    return delta

def BS_CALL(S, X, T, r, sigma, dividend):
    d1 = (math.log(S/X) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call = S * N(d1) - X * math.exp(-r*T) * N(d2)
    return call

def BS_PUT(S, X, T, r, sigma, dividend):
    d1 = (math.log(S/X) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put = X * math.exp(-r*T)*N(-d2) - S * N(-d1)
    return put

N = norm.cdf

S = 49
X = 50
day = 140
R = 5
Sigma = 20
dividend = 0

hedge_range = 7
periods_number = int(day/hedge_range + 1)

T = day/365
r = R/100
sigma = Sigma/100
call = BS_CALL(S, X, T, r, sigma, dividend)
put = BS_PUT(S, X, T, r, sigma, dividend)
delta = DELTA(S, X, T, r, sigma, dividend)
stock = delta * 100000
print(f"看涨期权价格 = {call:.2f}, 看跌期权价格 = {put:.2f}\t, Delta = {delta:.3f}")

print("周次\t到期时长\t股价变化\t股价\tDelta\t购买股票数量\t成本（千元)\t累计成本（千元）\t利息（千元）")
print(f"0\t{day}\t\t{0}\t\t{S:.2f}\t{delta:.3f}\t")
for i in range(1, periods_number):
    T = (day - i*hedge_range)/365
    days_left = day - i*hedge_range
    r = R/100
    sigma = Sigma/100
    delta_S = r*S*(hedge_range/365) + sigma*random.normalvariate(0,1)*S*math.sqrt(hedge_range/365)
    S = S + delta_S
    if T!=0:
        delta = DELTA(S, X, T, r, sigma, dividend)
    else:
        delta = 1
    
    print(f"{i}\t{days_left}\t\t{delta_S:.2f}\t\t{S:.2f}\t{delta:.3f}\t")