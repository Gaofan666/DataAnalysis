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

# 评估波动性
min_val = np.min(lowest_prices)
max_val = np.max(highest_prices)
print(min_val, '-', max_val)

# 最高价与最低价的日期,arg+..  相当于获取一个点对象
min_ind = np.argmin(lowest_prices)
max_ind = np.argmax(highest_prices)
print('min:', dates[min_ind])
print(('max:', dates[max_ind]))

# maximum  minimum
a=np.arange(1,10).reshape(3,3)
b=np.arange(1,10)[::-1].reshape(3,3)
print(a,b)
print(np.maximum(a,b))  # 相比较保留较大的数
print(np.minimum(a,b))

