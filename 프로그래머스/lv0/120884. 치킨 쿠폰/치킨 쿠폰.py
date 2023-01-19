def solution(chicken):
    answer = 0
    coup = 0
    #치킨을 10으로 나눠서 몫이 0 초과일 동안: 몫은 answer에 더하고 나머지는 coup에 더한다. 
    while chicken // 10 > 0:
        left = chicken % 10
        coup += left
        print(left)
        chicken = chicken // 10
        answer += chicken
        coup += 1       
        
    #while문이 끝났을 때 coup이 10으로 나눠서 몫이 0 초과일 동안: 10으로 나눈 몫을 answer에 더한다. 
    while coup // 10 > 0: 
        coup = coup // 10
        answer += coup
        print(answer)
    
    return answer