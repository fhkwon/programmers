def solution(sides):
    case1 = len(range(max(sides) - min(sides), max(sides)))
    case2 = len(range(max(sides), max(sides) +min(sides)))
    answer = case1 + case2 - 1
    return answer