def solution(food):
    answer = [0]
    del food[0]
    food.reverse()
    for idx, n in enumerate(food):
        if n < 2:
            pass
        else:
            answer[0:0] = [len(food)-idx]*(n//2)
            answer[len(answer):len(answer)] = [len(food)-idx]*(n//2)
    answer = ''.join(str(i) for i in answer)
    return answer