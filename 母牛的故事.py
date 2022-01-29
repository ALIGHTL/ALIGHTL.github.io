n=int(input())
if n<=4:
    print(n)
if n>4:
    a=1
    b=2
    c=3
    d=4
    for i in range(n-4):
        t=b+d
        a=b
        b=c
        c=d
        d=t
    print(d)
