x = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
y = ['1','0','X','9','8','7','6','5','4','3','2']
n = int(input())
m = 0
for i in range(n):
    num = str(input())
    if len(num)>18:
        print(num)
        m = 1
    else:
        a = num[:17]
        c = True
        b = 0
        for j in range(len(a)):
            try:
                b+=int(a[j])*x[j]
            except:
                c = False
                print(num)
                m = 1
                break
        if c:
            b = b%11
            if y[b]!=num[-1]:
                print(num)
                m = 1
if m==0:
    print('All passed')
