## 다른 사람의 풀이:
def solution(emergency):
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    for e in emergency:
        answer.append(emer_ls[e])
    return answer

이렇게 딕셔너리로 해야 시간을 log(N)으로 단축가능.
