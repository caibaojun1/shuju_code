import numpy as np

t1 = np.array([1,2,3])
# print(t1)
# print(type(t1))  # numpy.ndarray

t2 = np.array(range(10))  # 生成数组
# print(t2)

t3 = np.arange(10)
print(t3)
print(type(t3))
print(t3.dtype)

# numpy中的数据类型
t4 = np.array(range(1,4),dtype="float64")
print(t4)
print(t4.dtype)
print('*'*90)

# numpy中的bool类型
t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype('int8')
print(t6)
print(t6.dtype)

# numpy中的小数
import random
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

t8 = np.round(t7,2)  # 取2位小数
print(t8)