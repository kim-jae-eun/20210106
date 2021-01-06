print("*입력한 숫자만큼 데코문자를 출력하는 프로그램입니다.*")
while True:
    deco = input("데코문자를 입력하세요 : ")
    number = int(input("출력횟수를 입력하세요 : "))
    if len(deco)==0:
        break
    if number==0:
        break
    for i in range(number) :
        print(deco, end="")
    print()
print("\n*수행 종료됩니다.*")