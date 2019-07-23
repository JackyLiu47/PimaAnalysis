from numpy import loadtxt
#使用NumPy导入csv数据
filename='pima_data.csv'
with open(filename, 'rt') as raw_data:
    data=loadtxt(raw_data, delimiter=',')
    print(data.shape)