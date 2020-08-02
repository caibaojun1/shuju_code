import numpy as np
import  os
# print(os.getcwd()) #获取当前工作目录路径
# print(os.path.abspath('../youtube_video_data'))  # 获取当前工作目录路径
# print(os.listdir('../youtube_video_data'))  # 获取该目录下有哪些文件
us_file_path = "../youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../youtube_video_data/GB_video_data_numbers.csv"
# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)  # delimiter 确定分割符号;dtype 指定加载出来数据类型
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")  # unpack 转置
# print(t1)
print(t2)
print('*'*100)
# 取行
# print(t2[2])  # 去二维数组里的第三行

# 取连续多行
# print(t2[1:3])  # 取二维数组里第二行和第三行

# 取不连续多行,需要多套一个方括号 索引为二行 索引为八行 索引为10行;
# print(t2[[2,8,10]])

# 取行
# print(t2[1,:])
# print(t2[2:,:])
# print(t2[[2,10,3],:])

# 取列
# print(t2[:,0])  # 取第一列 把第一例的元素合成一个列表;
# print(t2[:,2:])  #取所有的行 列就取第三列以后的列

# 取不连续的多列
# print(t2[:,[1,3]])

# 取行和列,取第三行,第四列的值;
# a = t2[2,3]
# print(a)
# print(type(a))

# 取多行和多列,取第3行到第5行,第2列到第4列的结果
# print(t2[2:5,1:4])

# 取多个不相邻的点
c = t2[[0,2,2],[0,1,3]]  # 逗号前面一个中括号和后面一个中括号,前一个中括号里放行索引,后一个中括号放列索引;
# 选出来的结果是(0,0),(2,1),(2,3)
print(c)