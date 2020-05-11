import matplotlib.pyplot as mp


locators=['mp.NullLocator()','mp.MaxNLocator(nbins=4)',
          'mp.FixedLocator([3,6,9])','mp.AutoLocator()']

mp.figure('locators', facecolor='lightgray')

for i,locator in enumerate(locators):  # 拿到下标和元素
    mp.subplot(len(locators),1,i+1)  # 绘制子图 4行1列 内容：i+1
    mp.xlim(1, 10)  # 设置x轴的可视区间
    # 整理坐标轴
    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0.5))
    mp.yticks([])
    loc = eval(locator)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.show()
