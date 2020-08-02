import numpy as np

t2 = np.array(range(24)).reshape(4,6)

t2[t2<10] = 3

t2 = t2.astype(float)
t2[3,3] = np.nan
t2[:,0] = 0

print(t2)
print('*'*100)
# 取不为0的元素的个数
# print(np.count_nonzero(t2))



# 数组里是 nan 的元素有哪些
# print(t2!=t2)
# print(np.isnan(t2))

# 取出数组元素里的的元素和他本身不同的个数 也就是取出 nan 元素有几个
# print(np.count_nonzero(t2!=t2))  #
# print(np.count_nonzero(np.isnan(t2)))

# 求和
# print(np.sum(t2)) # nan 类型和任何数求和都为 nan

t3 = np.arange(12).reshape(3,4)
# print(t3)
# print(np.sum(t3))

t4 = np.sum(t3,axis=0)  # 计算每一行对应列相加的结果 一维数组
# print(t4)
t5 = np.sum(t3,axis=1)  # 计算每一列对应行相加的结果  一维数组
# print(t5)
# 求中值
# print(np.median(t2,axis=0))  # 从列中求中值 一维数组
# print(np.max(t2))  # 取整个数组的最大值
# print(np.max(t2,axis=0))  # 求各个列的最大值  一维数组
#求极值:最大值与最小值的差
# print(np.ptp(t2))  # 取整个数组的极值
print(np.ptp(t2,axis=0))  # 在列方向上的极值

# 标准差 表示每个元素相对于平均值的离散程度,越离散越不稳定



