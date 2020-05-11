"""
属性测试
"""

import numpy as np

a = np.arange(1, 9)
print(a, a.shape)
a.shape = (2, 4)
print(a, a.shape)
# 数据类型基本操作
print(a.dtype)
# a.dtype='float32'  #错误的修改数据类型的方式
# print(a,a.dtype)

b = a.astype('float32')
print(b, b.dtype)

# size属性
print(b, 'size:', b.size)

c = np.arange(1, 19)
c.shape = (3, 2, 3)  # 3页 2行 3列
print(c)
print(c[0, 1, 0])  # 取第一页第二行第一列

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i, j, k], end=' ')
