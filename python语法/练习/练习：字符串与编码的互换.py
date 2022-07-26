#凯撒密码
inp=input()
l=len(inp)#输出字符串长度
for i in range(l):
    if ord('A') <=ord(inp[i])<=ord('Z'):#将字符串转换为编码
        onew=ord('A')+((ord(inp[i])-ord('A'))+3)%26
    elif ord('a') <=ord(inp[i])<=ord('z'):
        onew=ord('a')+((ord(inp[i])-ord('a')) + 3 )%26
    else:
        onew=ord(inp[i])
    new=chr(onew)#将编码转换成字符串
    print(new,end='')
