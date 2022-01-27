a={}
a['0']='ling'
a['1']='yi'
a['2']='er'
a['3']='san'
a['4']='si'
a['5']='wu'
a['6']='liu'
a['7']='qi'
a['8']='ba'
a['9']='jiu'
a['-']='fu'
b=[]
b=list(input())
for i in range(len(b)):
    print(a[b[i]],end='')
    if i!=len(b)-1:
        print(" ",end='')
print('')
