from __future__ import unicode_literals

import numpy as np

"""
数组水平竖直深度方向操作
"""
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a)
print(b)

# 水平方向操作
c = np.hstack((a, b))
print(c, '->c')
a, b = np.hsplit(c, 2)
print(a)
print(b)

# 垂直方向操作
c = np.vstack((a, b))
print(c, '->c')
a, b = np.vsplit(c, 2)
print(a, '->a')
print(b, '->b')

# 深度方向操作
c = np.dstack((a, b))
print(c, '->c')
a, b = np.dsplit(c, 2)
print(a, '->da')
print(b, '->db')

# concatenate方法与split方法 0竖直  1水平  2深度方向
c = np.concatenate((a, b), axis=0)  # 竖直方向合并   axis:轴线
d = np.split(c, 2, axis=0)  # 竖直方向拆分为2个

# 一维数组的组合方案 row_stack   column_stack
a = np.arange(1, 9)
b = np.arange(9, 17)
print(a)
print(b)
print(np.row_stack((a, b)))  # 形成两行
print(np.column_stack((a, b)))  # 形成两列
