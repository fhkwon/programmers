def solution(A, B):
    answer = 0
    C = list(A)
    aa = {}
    for i in range(len(C)):
        C.insert(0,(C.pop()))
        aa[''.join(C)] = i+1
        if B in list(aa.keys()):
            break
    if B in list(aa.keys()):
        answer = aa[B]
    else:
        answer = -1
    if A == B:
        answer = 0
    return answer