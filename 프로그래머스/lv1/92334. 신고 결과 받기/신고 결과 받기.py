def solution(id_list, report, k):
    answer = []
    report_set = list(set(report))
    #리포트에 있는 id 분리
    report_id = {}
    for n in id_list:
        report_id[n] = []
    for rp in report_set:
        reporter, reported = rp.split(' ')    
        report_id[reported].append(reporter)
    for i, v in report_id.items():
        if len(v) < k: 
            report_id[i] = []
    va_list = []
    #value 값들을 리스트로 만들자=va_list
    for i, v in report_id.items():
        va_list.extend(v)
    numbers = {}
    for s in id_list: 
        numbers[s] = va_list.count(s)
    #value값만 리스트로 출력하기-answer
    for q, w in numbers.items(): 
        answer.append(w)

    return answer






