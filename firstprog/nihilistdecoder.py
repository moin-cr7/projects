def decod(z):
    y=str(z)
    d=[ int(y[i:i+2]) for i in range(0, len(y), 2)]
    # print(d)
    for z in range(len(d)):
        c=(8*(int(d[z]/10)-1)+(int(d[z]%10)-1))
        return (int(c))

a=[]
for i in range(48,58):
    a.append(chr(i))
for i in range(65,91):
    a.append(chr(i))
for i in range(97,123):
    a.append(chr(i))
a.append(chr(32))
a.append(chr(44))
k='32616172558731555865726368556655'
y=str(k)
d=[int(k[i:i+2]) for i in range(0, len(y), 2)]
# decod(k)
for _ in d:
    print(a[decod(_)],end='')

# b=37
# print(a[8*(int(b/10)-1)+(int(b%10)-1)])
