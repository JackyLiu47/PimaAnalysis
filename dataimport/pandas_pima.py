from pandas import read_csv
#使用pandas导入csv数据
filename='pima_data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
print(data.shape)