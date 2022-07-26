#使用time库
import time as t
p=t.gmtime()
print(t.strftime("%Y-%m-%d %H:%M:%S".format(p)))#获取当前时间
s=t.perf_counter()#获取开始时间
scale=20
print("start".center(50,'-'))
for i in range (scale+1):
    a=(i/scale)*100
    b='*'*i
    c='-'*(scale-i)
    e=t.perf_counter()#获取结束时间
    print("\r{}% [{}{}]{:.2f}s".format(a,b,c,e-s),end="")
    t.sleep(0.1)
print("end".center(50,'-'))
