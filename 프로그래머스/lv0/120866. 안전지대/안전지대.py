def solution(board):
    answer = 0
    n = len(board)
    #1의 위치 인덱스를 리스트로 만들자.
    idxlist=[(i,j) for i in range(n) for j in range(n) if board[i][j]==1]
    #x[i][j]에 대하여 주변이 0이면 1로 바꾸고, 1이면 놔둔다.
    #다만 idx 에러에 대해 try except로 처리
    for i, j in idxlist:
        aroundlist = [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i-1,j-1), (i+1,j-1), (i-1,j+1), (i,j)]
        for k , v in aroundlist: 
            if ((k < 0) or (v < 0)):
                aroundlist.remove((k,v))
        for k , v in aroundlist: 
            if ((k < 0) or (v < 0)):
                aroundlist.remove((k,v))
        for k,v in aroundlist:    
            try: 
                if board[k][v] == 0:
                    board[k][v] = 1
            except IndexError:
                pass
    #최종 매트릭스 중 0리스트 만들기
    zerolist=[(i,j) for i in range(n) for j in range(n) if board[i][j]==0]
    answer = len(zerolist)
    
    return answer