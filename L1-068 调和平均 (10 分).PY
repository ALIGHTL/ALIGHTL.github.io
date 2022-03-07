a=int(input())
c=0
b=list(map(float,input().split()))
for i in range(a):
    c+=(1/b[i])
c=c/a
print("%.2f"%(1/c))
