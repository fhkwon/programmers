def solution(n):
    answer = []
    defac_num = 2
    while defac_num <= n:
        if n % defac_num == 0:
            answer.append(defac_num)
            n = n/defac_num
        else:
            defac_num = defac_num + 1
    answer = sorted(list(set(answer)))
    return answer