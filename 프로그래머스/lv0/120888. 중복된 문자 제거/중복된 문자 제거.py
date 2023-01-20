def solution(my_string):
    answer = ''
    for i in list(my_string):
        if i not in answer:
            answer = answer+i
    return answer