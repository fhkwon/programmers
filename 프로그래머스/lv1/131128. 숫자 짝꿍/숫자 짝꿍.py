def solution(X, Y):
    X = [int(i) for i in X]
    Y = [int(j) for j in Y]
    W = X+Y
    V = X if len(X) < len(Y) else Y
    Z = list(set(X))+list(set(Y))
    xy_list = []
    for i in range(10):
        if Z.count(i) > 1:
            xy_list.append(i)
    ans_list = []
    for i in xy_list:
        w = W.count(i)
        if w>1:
            cnt_i = X.count(i) if X.count(i) < Y.count(i) else Y.count(i)
            ans_list.extend([i]*cnt_i)
    ans_list.sort(reverse = True)
    if len(ans_list) == 0:
        answer = '-1'
    elif list(set(ans_list)) == [0]:
        answer = '0'
    else:
        answer = ''.join([str(k) for k in ans_list])
    return answer