import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


# 直接读取该文件并且获取ndarray数组对象
# 返回值：
#     unpack=False：返回一个二维数组
#     unpack=True： 多个一维数组
# 日期转换函数
def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t


dates, opening_prices, highest_prices, lowest_prices, closeing_prices = np.loadtxt(
    './da_data/aapl.csv',  # 文件路径
    delimiter=',',  # 分隔符
    usecols=(1, 3, 4, 5, 6),  # 读取1、3两列 （下标从0开始）
    unpack=True,
    dtype='M8[D], f8, f8, f8, f8',  # 制定返回每一列数组中元素的类型
    converters={1: dmy2ymd})

# 绘制k线图，x为日期
mp.figure('APPL K', facecolor='lightgray')
mp.title('APPL K')
mp.xlabel('Day', fontsize=12)
mp.ylabel('Price', fontsize=12)

# 拿到坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())
mp.tick_params(labelsize=8)
dates = dates.astype(md.datetime.datetime)


mp.plot(dates, opening_prices, color='dodgerblue',
        linestyle='--')
mp.gcf().autofmt_xdate()
mp.show()
