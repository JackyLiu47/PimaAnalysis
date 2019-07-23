from csv import reader
import numpy as np
#使用标准python类库导入csv文件
filename='pima_data.csv'
with open(filename, 'rt') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x=list(readers)
    data=np.array(x).astype('float')
    print(data.shape)