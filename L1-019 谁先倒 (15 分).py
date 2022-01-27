a,b=map(int,input().split())
c=int(input())
x=0
y=0
for i in range(c):
    d,e,f,g=map(int,input().split())
    if d+f==e and e!=g:
        x+=1
    if d+f==g and e!=g:
        y+=1
    if x>a:
        print("A")
        print(y)
        break
    if y>b:
        print("B")
        print(x)
        break
