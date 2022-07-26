#TempConvert.py 输入符号加数字且符号为2个字符
TempStr = input("请输入带有符号的温度值: ")
if TempStr[0:2] in ['FE', 'fe']:#索引以后判断是否在列表内
    C = (eval(TempStr[2:]) - 32)/1.8#切片，转换成数字，运算
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[0:2] in ['CE', 'ce']:
    F = 1.8*eval(TempStr[2:]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
