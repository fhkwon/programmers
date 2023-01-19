def solution(array, n):
    dic_a = {}
    for i in array:
        dic_a[i] = abs(i - n) 
    aa = sorted(dic_a.items(), key = lambda x: (x[1], x[0]))
    answer = aa[0][0]
    return answer