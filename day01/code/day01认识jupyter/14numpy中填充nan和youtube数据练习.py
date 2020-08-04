import numpy as np


''' 该函数是把nan的元素替换为对应列的均值 '''
def fill_ndarray(t1):
    # 遍历列  # t1.shape[1] 取列的个数
    for i in range(t1.shape[1]):
        temp_col = t1[:,i] # 取当前列的元素列表
        nan_num = np.count_nonzero(temp_col != temp_col) # 统计不等于0的个数

        if nan_num !=0:
            temp_not_nan_col = temp_col[temp_col==temp_col]   # 取出去掉nan后剩下元素组成的数组
            res = temp_not_nan_col.mean()   # 取带有nan的数组里,不为nan的元素的平均值
            # temp_col[np.isnan(temp_col)]  # 取数组里带有nan的元素
            temp_col[temp_col != temp_col] = res  # 取当前数组里有nan的地方替换为 res
    return t1

if __name__ == '__main__':
    t1 = np.arange(24).reshape((4, 6)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    res = fill_ndarray(t1)
    print(res)