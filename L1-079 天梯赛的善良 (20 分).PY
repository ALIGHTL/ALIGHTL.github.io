a=int(input())
b=list(map(int,input().split()))
b.sort()
c=0
d=0
for i in range(a):
    if b[i]==b[0]:
        c+=1
    if b[i]==b[a-1]:
        d+=1
print(b[0],c)
print(b[a-1],d,end='')
