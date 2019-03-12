from collections import deque

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
r1, c1, r2, c2 = map(int, input().split())


def bfs():
    q = deque([(r1, c1)])
    while q:
        r, c = q.popleft()

        for dr, dc in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue

            if nr == r2 and nc == c2:
                return arr[r][c]+1

            if arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))

    return -1


print(bfs())

# for i in range(n):
#     print(*arr[i])
