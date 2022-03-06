a=int(input())
b=input()
n=len(b)%a
m=len(b)//a
for i in range(n):
    for j in range(m+1):
        print(b[len(b)-n-j*a+i],end='')
    print('')
for i in range(1,a-n+1):
    print(' ',end='')
    for j in range(m):
        print(b[len(b)-a-1-j*a+i],end='')
    print('')
