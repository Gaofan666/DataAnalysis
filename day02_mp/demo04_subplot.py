"""
矩阵式布局
"""

import numpy as np
import matplotlib.pyplot as mp

mp.figure('Subplot', facecolor='lightgray')
for i in range(1, 10):
    mp.subplot(3, 3, i)
    mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.6)

    mp.xticks([])  # x,y刻度设置为空
    mp.yticks([])
    mp.tight_layout()  # 设置紧凑布局，把图表相关参数都显示在窗口中

mp.show()
