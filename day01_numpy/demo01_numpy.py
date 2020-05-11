"""demo01_numpy.py  测试numpy"""

import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))
print(ary.shape)  # 输出当前ndarry对象的数组维度
ary.shape = (2, 3)  # 维度改为两行三列
print(ary, ary.shape)
ary.shape = (6,)  # 变成一维

print('*' * 30)
# 数组的运算
print(ary)
print(ary * 3)
# 数组中的每个数都和3做比较
print(ary > 3)
# 数组相加
print(ary + ary)
