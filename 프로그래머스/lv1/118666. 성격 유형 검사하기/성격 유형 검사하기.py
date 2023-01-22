def solution(survey, choices):
    answer = ''
    scores = {'R':0, 'T': 0, 'F':0, 'C':0, 'M':0, 'J':0, 'A':0, 'N':0}
    #각 질문에 대해:
    for i in range(len(choices)):
        score = abs(4-choices[i])
        # 선택점수가 4 초과면 첫번째 글자에 더해주기:
        if choices[i]<4:
            print(survey[i][0])
            scores[survey[i][0]] += score
        #미만이면 두번째 글자에 더해주기:
        else:
            scores[survey[i][1]] += score
    #scores를 성격유형 순으로 정렬하고 자른 후 각각 점수별 정렬
    alp_order = {'R':0, 'T': 1, 'C':2, 'F':3, 'J':4, 'M':5, 'A':6, 'N':7}
    scores = sorted(scores.items(), key=lambda x: alp_order[x[0]])
    RT_scores = sorted(scores[:2], key=lambda x: -x[1])
    CF_scores = sorted(scores[2:4], key=lambda x: -x[1])
    JM_scores = sorted(scores[4:6], key=lambda x: -x[1])
    AN_scores = sorted(scores[6:], key=lambda x: -x[1])
    #각 유형별 점수 더 높은 애들 불러오기 
    answer = RT_scores[0][0] +CF_scores[0][0]+JM_scores[0][0]+AN_scores[0][0]
    
    return answer