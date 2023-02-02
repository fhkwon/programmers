def solution(s):
    answer = []
    alph_idx = {}
    for idx, alph in enumerate(list(s)):
        if alph not in alph_idx:
            answer.append(-1)
        else:
            answer.append(idx - alph_idx[alph])
        alph_idx[alph] = idx
    return answer