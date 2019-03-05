from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for i in range(n)]

q = deque()
q.append((0, 0))

while q:
    y, x = q.popleft()
    for d in (-1, 0), (1, 0), (0, -1), (0, 1):
        dy, dx = y + d[0], x + d[1]

        if dy < 0 or dx < 0 or dy >= n or dx >= m:
            continue

        if board[dy][dx] == 1:
            board[dy][dx] = board[y][x] + 1
            q.append((dy, dx))

print(board[n-1][m-1])
