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

# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
# 设置刻度定位器
import matplotlib.dates as md

ax = mp.gca()
# 每周一为主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# 每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度文本格式
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
        label='Closing Price', linewidth=2, linestyle='--')

# 中位数
median = np.median(closing_prices)
mp.hlines(median, dates[0], dates[-1], color='violet', label='median')

# 自己算
sorted_prices = np.msort(closing_prices)
size = sorted_prices.size
m = ((sorted_prices[int((size - 1) / 2)]) + (sorted_prices[int(size / 2)])) / 2
print(median,'-',m)  # 比较自己算和系统算

median_val = np.argmin(closing_prices)
print(closing_prices[median_val])
print(dates[median_val])

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
