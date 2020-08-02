import random
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# 设置字体法二
my_font = font_manager.FontProperties(fname="C:/WINDOWS/FONTS/MSYH.TTC")

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

# 设置图形大小
plt.figure(figsize=(12,6),dpi=80)
# 绘图
plt.plot(x,y_1,label="自己",color="yellow",linestyle=":")  #  绘制出的折线说明:label=; color 折线的颜色
plt.plot(x,y_2,label="同桌",color="cyan",linestyle="-.")   # 折线的样式linestyle=


# 设置x轴刻度
_xtick_lables = ["{}岁".format(i) for i in x ]
plt.xticks(x,_xtick_lables,fontproperties=my_font)

# 设置图形信息 x,y轴,标题
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("人",fontproperties=my_font)
plt.title("年龄和谈恋爱的关系",fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.9,linestyle=":")  # alpha=0.4 设置网格透明度;linestyle= 给网格设置线的样式

# 设置水印
plt.text(x=15,               # 水印开头左下角对应的X点
         y=2,               # 水印开头左下角对应的Y点
         s="DujiaShuiyin",    # 水印文本
         fontsize=50,       # 水印大小
         color="gray",      # 水印颜色
         alpha=0.5,
         )

# 添加图形
plt.legend(prop=my_font,loc="upper left")   # 用来展示plt.plot(x,y_1,label="自己") 添加的label; prop=my_font 让折线说明展示中文;loc="" 显示折线说明信息的位置

# 展示
plt.show()