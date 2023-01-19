
def solution(numlist, n):
    answer = []
    absnums = []
    for i in range(len(numlist)):
        absnums.append((numlist[i], abs(numlist[i] - n)))
    answerdict = sorted(absnums, key=lambda x: (x[1], -x[0]))
    answer = [j[0] for j in answerdict]
    
    return answer

