import heapq
def solution(n, k, enemy):
    h = enemy[:k]
    heapq.heapify(h)
    for i in range(k, len(enemy)):
        n -= heapq.heappushpop(h,enemy[i])
        if n < 0 :
            return i
        
    return len(enemy)
