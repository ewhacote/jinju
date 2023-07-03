from collections import deque
import sys

def solution(board):
    answer = -1
    A = len(board)
    B = len(board[0])
    INF = sys.maxsize
    Queue = deque()
    dist = [[INF] * B for i in range(A)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(A):
        for j in range(B):
            if board[i][j] == 'R':
                Queue.append((i, j, 0))
                dist[i][j] = 0
                break

    while Queue:
        x, y, d = Queue.popleft()
        if board[x][y] == 'G':
            return d

        for i in range(4):
            nx, ny = x, y

            while 0 <= nx + dx[i] < A and 0 <= ny + dy[i] < B and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if dist[nx][ny] > d + 1:
                dist[nx][ny] = d + 1
                Queue.append((nx, ny, d + 1))

    return answer
