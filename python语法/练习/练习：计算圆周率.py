from random import *
from time import *
N=100000000#投N个点
hit=0#圆内的数量
s=perf_counter()
for i in range(1,N+1):
    x=random()#随机生成点
    y=random()#随机生成点
    if (x**2+y**2)**0.5<=1:#判断是否在圆内
        hit+=1
pi=4*hit/N
e=perf_counter()
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(e - s))
