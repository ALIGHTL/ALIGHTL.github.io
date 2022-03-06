a=int(input())
b=list(input().split())
d=[]
e=[]
f=1
g=0
for i in b:
    c=i.split('/')
    d.append(int(c[0]))
    e.append(int(c[1]))
for i in e:
    f*=i
for i in range(len(d)):
    g+=(f/e[i])*d[i]
if g<f and g%f!=0 and g>0:
    for i in range(int(g),1,-1):
        if g%i==0 and f%i==0:
            g=g/i
            f=f/i
    print(int(g),int(f),sep='/')
if g%f==0:
    print(int(g/f))
if g>f and g%f!=0 and g>0:
    h = g // f
    g = g - h * f
    for i in range(int(g),1,-1):
        if g%i==0 and f%i==0:
            g=g/i
            f=f/i
    print(int(h),int(g),end='/')
    print(int(f))
if g<0:
    g=-1*g
    if g<f and g%f!=0 and g>0:
        for i in range(int(g),1,-1):
            if g%i==0 and f%i==0:
                g=g/i
                f=f/i
        print(int(-g),int(f),sep='/')
    if g>f and g%f!=0 and g>0:
        h = g // f
        g = g - h * f
        for i in range(int(g),1,-1):
            if g%i==0 and f%i==0:
                g=g/i
                f=f/i
        print(int(-h),int(-g),end='/')
        print(int(f))
