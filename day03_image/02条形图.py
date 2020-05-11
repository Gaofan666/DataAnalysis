import numpy as np
import matplotlib.pyplot as mp

apples = np.array([21, 65, 16, 51, 89, 87, 56, 12, 56, 53, 21, 51])
oranges = np.array([16, 51, 32, 59, 12, 65, 43, 21, 21, 65, 43, 21])

# 绘制柱状图
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.grid(linestyle=':')
x = np.arange(apples.size)
# 0.4是柱子的宽度，10是柱子距离底边的距离
mp.bar(x - 0.2, apples, 0.4, 10, color='limegreen', label='Apples')
# align=center是为了刻度对齐柱子中间，有些版本对其在柱子边上
mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges', align='center')

# 设置刻度
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
