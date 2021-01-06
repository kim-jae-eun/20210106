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
```





### while 반복문

> 특정한 조건을 만족하는 동안 계속해서 실행하도록 명령하는 반복문



