def solution(emergency):
    em = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        answer.append(em.index(i)+1)
    return answer