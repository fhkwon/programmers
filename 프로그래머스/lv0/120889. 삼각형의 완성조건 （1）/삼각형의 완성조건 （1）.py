def solution(sides):
    max_len = max(sides)
    sides.remove(max_len)
    if max_len >= sum(sides):
        answer = 2
    else:
        answer = 1
    return answer