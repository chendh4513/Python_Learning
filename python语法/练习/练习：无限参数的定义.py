def cmul(a, *b):#*b为a以外的所有参数
    m = a
    for i in b:
        m *= i
    return m

print(eval("cmul({})".format(input())))
