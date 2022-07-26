def judge(m):#判断素数
    for i in range(2,m):
        if m % i == 0:
            return False
    return True
count=5
n=eval(input())
while count>0:#输出五个质数
    if judge(n):
        if count > 1:
            print(n, end=",")
        else:
            print(n, end="")
        count-=1
    n+=1
