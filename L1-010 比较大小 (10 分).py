a=[]
a=list(map(int,input().split()))
for i  in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            m=a[j]
            a[j]=a[j+1]
            a[j+1]=m
print(a[0],a[1],a[2],sep='->')
