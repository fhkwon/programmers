def solution(my_string, n):
    str_list = [i*n for i in list(my_string)]
    answer = ''.join(str_list)
    return answer