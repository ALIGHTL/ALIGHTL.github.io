n=int(input())
d=[]
e=[]
for i in range(n):
    a,b,c=input().split()
    d.append(a+' '+c)
    b=int(b)
    e.append(b)
m=int(input())
f=list(map(int,input().split()))
for i in f:
    for j in range(len(e)):
        if e[j]==i:
            print(d[j])
