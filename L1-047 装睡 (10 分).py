n=int(input())
for i in range(n):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    d=0
    if b>20 or b<15:
        d=1
    if c>70 or c<50:
        d=1
    if d==1:
        print(a)
