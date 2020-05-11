"""
自由布局   用的不多
"""

import matplotlib.pyplot as mp

mp.figure('自由布局', facecolor='lightgray')
mp.axes([0.03, 0.55, 0.94, 0.4])   # 距离左边的距离，距离右边的距离，宽，高
mp.text(0.5, 0.5, '1', ha='center', va='center')

mp.axes([0.03, 0.05, 0.94, 0.4])   # 距离左边的距离，距离右边的距离，宽，高
mp.text(0.5, 0.5, '2', ha='center', va='center')
mp.show()
