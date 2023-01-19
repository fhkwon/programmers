def solution(num, total):
    answer = []
    startnum = total//2
    #num이 홀수 일때:
    if num % 2 == 1:
        temp = list(range(startnum - num//2, startnum + num//2 + 1))
    #num이 짝수 일때:
    elif num % 2 == 0:
        temp = list(range(startnum - num//2 + 1, startnum + num//2 + 1))
    #sum(temp) != total일 동안,
    while sum(temp) != total:
        #만약 sum(temp)> total: 각 요소에 1씩 빼서 재할당
        if sum(temp) > total:
            temp = [i-1 for i in temp]
        #만약 sum(temp) < total: 각 요소에 1씩 더해서 재할당
        elif sum(temp) < total:
            temp = [i+1 for i in temp]
        else:
            break
    #최종 temp 정렬 = answer
    answer = sorted(temp)
            

    return answer