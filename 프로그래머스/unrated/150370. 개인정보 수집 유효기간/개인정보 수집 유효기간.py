def solution(today, terms, privacies):
    answer = []
    #오늘 날짜를 이어붙여서 int형으로 만들어두자. 나중에 유통기한과 비교하기 편하게
    ty, tm, td = today.split('.')
    today = int(ty)*12*28 + int(tm)*28 + int(td)
    #약관과 유효기관을 딕셔너리 타입으로 매핑해두자. 
    terms_dict = {i[:1]:int(i[2:])*28 for i in terms}
    #수집일자와 약관을 리스트에 튜블 타입으로 매핑해두자. - 딕셔너리는 같은 키값에 대한 중복 할당이 불가능 
    for i, p in enumerate(privacies):
        yy,mm,dd = p.split('.')
        dd,t = dd.split()
        date = int(yy)*12*28 + int(mm)*28 + int(dd)
        date = date + terms_dict[t]
        #계산한 유효기간 만료일이 지났으면 answer에 추가하자. 
        if date <= today:
            answer.append(i+1)
    return answer