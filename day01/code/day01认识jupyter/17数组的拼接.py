import numpy as np
list_1 = np.arange(12).reshape(2,6).astype('float')
list_2 = np.arange(12,24).reshape(2,6).astype('float')
# 竖直拼接
list_v = np.vstack((list_1,list_2))
print(list_v)
list_h = np.hstack((list_1,list_2))
print(list_h)