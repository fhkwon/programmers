
def solution(n):
    answer = 0
    for i in range(2, n+1):
        comp = []
        for j in range(1, i+1):
            if i%j == 0:
                comp.append(i)
        if comp.count(i) >= 3:
            answer += 1
    return answer