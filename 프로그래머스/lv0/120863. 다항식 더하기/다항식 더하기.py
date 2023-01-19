def solution(polynomial):
    answer = ''
    polynum = 0
    const = 0
    #먼저 공백 기준으로 나눠서 받기
    polylist = polynomial.split(' ')
    #짝수번째 인자에 대해서만:
    for i in range(0, len(polylist), 2):    
        #'x'가 포함이면:
        if 'x' in polylist[i]:
            #x 기준 스플릿 한 후에 계수 받아오기. 
            xnum, b = polylist[i].split('x')
            if xnum == '':
                polynum += 1
            else:
                polynum += int(xnum)
        else:
            const += int(polylist[i]) 
            print(const)
    if const == 0:
        if polynum == 1:
            answer = 'x'
        else:
            answer = f'{polynum}x'
    elif polynum == 1:
        answer = f'x + {const}'
    elif polynum == 0:
        answer = f'{const}'
    else:
        answer = f'{polynum}x + {const}'
        
    
    
    return answer