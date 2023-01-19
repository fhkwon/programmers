def solution(balls, share):
    answer = 0
    mo = []
    ja = []
    for i in range(share):
        mo.append(balls - i)
        ja.append(i+1)
    momo = mo[0]
    jaja = ja[0]
    for i in range(len(mo)-1):
        momo = momo*(mo[i+1])
    for i in range(len(ja)-1):
        jaja = jaja*(ja[i+1])
    answer = momo/jaja
    return answer