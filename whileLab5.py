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

