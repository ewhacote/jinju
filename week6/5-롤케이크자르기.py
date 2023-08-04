from collections import Counter
def solution(topping):
    answer = 0
    C  = Counter(topping)
    s = set()
    for t in topping:
        C[t] -= 1
        if C[t] == 0:
            del C[t]
        s.add(t)
        if len(C.keys()) == len(s):
            answer += 1
    return answer
