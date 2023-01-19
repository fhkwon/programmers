def solution(spell, dic):
    answer = 0
    dicletters = [list(i) for i in dic]
    # print(dicletters)
    dics = []
    #dic:
    for i in dic:
        #spell에 대해:
        for j in spell:
            #j가 i에 있으면:
            if j in i:
                answer += 1
                
        if answer < len(spell):
            answer = 0
            
    if answer != 0:
        answer = 1
    else:
        answer = 2
    return answer