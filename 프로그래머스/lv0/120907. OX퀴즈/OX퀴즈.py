def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        numlist = quiz[i].split(' ')
        ans = int(numlist[-1])
        op = numlist[1]
        num1 = int(numlist[0])
        num2 = int(numlist[2])
        if op == '-':
            if num1 - num2 == ans:
                answer.append('O')
            else:
                answer.append('X')
        else:
            if num1 + num2 == ans:
                answer.append('O')
            else:
                answer.append('X')       
    return answer