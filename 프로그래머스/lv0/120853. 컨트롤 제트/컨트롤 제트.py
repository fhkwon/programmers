def solution(s):
    answer = 0
    slist = s.split(' ')
    indeces = []
    while 'Z' in slist:
        idx = slist.index('Z')-1
        del slist[idx]
        slist.remove('Z')
    answer = sum([int(i) for i in slist])
    return answer