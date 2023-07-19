def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups :
        deliver_cap, pickup_cap = cap, cap
        while deliveries and deliveries[-1] == 0 :
            deliveries.pop()
        while pickups and pickups[-1] == 0 :
            pickups.pop()
        answer += max(len(deliveries), len(pickups))*2
        
        while deliveries and deliver_cap > 0:
            box = deliveries.pop()
            if box <= deliver_cap :
                deliver_cap -= box
            else :
                deliveries.append(box - deliver_cap)
                break
        while pickups and pickup_cap > 0 :
            box = pickups.pop()
            if box <= pickup_cap :
                pickup_cap -= box
            else :
                pickups.append(box - pickup_cap)
                break
        
    return answer
