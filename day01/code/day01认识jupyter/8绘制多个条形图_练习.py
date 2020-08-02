from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:/WINDOWS/FONTS/MSYH.TTC")
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]


# 设置图形大小
plt.figure(figsize=(12,6),dpi=80)

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]


plt.bar(x_14,b_14,width=bar_width,label="9月14日")  # label是设置图例(每条线对应每一天)
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

#设置图例
plt.legend(prop=my_font)

# x轴刻度 对应
plt.xticks(x_15,a,fontproperties=my_font)

plt.show()

