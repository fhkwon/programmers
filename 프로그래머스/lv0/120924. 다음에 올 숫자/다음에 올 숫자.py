def solution(common):
    answer = 0
    prog = 'IDK'
    #등차 수열인지 등비수열인지 판단. 
    divs = []
    last = common[-1] - common[-2]
    slast = common[-2] - common[-3]
    if last == slast:
        prog = 'alig'
    else:
        prog = 'geo'

    #등차수열이면 +1, 등비수열이면 *divs
    if prog == 'alig':
        answer = common.pop() + common[-1] - common[-2]
    else:
        answer = common.pop()*(common[-1] / common[-2])
    
    return answer