import random
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# 设置字体法二
my_font = font_manager.FontProperties(fname="C:/WINDOWS/FONTS/MSYH.TTC")
y =[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

# 设置图形大小
plt.figure(figsize=(12,6),dpi=80)
# 绘图
plt.plot(x,y)

# 设置x轴刻度
_xtick_lables = ["{}岁".format(i) for i in x ]
plt.xticks(x,_xtick_lables,fontproperties=my_font)

# 设置图形信息 x,y轴,标题
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("人",fontproperties=my_font)
plt.title("年龄和谈恋爱的关系",fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.4)  # alpha=0.4 设置网格透明度

# 展示
plt.show()