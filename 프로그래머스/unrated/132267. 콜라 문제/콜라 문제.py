def solution(a, b, n):
    answer = 0
    while (n!=0):
        remain = n%a
        n = n//a
        answer += n*b
        n = n*b + remain
        if n<a:
            break
    return answer