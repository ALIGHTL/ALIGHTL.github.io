a,d=input().split()
d=int(d)
c=int(a)
c1=c
while True:
    b=[]
    if len(a)==1:
        a='000'+a
    if len(a)==2:
        a='00'+a
    if len(a)==3:
        a='0'+a
    for i in a:
        if i not in b:
            b.append(i)
    if len(b)==d:
        print(c1-c,a)
        break
    c1+=1
    a=str(c1)
