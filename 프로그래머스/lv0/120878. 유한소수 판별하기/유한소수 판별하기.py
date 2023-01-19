def solution(a, b):
    answer = 0
    x, y = a, b
    #분자와 분모의 최대 공약수 구하기 
    def gcd(x,y):
        while(y):
            x,y = y, x%y
        return x
    c = gcd(a,b)

    #각각 최대 공약수로 나누기
    a = a/c
    b = b/c   
    
    for i in [2,5]:
        # b % i != 0일 때까지:
        while b % i == 0:
            b = b/i
        else:
            continue

    if b == 1:
        answer = 1
    else:
        answer = 2
    
    # 정수일 경우 1
    if x/y == 1:
        answer = 1

    return answer