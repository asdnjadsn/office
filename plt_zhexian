# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams.update({"font.size": 10})
names = [5, 10, 15, 18, 20]
x = range(len(names))
y = [57.25, 61.32, 63.29, 62.98, 62.54]
y1=[57.84, 63.24, 63.53, 63.53, 63.75]
y2=[57.59, 60.29, 64.86, 65.51, 65.54]
y3=[56.28, 59.76, 62.65, 64.82, 64.98]
y4=[56.08, 59.58, 62.25, 65.2, 65.04]

# plt.xlim(4, 22)  # 限定横轴的范围
plt.ylim(50, 68)  # 限定纵轴的范围
# print(x)
plt.plot(x, y, marker='^', mec='r', mfc='w',label=u'meta pairs=6')
plt.plot(x, y1, marker='^', ms=5,label=u'meta pairs=8')
plt.plot(x, y2, marker='^', ms=5,label=u'meta pairs=10')
plt.plot(x, y3, marker='^', ms=5,label=u'meta pairs=12')
plt.plot(x, y4, marker='^', ms=5,label=u'meta pairs=14')
plt.legend()  # 让图例生效
plt.xticks(x, names)
# plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"Epoch") #X轴标签
plt.ylabel("mIou") #Y轴标签
plt.title("Influence of the number of meta-pairs") #标题
# my_y_ticks = np.arange(50, 70, 2)
# plt.yticks(my_y_ticks)
# my_x_ticks = np.arange(4, 22, 2)
# plt.xticks(my_x_ticks)
# plt.grid(b="True",axis="y")
# plt.grid(b="True",axis="x")

plt.show()
