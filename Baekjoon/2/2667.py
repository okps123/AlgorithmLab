from collections import deque

n = int(input())
m = [list(map(int, input())) for i in range(n)]


def dfs(y, x):
    v = deque()
    v.append((y, x))

    l = 0
    m[y][x] = 0

    while v:
        y, x = v.pop()
        l += 1

        for d in (-1, 0), (1, 0), (0, -1), (0, 1):
            dy, dx = y + d[0], x + d[1]

            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue

            if m[dy][dx] == 1:
                m[dy][dx] = 0
                v.append((dy, dx))

    return l


sizes = []
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            sizes.append(dfs(i, j))


print(len(sizes))
print(*sorted(sizes), sep='\n')
