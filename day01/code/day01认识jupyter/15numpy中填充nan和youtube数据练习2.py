import numpy as np
from matplotlib import pyplot as plt
import  os
us_file_path = "../youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../youtube_video_data/GB_video_data_numbers.csv"
# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)  # delimiter 确定分割符号;dtype 指定加载出来数据类型
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")  # unpack 转置

# 取评论的数据
t_us_comments = t_us[:,-1]  # 取最后一列
print(t_us_comments)
# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

""" 首先需要知道整个数据最大值,和最小值,为了设置组距"""
""" 尝试着分为50组 """

d = 250
bin_nums = (t_us_comments.max()-t_us_comments.min())//d
# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)

plt.show()