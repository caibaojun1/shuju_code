import numpy as np
from matplotlib import pyplot as plt

us_file_path = "../youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../youtube_video_data/GB_video_data_numbers.csv"
# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)  # delimiter 确定分割符号;dtype 指定加载出来数据类型
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")  # unpack 转置

"""选择喜欢数比500000小的,这样既筛选出了comment,也筛选出了like"""
t_uk = t_uk[t_uk[:,1]<=500000]

t_uk_comment = t_uk[:,-1]  # 评论数 # 最后一列
t_uk_like = t_uk[:,1]  # 喜欢数  # 第一列

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(t_uk_like,t_uk_comment)  # 散点图

plt.show()