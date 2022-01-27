a,b=input().split()
a=int(a)
b=int(b)
n=0
sum=0
for i in range(a,b+1):
    print("%5d"%i,end='')
    n+=1
    sum+=i
    if n%5==0:
        print('')
if n%5!=0:
    print('')
print("Sum = %d"%sum)
