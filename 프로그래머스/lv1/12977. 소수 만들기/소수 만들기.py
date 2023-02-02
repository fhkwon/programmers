def prime_num(n):
    divs = []
    for i in range(1,n+1):
        if n%i == 0:
            divs.append(i)
    if len(divs) == 2:
        answer = True
    return True if len(divs) == 2 else False

from itertools import combinations
def solution(nums):
    answer = 0
    sum_nums = [sum(list(i)) for i in list(combinations(nums, 3))]
    for n in sum_nums:
        if prime_num(n) == True:
            answer +=1

    return answer