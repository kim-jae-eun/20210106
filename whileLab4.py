x=int(input('1부터 12까지의 숫자 중 하나를 입력해주세요. '))
while 1<=x<=12:
    if x==12 or x==1 or x==2:
        print(str(x)+'월은 겨울')
    if 3<=x<=5:
        print(str(x)+'월은 봄')
    if 6<=x<=8:
        print(str(x)+'월은 여름')
    if 9<=x<=11:
        print(str(x)+'월은 가을')
    x = int(input('1부터 12까지의 숫자 중 하나를 입력해주세요. '))
print('1~12 사이의 값을 입력하세요!')