import matplotlib.pyplot as mp

mp.figure('Grid Line', facecolor='lightgray')
ax = mp.gca()  # 获取figure对象句柄

# 修改刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))

# 设置网格线样式
ax.grid(which='major', axis='both', color='orangered', linewidth=0.75) # 主刻度
ax.grid(which='minor', axis='both', color='orangered', linewidth=0.15) # 次刻度

# 绘制曲线
y = [1, 10, 100, 1000, 100, 10, 1]
# mp.semilogy() # 半对数坐标轴  semilogy可直接替换下面的plot
# 系统会自动匹配X轴坐标与Y轴坐标对应
mp.plot(y, 'o-', color='dodgerblue')  # o- 连点成线时显示出圆点
mp.show()
