import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

plt.figure('3D Surface', facecolor='lightgray')
ax3d = plt.gca(projection='3d')
# rstride 行跨距  cstride列跨距  贴图的大小，每多少个像素当成一个整体
ax3d.plot_wireframe(x, y, z, cstride=30, rstride=30, linewidth=1, color='dodgerblue')
plt.show()
