import random
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager
# 设置字体法一
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font",**font)
# C:/WINDOWS/FONTS/MSYH>TTC

# 解决x轴中文不能识别问题
# 设置字体法二
my_font = font_manager.FontProperties(fname="C:/WINDOWS/FONTS/MSYH.TTC")


y = [random.randint(20,35) for i in range(120)]
x = range(0,120)
# list_x = [i*2 for i in range(0,60)]
# plt.xticks(list_x)
plt.figure(figsize=(12,6),dpi=80)  # 尺寸

# 绘图
plt.plot(x,y)
# 保存图片

#  调整x轴刻度  # 不想让他太密集可以转化成列表再去步长
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)  # rotation=90 旋转90度,让x轴的左边垂直显示

# 添加描述信息
plt.xlabel("时间",fontproperties=my_font)  # fontproperties=my_font  解决不识别中文问题
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("描述信息",fontproperties=my_font)

plt.show()