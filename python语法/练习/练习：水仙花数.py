s=''
for t in range(100,1000):
    i=str(t)
    if eval(i[0])**3+eval(i[1])**3+eval(i[2])**3==eval(i):
        s=s+"{},".format(i)
print(s[:-1])
