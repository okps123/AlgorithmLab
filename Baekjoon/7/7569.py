from collections import deque
import sys

m, n, h = map(int, input().split())
boxes = [[list(map(int, sys.stdin.readline().split()))
          for r in range(n)] for d in range(h)]
q = deque(maxlen=100**3)

for d in range(h):
    for r in range(n):
        for c in range(m):
            if boxes[d][r][c] == 1:
                q.append((d, r, c))

while q:
    d, r, c = q.popleft()

    for dd, dr, dc in (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0):
        nd, nr, nc = d + dd, r + dr, c + dc

        if nd < 0 or nr < 0 or nc < 0:
            continue

        if nd >= h or nr >= n or nc >= m:
            continue

        if boxes[nd][nr][nc] == 0:
            boxes[nd][nr][nc] = boxes[d][r][c] + 1
            q.append((nd, nr, nc))


def printBoxes():
    print()
    for d in range(h):
        print("#", d)
        for r in range(n):
            print(*boxes[d][r])
        print()


def solve():
    cnt = 0

    for d in range(h):
        for r in range(n):
            for c in range(m):
                if boxes[d][r][c] == 0:
                    return -1

                cnt = max(cnt, boxes[d][r][c])

    if cnt > 0:
        return cnt - 1
    else:
        return 0


print(solve())
