"""
测试mplot窗口
"""

import matplotlib.pyplot as mp

# 标题 和 窗体内部颜色   一个figure一个窗口
mp.figure('A Figure',facecolor='gray')
mp.plot([0,1],[1,2])
# mp.figure('B Figure',facecolor='lightgray')
# mp.plot([0,1],[1,2])

# 再次调用在A窗口编辑
mp.figure('A Figure',facecolor='gray')
mp.plot([1,2],[2,1])

# 设置窗口的参数
mp.title('A Figure',fontsize=18)
mp.xlabel('time',fontsize=14)
mp.ylabel('price',fontsize=14)
mp.tick_params(labelsize=10)  # 刻度字体的大小
mp.grid(linestyle=":")  # 设置图表网格线



mp.show()