"""切片操作"""
import numpy as np

# 二维数组切片
a = np.arange(1, 10)
a.resize(3, 3)
print(a)
# 取前两行的前两列
print(a[:2, :2])
# 1,3两行的所有列，2代表步长
print(a[::2, :])
# 取第一列
print(a[:, 0])

print('========================三维数组=======================')
b = np.arange(28)
b.resize(3, 3, 3)
print(b)
# 切出第一页
print(b[1, :, :])
# 切出所有页的1行
print(b[:, 1:2, :])
