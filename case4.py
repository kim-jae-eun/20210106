print("*입력한 숫자만큼 데코문자를 출력하는 프로그램입니다.*")
for z in range(3):
    deco = input("데코문자를 입력하세요 : ")
    number = int(input("출력횟수를 입력하세요 : "))
    for i in range(number) :
        print(deco, end="")
    print()
    aws=input("\n계속 수행할까요?(y/n) ")
    if aws=='n':
        break
print("\n*수행 종료됩니다.*")