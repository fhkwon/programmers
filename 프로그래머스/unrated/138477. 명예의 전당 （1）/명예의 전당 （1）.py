def solution(k, score):
    answer = []
    honor = []
    for i in score:
        honor.append(i)
        if len(honor) > k:
            honor.remove(min(honor))
        answer.append(min(honor))
    return answer