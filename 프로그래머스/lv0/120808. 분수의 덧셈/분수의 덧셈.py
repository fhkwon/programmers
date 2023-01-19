def solution(denum1, num1, denum2, num2):
    answer = []
    #만약 num1, num2가 같으면 :
    if num1 == num2:
        #denum끼리 더하고 num은 그대로 재할당
        answer = [denum1+denum2, num1]
    #만약 다르면:
    else: 
        #denum1*num2+ denum2*num1, num1*num2으로 재할당
        answer = [denum1*num2 + denum2*num1, num1*num2]    
    #최대공약수를 구하는 함수를 만들자. 
    def cdm_function(num):
        a, b = num[0], num[1]
        while b != 0:
            temp = a % b
            a = b
            b = temp 
        return abs(a)
    cdm = cdm_function(answer)
    #분자, 분모를 최대공약수로 나누자
    answer = [answer[i]/cdm for i in range(2)]

    return answer