def solution(s):
    answer = ''
    slist = sorted(list(s))
    for i in slist:
        if slist.count(i) == 1:
            answer += i
    return answer