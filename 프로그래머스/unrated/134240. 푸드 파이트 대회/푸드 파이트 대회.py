def solution(food):
    answer = "0"
    del food[0]
    food.reverse()
    for idx, n in enumerate(food):
        if n < 2:
            pass
        else:
            answer = str(len(food)-idx)*(n//2) + answer + str(len(food)-idx)*(n//2)
    return answer