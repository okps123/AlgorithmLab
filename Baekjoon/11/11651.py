n = int(input())
m = [tuple(map(int, input().split())) for i in range(n)]

for p in sorted(sorted(m, key=lambda point: point[0]), key=lambda point: point[1]):
    print(p[0], p[1])
