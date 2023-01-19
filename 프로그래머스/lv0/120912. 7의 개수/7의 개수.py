def solution(array):
    answer = 0
    print(str(array).count('7'))
    array = list(''.join(str(array)))
    while '7' in array:
        answer+=1
        array.remove('7')
    return answer