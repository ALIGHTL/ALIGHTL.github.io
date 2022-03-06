n=int(input())
a=list(map(int,input().split()))
x=0
y=0
for i in a:
    if i%2==0:
        x+=1
    if i%2!=0:
        y+=1
print(y,x)
