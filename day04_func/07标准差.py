import numpy as np
import matplotlib.pyplot as mp
import datetime as dt


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t


dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes = \
    np.loadtxt('./da_data/aapl.csv',
               delimiter=',', usecols=(1, 3, 4, 5, 6, 7),
               unpack=True, dtype='M8[D],f8,f8,f8,f8,f8',
               converters={1: dmy2ymd})

# 计算标准差
std = np.std(closing_prices,ddof=1)  # ddof=1 样本标准差
print(std)
# 手动计算
mean = np.mean(closing_prices)
d = closing_prices - mean
v = np.mean(d ** 2)
print(np.sqrt(v))
