def solution(my_string):
    strings = my_string.split(' ')
    m = [strings[i] for i in range(1, len(strings), 2)]
    n = [int(strings[i]) for i in range(0, len(strings), 2)]
    answer = n[0]
    
    for i in range(len(m)):
        if m[i] == '+':
            answer += n[i+1]
        else:
            answer -= n[i+1]
    return answer