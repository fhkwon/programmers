def solution(id_pw, db):
    answer = ''
    #id list, pwlist 저장
    idlist = [i[0] for i in db]
    pwlist = [i[1] for i in db]
    # id리스트에 있으면:
    if id_pw[0] in idlist:  
        #pwlist에도 있으면:
        if id_pw[1] == pwlist[idlist.index(id_pw[0])]:
            answer = 'login'
        #없으면:
        else:
            answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer