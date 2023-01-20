def solution(before, after):
    answer = 0
    after_list = list(after)
    before_list = list(before)
    for i in after_list:
        if i in before_list:
            answer += 1
            before_list.remove(i)
    if answer == len(after_list):
        answer = 1
    else:
        answer = 0
    return answer