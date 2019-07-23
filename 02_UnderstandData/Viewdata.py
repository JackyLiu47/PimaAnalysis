from pandas import read_csv
#显示前10行数据
filename = 'pima_data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename,names=names)
peek = data.head(10)
print(data.shape)
#数据维度
print(peek)
#数据概览（前十行）
print(data.dtypes)
#数据属性和类型