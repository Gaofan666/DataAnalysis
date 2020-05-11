from __future__ import unicode_literals
import numpy as np

a = np.array([[1 + 1j], [2 + 4j], [3 + 7j],
              [4 + 2j], [5 + 5j], [6 + 8j],
              [7 + 3j], [8 + 6j], [9 + 9j]])
print('a.shape-->', a.shape)
print('a.dtype-->', a.dtype)  # 元素类型
print('a.itemsize-->', a.itemsize) # 元素字节数
print('a.size:', a.size) # 元素数量
print('a.nbytes:', a.nbytes)  # 总字节数
print('实部:', a.real)  # 复数的实部
print('虚部:', a.imag)  # 复数的虚部 imagine
print('a.T:', a.T)  # 数组对象的转置视图
print([x for x in a.flat]) # 扁平迭代器
