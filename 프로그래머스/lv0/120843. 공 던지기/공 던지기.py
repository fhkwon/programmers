def solution(numbers, k):
    idx = 0
    idx += 2*(k-1)
    while idx>= len(numbers):
        idx -= len(numbers)
    answer = idx+1
    return answer