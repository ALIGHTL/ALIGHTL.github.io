b=[]
while True:
    a=input()
    if a=='.':
        break
    b.append(a)
if len(b)<14 and len(b)>=2:
    print(b[1],end='')
    print(" is the only one for you...")
if len(b)<2:
    print("Momo... No one is for you ...")
if len(b)>=14:
    print(b[1],end=' and ')
    print(b[13],end=' are inviting you to dinner...\n')
