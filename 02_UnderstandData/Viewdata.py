from pandas import read_csv
from pandas import set_option

#显示前10行数据
filename = 'pima_data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename,names=names)
peek = data.head(10)

print(data.shape)#数据维度
print(peek)#数据概览（前十行）
print(data.dtypes)#数据属性和类型

#描述性统计
set_option('display.width', 100)
set_option('precision', 4)
print(data.describe())

#数组分组分布
print(data.groupby('class').size())

#数据相关性（皮尔逊相关系数）
set_option('precision',2)#重设数据精确度
print(data.corr(method='pearson'))

#高斯分布偏离系数
print(data.skew())