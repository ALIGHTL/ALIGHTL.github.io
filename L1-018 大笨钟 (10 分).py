c,d=input().split(':')
a=int(c)
b=int(d)
e='Dang'
if a>12:
    if b!=0:
        print(e*(a-11))
    if b==0:
        print(e*(a-12))
if a==12:
    if b==0:
        print("Only 12:00.  Too early to Dang.")
    if b!=0:
        print(e*13)
if a<12:
    print("Only ",end='')
    print(c,d,sep=':',end='')
    print(".  Too early to Dang.")
