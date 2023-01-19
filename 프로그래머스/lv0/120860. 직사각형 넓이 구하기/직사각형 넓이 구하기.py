def solution(dots):
    answer = 0
    # x[0]기준으로 정렬
    dots = sorted(dots, key= lambda x: x[0])
    # |3[0] - 1[0]| * |2[1] - 1[1]|
    answer = abs(dots[2][0] - dots[0][0])*abs(dots[1][1]-dots[0][1]) 
    return answer