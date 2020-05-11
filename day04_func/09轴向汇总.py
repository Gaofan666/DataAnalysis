import numpy as np

# 二维数组的轴向汇总
ary = np.arange(1, 37).reshape(6, 6)
print(ary)


def apply(data):
    return data.mean()

# 1是按行  0按列
r = np.apply_along_axis(apply, 1, ary)
print(r)
