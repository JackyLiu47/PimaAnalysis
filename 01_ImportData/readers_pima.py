from csv import reader#使用标准python类库导入csv文件
import numpy as np#使用numpy导入csv文件
from pandas import read_csv#使用pandas导入csv文件

#标准类库
filename='pima_data.csv'
with open(filename, 'rt') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x=list(readers)
    data=np.array(x).astype('float')
    print('readdata:',data.shape)

#numpy
with open(filename, 'rt') as raw_data:
    data=np.loadtxt(raw_data, delimiter=',')
    print('numpydata:',data.shape)

#pandas
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
print('pandasdata:',data.shape)