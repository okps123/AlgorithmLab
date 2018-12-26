p, m = 0, 0
for i in range(4):
    a, b = map(int, input().split())
    p += b - a
    m = max(m, p)
print(m)
