import math
def prime_num(n):
    array = [True for i in range(n+1)] 
    for i in range(2, int(math.sqrt(n)) + 1):
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]
def solution(n):
    answer = len(prime_num(n))
    return answer