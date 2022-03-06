a=int(input())
d=0
e={}
f=[]
for i in range(a):
    b,c=input().split()
    c=int(c)
    e[c]=b
    d+=c
d=d//(2*a)
for i in e.keys():
    if i-d>0:
        f.append(i-d)
    if i-d<=0:
        f.append(d-i)
f.sort()
print("%d"%d,end=' ')
print(e[f[0]+d])
