def solution(s, skip, index):
    answer = ''
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    alphabets = [i for i in alphabets if i not in list(skip)]
    for alph in list(s):
        idx = alphabets.index(alph) + index
        while idx >= len(alphabets):
            idx -= len(alphabets)
        answer += alphabets[idx]
    return answer