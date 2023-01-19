def solution(dots):
    answer = 0
    dist = []
    m = []
    for i in range(3):
        d = (dots[i+1][0] - dots[i][0])**2 + (dots[i+1][1] - dots[i][1])**2
        dist.append(d)
        if (dots[i+1][0] - dots[i][0]) == 0:
            mm = 0
        else:
            mm = (dots[i+1][1] - dots[i][1])/(dots[i+1][0] - dots[i][0])
        m.append(mm)
    for i in range(2):
        d = (dots[i+2][0] - dots[i][0])**2 + (dots[i+2][1] - dots[i][1])**2
        dist.append(d)
        if (dots[i+2][0] - dots[i][0]) == 0:
            mm = 0
        else:
            mm = (dots[i+2][1] - dots[i][1])/(dots[i+2][0] - dots[i][0])
        m.append(mm)
    for i in range(1):
        d = (dots[i+3][0] - dots[i][0])**2 + (dots[i+3][1] - dots[i][1])**2
        dist.append(d)
        if (dots[i+3][0] - dots[i][0]) == 0:
            mm = 0
        else:
            mm = (dots[i+3][1] - dots[i][1])/(dots[i+3][0] - dots[i][0])
        m.append(mm)
    
    
    countdist = {}
    for j in dist:
        try: countdist[j] += 1
        except: countdist[j]=1
    
    countm = {}
    for k in m:
        try: countm[k] += 1
        except: countm[k]=1
    if (len(set(countm.values())) > 1) or (len(set(countdist.values())) > 1):
        answer = 1
    else: 
        answer = 0
    return answer