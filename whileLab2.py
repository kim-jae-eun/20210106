import random
pairNum1 = random.randint(1, 6)
pairNum2 = random.randint(1, 6)
while pairNum1!=pairNum2:
    if pairNum1>pairNum2:
        print(pairNum1,'이',pairNum2,'보다 크다.')
    else:
        print(pairNum1,'이',pairNum2,'보다 작다.')
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
print(pairNum1,'=',pairNum2,', 게임 끝')