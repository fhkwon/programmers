def solution(n):
    answer = 0
    #1-100까지 3의 배수의 개수를 구하자
    trips = [i for i in range(1, 101) if i%3 == 0]
    trips = [i for i in range(1, 200) if i%3 == 0]
    conthr = [i for i in range(1, 200) if '3' in str(i)]
    thr = trips + conthr
    #range(1, 100+3의 배수 개수 + 1)을 새로 만들어서 3의 배수를 빼자
    newnums = list(range(1, 100 + len(thr) + 1))
    newnums = [i for i in newnums if i not in thr]
    # answer = 그 리스트[n-1]
    answer = newnums[n-1]
    return answer