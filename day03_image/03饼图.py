import matplotlib.pyplot as mp
import numpy as np

# 整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']

mp.figure('Pie Chart')
mp.axis('equal')  # 设置x与y等比例输出
mp.pie(values, spaces, labels, colors, '%.1f%%', shadow=True)
mp.title('Pie Chart')
mp.legend()
mp.show()
