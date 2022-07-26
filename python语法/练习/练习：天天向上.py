def dayUp(x):
    dayup=1
    for i in range(365):
        if i%7 in[0,6]:
            dayup=dayup*(1-0.01)#周末每天退步1%
        else:
            dayup=dayup*(1+x)#工作日每天进步x
    return dayup
df=0.01
while dayUp(df)<37.78:#37.78为每天进步1%,一年的总进步
    df=df+0.001
print("{:.4f}".format(df))
