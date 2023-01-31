def solution(k, m, score):
    answer = 0
    apple_n = len(score)
    box_n = apple_n//m
    score = sorted(score, reverse=True)
    box_mins = []
    for i in range(box_n):
        try:
            min_s = min(score[i*m:i*m+m])
        except IndexError:
            min_s = min(score[i*m:])
        box_mins.append(min_s)
    answer = sum([i*m for i in box_mins])
    return answer