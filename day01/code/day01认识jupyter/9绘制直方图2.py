

from matplotlib import pyplot as plt

from matplotlib import font_manager

interval = [0,5,10,15,20,25,30,35,40,45,60,90]  # x 轴位置
width = [5,5,5,5,5,5,5,5,5,15,30,60]  # 组距
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

print(len(interval),len(width),len(quantity))

#设置图形大小
plt.figure(figsize=(12,6),dpi=80)

plt.bar(range(len(quantity)),quantity,width=1)

# 设置x轴刻度
_x = [i-0.5 for i in range(len(quantity)+1)]

_xtick_labels = interval + [150]
plt.xticks(_x,_xtick_labels)

plt.grid()
plt.show()