a=input()
n=0
if a[0] is '-':
    for i in a:
        if i is'2':
            n+=1
    if a[len(a)-1] in '02468':
        m=n/(len(a)-1)*1.5*2*100
    else:
        m=n/(len(a)-1)*1.5*100
if a[0] is not '-':
    for i in a:
        if i is '2':
            n+=1
    if a[len(a)-1] in '02468':
        m=n/len(a)*100*2
    else:
        m=n/len(a)*100
print("%.2f"%m,end='')
print("%")
