def solution(keyinput, board):
    answer = [0,0]
    xlen = abs(board[0]//2)
    ylen = abs(board[1]//2)
    
    keys = {'left': -1, 'right': 1, 'down': -1, 'up': 1}
    for i in keyinput:
        if (i == 'left') or (i =='right'):
            answer[0] += keys[i]
            if abs(answer[0]) > xlen:
                if answer[0]> 0:
                    answer[0] -= 1
                else:
                    answer[0] += 1
            print(answer)
        else:
            answer[1] += keys[i]
            if abs(answer[1]) > ylen:
                if answer[1]> 0:
                    answer[1] -= 1
                else:
                    answer[1] += 1
            print(answer)

    return answer