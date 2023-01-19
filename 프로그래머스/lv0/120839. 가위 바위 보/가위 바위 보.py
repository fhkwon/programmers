def solution(rsp):
    wins = {'2':'0', '0':'5', '5':'2'}
    rsp_list = list(rsp)
    for i in range(len(rsp_list)):
        rsp_list[i] = wins[rsp_list[i]]
    answer = ''.join(rsp_list)
    return answer