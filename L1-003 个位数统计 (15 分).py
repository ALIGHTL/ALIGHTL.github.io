x=input()
y={}
for i in range(len(x)):
    y[x[i]]=0
for i in range(len(x)):
    y[x[i]]+=1
a=[]
a=list(y.keys())
a.sort()
for i in range(len(a)):
    print(a[i],y[a[i]],sep=':')
