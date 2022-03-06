n=int(input())
for i in range(n):
    a,b=input().split()
    b=float(b)
    if a is 'M':
        c=b/1.09
    if a is 'F':
        c=b*1.09
    print("%.2f"%c)
