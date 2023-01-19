def solution(N, stages):
    challenger = len(stages)
    failed_id = 0
    p = 0
    fail_ip = []
    answer = []

    for i in range(1, N+1): 
        failed_id = stages.count(i)
        if challenger == 0:
            p = 0
        else: 
            p = failed_id/challenger
        fail_ip.append((p, i))    
        challenger -= failed_id

    fail_ip.sort(key=lambda x : (-x[0], x[1]))

    for j in range(N):
        answer.append(fail_ip[j][1])

    return answer
