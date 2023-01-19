def solution(array):
    answer = 0
    setarr = list(set(array))
    print(setarr)
    numnum = {}
    for i in setarr:
        numnum[i] = array.count(i)
    numnumcnts = [cnts for nums, cnts in numnum.items()]
    print(numnumcnts)
    numnum = sorted(numnum.items(), key= lambda x: x[1], reverse= True)
    print(numnum)
    maxn = numnum[0][0]
    print(maxn)
    maxcnt = numnum[0][1]
    print(maxcnt)
    maxnumcnt = numnumcnts.count(maxcnt)
    print(maxnumcnt)
    if maxnumcnt >1:
        answer = -1
    else:
        answer = maxn
    return answer