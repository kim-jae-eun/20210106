import random
x=random.randint(0, 30)
i=0
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while 0<x<27:
    print(a[x-1]+'('+str(x)+')')
    x = random.randint(0, 30)
    i+=1
print('수행횟수는',i,'번입니다.')