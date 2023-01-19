def solution(score):
    answer = []
    #먼저 평균의 리스트를 만든다. 
    means = [sum(score[i])/2 for i in range(len(score))]
    print(means)
    #평균값 기준으로 오름차순 정렬을 한다. 
    nmeans = sorted(means, reverse=True)
    print(nmeans)
    #이후 원래 평균값 순서대로 정렬한 평균값의 인덱스를 찾아 반환한다. 
    midx = [means.index(i)+1 for i in means]
    for i in range(len(means)):
        if means[i] in nmeans:
            nidx = nmeans.index(means[i])+1
            print(nidx)
            answer.append(nidx)
        

    return answer