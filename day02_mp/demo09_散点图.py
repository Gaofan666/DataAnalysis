import matplotlib.pyplot as mp
import numpy as np

# 172期望值   10标准差   n数字生成数量
n = 300
height = np.random.normal(175, 5, n)
weight = np.random.normal(70, 7, n)

mp.figure('Persons', facecolor='lightgray')  # 设置窗口标题
mp.title('Persons', fontsize=18)  # 设置图像标题
mp.xlabel('height', fontsize=14)
mp.ylabel('weight', fontsize=14)
mp.grid(linestyle=":")  # 绘制网格线
d = (height - 175) ** 2 + (weight - 70) ** 2
# cmap颜色映射  jet:数越大颜色越深  以c作为参数，取cmap作颜色映射
mp.scatter(height, weight, marker='o', s=50,
           label='persons', c=d, cmap='hsv')  # c=d判断的是找出特殊点???
# 去掉了color=dodgerblue  怎么确定渐变的颜色的???????  ↑---->jet渐变决定的
mp.legend()
mp.show()
