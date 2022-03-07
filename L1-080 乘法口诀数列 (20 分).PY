a,b,c=map(int,input().split())
d=[]
d.append(a)
d.append(b)
for i in range(2,c):
    if a*b//10==0:
        d.append(a*b)
    if a*b//10>0:
        d.append(a*b//10)
        d.append(a*b%10)
    b=d[i]
    a=d[i-1]
for i in range(c-1):
    print(d[i],end=' ')
print(d[c-1],end='')
