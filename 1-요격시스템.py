def solution(targets):
    # 구간 구하기 (s, e)
    answer = 0
    # 뒤 값을 기준으로 정렬하기
    targets.sort(key = lambda x: (x[1], x[0]))
    
    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 
