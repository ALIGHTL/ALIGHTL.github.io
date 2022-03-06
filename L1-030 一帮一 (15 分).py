a=int(input())
d=[]
e=[]
j0=a-1
j1=a-1
for i in range(a):
    b,c=input().split()
    d.append(int(b))
    e.append(c)
for i in range (a//2):
    print(e[i],end=' ')
    if d[i]==0:
        for j in range(j0,a//2-1,-1):
            if d[j]==1:
                print(e[j])
                j0=j-1
                break
    if d[i]==1:
        for j in range(j1,a//2-1,-1):
            if d[j]==0:
                print(e[j])
                j1=j-1
                break
