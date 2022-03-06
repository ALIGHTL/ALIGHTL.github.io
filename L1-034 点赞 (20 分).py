a={}
b=int(input())
max=0
max1=0
for i in range(b):
    c=list(input().split())
    for j in range(1,len(c)):
        if c[j] not in a.keys():
            a[c[j]]=1
        if c[j] in a.keys():
            a[c[j]]+=1
for i in a.keys():
    if a[i]>max:
        max=a[i]
for i in a.keys():
    if a[i]==max:
        d=int(i)
        if d>max1:
            max1=d
print(max1,max-1)
