
### 잘 푼 풀이:
```python
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
```

### 미흡한 점:
1. 일단 ans_list.extend([i]*cnt_i) 이부분에서 처음에는 cnt_i를 그냥 w//2로 넣음. 이렇게 되면 X,Y에 있는 모든 수의 중간값이기 때문에 더 짧은 수를 반환해야 되는 문제에서 틀린 풀이. 
2. collections의 counter 함수를 쓰면 계산 속도가 훨씬 빨라진다. 
3. 어차피 숫자는 0~9이기 때문에 굳이 리스트 내 모든 원소에 대해 for문 돌릴 필요 없이 range(10)을 쓰면 계산 속도가 더 빨라진다. 
