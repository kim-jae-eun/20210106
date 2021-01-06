import random
x=random.randint(1, 10)
y=random.randint(30, 40)
sum=0
for z in range(x, y+1):
    if z%2==0:
        sum += z
print(x,'부터',y,'까지의 짝수의 합 :', sum)