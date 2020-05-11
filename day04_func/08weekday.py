import numpy as np
import matplotlib.pyplot as mp
import datetime as dt


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.weekday()
    return t


wdays, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes = \
    np.loadtxt('./da_data/aapl.csv',
               delimiter=',', usecols=(1, 3, 4, 5, 6, 7),
               unpack=True, converters={1: dmy2ymd})

# 求每周n的收盘价的均值
ave_prices = np.zeros(5)
weekday = {0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五'}
for i in range(ave_prices.size):
    ave_prices[i] = np.mean(closing_prices[wdays == i])
    print(weekday[i], ave_prices)
