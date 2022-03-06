a=int(input())
x=[]
e=0
for i in range(a):
    c=list(input().split())
    for j in c:
        x.append(j)
d=int(input())
y=[]
z=[]
y=input().split()
for i in y:
    if i not in x:
        z.append(i)
        x.append(i)
        e=1
if e==1:
    for i in range(len(z)-1):
        print(z[i],end=' ')
    print(z[len(z)-1])
if e==0:
    print("No one is handsome")
