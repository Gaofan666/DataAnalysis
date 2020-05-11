from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

n = 300
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

# 绘制三维点阵
plt.figure('3D Scatter', facecolor='lightgray')
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('X')  # 设置坐标轴文本
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
d = x ** 2 + y ** 2 + z ** 2
ax3d.scatter(x, y, z, s=50, marker='o', c=d, cmap='jet')
plt.show()
