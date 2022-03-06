a=int(input())
b=1
e=1
while True:
    if b%a==0:
        print(b//a,len(str(b)))
        break
    b=1+10*b
