import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 3))

baseline = [46.36, 48.06, 48.33, 48.73]
remove_align = [42.86, 48.65, 47.84, 45.46]
best = [46.63, 48.95, 49.52, 49.87]
#x = ['REST','LAPT','AUTO']
x = np.arange(4) #总共有几组，就设置成几，我们这里有三组，所以设置为3
total_width, n = 0.8, 4    # 有多少个类型，只需更改n即可，比如这里我们对比了四个，那么就把n设成4
width = total_width / n
x = x - (total_width - width) / 2


plt.bar(x, baseline, color = "#A1A9D0",width=width,label='Baseline')
plt.bar(x + width, remove_align, color = "#F0988C",width=width,label='Remove Align')
plt.bar(x + 2 * width, best , color = "#96CCCB",width=width,label='Meta-Align')
# plt.xlabel("COCO-$20^i$ Split")
plt.ylabel("mIou")
plt.legend(loc = "best")
plt.xticks([0,1,2,3],['split-0','split-1','split-2','split-3'])
my_y_ticks = np.arange(0, 80, 10)
plt.ylim((0, 80))
plt.yticks(my_y_ticks)
plt.grid(axis='y')
plt.show()
