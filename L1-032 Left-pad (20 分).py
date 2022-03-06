a,b=input().split()
a=int(a)
c=input()
if len(c)<=a:
    print(b*(a-len(c)),end='')
    print(c)
if len(c)>a:
    print(c[len(c)-a:len(c)])
