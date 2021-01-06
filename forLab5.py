sum=0
for i in range(1,51):
    if i%3==0 and not i%5==0:
        sum+=i
print('결과 =',sum)