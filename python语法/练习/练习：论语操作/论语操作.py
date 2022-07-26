f=open("论语-网络版.txt",mode='r',encoding='utf-8')
ls=f.readlines()
text=[]
n=['1','2','3','4','5','6','7','8','9','0']
with open("论语-提取版.txt",mode='wt',encoding='utf-8')  as f1:
    for i in range(len(ls)):
        if ls[i]=="  【原文】\n":
            str1=ls[i+2]
            str1=str1[5:].replace("\n","")
            if str1[0] in n:
                str1=str1[1:]
            f1.write(str1)
    f1.close()
f.close()
f2=open("论语-提取版.txt",mode='r',encoding='utf-8')
str2=f2.read()
str2=str2.replace("(","")
str2=str2.replace(")","")
with open("论语-原文.txt",mode='wt',encoding='utf-8')  as f3:
    for i in range(9):
        m=str(i+1)
        str2=str2.replace(m,"")
    f3.write(str2)
    f3.close()
f2.close()
        
    



