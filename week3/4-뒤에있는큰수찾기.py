def solution(numbers):
    stack = []
    N = len(numbers)
    answer = [-1]*N
    
    for i in range(N):
        while stack and numbers[stack[-1]] < numbers[i]:
            s = stack.pop()
            answer[s] = numbers[i]
        stack.append(i)
    return answer
