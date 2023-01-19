def solution(bin1, bin2):
    _, answer = bin(int(bin1, 2)+int(bin2, 2)).split('0b')
    return answer