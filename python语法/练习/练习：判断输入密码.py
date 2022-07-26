count = 3
while count>0:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count -= 1
        if count == 1 or count == 2:
            print("请重新输入")
        elif count == 0:
            print("3次用户名或者密码均有误！退出程序。")
