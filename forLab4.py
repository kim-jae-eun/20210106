evenNum, oddNum = 0, 0
for x in range(1,101):
    if x%2==0:
        evenNum+=x
    else:
        oddNum+=x
print('1부터 100까지의 숫자들 중에서','\n''짝수의 합은',evenNum,'이고','\n''홀수의 합은',oddNum,'이다.')