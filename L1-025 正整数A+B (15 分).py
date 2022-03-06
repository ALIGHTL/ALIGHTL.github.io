a=list(input().split())
c=1
d=1
for i in a[0]:
    if i not in '0123456789':
        c=0
        break
if c==1:
    if int(a[0])>1000 or int(a[0])<1:
        c=0
if c==1:
    print(a[0],end=' ')
if c==0:
    print('? ',end='')
print('+ ',end='')
if len(a)!=2:
    d=0
for i in a[1]:
    if i not in '0123456789':
        d=0
        break
if d==1:
    if int(a[1])>1000 or int(a[1])<1:
        d=0
if d==1:
    print(a[1],end='')
if d==0:
    print('?',end='')
print(' = ',end='')
if c==0 or d==0:
    print('?',end='')
else:
    print(int(a[0])+int(a[1]))
