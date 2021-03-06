## 반복문

### for 반복문

> 컬렉션의 요소를 순서대로 반복하면서 루프의 명령을 실행하는 반복문

```python
sum=0
for i in range(1,51):
    if i%3==0:
        if i%5==0:
            continue
        sum+=i
print('결과 =',sum)

# --> 출력결과는 `결과 = 318` 이다.
```

for 의 뒤에는 제어변수 in 컬렉션 이 들어온다. 제어변수에는 원하는 변수의 이름을, 컬렉션에는 요소들의 집합을 넣는다.

예시)

- [1, 3, 4, 10]
- range([start number],[stop number],[step])

특별한 범위 없이 10번 수행하고자 한다면

`for x in range(10):`

이라고 쓰면 된다. 이 경우 10은 stop number의 기능을 하며, 0부터 9까지 1씩 증가하는 (1, 2, 3, ..., 9) 의 목록을 갖는다.

만약 1부터 10까지 반복하고자 한다면

`for x in range(1,11):`

이라고 쓰면 된다. stop number는 포함되지 않으므로, 원하는 마지막 수보다 +1한 값을 넣는다.

만약 역순으로 10부터 1까지 반복하고자 한다면

`for x in range(10,0,-1):`

과 같이, 마지막에 -1을 입력하여 1씩 감소하는 순서임을 입력시킨다. 다만 여기서 stop number는 1이 아닌 0이 되는데, 역순인 경우 원하는 마지막 수보다 -1한 값을 넣어주어야 한다.

#### continue

> 이번 루프 하나만 건너뛰고 다시 돌아가서 수행하게 하는 명령어

#### break

> 반복을 즉시 끝내게 하는 명령어



### while 반복문

> 특정한 조건을 만족하는 동안 계속해서 실행하도록 명령하는 반복문

``` python
while True:
    word = input('단어를 입력해주세요: ')
    wordlength = len(word)
    if wordlength==0:
        break
    elif 5<=wordlength<=8:
        continue
    elif wordlength<5:
        result='*'+word+'*'
    else:
        result='$'+word+'$'
    print('유효한 입력 결과 :',result)
   
# 실행 결과
#    단어를 입력해주세요: 안
#    유효한 입력 결과 : *안*
#    단어를 입력해주세요: 안녕
#    유효한 입력 결과 : *안녕*
#    단어를 입력해주세요: 안녕하
#    유효한 입력 결과 : *안녕하*
#    단어를 입력해주세요: 안녕하세
#    유효한 입력 결과 : *안녕하세*
#    단어를 입력해주세요: 안녕하세요
#    단어를 입력해주세요: 안녕하세요 저는
#    단어를 입력해주세요: 안녕하세요 저는 XXX입니다.
#    유효한 입력 결과 : $안녕하세요 저는 XXX입니다.$
#    단어를 입력해주세요: 만나서 반갑습니다.
#    유효한 입력 결과 : $만나서 반갑습니다.$
#    단어를 입력해주세요:    # 아무 것도 입력하지 않음 --> 루프 탈출

#    Process finished with exit code 0
```

while 뒤에는 조건이 따라온다. 조건은 `x==1` `1<=x<=10`과 같이 True/False 가 적용되는 조건이어야 한다. `while True:`도 가능한데, 이때는 별다른 조건이 없으면 루프가 무한히 반복된다.

for 문과는 달리 while 문은 제어변수의 초기값을 꼭 지정해주어야 한다. 또한 제어변수의 값이 자동으로 바뀌지 않으며(for x in range(10)을 하면 x는 0부터 9까지 차례대로 자동으로 변한다) 조건을 만족시키는 동안 루프가 무한히 반복된다.  따라서 언젠가는 루프를 탈출할 수 있도록 하기 위해 제어변수의 값을 바꾸어주어야 한다.

``` python
while y<=4:
    print(y,'->',y**2)
# --> error가 뜬다

y=1
while y<=4:
    print(y,'->',y**2)
# --> 무한 반복된다

y=1
while y<=4:
    print(y,'->',y**2)
    y+=1
# 출력
#    1 -> 1
#    2 -> 4
#    3 -> 9
#    4 -> 16

#    Process finished with exit code 0
```

