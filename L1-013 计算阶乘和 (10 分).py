x=int(input())
n=0
for i in range(1,x+1):
    m=1
    for j in range(1,i+1):
        m*=j
    n+=m
print(n)
