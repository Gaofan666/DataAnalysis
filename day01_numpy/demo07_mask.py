"""
掩码
"""

import numpy as np

a = np.arange(100)

# 基于bool数组的掩码  可以选择显示的内容
# print(a[a%3==0])
mask = (a % 3 == 0) & (a % 7 == 0)
print(mask)
print(a[mask])

# 基于索引的掩码  可以排序
names = np.array(['Apple', 'Mate30 pro', 'MI', 'Oppo', 'Vivo'])
rank = [1, 0, 3, 4, 2]
print(names[rank])
