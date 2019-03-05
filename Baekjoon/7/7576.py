from collections import deque
import sys
width, height = map(int, sys.stdin.readline().split())

boxes = []

tomatos = deque()

for i in range(height):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(width):
        if line[j] == 1:
            tomatos.append((j, i))

    boxes.append(line)

while tomatos:
    x, y = tomatos.popleft()

    for d in (-1, 0), (0, -1), (1, 0), (0, 1):
        nx, ny = x + d[0], y + d[1]

        if nx < 0 or ny < 0 or nx >= width or ny >= height:
            continue

        if boxes[ny][nx] == 0:
            boxes[ny][nx] = boxes[y][x] + 1
            tomatos.append((nx, ny))


def solve():
    n = 0
    for i in range(height):
        for j in range(width):
            if boxes[i][j] == 0:
                return -1

            n = max(n, boxes[i][j])

    if n > 0:
        return n - 1
    else:
        return 0


print(solve())
