a,b=input().split()
a=int(a)
b=int(b)
if b==0:
    print("%d/0"%a,end='')
    print("=Error")
if b>0:
    c=a/b
    print(a,b,sep='/',end='')
    print("=%.2f"%c)
if b<0:
    c=a/b
    print("%d/"%a,end='')
    print("(%d)"%b,end='')
    print("=%.2f"%c)  
