def solution(plans):
    #1. 시작 시간 기준으로 정렬하기
    #2. 멈춰둔 과제가 여러 개일 때, 가장 최근부터 시작 => stack 구조 떠올리기
    # -> 남은 과제를 stack에 담고 최근 과제부터 꺼내오도록 만들기
    
    #모든 과제의 시작 시간이 달라서 겹치지 않음, 시작시간 기준으로 오름차순 정렬
    plans.sort(key=lambda x:x[1])
    
    answer = []
    stack = []
    P = len(plans)
    
    for i in range(1, P):
        now_h, now_m = map(int, plans[i][1].split(":")) #hh:mm 형태의 string
        before_h, before_m = map(int, plans[i-1][1].split(":"))
        
        if now_m >= before_m:
            res_m = now_m - before_m
            res_h = now_h - before_h
            doing_time = res_m + (res_h*60)
        else:
            res_m = now_m + 60 - before_m
            res_h = now_h - 1 - before_h
            doing_time = res_m + (res_h*60)
            
        #doing_time과 playtime 비교
        
        if int(plans[i-1][2]) > doing_time:
            left = int(plans[i-1][2]) - doing_time
            stack.append((plans[i-1][0], left)) 
        elif int(plans[i-1][2]) < doing_time:
            answer.append(plans[i-1][0])
            now = doing_time - int(plans[i-1][2])
            while (now > 0) and stack:
                stack_n, stack_t = stack.pop()
                if now < stack_t:
                    stack_t -= now
                    stack.append((stack_n, stack_t))
                    break
                elif now == stack_t:
                    answer.append(stack_n)
                    break
                else:
                    answer.append(stack_n)
                    now -= stack_t
        else:
            answer.append(plans[i-1][0])
    
    # for 문이 끝나고 stack 순서의 반대로 answer에 붙여주기
    answer.append(plans[-1][0]) #마지막 과제가 가장 최신
    if stack:
        for i in range(len(stack)):
            n, t = stack.pop()
            answer.append(n)

    return answer
