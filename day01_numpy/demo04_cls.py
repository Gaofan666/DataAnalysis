"""
demo04_cls.py  数据类型
"""

import numpy as np

data = [('张三', [80, 50, 60], 19),
        ('李四', [63, 52, 14], 20),
        ('王五', [88, 77, 99], 18)]

# 第一种设置dtype的方式
# U2:unicode字符出现两个，3个int32的字符 1个int32的字符
a = np.array(data, dtype='U2,3int32,int32')
print(a)
# print(a[0][1])
for i in range(a.shape[0]):
    print(a[i][1][1])


# 第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str', 2),
                          ('scores', 'int32', 3),
                          ('age', 'int32', 1)])
print(b[0]['name'], ':', b[0]['scores'])
print('=================================================')

# 第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ':', c.itemsize)  # 元素字节数
print('====================================================')


# 第四种


print('******************************************************')
# 测试数组中存储日期数据类型
dates = ['2011-01-01', '2011', '2011-02', '2012-01-01', '2012-02-01 10:10:00']
dates = np.array(dates)
dates = dates.astype('M8[D]')
print(dates, dates.dtype)
print(dates[2] - dates[1])  # 根据M8的类型返回差值类型天数或秒
