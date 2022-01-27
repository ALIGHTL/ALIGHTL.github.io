a,b=input().split()
a=int(a)
if a%2==0:
    m=a//2
if a%2==1:
    m=a//2+1
for i in range(m):
    print(b*a)
