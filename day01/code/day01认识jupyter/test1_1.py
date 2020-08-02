from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
print(min(y),max(y))
#设置图片大小,清晰度
plt.figure(figsize=(16,8),dpi=80)  # figsize=(图形的宽,高),dpi 代表每英寸点的个数. dpi可以设置图片清晰度
 # 绘图
plt.plot(x,y)

# 设置x轴 的 刻度
_xtic_labels = [i/2 for i in range(4,49)]

# 绘制x轴的刻度(绘制自己想定义的轴) xticks()中传递哪些参数,绘制出来的图形x轴就会出现哪些参数
plt.xticks(_xtic_labels[::2])
# 绘制x轴的刻度(绘制自己想定义的轴)
plt.yticks(range(min(y),max(y)+1))
# 保存
# plt.savefig("./t1.png")

# 展示
plt.show()

