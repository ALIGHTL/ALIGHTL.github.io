a=int(input())
b=0
while True:
    c=input()
    b+=1
    if b%(a+1)==0:
        if c=='Bu':
            print('Bu')
        if c=='ChuiZi':
            print('ChuiZi')
        if c=='JianDao':
            print('JianDao')
    if b%(a+1)!=0:
        if c=='Bu':
            print('JianDao')
        if c=='ChuiZi':
            print('Bu')
        if c=='JianDao':
            print('ChuiZi')
    if c=='End':
        break
