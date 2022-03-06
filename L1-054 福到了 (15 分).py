a,b=input().split()
b=int(b)
c=[]
d=0
for i in range(b):
    c.append(input().replace('@',a))
for i in range(b//2):
    if c[i]!=c[b-1-i]:
        d=1
if d==1:
    for i in range(b):
        for j in range(len(c[b-1-i])):
            print(c[b-1-i][len(c[b-1-i])-j-1],end='')
        print('')
if d==0:
    print('bu yong dao le')
    for i in range(b):
        for j in range(len(c[b-1-i])):
            print(c[b-1-i][len(c[b-1-i])-j-1],end='')
        print('')
