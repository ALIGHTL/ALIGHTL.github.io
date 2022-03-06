n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=(a-100)*1.8
    if c-b>=0:
        if (c-b)<0.1*c:
            print("You are wan mei!")
        if (c-b)>=0.1*c:
            print("You are tai shou le!") 
    if c-b<0:
        if (b-c)<0.1*c:
            print("You are wan mei!")
        if (b-c)>=0.1*c:
            print("You are tai pang le!") 
