import numpy as np
import matplotlib.pyplot as mp

n = 100
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# 上述代码得到二维数组x,y直接组成坐标点矩阵
# z为通过每个坐标的x与y计算得到的高度值，模拟采集的海拔高度

# 画图
mp.figure('Counter', facecolor='lightgray')
mp.title('Counter', fontsize=16)
mp.axis('equal')
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, 8, colors='black', linewidths=0.5)
mp.clabel(cntr, fmt='%.2f', inline_spacing=2, fontsize=8)  # 添加文本
mp.contourf(x, y, z, 8, cmap='jet')  # 添加颜色映射
mp.show()
