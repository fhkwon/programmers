def solution(num_list, n):
    answer = []
    for i in range(int(len(num_list)/n)):
        answer.append(num_list[:n])
        num_list = num_list[n:]
    return answer