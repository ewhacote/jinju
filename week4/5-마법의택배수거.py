import math

d = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 5,
    7: 4,
    8: 3,
    9: 2,
    10: 1,
}

def solve(x):
    if x < 10:
        return d[x]
    
    s = str(x)
    if s[0] == '1' and all(i == '0' for i in s[1:]):
        return 1
    
    denom = 1
    while 1 <= x / denom:
        denom *= 10
    denom /= 10
    
    a = int(math.ceil(x / denom))
    b = int(math.floor(x / denom))
    
    return min(
        d[a] + solve(abs(a * denom - x)),
        d[b] + solve(abs(b * denom - x))
    )

def solution(storey):
    return solve(storey)
