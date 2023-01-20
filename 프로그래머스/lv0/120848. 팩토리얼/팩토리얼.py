def solution(n):
    answer = 0
    num = 1
    while num <= n:
        answer += 1
        num = num*(answer) 
    answer -= 1
    return answer