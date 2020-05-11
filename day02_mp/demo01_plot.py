import numpy as np
import matplotlib.pyplot as mp

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([12, 13, 45, 85, 6, 2])

# 绘制水平线，垂直线
# 多条水平线，起始位置和终止位置也可以用数组
mp.hlines([10, 20, 30, 40], [1, 2, 3, 4], [3, 4, 5, 6])
mp.vlines(4, 10, 80)
"""
绘制水平线，先给Y坐标，然后x的起始值和终止值
绘制竖直线，先给x坐标，然后y的起始值和终止值
"""
mp.plot(x, y)
mp.show()
