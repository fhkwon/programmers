def solution(n, lost, reserve):
    nlost = [i for i in lost if i not in reserve]
    nreserve = [i for i in reserve if i not in lost]
    lost = sorted(nlost)
    reserve = sorted(nreserve)
    answer = n - len(lost)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
            
    return answer