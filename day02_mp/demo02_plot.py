from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

# 线性拆分50个点   拆分的点越多，曲线越平滑
x = np.linspace(-np.pi, np.pi, 50)
y = np.linspace(-3, 3, 50)
# print(x,x.shape)
sinx = np.sin(x)
cosx = np.cos(x) / 2
tanx = np.tan(x) / 8

# 设置坐标轴的范围  可视区间
# mp.xlim(0,np.pi)
# mp.ylim(0,2)

"""
修改x轴的刻度文本  val是坐标轴上的位置点，text为每个点对应的名称
如果不设置对应文本的话，坐标轴显示数字：-3.14，，，，
texts = ['Π', '-Π/2', '0', 'Π/2', 'Π']
"""
vals = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
texts = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$']
mp.xticks(vals, texts)  # x轴的刻度文本
mp.yticks([-4.0, -3.0, -2.0, -1.0, -0.5, 0, 0.5, 1.0, 2.0, 3.0, 4.0])  # y轴的刻度文本

# 修改坐标轴
ax = mp.gca()  # 获取当前坐标轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

mp.plot(x, sinx, linestyle=':', linewidth=2, color='red', alpha=0.5
        , label=r'$y=sin(x)$')
mp.plot(x, cosx, '-.', linestyle='-.', linewidth=1, color='blue'
        , label=r'$y=\frac{1}{2}cos(x)$')
# mp.plot(x, tanx, '--', linestyle='--', linewidth=0.5, color='green', alpha=0.9)
# mp.plot(x, y, linestyle='-', linewidth=0.3, color='grey', alpha=1)

# 绘制特殊点
pointx = [np.pi / 2, np.pi / 2]  # 点的横坐标
pointy = [1, 0]  # 点的纵坐标
mp.scatter(pointx, pointy, marker='o', s=70, color='red', label='smaple points')

# 在图表中为某个点添加备注，包含备注文本，备注箭头
mp.annotate(
    r'$[\frac{\pi}{2},1]$',  # 备注中显示的文本内容
    xycoords='data',  # 备注目标点所使用的坐标系
    xy=(np.pi / 2, 1),  # 备注目标点的坐标
    textcoords='offset points',  # 备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(50, 30),  # 备注文本的坐标
    fontsize=14,  # 备注文本的字体大小
    arrowprops=dict(
        arrowstyle='fancy',
        connectionstyle='angle3')  # 使用字典定义文本指向目标箭头的样式,bar是桥直线
)

mp.legend()  # 显示图例
mp.show()
