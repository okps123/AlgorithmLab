n, k = map(int, input().split())
v = [int(input()) for i in range(n)]
u = 0

for i in range(len(v)-1, -1, -1):
    if k >= v[i]:
        u += int(k / v[i])
        k %= v[i]

print(u)
